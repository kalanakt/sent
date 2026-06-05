"""Auto-generated TL functions. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

@register
class SmsjobsIsEligibleToJoin(TLObject):
    CONSTRUCTOR_ID = 249313744
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(249313744, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class SmsjobsJoin(TLObject):
    CONSTRUCTOR_ID = 2806959661
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2806959661, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class SmsjobsLeave(TLObject):
    CONSTRUCTOR_ID = 2560142707
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2560142707, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class SmsjobsUpdateSettings(TLObject):
    CONSTRUCTOR_ID = 155164863
    __slots__ = ('allow_international')
    def __init__(self, allow_international: bool = None):
        self.allow_international = allow_international
    def to_dict(self):
        return {"allow_international": self.allow_international}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(155164863, signed=False)
        flags = 0
        if self.allow_international: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        allow_international = bool(flags & (1 << 0))
        return cls(allow_international)

@register
class SmsjobsGetStatus(TLObject):
    CONSTRUCTOR_ID = 279353576
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(279353576, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class SmsjobsGetSmsJob(TLObject):
    CONSTRUCTOR_ID = 2005766191
    __slots__ = ('job_id')
    def __init__(self, job_id: str):
        self.job_id = job_id
    def to_dict(self):
        return {"job_id": self.job_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2005766191, signed=False)
        writer.write_string(self.job_id)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        job_id = reader.read_string()
        return cls(job_id)

@register
class SmsjobsFinishJob(TLObject):
    CONSTRUCTOR_ID = 1327415076
    __slots__ = ('job_id', 'error')
    def __init__(self, job_id: str, error: str = None):
        self.job_id = job_id
        self.error = error
    def to_dict(self):
        return {"job_id": self.job_id, "error": self.error}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1327415076, signed=False)
        flags = 0
        if self.error is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write_string(self.job_id)
        if flags & (1 << 0):
            writer.write_string(self.error)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        job_id = reader.read_string()
        if flags & (1 << 0):
            error = reader.read_string()
        else:
            error = None
        return cls(job_id, error)

