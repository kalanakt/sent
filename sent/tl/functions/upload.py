"""Auto-generated TL functions. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

@register
class UploadSaveFilePart(TLObject):
    CONSTRUCTOR_ID = 3003426337
    __slots__ = ('file_id', 'file_part', 'bytes')
    def __init__(self, file_id: int, file_part: int, bytes: bytes):
        self.file_id = file_id
        self.file_part = file_part
        self.bytes = bytes
    def to_dict(self):
        return {"file_id": self.file_id, "file_part": self.file_part, "bytes": self.bytes}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3003426337, signed=False)
        writer.write_long(self.file_id, signed=False)
        writer.write_int(self.file_part, signed=True)
        writer.write_bytes(self.bytes)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        file_id = reader.read_long()
        file_part = reader.read_int()
        bytes = reader.read_bytes()
        return cls(file_id, file_part, bytes)

@register
class UploadGetFile(TLObject):
    CONSTRUCTOR_ID = 3193124286
    __slots__ = ('precise', 'cdn_supported', 'location', 'offset', 'limit')
    def __init__(self, location: 'InputFileLocation', offset: int, limit: int, precise: bool = None, cdn_supported: bool = None):
        self.precise = precise
        self.cdn_supported = cdn_supported
        self.location = location
        self.offset = offset
        self.limit = limit
    def to_dict(self):
        return {"precise": self.precise, "cdn_supported": self.cdn_supported, "location": self.location, "offset": self.offset, "limit": self.limit}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3193124286, signed=False)
        flags = 0
        if self.precise: flags |= 1 << 0
        if self.cdn_supported: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.location))
        writer.write_long(self.offset, signed=False)
        writer.write_int(self.limit, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        precise = bool(flags & (1 << 0))
        cdn_supported = bool(flags & (1 << 1))
        location = reader.tgread_object()
        offset = reader.read_long()
        limit = reader.read_int()
        return cls(precise, cdn_supported, location, offset, limit)

@register
class UploadSaveBigFilePart(TLObject):
    CONSTRUCTOR_ID = 3732629309
    __slots__ = ('file_id', 'file_part', 'file_total_parts', 'bytes')
    def __init__(self, file_id: int, file_part: int, file_total_parts: int, bytes: bytes):
        self.file_id = file_id
        self.file_part = file_part
        self.file_total_parts = file_total_parts
        self.bytes = bytes
    def to_dict(self):
        return {"file_id": self.file_id, "file_part": self.file_part, "file_total_parts": self.file_total_parts, "bytes": self.bytes}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3732629309, signed=False)
        writer.write_long(self.file_id, signed=False)
        writer.write_int(self.file_part, signed=True)
        writer.write_int(self.file_total_parts, signed=True)
        writer.write_bytes(self.bytes)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        file_id = reader.read_long()
        file_part = reader.read_int()
        file_total_parts = reader.read_int()
        bytes = reader.read_bytes()
        return cls(file_id, file_part, file_total_parts, bytes)

@register
class UploadGetWebFile(TLObject):
    CONSTRUCTOR_ID = 619086221
    __slots__ = ('location', 'offset', 'limit')
    def __init__(self, location: 'InputWebFileLocation', offset: int, limit: int):
        self.location = location
        self.offset = offset
        self.limit = limit
    def to_dict(self):
        return {"location": self.location, "offset": self.offset, "limit": self.limit}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(619086221, signed=False)
        writer.write(bytes(self.location))
        writer.write_int(self.offset, signed=True)
        writer.write_int(self.limit, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        location = reader.tgread_object()
        offset = reader.read_int()
        limit = reader.read_int()
        return cls(location, offset, limit)

@register
class UploadGetCdnFile(TLObject):
    CONSTRUCTOR_ID = 962554330
    __slots__ = ('file_token', 'offset', 'limit')
    def __init__(self, file_token: bytes, offset: int, limit: int):
        self.file_token = file_token
        self.offset = offset
        self.limit = limit
    def to_dict(self):
        return {"file_token": self.file_token, "offset": self.offset, "limit": self.limit}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(962554330, signed=False)
        writer.write_bytes(self.file_token)
        writer.write_long(self.offset, signed=False)
        writer.write_int(self.limit, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        file_token = reader.read_bytes()
        offset = reader.read_long()
        limit = reader.read_int()
        return cls(file_token, offset, limit)

@register
class UploadReuploadCdnFile(TLObject):
    CONSTRUCTOR_ID = 2603046056
    __slots__ = ('file_token', 'request_token')
    def __init__(self, file_token: bytes, request_token: bytes):
        self.file_token = file_token
        self.request_token = request_token
    def to_dict(self):
        return {"file_token": self.file_token, "request_token": self.request_token}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2603046056, signed=False)
        writer.write_bytes(self.file_token)
        writer.write_bytes(self.request_token)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        file_token = reader.read_bytes()
        request_token = reader.read_bytes()
        return cls(file_token, request_token)

@register
class UploadGetCdnFileHashes(TLObject):
    CONSTRUCTOR_ID = 2447130417
    __slots__ = ('file_token', 'offset')
    def __init__(self, file_token: bytes, offset: int):
        self.file_token = file_token
        self.offset = offset
    def to_dict(self):
        return {"file_token": self.file_token, "offset": self.offset}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2447130417, signed=False)
        writer.write_bytes(self.file_token)
        writer.write_long(self.offset, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        file_token = reader.read_bytes()
        offset = reader.read_long()
        return cls(file_token, offset)

@register
class UploadGetFileHashes(TLObject):
    CONSTRUCTOR_ID = 2438371370
    __slots__ = ('location', 'offset')
    def __init__(self, location: 'InputFileLocation', offset: int):
        self.location = location
        self.offset = offset
    def to_dict(self):
        return {"location": self.location, "offset": self.offset}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2438371370, signed=False)
        writer.write(bytes(self.location))
        writer.write_long(self.offset, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        location = reader.tgread_object()
        offset = reader.read_long()
        return cls(location, offset)

