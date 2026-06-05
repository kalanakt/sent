"""Auto-generated TL types. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional, TYPE_CHECKING
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

@register
class ContactsContactsNotModified(TLObject):
    CONSTRUCTOR_ID = 3075189202
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3075189202, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class ContactsContacts(TLObject):
    CONSTRUCTOR_ID = 3941105218
    __slots__ = ('contacts', 'saved_count', 'users')
    def __init__(self, contacts: 'Vector', saved_count: int, users: 'Vector'):
        self.contacts = contacts
        self.saved_count = saved_count
        self.users = users
    def to_dict(self):
        return {"contacts": self.contacts, "saved_count": self.saved_count, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3941105218, signed=False)
        writer.write(bytes(self.contacts))
        writer.write_int(self.saved_count, signed=True)
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        contacts = reader.tgread_object()
        saved_count = reader.read_int()
        users = reader.tgread_object()
        return cls(contacts, saved_count, users)

@register
class ContactsImportedContacts(TLObject):
    CONSTRUCTOR_ID = 2010127419
    __slots__ = ('imported', 'popular_invites', 'retry_contacts', 'users')
    def __init__(self, imported: 'Vector', popular_invites: 'Vector', retry_contacts: 'Vector', users: 'Vector'):
        self.imported = imported
        self.popular_invites = popular_invites
        self.retry_contacts = retry_contacts
        self.users = users
    def to_dict(self):
        return {"imported": self.imported, "popular_invites": self.popular_invites, "retry_contacts": self.retry_contacts, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2010127419, signed=False)
        writer.write(bytes(self.imported))
        writer.write(bytes(self.popular_invites))
        writer.write(bytes(self.retry_contacts))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        imported = reader.tgread_object()
        popular_invites = reader.tgread_object()
        retry_contacts = reader.tgread_object()
        users = reader.tgread_object()
        return cls(imported, popular_invites, retry_contacts, users)

@register
class ContactsBlocked(TLObject):
    CONSTRUCTOR_ID = 182326673
    __slots__ = ('blocked', 'chats', 'users')
    def __init__(self, blocked: 'Vector', chats: 'Vector', users: 'Vector'):
        self.blocked = blocked
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"blocked": self.blocked, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(182326673, signed=False)
        writer.write(bytes(self.blocked))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        blocked = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(blocked, chats, users)

@register
class ContactsBlockedSlice(TLObject):
    CONSTRUCTOR_ID = 3781575060
    __slots__ = ('count', 'blocked', 'chats', 'users')
    def __init__(self, count: int, blocked: 'Vector', chats: 'Vector', users: 'Vector'):
        self.count = count
        self.blocked = blocked
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"count": self.count, "blocked": self.blocked, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3781575060, signed=False)
        writer.write_int(self.count, signed=True)
        writer.write(bytes(self.blocked))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        count = reader.read_int()
        blocked = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(count, blocked, chats, users)

@register
class ContactsFound(TLObject):
    CONSTRUCTOR_ID = 3004386717
    __slots__ = ('my_results', 'results', 'chats', 'users')
    def __init__(self, my_results: 'Vector', results: 'Vector', chats: 'Vector', users: 'Vector'):
        self.my_results = my_results
        self.results = results
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"my_results": self.my_results, "results": self.results, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3004386717, signed=False)
        writer.write(bytes(self.my_results))
        writer.write(bytes(self.results))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        my_results = reader.tgread_object()
        results = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(my_results, results, chats, users)

@register
class ContactsResolvedPeer(TLObject):
    CONSTRUCTOR_ID = 2131196633
    __slots__ = ('peer', 'chats', 'users')
    def __init__(self, peer: 'Peer', chats: 'Vector', users: 'Vector'):
        self.peer = peer
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"peer": self.peer, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2131196633, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(peer, chats, users)

@register
class ContactsTopPeersNotModified(TLObject):
    CONSTRUCTOR_ID = 3727060725
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3727060725, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class ContactsTopPeers(TLObject):
    CONSTRUCTOR_ID = 1891070632
    __slots__ = ('categories', 'chats', 'users')
    def __init__(self, categories: 'Vector', chats: 'Vector', users: 'Vector'):
        self.categories = categories
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"categories": self.categories, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1891070632, signed=False)
        writer.write(bytes(self.categories))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        categories = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(categories, chats, users)

@register
class ContactsTopPeersDisabled(TLObject):
    CONSTRUCTOR_ID = 3039597469
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3039597469, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class ContactsContactBirthdays(TLObject):
    CONSTRUCTOR_ID = 290452237
    __slots__ = ('contacts', 'users')
    def __init__(self, contacts: 'Vector', users: 'Vector'):
        self.contacts = contacts
        self.users = users
    def to_dict(self):
        return {"contacts": self.contacts, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(290452237, signed=False)
        writer.write(bytes(self.contacts))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        contacts = reader.tgread_object()
        users = reader.tgread_object()
        return cls(contacts, users)

@register
class ContactsSponsoredPeersEmpty(TLObject):
    CONSTRUCTOR_ID = 3929191601
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3929191601, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class ContactsSponsoredPeers(TLObject):
    CONSTRUCTOR_ID = 3942852740
    __slots__ = ('peers', 'chats', 'users')
    def __init__(self, peers: 'Vector', chats: 'Vector', users: 'Vector'):
        self.peers = peers
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"peers": self.peers, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3942852740, signed=False)
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

