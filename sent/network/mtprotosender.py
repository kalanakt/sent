"""MTProto sender: RPC engine with send/recv loops."""

from __future__ import annotations

import asyncio
import logging
import time
from typing import Any, Callable, Dict, List, Optional

from sent.crypto.auth_key import AuthKey
from sent.errors.common import FloodWaitError, RPCError, rpc_message_to_error
from sent.network.connection import get_connection
from sent.network.mtprotostate import MTProtoState
from sent.network.requeststate import RequestState
from sent.tl.core import GzipPacked
from sent.tl.mtproto_types import ContainerMessage, MsgContainer, RpcResult
from sent.tl.serialization import BinaryReader
from sent.tl.tlobject import TLObject, read_object

logger = logging.getLogger("sent.network")


class MTProtoSender:
    """Handles sending and receiving MTProto RPC requests."""

    def __init__(
        self,
        auth_key: AuthKey,
        *,
        dc_id: int = 2,
        ip: str = "149.154.167.51",
        port: int = 443,
        connection_mode: str = "abridged",
        session=None,
        request_retries: int = 5,
        flood_sleep_threshold: int = 60,
        proxy=None,
    ):
        self.auth_key = auth_key
        self.dc_id = dc_id
        self.ip = ip
        self.port = port
        self.connection_mode = connection_mode
        self.session = session
        self.request_retries = request_retries
        self.flood_sleep_threshold = flood_sleep_threshold
        self.proxy = proxy

        session_id = None
        salt = 0
        if session is not None:
            session_id = getattr(session, "get_session_id", lambda: None)()
            salt = getattr(session, "get_salt", lambda: 0)()

        self._state = MTProtoState(auth_key, session_id=session_id, salt=salt)
        self._connection = None
        self._send_queue: asyncio.Queue = asyncio.Queue()
        self._pending: Dict[int, RequestState] = {}
        self._send_task: Optional[asyncio.Task] = None
        self._recv_task: Optional[asyncio.Task] = None
        self._connected = False
        self._user_connected = True
        self._retries = 5
        self._auto_reconnect = True
        self._updates_queue: asyncio.Queue = asyncio.Queue()
        self._handlers: List = []
        self._need_ack: List[int] = []
        self._last_ack_time = time.time()
        self._ping_futures: Dict[int, asyncio.Future] = {}

    @property
    def connected(self) -> bool:
        return self._connected

    @property
    def state(self) -> MTProtoState:
        return self._state

    async def connect(self) -> None:
        if self._connected:
            return
        self._connection = get_connection(
            self.ip, self.port, self.connection_mode, proxy=self.proxy
        )
        await self._connection.connect()
        self._connected = True
        self._send_task = asyncio.create_task(self._send_loop())
        self._recv_task = asyncio.create_task(self._recv_loop())
        await self._fetch_future_salts()
        logger.debug("Connected to %s:%s (DC %s)", self.ip, self.port, self.dc_id)

    async def disconnect(self) -> None:
        self._user_connected = False
        self._connected = False
        if self._send_task:
            self._send_task.cancel()
        if self._recv_task:
            self._recv_task.cancel()
        if self._connection:
            await self._connection.disconnect()
        for state in self._pending.values():
            if not state.future.done():
                state.future.set_exception(ConnectionError("Disconnected"))
        self._pending.clear()
        self._persist_state()

    def _persist_state(self) -> None:
        if self.session is None:
            return
        if hasattr(self.session, "set_mtproto_state"):
            self.session.set_mtproto_state(self._state.salt, self._state.session_id)
        else:
            if hasattr(self.session, "set_salt"):
                self.session.set_salt(self._state.salt)
            if hasattr(self.session, "set_session_id"):
                self.session.set_session_id(self._state.session_id)
        if hasattr(self.session, "save"):
            self.session.save()

    async def send(self, request: TLObject, *, ordered: bool = False) -> Any:
        """Send an RPC request and wait for the result."""
        if not self._connected:
            await self.connect()

        last_error = None
        for attempt in range(self.request_retries):
            state = RequestState(request=request)
            await self._send_queue.put(state)
            try:
                return await asyncio.wait_for(state.future, timeout=60.0)
            except FloodWaitError as e:
                if e.seconds <= self.flood_sleep_threshold:
                    await asyncio.sleep(e.seconds)
                    last_error = e
                    continue
                raise
            except asyncio.TimeoutError:
                self._pending.pop(state.msg_id, None)
                last_error = TimeoutError(
                    f"Request {request.__class__.__name__} timed out"
                )
            except Exception as e:
                last_error = e
                if attempt + 1 >= self.request_retries:
                    raise
        if last_error:
            raise last_error
        raise RuntimeError("Request failed without error")

    async def _send_loop(self) -> None:
        while self._connected:
            try:
                state = await asyncio.wait_for(self._send_queue.get(), timeout=1.0)
            except asyncio.TimeoutError:
                await self._maybe_send_ack()
                continue
            try:
                await self._send_request(state)
            except Exception as e:
                if not state.future.done():
                    state.future.set_exception(e)

    async def _encrypt_and_frame(
        self,
        body: bytes,
        *,
        content_related: bool,
    ) -> tuple[int, bytes]:
        """Build, encrypt, and return (msg_id, encrypted_payload)."""
        msg_id, _, data = self._state.build_message_data(
            body, content_related=content_related
        )
        encrypted = self._state.encrypt_message_data(data)
        return msg_id, encrypted

    async def _send_request(self, state: RequestState) -> None:
        body = bytes(state.request)
        msg_id, encrypted = await self._encrypt_and_frame(body, content_related=True)
        state.msg_id = msg_id
        await self._connection.send(encrypted)
        self._pending[msg_id] = state

    async def _recv_loop(self) -> None:
        while self._connected:
            try:
                data = await self._connection.recv()
                await self._process_message(data)
                await self._maybe_send_ack()
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.warning("Recv error: %s", e)
                if self._auto_reconnect and self._user_connected:
                    await self._reconnect()
                else:
                    break

    async def _process_message(self, data: bytes) -> None:
        try:
            decrypted = self._state.decrypt_message_data(data)
        except Exception:
            decrypted = data

        if len(decrypted) < 32:
            return

        salt, session_id, msg_id, seq_no, body = self._state.parse_message_data(decrypted)

        if session_id and session_id != self._state.session_id:
            logger.debug(
                "Ignoring message for different session_id %s (ours %s)",
                session_id,
                self._state.session_id,
            )
            return

        if salt:
            self._state.salt = salt

        self._need_ack.append(msg_id)

        reader = BinaryReader(body)
        obj = read_object(reader)
        await self._dispatch_object(obj, msg_id)

    async def _dispatch_object(self, obj: TLObject, msg_id: int) -> None:
        cls_name = obj.__class__.__name__

        if cls_name == "GzipPacked":
            await self._dispatch_object(obj.data, msg_id)
            return

        if cls_name == "MsgContainer":
            for message in obj.messages:
                await self._dispatch_object(message.body, message.msg_id)
            return

        if cls_name == "RpcResult":
            await self._handle_rpc_result(obj)
            return

        if cls_name == "RpcError":
            await self._handle_rpc_error(obj, msg_id)
            return

        if cls_name == "Pong":
            ping_id = getattr(obj, "ping_id", None)
            if ping_id in self._ping_futures:
                future = self._ping_futures.pop(ping_id)
                if not future.done():
                    future.set_result(obj)
            return

        if cls_name == "BadServerSalt":
            self._state.salt = obj.new_server_salt
            self._persist_state()
            await self._resend_all_pending()
            return

        if cls_name == "BadMsgNotification":
            await self._handle_bad_msg(obj)
            return

        if cls_name == "NewSessionCreated":
            self._state.salt = obj.server_salt
            self._persist_state()
            return

        if cls_name == "FutureSalts":
            if obj.salts:
                self._state.salt = obj.salts[0].salt
                self._persist_state()
            return

        req_msg_id = getattr(obj, "req_msg_id", None)
        if req_msg_id and req_msg_id in self._pending:
            state = self._pending.pop(req_msg_id)
            result = getattr(obj, "result", obj)
            if not state.future.done():
                state.future.set_result(result)
            return

        await self._updates_queue.put(obj)

    async def _handle_rpc_result(self, result: RpcResult) -> None:
        req_msg_id = result.req_msg_id
        inner = result.result
        if inner.__class__.__name__ == "GzipPacked":
            inner = inner.data
        if inner.__class__.__name__ == "RpcError":
            await self._handle_rpc_error(inner, req_msg_id)
            return
        if req_msg_id in self._pending:
            state = self._pending.pop(req_msg_id)
            if not state.future.done():
                state.future.set_result(inner)
            return
        await self._updates_queue.put(inner)

    async def _handle_rpc_error(self, error, req_msg_id: int) -> None:
        code = error.error_code
        message = error.error_message

        if code == 420 and message.startswith("FLOOD_WAIT_"):
            try:
                seconds = int(message.split("_")[-1])
            except ValueError:
                seconds = 60
            exc = FloodWaitError(seconds, message)
            state = self._pending.pop(req_msg_id, None)
            if state and not state.future.done():
                state.future.set_exception(exc)
            return

        exc = rpc_message_to_error(message, code)
        state = self._pending.pop(req_msg_id, None)
        if state and not state.future.done():
            state.future.set_exception(exc)
            return

        for pending_id, pending_state in list(self._pending.items()):
            if not pending_state.future.done():
                pending_state.future.set_exception(exc)
                del self._pending[pending_id]
                break

    async def _handle_bad_msg(self, bad_msg) -> None:
        error_code = bad_msg.error_code
        if error_code in (16, 17):
            self._state.time_offset += error_code - 16
        elif error_code == 32:
            self._state._seq_no = 0
        elif error_code == 48:
            return
        await self._resend_all_pending()

    async def _resend_all_pending(self) -> None:
        pending = list(self._pending.values())
        self._pending.clear()
        for state in pending:
            if not state.future.done():
                await self._send_queue.put(state)

    async def _maybe_send_ack(self) -> None:
        if not self._need_ack:
            return
        if time.time() - self._last_ack_time < 0.5 and len(self._need_ack) < 10:
            return
        from sent.tl.types.all import MsgsAck

        msg_ids = self._need_ack[:500]
        self._need_ack = self._need_ack[500:]
        ack = MsgsAck(msg_ids=msg_ids)
        await self._send_service(ack)
        self._last_ack_time = time.time()

    async def _send_service(self, request: TLObject) -> None:
        body = bytes(request)
        _, encrypted = await self._encrypt_and_frame(body, content_related=False)
        await self._connection.send(encrypted)

    async def _fetch_future_salts(self) -> None:
        from sent.tl.functions.all import GetFutureSalts

        try:
            await self._send_service(GetFutureSalts(num=32))
        except Exception as e:
            logger.debug("Could not fetch future salts: %s", e)

    async def _reconnect(self) -> None:
        for attempt in range(self._retries):
            try:
                if self._connection:
                    await self._connection.disconnect()
                self._connection = get_connection(
                    self.ip, self.port, self.connection_mode
                )
                await self._connection.connect()
                self._connected = True
                await self._resend_all_pending()
                await self._fetch_future_salts()
                logger.info("Reconnected to DC %s (attempt %d)", self.dc_id, attempt + 1)
                return
            except Exception as e:
                logger.warning("Reconnect attempt %d failed: %s", attempt + 1, e)
                await asyncio.sleep(2**attempt)

    async def ping(self, ping_id: Optional[int] = None) -> None:
        from sent.tl.functions.all import Ping

        if ping_id is None:
            ping_id = int(time.time())
        future = asyncio.get_event_loop().create_future()
        self._ping_futures[ping_id] = future
        await self._send_service(Ping(ping_id=ping_id))
        try:
            await asyncio.wait_for(future, timeout=10.0)
        finally:
            self._ping_futures.pop(ping_id, None)

    def add_update_handler(self, handler) -> None:
        self._handlers.append(handler)

    async def get_updates(self, timeout: float = 1.0):
        try:
            return await asyncio.wait_for(self._updates_queue.get(), timeout=timeout)
        except asyncio.TimeoutError:
            return None
