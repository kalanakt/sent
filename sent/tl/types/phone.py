"""Auto-generated TL types. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional, TYPE_CHECKING
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

@register
class PhonePhoneCall(TLObject):
    CONSTRUCTOR_ID = 3968000320
    __slots__ = ('phone_call', 'users')
    def __init__(self, phone_call: 'PhoneCall', users: 'Vector'):
        self.phone_call = phone_call
        self.users = users
    def to_dict(self):
        return {"phone_call": self.phone_call, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3968000320, signed=False)
        writer.write(bytes(self.phone_call))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        phone_call = reader.tgread_object()
        users = reader.tgread_object()
        return cls(phone_call, users)

@register
class PhoneGroupCall(TLObject):
    CONSTRUCTOR_ID = 2658302637
    __slots__ = ('call', 'participants', 'participants_next_offset', 'chats', 'users')
    def __init__(self, call: 'GroupCall', participants: 'Vector', participants_next_offset: str, chats: 'Vector', users: 'Vector'):
        self.call = call
        self.participants = participants
        self.participants_next_offset = participants_next_offset
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"call": self.call, "participants": self.participants, "participants_next_offset": self.participants_next_offset, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2658302637, signed=False)
        writer.write(bytes(self.call))
        writer.write(bytes(self.participants))
        writer.write_string(self.participants_next_offset)
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        call = reader.tgread_object()
        participants = reader.tgread_object()
        participants_next_offset = reader.read_string()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(call, participants, participants_next_offset, chats, users)

@register
class PhoneGroupParticipants(TLObject):
    CONSTRUCTOR_ID = 4101460406
    __slots__ = ('count', 'participants', 'next_offset', 'chats', 'users', 'version')
    def __init__(self, count: int, participants: 'Vector', next_offset: str, chats: 'Vector', users: 'Vector', version: int):
        self.count = count
        self.participants = participants
        self.next_offset = next_offset
        self.chats = chats
        self.users = users
        self.version = version
    def to_dict(self):
        return {"count": self.count, "participants": self.participants, "next_offset": self.next_offset, "chats": self.chats, "users": self.users, "version": self.version}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4101460406, signed=False)
        writer.write_int(self.count, signed=True)
        writer.write(bytes(self.participants))
        writer.write_string(self.next_offset)
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        writer.write_int(self.version, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        count = reader.read_int()
        participants = reader.tgread_object()
        next_offset = reader.read_string()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        version = reader.read_int()
        return cls(count, participants, next_offset, chats, users, version)

@register
class PhoneJoinAsPeers(TLObject):
    CONSTRUCTOR_ID = 2951045695
    __slots__ = ('peers', 'chats', 'users')
    def __init__(self, peers: 'Vector', chats: 'Vector', users: 'Vector'):
        self.peers = peers
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"peers": self.peers, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2951045695, signed=False)
        writer.write(bytes(self.peers))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peers = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(peers, chats, users)

@register
class PhoneExportedGroupCallInvite(TLObject):
    CONSTRUCTOR_ID = 541839704
    __slots__ = ('link')
    def __init__(self, link: str):
        self.link = link
    def to_dict(self):
        return {"link": self.link}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(541839704, signed=False)
        writer.write_string(self.link)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        link = reader.read_string()
        return cls(link)

@register
class PhoneGroupCallStreamChannels(TLObject):
    CONSTRUCTOR_ID = 3504636594
    __slots__ = ('channels')
    def __init__(self, channels: 'Vector'):
        self.channels = channels
    def to_dict(self):
        return {"channels": self.channels}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3504636594, signed=False)
        writer.write(bytes(self.channels))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        channels = reader.tgread_object()
        return cls(channels)

@register
class PhoneGroupCallStreamRtmpUrl(TLObject):
    CONSTRUCTOR_ID = 767505458
    __slots__ = ('url', 'key')
    def __init__(self, url: str, key: str):
        self.url = url
        self.key = key
    def to_dict(self):
        return {"url": self.url, "key": self.key}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(767505458, signed=False)
        writer.write_string(self.url)
        writer.write_string(self.key)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        url = reader.read_string()
        key = reader.read_string()
        return cls(url, key)

@register
class PhoneGroupCallStars(TLObject):
    CONSTRUCTOR_ID = 2635971878
    __slots__ = ('total_stars', 'top_donors', 'chats', 'users')
    def __init__(self, total_stars: int, top_donors: 'Vector', chats: 'Vector', users: 'Vector'):
        self.total_stars = total_stars
        self.top_donors = top_donors
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"total_stars": self.total_stars, "top_donors": self.top_donors, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2635971878, signed=False)
        writer.write_long(self.total_stars, signed=False)
        writer.write(bytes(self.top_donors))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        total_stars = reader.read_long()
        top_donors = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(total_stars, top_donors, chats, users)

