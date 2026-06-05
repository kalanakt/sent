"""Auto-generated TL functions. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

@register
class PhoneGetCallConfig(TLObject):
    CONSTRUCTOR_ID = 1430593449
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1430593449, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class PhoneRequestCall(TLObject):
    CONSTRUCTOR_ID = 1124046573
    __slots__ = ('video', 'user_id', 'random_id', 'g_a_hash', 'protocol')
    def __init__(self, user_id: 'InputUser', random_id: int, g_a_hash: bytes, protocol: 'PhoneCallProtocol', video: bool = None):
        self.video = video
        self.user_id = user_id
        self.random_id = random_id
        self.g_a_hash = g_a_hash
        self.protocol = protocol
    def to_dict(self):
        return {"video": self.video, "user_id": self.user_id, "random_id": self.random_id, "g_a_hash": self.g_a_hash, "protocol": self.protocol}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1124046573, signed=False)
        flags = 0
        if self.video: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.user_id))
        writer.write_int(self.random_id, signed=True)
        writer.write_bytes(self.g_a_hash)
        writer.write(bytes(self.protocol))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        video = bool(flags & (1 << 0))
        user_id = reader.tgread_object()
        random_id = reader.read_int()
        g_a_hash = reader.read_bytes()
        protocol = reader.tgread_object()
        return cls(video, user_id, random_id, g_a_hash, protocol)

@register
class PhoneAcceptCall(TLObject):
    CONSTRUCTOR_ID = 1003664544
    __slots__ = ('peer', 'g_b', 'protocol')
    def __init__(self, peer: 'InputPhoneCall', g_b: bytes, protocol: 'PhoneCallProtocol'):
        self.peer = peer
        self.g_b = g_b
        self.protocol = protocol
    def to_dict(self):
        return {"peer": self.peer, "g_b": self.g_b, "protocol": self.protocol}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1003664544, signed=False)
        writer.write(bytes(self.peer))
        writer.write_bytes(self.g_b)
        writer.write(bytes(self.protocol))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        g_b = reader.read_bytes()
        protocol = reader.tgread_object()
        return cls(peer, g_b, protocol)

@register
class PhoneConfirmCall(TLObject):
    CONSTRUCTOR_ID = 788404002
    __slots__ = ('peer', 'g_a', 'key_fingerprint', 'protocol')
    def __init__(self, peer: 'InputPhoneCall', g_a: bytes, key_fingerprint: int, protocol: 'PhoneCallProtocol'):
        self.peer = peer
        self.g_a = g_a
        self.key_fingerprint = key_fingerprint
        self.protocol = protocol
    def to_dict(self):
        return {"peer": self.peer, "g_a": self.g_a, "key_fingerprint": self.key_fingerprint, "protocol": self.protocol}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(788404002, signed=False)
        writer.write(bytes(self.peer))
        writer.write_bytes(self.g_a)
        writer.write_long(self.key_fingerprint, signed=False)
        writer.write(bytes(self.protocol))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        g_a = reader.read_bytes()
        key_fingerprint = reader.read_long()
        protocol = reader.tgread_object()
        return cls(peer, g_a, key_fingerprint, protocol)

@register
class PhoneReceivedCall(TLObject):
    CONSTRUCTOR_ID = 399855457
    __slots__ = ('peer')
    def __init__(self, peer: 'InputPhoneCall'):
        self.peer = peer
    def to_dict(self):
        return {"peer": self.peer}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(399855457, signed=False)
        writer.write(bytes(self.peer))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        return cls(peer)

@register
class PhoneDiscardCall(TLObject):
    CONSTRUCTOR_ID = 2999697856
    __slots__ = ('video', 'peer', 'duration', 'reason', 'connection_id')
    def __init__(self, peer: 'InputPhoneCall', duration: int, reason: 'PhoneCallDiscardReason', connection_id: int, video: bool = None):
        self.video = video
        self.peer = peer
        self.duration = duration
        self.reason = reason
        self.connection_id = connection_id
    def to_dict(self):
        return {"video": self.video, "peer": self.peer, "duration": self.duration, "reason": self.reason, "connection_id": self.connection_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2999697856, signed=False)
        flags = 0
        if self.video: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.duration, signed=True)
        writer.write(bytes(self.reason))
        writer.write_long(self.connection_id, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        video = bool(flags & (1 << 0))
        peer = reader.tgread_object()
        duration = reader.read_int()
        reason = reader.tgread_object()
        connection_id = reader.read_long()
        return cls(video, peer, duration, reason, connection_id)

@register
class PhoneSetCallRating(TLObject):
    CONSTRUCTOR_ID = 1508562471
    __slots__ = ('user_initiative', 'peer', 'rating', 'comment')
    def __init__(self, peer: 'InputPhoneCall', rating: int, comment: str, user_initiative: bool = None):
        self.user_initiative = user_initiative
        self.peer = peer
        self.rating = rating
        self.comment = comment
    def to_dict(self):
        return {"user_initiative": self.user_initiative, "peer": self.peer, "rating": self.rating, "comment": self.comment}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1508562471, signed=False)
        flags = 0
        if self.user_initiative: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.rating, signed=True)
        writer.write_string(self.comment)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        user_initiative = bool(flags & (1 << 0))
        peer = reader.tgread_object()
        rating = reader.read_int()
        comment = reader.read_string()
        return cls(user_initiative, peer, rating, comment)

@register
class PhoneSaveCallDebug(TLObject):
    CONSTRUCTOR_ID = 662363518
    __slots__ = ('peer', 'debug')
    def __init__(self, peer: 'InputPhoneCall', debug: 'DataJSON'):
        self.peer = peer
        self.debug = debug
    def to_dict(self):
        return {"peer": self.peer, "debug": self.debug}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(662363518, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.debug))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        debug = reader.tgread_object()
        return cls(peer, debug)

@register
class PhoneSendSignalingData(TLObject):
    CONSTRUCTOR_ID = 4286223235
    __slots__ = ('peer', 'data')
    def __init__(self, peer: 'InputPhoneCall', data: bytes):
        self.peer = peer
        self.data = data
    def to_dict(self):
        return {"peer": self.peer, "data": self.data}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4286223235, signed=False)
        writer.write(bytes(self.peer))
        writer.write_bytes(self.data)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        data = reader.read_bytes()
        return cls(peer, data)

@register
class PhoneCreateGroupCall(TLObject):
    CONSTRUCTOR_ID = 1221445336
    __slots__ = ('rtmp_stream', 'peer', 'random_id', 'title', 'schedule_date')
    def __init__(self, peer: 'InputPeer', random_id: int, rtmp_stream: bool = None, title: str = None, schedule_date: int = None):
        self.rtmp_stream = rtmp_stream
        self.peer = peer
        self.random_id = random_id
        self.title = title
        self.schedule_date = schedule_date
    def to_dict(self):
        return {"rtmp_stream": self.rtmp_stream, "peer": self.peer, "random_id": self.random_id, "title": self.title, "schedule_date": self.schedule_date}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1221445336, signed=False)
        flags = 0
        if self.rtmp_stream: flags |= 1 << 2
        if self.title is not None: flags |= 1 << 0
        if self.schedule_date is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.random_id, signed=True)
        if flags & (1 << 0):
            writer.write_string(self.title)
        if flags & (1 << 1):
            writer.write_int(self.schedule_date, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        rtmp_stream = bool(flags & (1 << 2))
        peer = reader.tgread_object()
        random_id = reader.read_int()
        if flags & (1 << 0):
            title = reader.read_string()
        else:
            title = None
        if flags & (1 << 1):
            schedule_date = reader.read_int()
        else:
            schedule_date = None
        return cls(rtmp_stream, peer, random_id, title, schedule_date)

@register
class PhoneJoinGroupCall(TLObject):
    CONSTRUCTOR_ID = 2411016279
    __slots__ = ('muted', 'video_stopped', 'call', 'join_as', 'invite_hash', 'public_key', 'block', 'params')
    def __init__(self, call: 'InputGroupCall', join_as: 'InputPeer', params: 'DataJSON', muted: bool = None, video_stopped: bool = None, invite_hash: str = None, public_key: bytes = None, block: bytes = None):
        self.muted = muted
        self.video_stopped = video_stopped
        self.call = call
        self.join_as = join_as
        self.invite_hash = invite_hash
        self.public_key = public_key
        self.block = block
        self.params = params
    def to_dict(self):
        return {"muted": self.muted, "video_stopped": self.video_stopped, "call": self.call, "join_as": self.join_as, "invite_hash": self.invite_hash, "public_key": self.public_key, "block": self.block, "params": self.params}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2411016279, signed=False)
        flags = 0
        if self.muted: flags |= 1 << 0
        if self.video_stopped: flags |= 1 << 2
        if self.invite_hash is not None: flags |= 1 << 1
        if self.public_key is not None: flags |= 1 << 3
        if self.block is not None: flags |= 1 << 3
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.call))
        writer.write(bytes(self.join_as))
        if flags & (1 << 1):
            writer.write_string(self.invite_hash)
        if flags & (1 << 3):
            writer.write_raw(self.public_key)
        if flags & (1 << 3):
            writer.write_bytes(self.block)
        writer.write(bytes(self.params))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        muted = bool(flags & (1 << 0))
        video_stopped = bool(flags & (1 << 2))
        call = reader.tgread_object()
        join_as = reader.tgread_object()
        if flags & (1 << 1):
            invite_hash = reader.read_string()
        else:
            invite_hash = None
        if flags & (1 << 3):
            public_key = reader.read(32)
        else:
            public_key = None
        if flags & (1 << 3):
            block = reader.read_bytes()
        else:
            block = None
        params = reader.tgread_object()
        return cls(muted, video_stopped, call, join_as, invite_hash, public_key, block, params)

@register
class PhoneLeaveGroupCall(TLObject):
    CONSTRUCTOR_ID = 1342404601
    __slots__ = ('call', 'source')
    def __init__(self, call: 'InputGroupCall', source: int):
        self.call = call
        self.source = source
    def to_dict(self):
        return {"call": self.call, "source": self.source}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1342404601, signed=False)
        writer.write(bytes(self.call))
        writer.write_int(self.source, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        call = reader.tgread_object()
        source = reader.read_int()
        return cls(call, source)

@register
class PhoneInviteToGroupCall(TLObject):
    CONSTRUCTOR_ID = 2067345760
    __slots__ = ('call', 'users')
    def __init__(self, call: 'InputGroupCall', users: 'Vector'):
        self.call = call
        self.users = users
    def to_dict(self):
        return {"call": self.call, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2067345760, signed=False)
        writer.write(bytes(self.call))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        call = reader.tgread_object()
        users = reader.tgread_object()
        return cls(call, users)

@register
class PhoneDiscardGroupCall(TLObject):
    CONSTRUCTOR_ID = 2054648117
    __slots__ = ('call')
    def __init__(self, call: 'InputGroupCall'):
        self.call = call
    def to_dict(self):
        return {"call": self.call}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2054648117, signed=False)
        writer.write(bytes(self.call))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        call = reader.tgread_object()
        return cls(call)

@register
class PhoneToggleGroupCallSettings(TLObject):
    CONSTRUCTOR_ID = 2537788146
    __slots__ = ('reset_invite_hash', 'call', 'join_muted', 'messages_enabled', 'send_paid_messages_stars')
    def __init__(self, call: 'InputGroupCall', reset_invite_hash: bool = None, join_muted: bool = None, messages_enabled: bool = None, send_paid_messages_stars: int = None):
        self.reset_invite_hash = reset_invite_hash
        self.call = call
        self.join_muted = join_muted
        self.messages_enabled = messages_enabled
        self.send_paid_messages_stars = send_paid_messages_stars
    def to_dict(self):
        return {"reset_invite_hash": self.reset_invite_hash, "call": self.call, "join_muted": self.join_muted, "messages_enabled": self.messages_enabled, "send_paid_messages_stars": self.send_paid_messages_stars}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2537788146, signed=False)
        flags = 0
        if self.reset_invite_hash: flags |= 1 << 1
        if self.join_muted is not None: flags |= 1 << 0
        if self.messages_enabled is not None: flags |= 1 << 2
        if self.send_paid_messages_stars is not None: flags |= 1 << 3
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.call))
        if flags & (1 << 0):
            writer.write(serialize_bool(self.join_muted))
        if flags & (1 << 2):
            writer.write(serialize_bool(self.messages_enabled))
        if flags & (1 << 3):
            writer.write_long(self.send_paid_messages_stars, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        reset_invite_hash = bool(flags & (1 << 1))
        call = reader.tgread_object()
        if flags & (1 << 0):
            join_muted = reader.tgread_bool()
        else:
            join_muted = None
        if flags & (1 << 2):
            messages_enabled = reader.tgread_bool()
        else:
            messages_enabled = None
        if flags & (1 << 3):
            send_paid_messages_stars = reader.read_long()
        else:
            send_paid_messages_stars = None
        return cls(reset_invite_hash, call, join_muted, messages_enabled, send_paid_messages_stars)

@register
class PhoneGetGroupCall(TLObject):
    CONSTRUCTOR_ID = 68699611
    __slots__ = ('call', 'limit')
    def __init__(self, call: 'InputGroupCall', limit: int):
        self.call = call
        self.limit = limit
    def to_dict(self):
        return {"call": self.call, "limit": self.limit}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(68699611, signed=False)
        writer.write(bytes(self.call))
        writer.write_int(self.limit, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        call = reader.tgread_object()
        limit = reader.read_int()
        return cls(call, limit)

@register
class PhoneGetGroupParticipants(TLObject):
    CONSTRUCTOR_ID = 3310934187
    __slots__ = ('call', 'ids', 'sources', 'offset', 'limit')
    def __init__(self, call: 'InputGroupCall', ids: 'Vector', sources: 'Vector', offset: str, limit: int):
        self.call = call
        self.ids = ids
        self.sources = sources
        self.offset = offset
        self.limit = limit
    def to_dict(self):
        return {"call": self.call, "ids": self.ids, "sources": self.sources, "offset": self.offset, "limit": self.limit}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3310934187, signed=False)
        writer.write(bytes(self.call))
        writer.write(bytes(self.ids))
        writer.write(bytes(self.sources))
        writer.write_string(self.offset)
        writer.write_int(self.limit, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        call = reader.tgread_object()
        ids = reader.tgread_object()
        sources = reader.tgread_object()
        offset = reader.read_string()
        limit = reader.read_int()
        return cls(call, ids, sources, offset, limit)

@register
class PhoneCheckGroupCall(TLObject):
    CONSTRUCTOR_ID = 3046963575
    __slots__ = ('call', 'sources')
    def __init__(self, call: 'InputGroupCall', sources: 'Vector'):
        self.call = call
        self.sources = sources
    def to_dict(self):
        return {"call": self.call, "sources": self.sources}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3046963575, signed=False)
        writer.write(bytes(self.call))
        writer.write(bytes(self.sources))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        call = reader.tgread_object()
        sources = reader.tgread_object()
        return cls(call, sources)

@register
class PhoneToggleGroupCallRecord(TLObject):
    CONSTRUCTOR_ID = 4045981448
    __slots__ = ('start', 'video', 'call', 'title', 'video_portrait')
    def __init__(self, call: 'InputGroupCall', start: bool = None, video: bool = None, title: str = None, video_portrait: bool = None):
        self.start = start
        self.video = video
        self.call = call
        self.title = title
        self.video_portrait = video_portrait
    def to_dict(self):
        return {"start": self.start, "video": self.video, "call": self.call, "title": self.title, "video_portrait": self.video_portrait}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4045981448, signed=False)
        flags = 0
        if self.start: flags |= 1 << 0
        if self.video: flags |= 1 << 2
        if self.title is not None: flags |= 1 << 1
        if self.video_portrait is not None: flags |= 1 << 2
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.call))
        if flags & (1 << 1):
            writer.write_string(self.title)
        if flags & (1 << 2):
            writer.write(serialize_bool(self.video_portrait))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        start = bool(flags & (1 << 0))
        video = bool(flags & (1 << 2))
        call = reader.tgread_object()
        if flags & (1 << 1):
            title = reader.read_string()
        else:
            title = None
        if flags & (1 << 2):
            video_portrait = reader.tgread_bool()
        else:
            video_portrait = None
        return cls(start, video, call, title, video_portrait)

@register
class PhoneEditGroupCallParticipant(TLObject):
    CONSTRUCTOR_ID = 2770811583
    __slots__ = ('call', 'participant', 'muted', 'volume', 'raise_hand', 'video_stopped', 'video_paused', 'presentation_paused')
    def __init__(self, call: 'InputGroupCall', participant: 'InputPeer', muted: bool = None, volume: int = None, raise_hand: bool = None, video_stopped: bool = None, video_paused: bool = None, presentation_paused: bool = None):
        self.call = call
        self.participant = participant
        self.muted = muted
        self.volume = volume
        self.raise_hand = raise_hand
        self.video_stopped = video_stopped
        self.video_paused = video_paused
        self.presentation_paused = presentation_paused
    def to_dict(self):
        return {"call": self.call, "participant": self.participant, "muted": self.muted, "volume": self.volume, "raise_hand": self.raise_hand, "video_stopped": self.video_stopped, "video_paused": self.video_paused, "presentation_paused": self.presentation_paused}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2770811583, signed=False)
        flags = 0
        if self.muted is not None: flags |= 1 << 0
        if self.volume is not None: flags |= 1 << 1
        if self.raise_hand is not None: flags |= 1 << 2
        if self.video_stopped is not None: flags |= 1 << 3
        if self.video_paused is not None: flags |= 1 << 4
        if self.presentation_paused is not None: flags |= 1 << 5
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.call))
        writer.write(bytes(self.participant))
        if flags & (1 << 0):
            writer.write(serialize_bool(self.muted))
        if flags & (1 << 1):
            writer.write_int(self.volume, signed=True)
        if flags & (1 << 2):
            writer.write(serialize_bool(self.raise_hand))
        if flags & (1 << 3):
            writer.write(serialize_bool(self.video_stopped))
        if flags & (1 << 4):
            writer.write(serialize_bool(self.video_paused))
        if flags & (1 << 5):
            writer.write(serialize_bool(self.presentation_paused))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        call = reader.tgread_object()
        participant = reader.tgread_object()
        if flags & (1 << 0):
            muted = reader.tgread_bool()
        else:
            muted = None
        if flags & (1 << 1):
            volume = reader.read_int()
        else:
            volume = None
        if flags & (1 << 2):
            raise_hand = reader.tgread_bool()
        else:
            raise_hand = None
        if flags & (1 << 3):
            video_stopped = reader.tgread_bool()
        else:
            video_stopped = None
        if flags & (1 << 4):
            video_paused = reader.tgread_bool()
        else:
            video_paused = None
        if flags & (1 << 5):
            presentation_paused = reader.tgread_bool()
        else:
            presentation_paused = None
        return cls(call, participant, muted, volume, raise_hand, video_stopped, video_paused, presentation_paused)

@register
class PhoneEditGroupCallTitle(TLObject):
    CONSTRUCTOR_ID = 480685066
    __slots__ = ('call', 'title')
    def __init__(self, call: 'InputGroupCall', title: str):
        self.call = call
        self.title = title
    def to_dict(self):
        return {"call": self.call, "title": self.title}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(480685066, signed=False)
        writer.write(bytes(self.call))
        writer.write_string(self.title)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        call = reader.tgread_object()
        title = reader.read_string()
        return cls(call, title)

@register
class PhoneGetGroupCallJoinAs(TLObject):
    CONSTRUCTOR_ID = 4017889594
    __slots__ = ('peer')
    def __init__(self, peer: 'InputPeer'):
        self.peer = peer
    def to_dict(self):
        return {"peer": self.peer}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4017889594, signed=False)
        writer.write(bytes(self.peer))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        return cls(peer)

@register
class PhoneExportGroupCallInvite(TLObject):
    CONSTRUCTOR_ID = 3869926527
    __slots__ = ('can_self_unmute', 'call')
    def __init__(self, call: 'InputGroupCall', can_self_unmute: bool = None):
        self.can_self_unmute = can_self_unmute
        self.call = call
    def to_dict(self):
        return {"can_self_unmute": self.can_self_unmute, "call": self.call}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3869926527, signed=False)
        flags = 0
        if self.can_self_unmute: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.call))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        can_self_unmute = bool(flags & (1 << 0))
        call = reader.tgread_object()
        return cls(can_self_unmute, call)

@register
class PhoneToggleGroupCallStartSubscription(TLObject):
    CONSTRUCTOR_ID = 563885286
    __slots__ = ('call', 'subscribed')
    def __init__(self, call: 'InputGroupCall', subscribed: bool):
        self.call = call
        self.subscribed = subscribed
    def to_dict(self):
        return {"call": self.call, "subscribed": self.subscribed}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(563885286, signed=False)
        writer.write(bytes(self.call))
        writer.write(serialize_bool(self.subscribed))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        call = reader.tgread_object()
        subscribed = reader.tgread_bool()
        return cls(call, subscribed)

@register
class PhoneStartScheduledGroupCall(TLObject):
    CONSTRUCTOR_ID = 1451287362
    __slots__ = ('call')
    def __init__(self, call: 'InputGroupCall'):
        self.call = call
    def to_dict(self):
        return {"call": self.call}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1451287362, signed=False)
        writer.write(bytes(self.call))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        call = reader.tgread_object()
        return cls(call)

@register
class PhoneSaveDefaultGroupCallJoinAs(TLObject):
    CONSTRUCTOR_ID = 1465786252
    __slots__ = ('peer', 'join_as')
    def __init__(self, peer: 'InputPeer', join_as: 'InputPeer'):
        self.peer = peer
        self.join_as = join_as
    def to_dict(self):
        return {"peer": self.peer, "join_as": self.join_as}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1465786252, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.join_as))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        join_as = reader.tgread_object()
        return cls(peer, join_as)

@register
class PhoneJoinGroupCallPresentation(TLObject):
    CONSTRUCTOR_ID = 3421137860
    __slots__ = ('call', 'params')
    def __init__(self, call: 'InputGroupCall', params: 'DataJSON'):
        self.call = call
        self.params = params
    def to_dict(self):
        return {"call": self.call, "params": self.params}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3421137860, signed=False)
        writer.write(bytes(self.call))
        writer.write(bytes(self.params))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        call = reader.tgread_object()
        params = reader.tgread_object()
        return cls(call, params)

@register
class PhoneLeaveGroupCallPresentation(TLObject):
    CONSTRUCTOR_ID = 475058500
    __slots__ = ('call')
    def __init__(self, call: 'InputGroupCall'):
        self.call = call
    def to_dict(self):
        return {"call": self.call}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(475058500, signed=False)
        writer.write(bytes(self.call))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        call = reader.tgread_object()
        return cls(call)

@register
class PhoneGetGroupCallStreamChannels(TLObject):
    CONSTRUCTOR_ID = 447879488
    __slots__ = ('call')
    def __init__(self, call: 'InputGroupCall'):
        self.call = call
    def to_dict(self):
        return {"call": self.call}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(447879488, signed=False)
        writer.write(bytes(self.call))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        call = reader.tgread_object()
        return cls(call)

@register
class PhoneGetGroupCallStreamRtmpUrl(TLObject):
    CONSTRUCTOR_ID = 1525991226
    __slots__ = ('live_story', 'peer', 'revoke')
    def __init__(self, peer: 'InputPeer', revoke: bool, live_story: bool = None):
        self.live_story = live_story
        self.peer = peer
        self.revoke = revoke
    def to_dict(self):
        return {"live_story": self.live_story, "peer": self.peer, "revoke": self.revoke}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1525991226, signed=False)
        flags = 0
        if self.live_story: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write(serialize_bool(self.revoke))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        live_story = bool(flags & (1 << 0))
        peer = reader.tgread_object()
        revoke = reader.tgread_bool()
        return cls(live_story, peer, revoke)

@register
class PhoneSaveCallLog(TLObject):
    CONSTRUCTOR_ID = 1092913030
    __slots__ = ('peer', 'file')
    def __init__(self, peer: 'InputPhoneCall', file: 'InputFile'):
        self.peer = peer
        self.file = file
    def to_dict(self):
        return {"peer": self.peer, "file": self.file}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1092913030, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.file))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        file = reader.tgread_object()
        return cls(peer, file)

@register
class PhoneCreateConferenceCall(TLObject):
    CONSTRUCTOR_ID = 2097431739
    __slots__ = ('muted', 'video_stopped', 'join', 'random_id', 'public_key', 'block', 'params')
    def __init__(self, random_id: int, muted: bool = None, video_stopped: bool = None, join: bool = None, public_key: bytes = None, block: bytes = None, params: 'DataJSON' = None):
        self.muted = muted
        self.video_stopped = video_stopped
        self.join = join
        self.random_id = random_id
        self.public_key = public_key
        self.block = block
        self.params = params
    def to_dict(self):
        return {"muted": self.muted, "video_stopped": self.video_stopped, "join": self.join, "random_id": self.random_id, "public_key": self.public_key, "block": self.block, "params": self.params}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2097431739, signed=False)
        flags = 0
        if self.muted: flags |= 1 << 0
        if self.video_stopped: flags |= 1 << 2
        if self.join: flags |= 1 << 3
        if self.public_key is not None: flags |= 1 << 3
        if self.block is not None: flags |= 1 << 3
        if self.params is not None: flags |= 1 << 3
        writer.write_int(flags, signed=False)
        writer.write_int(self.random_id, signed=True)
        if flags & (1 << 3):
            writer.write_raw(self.public_key)
        if flags & (1 << 3):
            writer.write_bytes(self.block)
        if flags & (1 << 3):
            writer.write(bytes(self.params))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        muted = bool(flags & (1 << 0))
        video_stopped = bool(flags & (1 << 2))
        join = bool(flags & (1 << 3))
        random_id = reader.read_int()
        if flags & (1 << 3):
            public_key = reader.read(32)
        else:
            public_key = None
        if flags & (1 << 3):
            block = reader.read_bytes()
        else:
            block = None
        if flags & (1 << 3):
            params = reader.tgread_object()
        else:
            params = None
        return cls(muted, video_stopped, join, random_id, public_key, block, params)

@register
class PhoneDeleteConferenceCallParticipants(TLObject):
    CONSTRUCTOR_ID = 2359690533
    __slots__ = ('only_left', 'kick', 'call', 'ids', 'block')
    def __init__(self, call: 'InputGroupCall', ids: 'Vector', block: bytes, only_left: bool = None, kick: bool = None):
        self.only_left = only_left
        self.kick = kick
        self.call = call
        self.ids = ids
        self.block = block
    def to_dict(self):
        return {"only_left": self.only_left, "kick": self.kick, "call": self.call, "ids": self.ids, "block": self.block}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2359690533, signed=False)
        flags = 0
        if self.only_left: flags |= 1 << 0
        if self.kick: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.call))
        writer.write(bytes(self.ids))
        writer.write_bytes(self.block)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        only_left = bool(flags & (1 << 0))
        kick = bool(flags & (1 << 1))
        call = reader.tgread_object()
        ids = reader.tgread_object()
        block = reader.read_bytes()
        return cls(only_left, kick, call, ids, block)

@register
class PhoneSendConferenceCallBroadcast(TLObject):
    CONSTRUCTOR_ID = 3329235200
    __slots__ = ('call', 'block')
    def __init__(self, call: 'InputGroupCall', block: bytes):
        self.call = call
        self.block = block
    def to_dict(self):
        return {"call": self.call, "block": self.block}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3329235200, signed=False)
        writer.write(bytes(self.call))
        writer.write_bytes(self.block)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        call = reader.tgread_object()
        block = reader.read_bytes()
        return cls(call, block)

@register
class PhoneInviteConferenceCallParticipant(TLObject):
    CONSTRUCTOR_ID = 3169986181
    __slots__ = ('video', 'call', 'user_id')
    def __init__(self, call: 'InputGroupCall', user_id: 'InputUser', video: bool = None):
        self.video = video
        self.call = call
        self.user_id = user_id
    def to_dict(self):
        return {"video": self.video, "call": self.call, "user_id": self.user_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3169986181, signed=False)
        flags = 0
        if self.video: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.call))
        writer.write(bytes(self.user_id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        video = bool(flags & (1 << 0))
        call = reader.tgread_object()
        user_id = reader.tgread_object()
        return cls(video, call, user_id)

@register
class PhoneDeclineConferenceCallInvite(TLObject):
    CONSTRUCTOR_ID = 1011325297
    __slots__ = ('msg_id')
    def __init__(self, msg_id: int):
        self.msg_id = msg_id
    def to_dict(self):
        return {"msg_id": self.msg_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1011325297, signed=False)
        writer.write_int(self.msg_id, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        msg_id = reader.read_int()
        return cls(msg_id)

@register
class PhoneGetGroupCallChainBlocks(TLObject):
    CONSTRUCTOR_ID = 4003432614
    __slots__ = ('call', 'sub_chain_id', 'offset', 'limit')
    def __init__(self, call: 'InputGroupCall', sub_chain_id: int, offset: int, limit: int):
        self.call = call
        self.sub_chain_id = sub_chain_id
        self.offset = offset
        self.limit = limit
    def to_dict(self):
        return {"call": self.call, "sub_chain_id": self.sub_chain_id, "offset": self.offset, "limit": self.limit}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4003432614, signed=False)
        writer.write(bytes(self.call))
        writer.write_int(self.sub_chain_id, signed=True)
        writer.write_int(self.offset, signed=True)
        writer.write_int(self.limit, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        call = reader.tgread_object()
        sub_chain_id = reader.read_int()
        offset = reader.read_int()
        limit = reader.read_int()
        return cls(call, sub_chain_id, offset, limit)

@register
class PhoneSendGroupCallMessage(TLObject):
    CONSTRUCTOR_ID = 2983269392
    __slots__ = ('call', 'random_id', 'message', 'allow_paid_stars', 'send_as')
    def __init__(self, call: 'InputGroupCall', random_id: int, message: 'TextWithEntities', allow_paid_stars: int = None, send_as: 'InputPeer' = None):
        self.call = call
        self.random_id = random_id
        self.message = message
        self.allow_paid_stars = allow_paid_stars
        self.send_as = send_as
    def to_dict(self):
        return {"call": self.call, "random_id": self.random_id, "message": self.message, "allow_paid_stars": self.allow_paid_stars, "send_as": self.send_as}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2983269392, signed=False)
        flags = 0
        if self.allow_paid_stars is not None: flags |= 1 << 0
        if self.send_as is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.call))
        writer.write_long(self.random_id, signed=False)
        writer.write(bytes(self.message))
        if flags & (1 << 0):
            writer.write_long(self.allow_paid_stars, signed=False)
        if flags & (1 << 1):
            writer.write(bytes(self.send_as))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        call = reader.tgread_object()
        random_id = reader.read_long()
        message = reader.tgread_object()
        if flags & (1 << 0):
            allow_paid_stars = reader.read_long()
        else:
            allow_paid_stars = None
        if flags & (1 << 1):
            send_as = reader.tgread_object()
        else:
            send_as = None
        return cls(call, random_id, message, allow_paid_stars, send_as)

@register
class PhoneSendGroupCallEncryptedMessage(TLObject):
    CONSTRUCTOR_ID = 3853493613
    __slots__ = ('call', 'encrypted_message')
    def __init__(self, call: 'InputGroupCall', encrypted_message: bytes):
        self.call = call
        self.encrypted_message = encrypted_message
    def to_dict(self):
        return {"call": self.call, "encrypted_message": self.encrypted_message}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3853493613, signed=False)
        writer.write(bytes(self.call))
        writer.write_bytes(self.encrypted_message)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        call = reader.tgread_object()
        encrypted_message = reader.read_bytes()
        return cls(call, encrypted_message)

@register
class PhoneDeleteGroupCallMessages(TLObject):
    CONSTRUCTOR_ID = 4132394231
    __slots__ = ('report_spam', 'call', 'messages')
    def __init__(self, call: 'InputGroupCall', messages: 'Vector', report_spam: bool = None):
        self.report_spam = report_spam
        self.call = call
        self.messages = messages
    def to_dict(self):
        return {"report_spam": self.report_spam, "call": self.call, "messages": self.messages}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4132394231, signed=False)
        flags = 0
        if self.report_spam: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.call))
        writer.write(bytes(self.messages))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        report_spam = bool(flags & (1 << 0))
        call = reader.tgread_object()
        messages = reader.tgread_object()
        return cls(report_spam, call, messages)

@register
class PhoneDeleteGroupCallParticipantMessages(TLObject):
    CONSTRUCTOR_ID = 499117216
    __slots__ = ('report_spam', 'call', 'participant')
    def __init__(self, call: 'InputGroupCall', participant: 'InputPeer', report_spam: bool = None):
        self.report_spam = report_spam
        self.call = call
        self.participant = participant
    def to_dict(self):
        return {"report_spam": self.report_spam, "call": self.call, "participant": self.participant}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(499117216, signed=False)
        flags = 0
        if self.report_spam: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.call))
        writer.write(bytes(self.participant))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        report_spam = bool(flags & (1 << 0))
        call = reader.tgread_object()
        participant = reader.tgread_object()
        return cls(report_spam, call, participant)

@register
class PhoneGetGroupCallStars(TLObject):
    CONSTRUCTOR_ID = 1868784386
    __slots__ = ('call')
    def __init__(self, call: 'InputGroupCall'):
        self.call = call
    def to_dict(self):
        return {"call": self.call}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1868784386, signed=False)
        writer.write(bytes(self.call))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        call = reader.tgread_object()
        return cls(call)

@register
class PhoneSaveDefaultSendAs(TLObject):
    CONSTRUCTOR_ID = 1097313745
    __slots__ = ('call', 'send_as')
    def __init__(self, call: 'InputGroupCall', send_as: 'InputPeer'):
        self.call = call
        self.send_as = send_as
    def to_dict(self):
        return {"call": self.call, "send_as": self.send_as}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1097313745, signed=False)
        writer.write(bytes(self.call))
        writer.write(bytes(self.send_as))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        call = reader.tgread_object()
        send_as = reader.tgread_object()
        return cls(call, send_as)

