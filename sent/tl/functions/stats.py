"""Auto-generated TL functions. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

@register
class StatsGetBroadcastStats(TLObject):
    CONSTRUCTOR_ID = 2873246746
    __slots__ = ('dark', 'channel')
    def __init__(self, channel: 'InputChannel', dark: bool = None):
        self.dark = dark
        self.channel = channel
    def to_dict(self):
        return {"dark": self.dark, "channel": self.channel}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2873246746, signed=False)
        flags = 0
        if self.dark: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.channel))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        dark = bool(flags & (1 << 0))
        channel = reader.tgread_object()
        return cls(dark, channel)

@register
class StatsLoadAsyncGraph(TLObject):
    CONSTRUCTOR_ID = 1646092192
    __slots__ = ('token', 'x')
    def __init__(self, token: str, x: int = None):
        self.token = token
        self.x = x
    def to_dict(self):
        return {"token": self.token, "x": self.x}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1646092192, signed=False)
        flags = 0
        if self.x is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write_string(self.token)
        if flags & (1 << 0):
            writer.write_long(self.x, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        token = reader.read_string()
        if flags & (1 << 0):
            x = reader.read_long()
        else:
            x = None
        return cls(token, x)

@register
class StatsGetMegagroupStats(TLObject):
    CONSTRUCTOR_ID = 3705636359
    __slots__ = ('dark', 'channel')
    def __init__(self, channel: 'InputChannel', dark: bool = None):
        self.dark = dark
        self.channel = channel
    def to_dict(self):
        return {"dark": self.dark, "channel": self.channel}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3705636359, signed=False)
        flags = 0
        if self.dark: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.channel))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        dark = bool(flags & (1 << 0))
        channel = reader.tgread_object()
        return cls(dark, channel)

@register
class StatsGetMessagePublicForwards(TLObject):
    CONSTRUCTOR_ID = 1595212100
    __slots__ = ('channel', 'msg_id', 'offset', 'limit')
    def __init__(self, channel: 'InputChannel', msg_id: int, offset: str, limit: int):
        self.channel = channel
        self.msg_id = msg_id
        self.offset = offset
        self.limit = limit
    def to_dict(self):
        return {"channel": self.channel, "msg_id": self.msg_id, "offset": self.offset, "limit": self.limit}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1595212100, signed=False)
        writer.write(bytes(self.channel))
        writer.write_int(self.msg_id, signed=True)
        writer.write_string(self.offset)
        writer.write_int(self.limit, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        channel = reader.tgread_object()
        msg_id = reader.read_int()
        offset = reader.read_string()
        limit = reader.read_int()
        return cls(channel, msg_id, offset, limit)

@register
class StatsGetMessageStats(TLObject):
    CONSTRUCTOR_ID = 3068175349
    __slots__ = ('dark', 'channel', 'msg_id')
    def __init__(self, channel: 'InputChannel', msg_id: int, dark: bool = None):
        self.dark = dark
        self.channel = channel
        self.msg_id = msg_id
    def to_dict(self):
        return {"dark": self.dark, "channel": self.channel, "msg_id": self.msg_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3068175349, signed=False)
        flags = 0
        if self.dark: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.channel))
        writer.write_int(self.msg_id, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        dark = bool(flags & (1 << 0))
        channel = reader.tgread_object()
        msg_id = reader.read_int()
        return cls(dark, channel, msg_id)

@register
class StatsGetStoryStats(TLObject):
    CONSTRUCTOR_ID = 927985472
    __slots__ = ('dark', 'peer', 'id')
    def __init__(self, peer: 'InputPeer', id: int, dark: bool = None):
        self.dark = dark
        self.peer = peer
        self.id = id
    def to_dict(self):
        return {"dark": self.dark, "peer": self.peer, "id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(927985472, signed=False)
        flags = 0
        if self.dark: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.id, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        dark = bool(flags & (1 << 0))
        peer = reader.tgread_object()
        id = reader.read_int()
        return cls(dark, peer, id)

@register
class StatsGetStoryPublicForwards(TLObject):
    CONSTRUCTOR_ID = 2789441270
    __slots__ = ('peer', 'id', 'offset', 'limit')
    def __init__(self, peer: 'InputPeer', id: int, offset: str, limit: int):
        self.peer = peer
        self.id = id
        self.offset = offset
        self.limit = limit
    def to_dict(self):
        return {"peer": self.peer, "id": self.id, "offset": self.offset, "limit": self.limit}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2789441270, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.id, signed=True)
        writer.write_string(self.offset)
        writer.write_int(self.limit, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        id = reader.read_int()
        offset = reader.read_string()
        limit = reader.read_int()
        return cls(peer, id, offset, limit)

@register
class StatsGetPollStats(TLObject):
    CONSTRUCTOR_ID = 3263036008
    __slots__ = ('dark', 'peer', 'msg_id')
    def __init__(self, peer: 'InputPeer', msg_id: int, dark: bool = None):
        self.dark = dark
        self.peer = peer
        self.msg_id = msg_id
    def to_dict(self):
        return {"dark": self.dark, "peer": self.peer, "msg_id": self.msg_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3263036008, signed=False)
        flags = 0
        if self.dark: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.msg_id, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        dark = bool(flags & (1 << 0))
        peer = reader.tgread_object()
        msg_id = reader.read_int()
        return cls(dark, peer, msg_id)

