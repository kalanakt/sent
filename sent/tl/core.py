"""Core TL types (Bool, Vector, GzipPacked, etc.)."""

from __future__ import annotations

import gzip
import struct

from sent.tl.tlobject import TLObject, register, read_object


@register
class BoolFalse(TLObject):
    CONSTRUCTOR_ID = 0xBC799737
    SUBCLASS_OF_ID = 0xB5286E24  # Bool
    __slots__ = ()

    def to_dict(self):
        return {}

    def _bytes(self):
        return struct.pack("<I", self.CONSTRUCTOR_ID)


@register
class BoolTrue(TLObject):
    CONSTRUCTOR_ID = 0x997275B5
    SUBCLASS_OF_ID = 0xB5286E24
    __slots__ = ()

    def to_dict(self):
        return {}

    def _bytes(self):
        return struct.pack("<I", self.CONSTRUCTOR_ID)


@register
class Null(TLObject):
    CONSTRUCTOR_ID = 0x56730BCC
    __slots__ = ()

    def to_dict(self):
        return {}

    def _bytes(self):
        return struct.pack("<I", self.CONSTRUCTOR_ID)

    @classmethod
    def from_reader(cls, reader):
        return cls()


@register
class GzipPacked(TLObject):
    CONSTRUCTOR_ID = 0x3072CFA1
    __slots__ = ("data",)

    def __init__(self, data: TLObject):
        self.data = data

    def to_dict(self):
        return {"data": self.data.to_dict() if self.data else None}

    def _bytes(self):
        packed = gzip.compress(bytes(self.data))
        from sent.tl.tlobject import serialize_bytes

        return struct.pack("<I", self.CONSTRUCTOR_ID) + serialize_bytes(packed)

    @classmethod
    def from_reader(cls, reader):
        packed = reader.read_bytes()
        data = gzip.decompress(packed)
        from sent.tl.serialization import BinaryReader

        return cls(read_object(BinaryReader(data)))


# Re-export for convenience (typing alias only)
from typing import Union

Bool = Union[BoolFalse, BoolTrue]
