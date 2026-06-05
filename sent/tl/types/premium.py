"""Auto-generated TL types. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional, TYPE_CHECKING
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

@register
class PremiumBoostsList(TLObject):
    CONSTRUCTOR_ID = 2264424764
    __slots__ = ('count', 'boosts', 'next_offset', 'users')
    def __init__(self, count: int, boosts: 'Vector', users: 'Vector', next_offset: str = None):
        self.count = count
        self.boosts = boosts
        self.next_offset = next_offset
        self.users = users
    def to_dict(self):
        return {"count": self.count, "boosts": self.boosts, "next_offset": self.next_offset, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2264424764, signed=False)
        flags = 0
        if self.next_offset is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write_int(self.count, signed=True)
        writer.write(bytes(self.boosts))
        if flags & (1 << 0):
            writer.write_string(self.next_offset)
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        count = reader.read_int()
        boosts = reader.tgread_object()
        if flags & (1 << 0):
            next_offset = reader.read_string()
        else:
            next_offset = None
        users = reader.tgread_object()
        return cls(count, boosts, next_offset, users)

@register
class PremiumMyBoosts(TLObject):
    CONSTRUCTOR_ID = 2598512866
    __slots__ = ('my_boosts', 'chats', 'users')
    def __init__(self, my_boosts: 'Vector', chats: 'Vector', users: 'Vector'):
        self.my_boosts = my_boosts
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"my_boosts": self.my_boosts, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2598512866, signed=False)
        writer.write(bytes(self.my_boosts))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        my_boosts = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(my_boosts, chats, users)

@register
class PremiumBoostsStatus(TLObject):
    CONSTRUCTOR_ID = 1230586490
    __slots__ = ('my_boost', 'level', 'current_level_boosts', 'boosts', 'gift_boosts', 'next_level_boosts', 'premium_audience', 'boost_url', 'prepaid_giveaways', 'my_boost_slots')
    def __init__(self, level: int, current_level_boosts: int, boosts: int, boost_url: str, my_boost: bool = None, gift_boosts: int = None, next_level_boosts: int = None, premium_audience: 'StatsPercentValue' = None, prepaid_giveaways: 'Vector' = None, my_boost_slots: 'Vector' = None):
        self.my_boost = my_boost
        self.level = level
        self.current_level_boosts = current_level_boosts
        self.boosts = boosts
        self.gift_boosts = gift_boosts
        self.next_level_boosts = next_level_boosts
        self.premium_audience = premium_audience
        self.boost_url = boost_url
        self.prepaid_giveaways = prepaid_giveaways
        self.my_boost_slots = my_boost_slots
    def to_dict(self):
        return {"my_boost": self.my_boost, "level": self.level, "current_level_boosts": self.current_level_boosts, "boosts": self.boosts, "gift_boosts": self.gift_boosts, "next_level_boosts": self.next_level_boosts, "premium_audience": self.premium_audience, "boost_url": self.boost_url, "prepaid_giveaways": self.prepaid_giveaways, "my_boost_slots": self.my_boost_slots}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1230586490, signed=False)
        flags = 0
        if self.my_boost: flags |= 1 << 2
        if self.gift_boosts is not None: flags |= 1 << 4
        if self.next_level_boosts is not None: flags |= 1 << 0
        if self.premium_audience is not None: flags |= 1 << 1
        if self.prepaid_giveaways is not None: flags |= 1 << 3
        if self.my_boost_slots is not None: flags |= 1 << 2
        writer.write_int(flags, signed=False)
        writer.write_int(self.level, signed=True)
        writer.write_int(self.current_level_boosts, signed=True)
        writer.write_int(self.boosts, signed=True)
        if flags & (1 << 4):
            writer.write_int(self.gift_boosts, signed=True)
        if flags & (1 << 0):
            writer.write_int(self.next_level_boosts, signed=True)
        if flags & (1 << 1):
            writer.write(bytes(self.premium_audience))
        writer.write_string(self.boost_url)
        if flags & (1 << 3):
            writer.write(bytes(self.prepaid_giveaways))
        if flags & (1 << 2):
            writer.write(bytes(self.my_boost_slots))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        my_boost = bool(flags & (1 << 2))
        level = reader.read_int()
        current_level_boosts = reader.read_int()
        boosts = reader.read_int()
        if flags & (1 << 4):
            gift_boosts = reader.read_int()
        else:
            gift_boosts = None
        if flags & (1 << 0):
            next_level_boosts = reader.read_int()
        else:
            next_level_boosts = None
        if flags & (1 << 1):
            premium_audience = reader.tgread_object()
        else:
            premium_audience = None
        boost_url = reader.read_string()
        if flags & (1 << 3):
            prepaid_giveaways = reader.tgread_object()
        else:
            prepaid_giveaways = None
        if flags & (1 << 2):
            my_boost_slots = reader.tgread_object()
        else:
            my_boost_slots = None
        return cls(my_boost, level, current_level_boosts, boosts, gift_boosts, next_level_boosts, premium_audience, boost_url, prepaid_giveaways, my_boost_slots)

