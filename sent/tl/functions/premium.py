"""Auto-generated TL functions. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

@register
class PremiumGetBoostsList(TLObject):
    CONSTRUCTOR_ID = 1626764896
    __slots__ = ('gifts', 'peer', 'offset', 'limit')
    def __init__(self, peer: 'InputPeer', offset: str, limit: int, gifts: bool = None):
        self.gifts = gifts
        self.peer = peer
        self.offset = offset
        self.limit = limit
    def to_dict(self):
        return {"gifts": self.gifts, "peer": self.peer, "offset": self.offset, "limit": self.limit}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1626764896, signed=False)
        flags = 0
        if self.gifts: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write_string(self.offset)
        writer.write_int(self.limit, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        gifts = bool(flags & (1 << 0))
        peer = reader.tgread_object()
        offset = reader.read_string()
        limit = reader.read_int()
        return cls(gifts, peer, offset, limit)

@register
class PremiumGetMyBoosts(TLObject):
    CONSTRUCTOR_ID = 199719754
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(199719754, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class PremiumApplyBoost(TLObject):
    CONSTRUCTOR_ID = 1803396934
    __slots__ = ('slots', 'peer')
    def __init__(self, peer: 'InputPeer', slots: 'Vector' = None):
        self.slots = slots
        self.peer = peer
    def to_dict(self):
        return {"slots": self.slots, "peer": self.peer}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1803396934, signed=False)
        flags = 0
        if self.slots is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        if flags & (1 << 0):
            writer.write(bytes(self.slots))
        writer.write(bytes(self.peer))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        if flags & (1 << 0):
            slots = reader.tgread_object()
        else:
            slots = None
        peer = reader.tgread_object()
        return cls(slots, peer)

@register
class PremiumGetBoostsStatus(TLObject):
    CONSTRUCTOR_ID = 70197089
    __slots__ = ('peer')
    def __init__(self, peer: 'InputPeer'):
        self.peer = peer
    def to_dict(self):
        return {"peer": self.peer}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(70197089, signed=False)
        writer.write(bytes(self.peer))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        return cls(peer)

@register
class PremiumGetUserBoosts(TLObject):
    CONSTRUCTOR_ID = 965037343
    __slots__ = ('peer', 'user_id')
    def __init__(self, peer: 'InputPeer', user_id: 'InputUser'):
        self.peer = peer
        self.user_id = user_id
    def to_dict(self):
        return {"peer": self.peer, "user_id": self.user_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(965037343, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.user_id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        user_id = reader.tgread_object()
        return cls(peer, user_id)

