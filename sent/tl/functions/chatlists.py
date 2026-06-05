"""Auto-generated TL functions. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

@register
class ChatlistsExportChatlistInvite(TLObject):
    CONSTRUCTOR_ID = 2222081934
    __slots__ = ('chatlist', 'title', 'peers')
    def __init__(self, chatlist: 'InputChatlist', title: str, peers: 'Vector'):
        self.chatlist = chatlist
        self.title = title
        self.peers = peers
    def to_dict(self):
        return {"chatlist": self.chatlist, "title": self.title, "peers": self.peers}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2222081934, signed=False)
        writer.write(bytes(self.chatlist))
        writer.write_string(self.title)
        writer.write(bytes(self.peers))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        chatlist = reader.tgread_object()
        title = reader.read_string()
        peers = reader.tgread_object()
        return cls(chatlist, title, peers)

@register
class ChatlistsDeleteExportedInvite(TLObject):
    CONSTRUCTOR_ID = 1906072670
    __slots__ = ('chatlist', 'slug')
    def __init__(self, chatlist: 'InputChatlist', slug: str):
        self.chatlist = chatlist
        self.slug = slug
    def to_dict(self):
        return {"chatlist": self.chatlist, "slug": self.slug}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1906072670, signed=False)
        writer.write(bytes(self.chatlist))
        writer.write_string(self.slug)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        chatlist = reader.tgread_object()
        slug = reader.read_string()
        return cls(chatlist, slug)

@register
class ChatlistsEditExportedInvite(TLObject):
    CONSTRUCTOR_ID = 1698543165
    __slots__ = ('chatlist', 'slug', 'title', 'peers')
    def __init__(self, chatlist: 'InputChatlist', slug: str, title: str = None, peers: 'Vector' = None):
        self.chatlist = chatlist
        self.slug = slug
        self.title = title
        self.peers = peers
    def to_dict(self):
        return {"chatlist": self.chatlist, "slug": self.slug, "title": self.title, "peers": self.peers}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1698543165, signed=False)
        flags = 0
        if self.title is not None: flags |= 1 << 1
        if self.peers is not None: flags |= 1 << 2
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.chatlist))
        writer.write_string(self.slug)
        if flags & (1 << 1):
            writer.write_string(self.title)
        if flags & (1 << 2):
            writer.write(bytes(self.peers))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        chatlist = reader.tgread_object()
        slug = reader.read_string()
        if flags & (1 << 1):
            title = reader.read_string()
        else:
            title = None
        if flags & (1 << 2):
            peers = reader.tgread_object()
        else:
            peers = None
        return cls(chatlist, slug, title, peers)

@register
class ChatlistsGetExportedInvites(TLObject):
    CONSTRUCTOR_ID = 3456359043
    __slots__ = ('chatlist')
    def __init__(self, chatlist: 'InputChatlist'):
        self.chatlist = chatlist
    def to_dict(self):
        return {"chatlist": self.chatlist}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3456359043, signed=False)
        writer.write(bytes(self.chatlist))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        chatlist = reader.tgread_object()
        return cls(chatlist)

@register
class ChatlistsCheckChatlistInvite(TLObject):
    CONSTRUCTOR_ID = 1103171583
    __slots__ = ('slug')
    def __init__(self, slug: str):
        self.slug = slug
    def to_dict(self):
        return {"slug": self.slug}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1103171583, signed=False)
        writer.write_string(self.slug)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        slug = reader.read_string()
        return cls(slug)

@register
class ChatlistsJoinChatlistInvite(TLObject):
    CONSTRUCTOR_ID = 2796675994
    __slots__ = ('slug', 'peers')
    def __init__(self, slug: str, peers: 'Vector'):
        self.slug = slug
        self.peers = peers
    def to_dict(self):
        return {"slug": self.slug, "peers": self.peers}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2796675994, signed=False)
        writer.write_string(self.slug)
        writer.write(bytes(self.peers))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        slug = reader.read_string()
        peers = reader.tgread_object()
        return cls(slug, peers)

@register
class ChatlistsGetChatlistUpdates(TLObject):
    CONSTRUCTOR_ID = 2302776609
    __slots__ = ('chatlist')
    def __init__(self, chatlist: 'InputChatlist'):
        self.chatlist = chatlist
    def to_dict(self):
        return {"chatlist": self.chatlist}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2302776609, signed=False)
        writer.write(bytes(self.chatlist))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        chatlist = reader.tgread_object()
        return cls(chatlist)

@register
class ChatlistsJoinChatlistUpdates(TLObject):
    CONSTRUCTOR_ID = 3767138549
    __slots__ = ('chatlist', 'peers')
    def __init__(self, chatlist: 'InputChatlist', peers: 'Vector'):
        self.chatlist = chatlist
        self.peers = peers
    def to_dict(self):
        return {"chatlist": self.chatlist, "peers": self.peers}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3767138549, signed=False)
        writer.write(bytes(self.chatlist))
        writer.write(bytes(self.peers))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        chatlist = reader.tgread_object()
        peers = reader.tgread_object()
        return cls(chatlist, peers)

@register
class ChatlistsHideChatlistUpdates(TLObject):
    CONSTRUCTOR_ID = 1726252795
    __slots__ = ('chatlist')
    def __init__(self, chatlist: 'InputChatlist'):
        self.chatlist = chatlist
    def to_dict(self):
        return {"chatlist": self.chatlist}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1726252795, signed=False)
        writer.write(bytes(self.chatlist))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        chatlist = reader.tgread_object()
        return cls(chatlist)

@register
class ChatlistsGetLeaveChatlistSuggestions(TLObject):
    CONSTRUCTOR_ID = 4257011476
    __slots__ = ('chatlist')
    def __init__(self, chatlist: 'InputChatlist'):
        self.chatlist = chatlist
    def to_dict(self):
        return {"chatlist": self.chatlist}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4257011476, signed=False)
        writer.write(bytes(self.chatlist))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        chatlist = reader.tgread_object()
        return cls(chatlist)

@register
class ChatlistsLeaveChatlist(TLObject):
    CONSTRUCTOR_ID = 1962598714
    __slots__ = ('chatlist', 'peers')
    def __init__(self, chatlist: 'InputChatlist', peers: 'Vector'):
        self.chatlist = chatlist
        self.peers = peers
    def to_dict(self):
        return {"chatlist": self.chatlist, "peers": self.peers}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1962598714, signed=False)
        writer.write(bytes(self.chatlist))
        writer.write(bytes(self.peers))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        chatlist = reader.tgread_object()
        peers = reader.tgread_object()
        return cls(chatlist, peers)

