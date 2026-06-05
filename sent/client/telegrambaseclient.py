"""Base Telegram client with connection management."""

from __future__ import annotations

import asyncio
import logging
import platform
import re
from typing import Any, Optional, Union

from sent.client.entity import EntityCache
from sent.crypto.auth_key import AuthKey
from sent.errors.common import FloodWaitError, RPCError
from sent.network.authenticator import do_authentication
from sent.network.connection import get_connection
from sent.network.dc import get_dc
from sent.network.mtprotosender import MTProtoSender
from sent.sessions import MemorySession, SQLiteSession, StringSession
from sent.sessions.abstract import Session
from sent.tl.alltlobjects import LAYER
from sent.tl.tlobject import TLObject
from sent.version import __version__

logger = logging.getLogger("sent.client")

_MIGRATE_RE = re.compile(r"^(PHONE|FILE|NETWORK|USER)_MIGRATE_(\d+)$")


class TelegramBaseClient:
    """Base MTProto client handling connection and RPC."""

    def __init__(
        self,
        session: Union[str, Session],
        api_id: int,
        api_hash: str,
        *,
        connection: str = "abridged",
        use_ipv6: bool = False,
        proxy=None,
        timeout: int = 10,
        request_retries: int = 5,
        entity_cache_limit: int = 5000,
        flood_sleep_threshold: int = 60,
        raise_last_call_error: bool = False,
        device_model: str = None,
        system_version: str = None,
        app_version: str = None,
        lang_code: str = "en",
        system_lang_code: str = "en",
    ):
        self.api_id = api_id
        self.api_hash = api_hash
        self.connection_mode = connection
        self.use_ipv6 = use_ipv6
        self.proxy = proxy
        self.timeout = timeout
        self.request_retries = request_retries
        self.flood_sleep_threshold = flood_sleep_threshold
        self.raise_last_call_error = raise_last_call_error
        self.device_model = device_model or platform.node() or "Unknown"
        self.system_version = system_version or platform.system() or "Unknown"
        self.app_version = app_version or __version__
        self.lang_code = lang_code
        self.system_lang_code = system_lang_code

        if isinstance(session, str):
            if session.startswith("1") and len(session) > 20:
                self.session = StringSession(session)
            elif session.endswith(".session") or "/" in session:
                self.session = SQLiteSession(session.replace(".session", ""))
            else:
                self.session = SQLiteSession(session)
        else:
            self.session = session or MemorySession()

        self._sender: Optional[MTProtoSender] = None
        self._authorized = False
        self._phone = None
        self._phone_code_hash = None
        self._entity_cache = EntityCache(self.session, limit=entity_cache_limit)
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
        self._disconnected = loop.create_future()
        self._borrowed_senders: dict[int, MTProtoSender] = {}
        self._init_connection_sent = False

    def _resolve_dc(self) -> tuple[int, str, int]:
        dc_id, ip, port = self.session.get_dc()
        if self.use_ipv6:
            dc = get_dc(dc_id)
            if dc and dc.ipv6:
                ip = dc.ipv6
        return dc_id, ip, port

    async def connect(self) -> None:
        if self._sender and self._sender.connected:
            return

        dc_id, ip, port = self._resolve_dc()
        auth_key_bytes = self.session.auth_key()

        if auth_key_bytes is None:
            connection = get_connection(ip, port, self.connection_mode, proxy=self.proxy)
            await connection.connect()
            auth_key = await do_authentication(connection)
            await connection.disconnect()
            self.session.set_auth_key(auth_key.key)
            self.session.save()
        else:
            auth_key = AuthKey(auth_key_bytes)

        self._sender = MTProtoSender(
            auth_key,
            dc_id=dc_id,
            ip=ip,
            port=port,
            connection_mode=self.connection_mode,
            session=self.session,
            request_retries=self.request_retries,
            flood_sleep_threshold=self.flood_sleep_threshold,
            proxy=self.proxy,
        )
        await self._sender.connect()
        self._init_connection_sent = False
        if hasattr(self, "_sync_update_state"):
            try:
                await self._sync_update_state()
            except Exception:
                pass
        if self._disconnected.done():
            try:
                loop = asyncio.get_running_loop()
            except RuntimeError:
                loop = asyncio.new_event_loop()
            self._disconnected = loop.create_future()

    async def disconnect(self) -> None:
        if self._sender:
            await self._sender.disconnect()
        for sender in self._borrowed_senders.values():
            if sender.connected:
                await sender.disconnect()
        self._borrowed_senders.clear()
        self.session.save()
        self.session.close()
        if not self._disconnected.done():
            self._disconnected.set_result(None)

    def is_connected(self) -> bool:
        return self._sender is not None and self._sender.connected

    def _wrap_init_connection(self, request: TLObject) -> TLObject:
        from sent.tl.functions.all import InitConnection, InvokeWithLayer

        if self._init_connection_sent:
            return request
        self._init_connection_sent = True
        wrapped = InitConnection(
            api_id=self.api_id,
            device_model=self.device_model,
            system_version=self.system_version,
            app_version=self.app_version,
            system_lang_code=self.system_lang_code,
            lang_pack="",
            lang_code=self.lang_code,
            query=request,
            proxy=self.proxy,
        )
        return InvokeWithLayer(layer=LAYER, query=wrapped)

    async def __call__(self, request: TLObject) -> Any:
        """Invoke an RPC method."""
        if not self.is_connected():
            await self.connect()
        wrapped = self._wrap_init_connection(request)
        try:
            return await self._sender.send(wrapped)
        except RPCError as e:
            migrate = _MIGRATE_RE.match(e.message)
            if migrate:
                new_dc = int(migrate.group(2))
                await self._switch_dc(new_dc)
                wrapped = self._wrap_init_connection(request)
                return await self._sender.send(wrapped)
            raise

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.disconnect()

    async def _switch_dc(self, new_dc_id: int):
        dc = get_dc(new_dc_id)
        self.session.set_dc(dc.id, dc.ip, dc.port)
        if self._sender:
            await self._sender.disconnect()
        self._sender = None
        self._init_connection_sent = False
        await self.connect()

    async def _export_sender(self, dc_id: int) -> MTProtoSender:
        if dc_id in self._borrowed_senders:
            sender = self._borrowed_senders[dc_id]
            if not sender.connected:
                await sender.connect()
            return sender
        dc = get_dc(dc_id)
        auth_key_bytes = self.session.auth_key()
        ip = dc.ipv6 if self.use_ipv6 and dc.ipv6 else dc.ip
        sender = MTProtoSender(
            AuthKey(auth_key_bytes),
            dc_id=dc.id,
            ip=ip,
            port=dc.port,
            connection_mode=self.connection_mode,
            session=self.session,
            request_retries=self.request_retries,
            flood_sleep_threshold=self.flood_sleep_threshold,
            proxy=self.proxy,
        )
        await sender.connect()
        self._borrowed_senders[dc_id] = sender
        return sender
