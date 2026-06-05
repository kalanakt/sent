"""Auto-generated TL types. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional, TYPE_CHECKING
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

@register
class SmsjobsEligibleToJoin(TLObject):
    CONSTRUCTOR_ID = 3700114639
    __slots__ = ('terms_url', 'monthly_sent_sms')
    def __init__(self, terms_url: str, monthly_sent_sms: int):
        self.terms_url = terms_url
        self.monthly_sent_sms = monthly_sent_sms
    def to_dict(self):
        return {"terms_url": self.terms_url, "monthly_sent_sms": self.monthly_sent_sms}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3700114639, signed=False)
        writer.write_string(self.terms_url)
        writer.write_int(self.monthly_sent_sms, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        terms_url = reader.read_string()
        monthly_sent_sms = reader.read_int()
        return cls(terms_url, monthly_sent_sms)

@register
class SmsjobsStatus(TLObject):
    CONSTRUCTOR_ID = 720277905
    __slots__ = ('allow_international', 'recent_sent', 'recent_since', 'recent_remains', 'total_sent', 'total_since', 'last_gift_slug', 'terms_url')
    def __init__(self, recent_sent: int, recent_since: int, recent_remains: int, total_sent: int, total_since: int, terms_url: str, allow_international: bool = None, last_gift_slug: str = None):
        self.allow_international = allow_international
        self.recent_sent = recent_sent
        self.recent_since = recent_since
        self.recent_remains = recent_remains
        self.total_sent = total_sent
        self.total_since = total_since
        self.last_gift_slug = last_gift_slug
        self.terms_url = terms_url
    def to_dict(self):
        return {"allow_international": self.allow_international, "recent_sent": self.recent_sent, "recent_since": self.recent_since, "recent_remains": self.recent_remains, "total_sent": self.total_sent, "total_since": self.total_since, "last_gift_slug": self.last_gift_slug, "terms_url": self.terms_url}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(720277905, signed=False)
        flags = 0
        if self.allow_international: flags |= 1 << 0
        if self.last_gift_slug is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write_int(self.recent_sent, signed=True)
        writer.write_int(self.recent_since, signed=True)
        writer.write_int(self.recent_remains, signed=True)
        writer.write_int(self.total_sent, signed=True)
        writer.write_int(self.total_since, signed=True)
        if flags & (1 << 1):
            writer.write_string(self.last_gift_slug)
        writer.write_string(self.terms_url)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        allow_international = bool(flags & (1 << 0))
        recent_sent = reader.read_int()
        recent_since = reader.read_int()
        recent_remains = reader.read_int()
        total_sent = reader.read_int()
        total_since = reader.read_int()
        if flags & (1 << 1):
            last_gift_slug = reader.read_string()
        else:
            last_gift_slug = None
        terms_url = reader.read_string()
        return cls(allow_international, recent_sent, recent_since, recent_remains, total_sent, total_since, last_gift_slug, terms_url)

