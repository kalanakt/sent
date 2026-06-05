"""TCP connection abstractions for MTProto."""

from __future__ import annotations

import asyncio
import os
import struct
from abc import ABC, abstractmethod
from typing import Optional


async def _open_connection(ip: str, port: int, proxy=None, timeout: float = 10.0):
    if proxy is None:
        return await asyncio.wait_for(asyncio.open_connection(ip, port), timeout=timeout)

    proxy_type = proxy[0] if isinstance(proxy, (list, tuple)) else getattr(proxy, "proxy_type", None)
    if proxy_type in (2, "socks5", "SOCKS5"):
        try:
            import python_socks

            proxy_host = proxy[1] if isinstance(proxy, (list, tuple)) else proxy.addr
            proxy_port = proxy[2] if isinstance(proxy, (list, tuple)) else proxy.port
            proxy_user = proxy[4] if isinstance(proxy, (list, tuple)) and len(proxy) > 4 else None
            proxy_pass = proxy[5] if isinstance(proxy, (list, tuple)) and len(proxy) > 5 else None
            proxy_conn = python_socks.Proxy.from_url(
                f"socks5://{proxy_host}:{proxy_port}",
                username=proxy_user,
                password=proxy_pass,
            )
            raw = await asyncio.wait_for(
                proxy_conn.connect(dest_host=ip, dest_port=port),
                timeout=timeout,
            )
            reader, writer = await asyncio.open_connection(sock=raw)
            return reader, writer
        except ImportError:
            pass
    return await asyncio.wait_for(asyncio.open_connection(ip, port), timeout=timeout)


class Connection(ABC):
    """Abstract async TCP connection."""

    packet_codec = None

    def __init__(self, ip: str, port: int, proxy=None):
        self._ip = ip
        self._port = port
        self._proxy = proxy
        self._reader: Optional[asyncio.StreamReader] = None
        self._writer: Optional[asyncio.StreamWriter] = None
        self._connected = False

    async def connect(self, timeout: float = 10.0) -> None:
        self._reader, self._writer = await _open_connection(
            self._ip, self._port, self._proxy, timeout=timeout
        )
        self._connected = True
        await self._init_connection()

    @abstractmethod
    async def _init_connection(self) -> None:
        pass

    async def disconnect(self) -> None:
        if self._writer:
            self._writer.close()
            try:
                await self._writer.wait_closed()
            except Exception:
                pass
        self._connected = False

    async def send(self, data: bytes) -> None:
        if not self._writer:
            raise ConnectionError("Not connected")
        self._writer.write(data)
        await self._writer.drain()

    async def recv(self) -> bytes:
        if not self._reader:
            raise ConnectionError("Not connected")
        return await self._recv_impl()

    @abstractmethod
    async def _recv_impl(self) -> bytes:
        pass

    @property
    def connected(self) -> bool:
        return self._connected


class AbridgedPacketCodec:
    """Abridged packet framing (4-byte length header)."""

    @staticmethod
    def encode(data: bytes) -> bytes:
        length = len(data) // 4
        if length < 127:
            return struct.pack("<B", length) + data
        return b"\x7f" + struct.pack("<I", length)[1:4] + data

    @staticmethod
    async def read_packet(reader: asyncio.StreamReader) -> bytes:
        first = await reader.readexactly(1)
        if first == b"\x7f":
            length_bytes = await reader.readexactly(3)
            length = struct.unpack("<I", length_bytes + b"\x00")[0]
        else:
            length = first[0]
        return await reader.readexactly(length * 4)


class TCPAbridged(Connection):
    """TCP connection with abridged protocol (default)."""

    async def _init_connection(self) -> None:
        await self.send(b"\xef")

    async def _recv_impl(self) -> bytes:
        return await AbridgedPacketCodec.read_packet(self._reader)

    async def send(self, data: bytes) -> None:
        await super().send(AbridgedPacketCodec.encode(data))


class TCPIntermediate(Connection):
    """TCP connection with intermediate protocol."""

    async def _init_connection(self) -> None:
        await self.send(b"\xee\xee\xee\xee")

    async def _recv_impl(self) -> bytes:
        length_bytes = await self._reader.readexactly(4)
        length = struct.unpack("<I", length_bytes)[0]
        return await self._reader.readexactly(length)

    async def send(self, data: bytes) -> None:
        await super().send(struct.pack("<I", len(data)) + data)


class TCPFull(Connection):
    """TCP connection with full protocol."""

    async def _init_connection(self) -> None:
        pass

    async def _recv_impl(self) -> bytes:
        header = await self._reader.readexactly(8)
        length = struct.unpack("<I", header[4:8])[0] - 8
        return await self._reader.readexactly(length)

    async def send(self, data: bytes) -> None:
        seq = os.urandom(4)
        payload = seq + struct.pack("<I", len(data) + 8) + data
        await super().send(payload)


def get_connection(ip: str, port: int, mode: str = "abridged", proxy=None) -> Connection:
    modes = {
        "abridged": TCPAbridged,
        "intermediate": TCPIntermediate,
        "full": TCPFull,
        "obfuscated": TCPIntermediate,
    }
    cls = modes.get(mode, TCPAbridged)

    class _Conn(cls):
        def __init__(self, ip, port):
            super().__init__(ip, port, proxy=proxy)

    return _Conn(ip, port)
