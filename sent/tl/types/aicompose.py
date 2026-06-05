"""Auto-generated TL types. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional, TYPE_CHECKING
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

@register
class AicomposeTonesNotModified(TLObject):
    CONSTRUCTOR_ID = 3254018307
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3254018307, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class AicomposeTones(TLObject):
    CONSTRUCTOR_ID = 1822232318
    __slots__ = ('hash', 'tones', 'users')
    def __init__(self, hash: int, tones: 'Vector', users: 'Vector'):
        self.hash = hash
        self.tones = tones
        self.users = users
    def to_dict(self):
        return {"hash": self.hash, "tones": self.tones, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1822232318, signed=False)
        writer.write_long(self.hash, signed=False)
        writer.write(bytes(self.tones))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_long()
        tones = reader.tgread_object()
        users = reader.tgread_object()
        return cls(hash, tones, users)

