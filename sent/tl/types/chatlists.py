"""Auto-generated TL types. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional, TYPE_CHECKING
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

@register
class ChatlistsExportedChatlistInvite(TLObject):
    CONSTRUCTOR_ID = 283567014
    __slots__ = ('filter', 'invite')
    def __init__(self, filter: 'DialogFilter', invite: 'ExportedChatlistInvite'):
        self.filter = filter
        self.invite = invite
    def to_dict(self):
        return {"filter": self.filter, "invite": self.invite}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(283567014, signed=False)
        writer.write(bytes(self.filter))
        writer.write(bytes(self.invite))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        filter = reader.tgread_object()
        invite = reader.tgread_object()
        return cls(filter, invite)

@register
class ChatlistsExportedInvites(TLObject):
    CONSTRUCTOR_ID = 279670215
    __slots__ = ('invites', 'chats', 'users')
    def __init__(self, invites: 'Vector', chats: 'Vector', users: 'Vector'):
        self.invites = invites
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"invites": self.invites, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(279670215, signed=False)
        writer.write(bytes(self.invites))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        invites = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(invites, chats, users)

@register
class ChatlistsChatlistInviteAlready(TLObject):
    CONSTRUCTOR_ID = 4203214425
    __slots__ = ('filter_id', 'missing_peers', 'already_peers', 'chats', 'users')
    def __init__(self, filter_id: int, missing_peers: 'Vector', already_peers: 'Vector', chats: 'Vector', users: 'Vector'):
        self.filter_id = filter_id
        self.missing_peers = missing_peers
        self.already_peers = already_peers
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"filter_id": self.filter_id, "missing_peers": self.missing_peers, "already_peers": self.already_peers, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4203214425, signed=False)
        writer.write_int(self.filter_id, signed=True)
        writer.write(bytes(self.missing_peers))
        writer.write(bytes(self.already_peers))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        filter_id = reader.read_int()
        missing_peers = reader.tgread_object()
        already_peers = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(filter_id, missing_peers, already_peers, chats, users)

@register
class ChatlistsChatlistInvite(TLObject):
    CONSTRUCTOR_ID = 4044279343
    __slots__ = ('title_noanimate', 'title', 'emoticon', 'peers', 'chats', 'users')
    def __init__(self, title: 'TextWithEntities', peers: 'Vector', chats: 'Vector', users: 'Vector', title_noanimate: bool = None, emoticon: str = None):
        self.title_noanimate = title_noanimate
        self.title = title
        self.emoticon = emoticon
        self.peers = peers
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"title_noanimate": self.title_noanimate, "title": self.title, "emoticon": self.emoticon, "peers": self.peers, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4044279343, signed=False)
        flags = 0
        if self.title_noanimate: flags |= 1 << 1
        if self.emoticon is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.title))
        if flags & (1 << 0):
            writer.write_string(self.emoticon)
        writer.write(bytes(self.peers))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        title_noanimate = bool(flags & (1 << 1))
        title = reader.tgread_object()
        if flags & (1 << 0):
            emoticon = reader.read_string()
        else:
            emoticon = None
        peers = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(title_noanimate, title, emoticon, peers, chats, users)

@register
class ChatlistsChatlistUpdates(TLObject):
    CONSTRUCTOR_ID = 2478671757
    __slots__ = ('missing_peers', 'chats', 'users')
    def __init__(self, missing_peers: 'Vector', chats: 'Vector', users: 'Vector'):
        self.missing_peers = missing_peers
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"missing_peers": self.missing_peers, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2478671757, signed=False)
        writer.write(bytes(self.missing_peers))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        missing_peers = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(missing_peers, chats, users)

