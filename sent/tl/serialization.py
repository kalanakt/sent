"""TL binary serialization reader and writer."""

from __future__ import annotations

import gzip
import io
import struct
from typing import List, Optional, Union

from sent.tl.tlobject import TLObject, read_object, serialize_bytes

_INT = struct.Struct("<i")
_UINT = struct.Struct("<I")
_LONG = struct.Struct("<q")
_ULONG = struct.Struct("<Q")
_DOUBLE = struct.Struct("<d")

_VECTOR_CONSTRUCTOR = 0x1CB5C415
_BOOL_FALSE_ID = 0xBC799737
_BOOL_TRUE_ID = 0x997275B5


class BinaryReader:
    """Reads TL binary data."""

    __slots__ = ("_stream", "_len")

    def __init__(self, data: bytes):
        self._stream = io.BytesIO(data)
        self._len = len(data)

    @property
    def remaining(self) -> int:
        return self._len - self._stream.tell()

    def read(self, n: int = -1) -> bytes:
        return self._stream.read(n)

    def read_int(self, signed: bool = True) -> int:
        data = self._stream.read(4)
        if len(data) < 4:
            raise EOFError("Not enough bytes for int")
        return (_INT if signed else _UINT).unpack(data)[0]

    def read_long(self, signed: bool = True) -> int:
        data = self._stream.read(8)
        if len(data) < 8:
            raise EOFError("Not enough bytes for long")
        return (_LONG if signed else _ULONG).unpack(data)[0]

    def read_double(self) -> float:
        data = self._stream.read(8)
        if len(data) < 8:
            raise EOFError("Not enough bytes for double")
        return _DOUBLE.unpack(data)[0]

    def read_bytes(self) -> bytes:
        first = self._stream.read(1)
        if not first:
            raise EOFError("Not enough bytes")
        length = first[0]
        if length == 254:
            length = _UINT.unpack(self._stream.read(3) + b"\x00")[0]
            data = self._stream.read(length)
            self._stream.read((4 - (length % 4)) % 4)
        else:
            data = self._stream.read(length)
            self._stream.read((4 - ((length + 1) % 4)) % 4)
        return data

    def read_string(self) -> str:
        return self.read_bytes().decode("utf-8", errors="replace")

    def tgread_object(self) -> TLObject:
        return read_object(self)

    def tgread_vector(self) -> list:
        constructor = self.read_int(signed=False)
        if constructor != _VECTOR_CONSTRUCTOR:
            raise ValueError(f"Expected vector constructor, got {constructor:#x}")
        count = self.read_int(signed=False)
        return [self.tgread_object() for _ in range(count)]

    def tgread_vector_int(self) -> list:
        constructor = self.read_int(signed=False)
        if constructor != _VECTOR_CONSTRUCTOR:
            raise ValueError(f"Expected vector constructor, got {constructor:#x}")
        count = self.read_int(signed=False)
        return [self.read_int() for _ in range(count)]

    def tgread_vector_long(self) -> list:
        constructor = self.read_int(signed=False)
        if constructor != _VECTOR_CONSTRUCTOR:
            raise ValueError(f"Expected vector constructor, got {constructor:#x}")
        count = self.read_int(signed=False)
        return [self.read_long(signed=False) for _ in range(count)]

    def tgread_vector_string(self) -> list:
        constructor = self.read_int(signed=False)
        if constructor != _VECTOR_CONSTRUCTOR:
            raise ValueError(f"Expected vector constructor, got {constructor:#x}")
        count = self.read_int(signed=False)
        return [self.read_string() for _ in range(count)]

    def tgread_bool(self) -> bool:
        val = self.read_int(signed=False)
        if val == _BOOL_FALSE_ID:
            return False
        if val == _BOOL_TRUE_ID:
            return True
        raise ValueError(f"Invalid bool constructor {val:#x}")


class BinaryWriter:
    """Writes TL binary data."""

    __slots__ = ("_parts",)

    def __init__(self):
        self._parts: List[bytes] = []

    def write(self, data: bytes) -> None:
        self._parts.append(data)

    def write_int(self, value: int, signed: bool = True) -> None:
        self._parts.append((_INT if signed else _UINT).pack(value))

    def write_long(self, value: int, signed: bool = True) -> None:
        self._parts.append((_LONG if signed else _ULONG).pack(value))

    def write_double(self, value: float) -> None:
        self._parts.append(_DOUBLE.pack(value))

    def write_bytes(self, data: bytes) -> None:
        self._parts.append(serialize_bytes(data))

    def write_raw(self, data: bytes) -> None:
        """Write raw bytes without TL length prefix (for int128/int256)."""
        self._parts.append(data)

    def write_string(self, value: str) -> None:
        self.write_bytes(value.encode("utf-8"))

    def get_bytes(self) -> bytes:
        return b"".join(self._parts)

    @classmethod
    def serialize_object(cls, obj: TLObject) -> bytes:
        return bytes(obj)

    @classmethod
    def serialize_vector(
        cls,
        items: list,
        boxed: bool = True,
        item_type: str | None = None,
    ) -> bytes:
        w = cls()
        if boxed:
            w.write_int(_VECTOR_CONSTRUCTOR, signed=False)
        w.write_int(len(items), signed=False)
        for item in items:
            if item_type == "int":
                w.write_int(item)
            elif item_type == "long":
                w.write_long(item, signed=False)
            elif item_type == "string":
                w.write_string(item)
            elif isinstance(item, TLObject):
                w.write(bytes(item))
            elif isinstance(item, bool):
                from sent.tl.tlobject import serialize_bool

                w.write(serialize_bool(item))
            elif isinstance(item, int):
                if -2147483648 <= item <= 2147483647:
                    w.write_int(item)
                elif -9223372036854775808 <= item <= 9223372036854775807:
                    w.write_long(item)
                else:
                    w.write_long(item, signed=False)
            elif isinstance(item, bytes):
                w.write_bytes(item)
            elif isinstance(item, str):
                w.write_string(item)
            else:
                raise TypeError(f"Cannot serialize vector item {type(item)}")
        return w.get_bytes()
