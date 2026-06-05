"""Auto-generated TL types. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional, TYPE_CHECKING
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

@register
class UploadFile(TLObject):
    CONSTRUCTOR_ID = 157948117
    __slots__ = ('type_', 'mtime', 'bytes')
    def __init__(self, type_: 'StorageFileType', mtime: int, bytes: bytes):
        self.type_ = type_
        self.mtime = mtime
        self.bytes = bytes
    def to_dict(self):
        return {"type": self.type_, "mtime": self.mtime, "bytes": self.bytes}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(157948117, signed=False)
        writer.write(bytes(self.type_))
        writer.write_int(self.mtime, signed=True)
        writer.write_bytes(self.bytes)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        type_ = reader.tgread_object()
        mtime = reader.read_int()
        bytes = reader.read_bytes()
        return cls(type_, mtime, bytes)

@register
class UploadFileCdnRedirect(TLObject):
    CONSTRUCTOR_ID = 4052539972
    __slots__ = ('dc_id', 'file_token', 'encryption_key', 'encryption_iv', 'file_hashes')
    def __init__(self, dc_id: int, file_token: bytes, encryption_key: bytes, encryption_iv: bytes, file_hashes: 'Vector'):
        self.dc_id = dc_id
        self.file_token = file_token
        self.encryption_key = encryption_key
        self.encryption_iv = encryption_iv
        self.file_hashes = file_hashes
    def to_dict(self):
        return {"dc_id": self.dc_id, "file_token": self.file_token, "encryption_key": self.encryption_key, "encryption_iv": self.encryption_iv, "file_hashes": self.file_hashes}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4052539972, signed=False)
        writer.write_int(self.dc_id, signed=True)
        writer.write_bytes(self.file_token)
        writer.write_bytes(self.encryption_key)
        writer.write_bytes(self.encryption_iv)
        writer.write(bytes(self.file_hashes))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        dc_id = reader.read_int()
        file_token = reader.read_bytes()
        encryption_key = reader.read_bytes()
        encryption_iv = reader.read_bytes()
        file_hashes = reader.tgread_object()
        return cls(dc_id, file_token, encryption_key, encryption_iv, file_hashes)

@register
class UploadWebFile(TLObject):
    CONSTRUCTOR_ID = 568808380
    __slots__ = ('size', 'mime_type', 'file_type', 'mtime', 'bytes')
    def __init__(self, size: int, mime_type: str, file_type: 'StorageFileType', mtime: int, bytes: bytes):
        self.size = size
        self.mime_type = mime_type
        self.file_type = file_type
        self.mtime = mtime
        self.bytes = bytes
    def to_dict(self):
        return {"size": self.size, "mime_type": self.mime_type, "file_type": self.file_type, "mtime": self.mtime, "bytes": self.bytes}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(568808380, signed=False)
        writer.write_int(self.size, signed=True)
        writer.write_string(self.mime_type)
        writer.write(bytes(self.file_type))
        writer.write_int(self.mtime, signed=True)
        writer.write_bytes(self.bytes)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        size = reader.read_int()
        mime_type = reader.read_string()
        file_type = reader.tgread_object()
        mtime = reader.read_int()
        bytes = reader.read_bytes()
        return cls(size, mime_type, file_type, mtime, bytes)

@register
class UploadCdnFileReuploadNeeded(TLObject):
    CONSTRUCTOR_ID = 4004045934
    __slots__ = ('request_token')
    def __init__(self, request_token: bytes):
        self.request_token = request_token
    def to_dict(self):
        return {"request_token": self.request_token}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4004045934, signed=False)
        writer.write_bytes(self.request_token)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        request_token = reader.read_bytes()
        return cls(request_token)

@register
class UploadCdnFile(TLObject):
    CONSTRUCTOR_ID = 2845821519
    __slots__ = ('bytes')
    def __init__(self, bytes: bytes):
        self.bytes = bytes
    def to_dict(self):
        return {"bytes": self.bytes}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2845821519, signed=False)
        writer.write_bytes(self.bytes)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        bytes = reader.read_bytes()
        return cls(bytes)

