"""Auto-generated TL types. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional, TYPE_CHECKING
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

@register
class ChannelsChannelParticipants(TLObject):
    CONSTRUCTOR_ID = 2595290799
    __slots__ = ('count', 'participants', 'chats', 'users')
    def __init__(self, count: int, participants: 'Vector', chats: 'Vector', users: 'Vector'):
        self.count = count
        self.participants = participants
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"count": self.count, "participants": self.participants, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2595290799, signed=False)
        writer.write_int(self.count, signed=True)
        writer.write(bytes(self.participants))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        count = reader.read_int()
        participants = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(count, participants, chats, users)

@register
class ChannelsChannelParticipantsNotModified(TLObject):
    CONSTRUCTOR_ID = 4028055529
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4028055529, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class ChannelsChannelParticipant(TLObject):
    CONSTRUCTOR_ID = 3753378583
    __slots__ = ('participant', 'chats', 'users')
    def __init__(self, participant: 'ChannelParticipant', chats: 'Vector', users: 'Vector'):
        self.participant = participant
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"participant": self.participant, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3753378583, signed=False)
        writer.write(bytes(self.participant))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        participant = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(participant, chats, users)

@register
class ChannelsAdminLogResults(TLObject):
    CONSTRUCTOR_ID = 3985307469
    __slots__ = ('events', 'chats', 'users')
    def __init__(self, events: 'Vector', chats: 'Vector', users: 'Vector'):
        self.events = events
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"events": self.events, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3985307469, signed=False)
        writer.write(bytes(self.events))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        events = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(events, chats, users)

@register
class ChannelsSendAsPeers(TLObject):
    CONSTRUCTOR_ID = 4103516358
    __slots__ = ('peers', 'chats', 'users')
    def __init__(self, peers: 'Vector', chats: 'Vector', users: 'Vector'):
        self.peers = peers
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"peers": self.peers, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4103516358, signed=False)
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
class ChannelsSponsoredMessageReportResultChooseOption(TLObject):
    CONSTRUCTOR_ID = 2221907522
    __slots__ = ('title', 'options')
    def __init__(self, title: str, options: 'Vector'):
        self.title = title
        self.options = options
    def to_dict(self):
        return {"title": self.title, "options": self.options}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2221907522, signed=False)
        writer.write_string(self.title)
        writer.write(bytes(self.options))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        title = reader.read_string()
        options = reader.tgread_object()
        return cls(title, options)

@register
class ChannelsSponsoredMessageReportResultAdsHidden(TLObject):
    CONSTRUCTOR_ID = 1044107055
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1044107055, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class ChannelsSponsoredMessageReportResultReported(TLObject):
    CONSTRUCTOR_ID = 2910423113
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2910423113, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

