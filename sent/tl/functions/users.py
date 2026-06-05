"""Auto-generated TL functions. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

@register
class UsersGetUsers(TLObject):
    CONSTRUCTOR_ID = 227648840
    __slots__ = ('id')
    def __init__(self, id: 'Vector'):
        self.id = id
    def to_dict(self):
        return {"id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(227648840, signed=False)
        writer.write(bytes(self.id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        id = reader.tgread_object()
        return cls(id)

@register
class UsersGetFullUser(TLObject):
    CONSTRUCTOR_ID = 3054459160
    __slots__ = ('id')
    def __init__(self, id: 'InputUser'):
        self.id = id
    def to_dict(self):
        return {"id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3054459160, signed=False)
        writer.write(bytes(self.id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        id = reader.tgread_object()
        return cls(id)

@register
class UsersSetSecureValueErrors(TLObject):
    CONSTRUCTOR_ID = 2429064373
    __slots__ = ('id', 'errors')
    def __init__(self, id: 'InputUser', errors: 'Vector'):
        self.id = id
        self.errors = errors
    def to_dict(self):
        return {"id": self.id, "errors": self.errors}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2429064373, signed=False)
        writer.write(bytes(self.id))
        writer.write(bytes(self.errors))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        id = reader.tgread_object()
        errors = reader.tgread_object()
        return cls(id, errors)

@register
class UsersGetRequirementsToContact(TLObject):
    CONSTRUCTOR_ID = 3634004899
    __slots__ = ('id')
    def __init__(self, id: 'Vector'):
        self.id = id
    def to_dict(self):
        return {"id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3634004899, signed=False)
        writer.write(bytes(self.id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        id = reader.tgread_object()
        return cls(id)

@register
class UsersGetSavedMusic(TLObject):
    CONSTRUCTOR_ID = 2022539235
    __slots__ = ('id', 'offset', 'limit', 'hash')
    def __init__(self, id: 'InputUser', offset: int, limit: int, hash: int):
        self.id = id
        self.offset = offset
        self.limit = limit
        self.hash = hash
    def to_dict(self):
        return {"id": self.id, "offset": self.offset, "limit": self.limit, "hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2022539235, signed=False)
        writer.write(bytes(self.id))
        writer.write_int(self.offset, signed=True)
        writer.write_int(self.limit, signed=True)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        id = reader.tgread_object()
        offset = reader.read_int()
        limit = reader.read_int()
        hash = reader.read_long()
        return cls(id, offset, limit, hash)

@register
class UsersGetSavedMusicByID(TLObject):
    CONSTRUCTOR_ID = 1970513129
    __slots__ = ('id', 'documents')
    def __init__(self, id: 'InputUser', documents: 'Vector'):
        self.id = id
        self.documents = documents
    def to_dict(self):
        return {"id": self.id, "documents": self.documents}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1970513129, signed=False)
        writer.write(bytes(self.id))
        writer.write(bytes(self.documents))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        id = reader.tgread_object()
        documents = reader.tgread_object()
        return cls(id, documents)

@register
class UsersSuggestBirthday(TLObject):
    CONSTRUCTOR_ID = 4233311090
    __slots__ = ('id', 'birthday')
    def __init__(self, id: 'InputUser', birthday: 'Birthday'):
        self.id = id
        self.birthday = birthday
    def to_dict(self):
        return {"id": self.id, "birthday": self.birthday}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4233311090, signed=False)
        writer.write(bytes(self.id))
        writer.write(bytes(self.birthday))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        id = reader.tgread_object()
        birthday = reader.tgread_object()
        return cls(id, birthday)

