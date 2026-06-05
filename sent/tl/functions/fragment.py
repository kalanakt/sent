"""Auto-generated TL functions. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

@register
class FragmentGetCollectibleInfo(TLObject):
    CONSTRUCTOR_ID = 3189671354
    __slots__ = ('collectible')
    def __init__(self, collectible: 'InputCollectible'):
        self.collectible = collectible
    def to_dict(self):
        return {"collectible": self.collectible}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3189671354, signed=False)
        writer.write(bytes(self.collectible))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        collectible = reader.tgread_object()
        return cls(collectible)

