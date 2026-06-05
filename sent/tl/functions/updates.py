"""Auto-generated TL functions. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

@register
class UpdatesGetState(TLObject):
    CONSTRUCTOR_ID = 3990128682
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3990128682, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class UpdatesGetDifference(TLObject):
    CONSTRUCTOR_ID = 432207715
    __slots__ = ('pts', 'pts_limit', 'pts_total_limit', 'date', 'qts', 'qts_limit')
    def __init__(self, pts: int, date: int, qts: int, pts_limit: int = None, pts_total_limit: int = None, qts_limit: int = None):
        self.pts = pts
        self.pts_limit = pts_limit
        self.pts_total_limit = pts_total_limit
        self.date = date
        self.qts = qts
        self.qts_limit = qts_limit
    def to_dict(self):
        return {"pts": self.pts, "pts_limit": self.pts_limit, "pts_total_limit": self.pts_total_limit, "date": self.date, "qts": self.qts, "qts_limit": self.qts_limit}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(432207715, signed=False)
        flags = 0
        if self.pts_limit is not None: flags |= 1 << 1
        if self.pts_total_limit is not None: flags |= 1 << 0
        if self.qts_limit is not None: flags |= 1 << 2
        writer.write_int(flags, signed=False)
        writer.write_int(self.pts, signed=True)
        if flags & (1 << 1):
            writer.write_int(self.pts_limit, signed=True)
        if flags & (1 << 0):
            writer.write_int(self.pts_total_limit, signed=True)
        writer.write_int(self.date, signed=True)
        writer.write_int(self.qts, signed=True)
        if flags & (1 << 2):
            writer.write_int(self.qts_limit, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        pts = reader.read_int()
        if flags & (1 << 1):
            pts_limit = reader.read_int()
        else:
            pts_limit = None
        if flags & (1 << 0):
            pts_total_limit = reader.read_int()
        else:
            pts_total_limit = None
        date = reader.read_int()
        qts = reader.read_int()
        if flags & (1 << 2):
            qts_limit = reader.read_int()
        else:
            qts_limit = None
        return cls(pts, pts_limit, pts_total_limit, date, qts, qts_limit)

@register
class UpdatesGetChannelDifference(TLObject):
    CONSTRUCTOR_ID = 51854712
    __slots__ = ('force', 'channel', 'filter', 'pts', 'limit')
    def __init__(self, channel: 'InputChannel', filter: 'ChannelMessagesFilter', pts: int, limit: int, force: bool = None):
        self.force = force
        self.channel = channel
        self.filter = filter
        self.pts = pts
        self.limit = limit
    def to_dict(self):
        return {"force": self.force, "channel": self.channel, "filter": self.filter, "pts": self.pts, "limit": self.limit}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(51854712, signed=False)
        flags = 0
        if self.force: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.channel))
        writer.write(bytes(self.filter))
        writer.write_int(self.pts, signed=True)
        writer.write_int(self.limit, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        force = bool(flags & (1 << 0))
        channel = reader.tgread_object()
        filter = reader.tgread_object()
        pts = reader.read_int()
        limit = reader.read_int()
        return cls(force, channel, filter, pts, limit)

