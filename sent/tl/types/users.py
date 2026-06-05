"""Auto-generated TL types. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional, TYPE_CHECKING
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

@register
class UsersUserFull(TLObject):
    CONSTRUCTOR_ID = 997004590
    __slots__ = ('full_user', 'chats', 'users')
    def __init__(self, full_user: 'UserFull', chats: 'Vector', users: 'Vector'):
        self.full_user = full_user
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"full_user": self.full_user, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(997004590, signed=False)
        writer.write(bytes(self.full_user))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        full_user = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(full_user, chats, users)

@register
class UsersUsers(TLObject):
    CONSTRUCTOR_ID = 1658259128
    __slots__ = ('users')
    def __init__(self, users: 'Vector'):
        self.users = users
    def to_dict(self):
        return {"users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1658259128, signed=False)
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        users = reader.tgread_object()
        return cls(users)

@register
class UsersUsersSlice(TLObject):
    CONSTRUCTOR_ID = 828000628
    __slots__ = ('count', 'users')
    def __init__(self, count: int, users: 'Vector'):
        self.count = count
        self.users = users
    def to_dict(self):
        return {"count": self.count, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(828000628, signed=False)
        writer.write_int(self.count, signed=True)
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        count = reader.read_int()
        users = reader.tgread_object()
        return cls(count, users)

@register
class UsersSavedMusicNotModified(TLObject):
    CONSTRUCTOR_ID = 3817310884
    __slots__ = ('count')
    def __init__(self, count: int):
        self.count = count
    def to_dict(self):
        return {"count": self.count}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3817310884, signed=False)
        writer.write_int(self.count, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        count = reader.read_int()
        return cls(count)

@register
class UsersSavedMusic(TLObject):
    CONSTRUCTOR_ID = 883094167
    __slots__ = ('count', 'documents')
    def __init__(self, count: int, documents: 'Vector'):
        self.count = count
        self.documents = documents
    def to_dict(self):
        return {"count": self.count, "documents": self.documents}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(883094167, signed=False)
        writer.write_int(self.count, signed=True)
        writer.write(bytes(self.documents))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        count = reader.read_int()
        documents = reader.tgread_object()
        return cls(count, documents)

