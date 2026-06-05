"""Auto-generated TL types. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional, TYPE_CHECKING
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

@register
class PhotosPhotos(TLObject):
    CONSTRUCTOR_ID = 2378853029
    __slots__ = ('photos', 'users')
    def __init__(self, photos: 'Vector', users: 'Vector'):
        self.photos = photos
        self.users = users
    def to_dict(self):
        return {"photos": self.photos, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2378853029, signed=False)
        writer.write(bytes(self.photos))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        photos = reader.tgread_object()
        users = reader.tgread_object()
        return cls(photos, users)

@register
class PhotosPhotosSlice(TLObject):
    CONSTRUCTOR_ID = 352657236
    __slots__ = ('count', 'photos', 'users')
    def __init__(self, count: int, photos: 'Vector', users: 'Vector'):
        self.count = count
        self.photos = photos
        self.users = users
    def to_dict(self):
        return {"count": self.count, "photos": self.photos, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(352657236, signed=False)
        writer.write_int(self.count, signed=True)
        writer.write(bytes(self.photos))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        count = reader.read_int()
        photos = reader.tgread_object()
        users = reader.tgread_object()
        return cls(count, photos, users)

@register
class PhotosPhoto(TLObject):
    CONSTRUCTOR_ID = 539045032
    __slots__ = ('photo', 'users')
    def __init__(self, photo: 'Photo', users: 'Vector'):
        self.photo = photo
        self.users = users
    def to_dict(self):
        return {"photo": self.photo, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(539045032, signed=False)
        writer.write(bytes(self.photo))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        photo = reader.tgread_object()
        users = reader.tgread_object()
        return cls(photo, users)

