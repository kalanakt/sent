"""Auto-generated TL types. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional, TYPE_CHECKING
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

@register
class StickersSuggestedShortName(TLObject):
    CONSTRUCTOR_ID = 2248056895
    __slots__ = ('short_name')
    def __init__(self, short_name: str):
        self.short_name = short_name
    def to_dict(self):
        return {"short_name": self.short_name}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2248056895, signed=False)
        writer.write_string(self.short_name)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        short_name = reader.read_string()
        return cls(short_name)

