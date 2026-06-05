"""Base TL object and registry."""

from __future__ import annotations

import struct
from typing import TYPE_CHECKING, Any, ClassVar, Dict, Type, TypeVar

if TYPE_CHECKING:
    from sent.tl.serialization import BinaryReader

T = TypeVar("T", bound="TLObject")

# Global registry: constructor_id -> class
CONSTRUCTORS: Dict[int, Type["TLObject"]] = {}

_INT = struct.Struct("<i")
_UINT = struct.Struct("<I")
_LONG = struct.Struct("<q")
_DOUBLE = struct.Struct("<d")

_BOOL_FALSE_ID = 0xBC799737
_BOOL_TRUE_ID = 0x997275B5


class TLObject:
    """Base class for all TL types and RPC functions."""

    __slots__ = ()

    CONSTRUCTOR_ID: ClassVar[int] = 0
    SUBCLASS_OF_ID: ClassVar[int] = 0

    def to_dict(self) -> dict:
        raise NotImplementedError

    def _bytes(self) -> bytes:
        raise NotImplementedError

    def __bytes__(self) -> bytes:
        return self._bytes()

    @classmethod
    def from_reader(cls, reader: "BinaryReader") -> "TLObject":
        raise NotImplementedError

    @classmethod
    def pretty_format(cls, obj: Any, indent: int = 0) -> str:
        if obj is None:
            return "None"
        if isinstance(obj, bytes):
            return f"b'{obj[:16].hex()}...'" if len(obj) > 16 else repr(obj)
        if isinstance(obj, (list, tuple)):
            if not obj:
                return "[]"
            items = ",\n".join(
                " " * (indent + 4) + cls.pretty_format(x, indent + 4) for x in obj
            )
            return "[\n" + items + "\n" + " " * indent + "]"
        if isinstance(obj, TLObject):
            return repr(obj)
        return repr(obj)

    def __repr__(self) -> str:
        cls_name = self.__class__.__name__
        parts = []
        for k, v in self.to_dict().items():
            parts.append(f"{k}={TLObject.pretty_format(v)}")
        return f"{cls_name}({', '.join(parts)})"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, self.__class__) and self.to_dict() == other.to_dict()

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)


def register(cls: Type[TLObject]) -> Type[TLObject]:
    """Register a TL class by its constructor ID."""
    if cls.CONSTRUCTOR_ID:
        CONSTRUCTORS[cls.CONSTRUCTOR_ID] = cls
    return cls


def read_object(reader: "BinaryReader") -> TLObject:
    """Read a TL object from the stream using its constructor ID."""
    constructor_id = reader.read_int(signed=False)
    cls = CONSTRUCTORS.get(constructor_id)
    if cls is None:
        from sent.tl.core import GzipPacked

        if constructor_id == GzipPacked.CONSTRUCTOR_ID:
            return GzipPacked.from_reader(reader)
        raise ValueError(
            f"Unknown constructor ID {constructor_id:#010x}. "
            "Update the TL schema or regenerate types."
        )
    return cls.from_reader(reader)


def serialize_bytes(data: bytes) -> bytes:
    """Serialize bytes/string per TL rules."""
    length = len(data)
    if length <= 253:
        padding = (4 - ((length + 1) % 4)) % 4
        return bytes([length]) + data + b"\x00" * padding
    else:
        padding = (4 - (length % 4)) % 4
        return _INT.pack(length) + data + b"\x00" * padding


def serialize_int(value: int) -> bytes:
    return _INT.pack(value)


def serialize_long(value: int) -> bytes:
    return _LONG.pack(value)


def serialize_double(value: float) -> bytes:
    return _DOUBLE.pack(value)


def serialize_bool(value: bool) -> bytes:
    return _UINT.pack(_BOOL_TRUE_ID if value else _BOOL_FALSE_ID)
