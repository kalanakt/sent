"""Auto-generated TL functions. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

@register
class ChannelsReadHistory(TLObject):
    CONSTRUCTOR_ID = 3423619383
    __slots__ = ('channel', 'max_id')
    def __init__(self, channel: 'InputChannel', max_id: int):
        self.channel = channel
        self.max_id = max_id
    def to_dict(self):
        return {"channel": self.channel, "max_id": self.max_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3423619383, signed=False)
        writer.write(bytes(self.channel))
        writer.write_int(self.max_id, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        channel = reader.tgread_object()
        max_id = reader.read_int()
        return cls(channel, max_id)

@register
class ChannelsDeleteMessages(TLObject):
    CONSTRUCTOR_ID = 2227305806
    __slots__ = ('channel', 'id')
    def __init__(self, channel: 'InputChannel', id: 'Vector'):
        self.channel = channel
        self.id = id
    def to_dict(self):
        return {"channel": self.channel, "id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2227305806, signed=False)
        writer.write(bytes(self.channel))
        writer.write(bytes(self.id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        channel = reader.tgread_object()
        id = reader.tgread_object()
        return cls(channel, id)

@register
class ChannelsReportSpam(TLObject):
    CONSTRUCTOR_ID = 4098523925
    __slots__ = ('channel', 'participant', 'id')
    def __init__(self, channel: 'InputChannel', participant: 'InputPeer', id: 'Vector'):
        self.channel = channel
        self.participant = participant
        self.id = id
    def to_dict(self):
        return {"channel": self.channel, "participant": self.participant, "id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4098523925, signed=False)
        writer.write(bytes(self.channel))
        writer.write(bytes(self.participant))
        writer.write(bytes(self.id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        channel = reader.tgread_object()
        participant = reader.tgread_object()
        id = reader.tgread_object()
        return cls(channel, participant, id)

@register
class ChannelsGetMessages(TLObject):
    CONSTRUCTOR_ID = 2911672867
    __slots__ = ('channel', 'id')
    def __init__(self, channel: 'InputChannel', id: 'Vector'):
        self.channel = channel
        self.id = id
    def to_dict(self):
        return {"channel": self.channel, "id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2911672867, signed=False)
        writer.write(bytes(self.channel))
        writer.write(bytes(self.id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        channel = reader.tgread_object()
        id = reader.tgread_object()
        return cls(channel, id)

@register
class ChannelsGetParticipants(TLObject):
    CONSTRUCTOR_ID = 2010044880
    __slots__ = ('channel', 'filter', 'offset', 'limit', 'hash')
    def __init__(self, channel: 'InputChannel', filter: 'ChannelParticipantsFilter', offset: int, limit: int, hash: int):
        self.channel = channel
        self.filter = filter
        self.offset = offset
        self.limit = limit
        self.hash = hash
    def to_dict(self):
        return {"channel": self.channel, "filter": self.filter, "offset": self.offset, "limit": self.limit, "hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2010044880, signed=False)
        writer.write(bytes(self.channel))
        writer.write(bytes(self.filter))
        writer.write_int(self.offset, signed=True)
        writer.write_int(self.limit, signed=True)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        channel = reader.tgread_object()
        filter = reader.tgread_object()
        offset = reader.read_int()
        limit = reader.read_int()
        hash = reader.read_long()
        return cls(channel, filter, offset, limit, hash)

@register
class ChannelsGetParticipant(TLObject):
    CONSTRUCTOR_ID = 2695589062
    __slots__ = ('channel', 'participant')
    def __init__(self, channel: 'InputChannel', participant: 'InputPeer'):
        self.channel = channel
        self.participant = participant
    def to_dict(self):
        return {"channel": self.channel, "participant": self.participant}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2695589062, signed=False)
        writer.write(bytes(self.channel))
        writer.write(bytes(self.participant))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        channel = reader.tgread_object()
        participant = reader.tgread_object()
        return cls(channel, participant)

@register
class ChannelsGetChannels(TLObject):
    CONSTRUCTOR_ID = 176122811
    __slots__ = ('id')
    def __init__(self, id: 'Vector'):
        self.id = id
    def to_dict(self):
        return {"id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(176122811, signed=False)
        writer.write(bytes(self.id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        id = reader.tgread_object()
        return cls(id)

@register
class ChannelsGetFullChannel(TLObject):
    CONSTRUCTOR_ID = 141781513
    __slots__ = ('channel')
    def __init__(self, channel: 'InputChannel'):
        self.channel = channel
    def to_dict(self):
        return {"channel": self.channel}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(141781513, signed=False)
        writer.write(bytes(self.channel))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        channel = reader.tgread_object()
        return cls(channel)

@register
class ChannelsCreateChannel(TLObject):
    CONSTRUCTOR_ID = 2432722695
    __slots__ = ('broadcast', 'megagroup', 'for_import', 'forum', 'title', 'about', 'geo_point', 'address', 'ttl_period')
    def __init__(self, title: str, about: str, broadcast: bool = None, megagroup: bool = None, for_import: bool = None, forum: bool = None, geo_point: 'InputGeoPoint' = None, address: str = None, ttl_period: int = None):
        self.broadcast = broadcast
        self.megagroup = megagroup
        self.for_import = for_import
        self.forum = forum
        self.title = title
        self.about = about
        self.geo_point = geo_point
        self.address = address
        self.ttl_period = ttl_period
    def to_dict(self):
        return {"broadcast": self.broadcast, "megagroup": self.megagroup, "for_import": self.for_import, "forum": self.forum, "title": self.title, "about": self.about, "geo_point": self.geo_point, "address": self.address, "ttl_period": self.ttl_period}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2432722695, signed=False)
        flags = 0
        if self.broadcast: flags |= 1 << 0
        if self.megagroup: flags |= 1 << 1
        if self.for_import: flags |= 1 << 3
        if self.forum: flags |= 1 << 5
        if self.geo_point is not None: flags |= 1 << 2
        if self.address is not None: flags |= 1 << 2
        if self.ttl_period is not None: flags |= 1 << 4
        writer.write_int(flags, signed=False)
        writer.write_string(self.title)
        writer.write_string(self.about)
        if flags & (1 << 2):
            writer.write(bytes(self.geo_point))
        if flags & (1 << 2):
            writer.write_string(self.address)
        if flags & (1 << 4):
            writer.write_int(self.ttl_period, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        broadcast = bool(flags & (1 << 0))
        megagroup = bool(flags & (1 << 1))
        for_import = bool(flags & (1 << 3))
        forum = bool(flags & (1 << 5))
        title = reader.read_string()
        about = reader.read_string()
        if flags & (1 << 2):
            geo_point = reader.tgread_object()
        else:
            geo_point = None
        if flags & (1 << 2):
            address = reader.read_string()
        else:
            address = None
        if flags & (1 << 4):
            ttl_period = reader.read_int()
        else:
            ttl_period = None
        return cls(broadcast, megagroup, for_import, forum, title, about, geo_point, address, ttl_period)

@register
class ChannelsEditAdmin(TLObject):
    CONSTRUCTOR_ID = 2593697128
    __slots__ = ('channel', 'user_id', 'admin_rights', 'rank')
    def __init__(self, channel: 'InputChannel', user_id: 'InputUser', admin_rights: 'ChatAdminRights', rank: str = None):
        self.channel = channel
        self.user_id = user_id
        self.admin_rights = admin_rights
        self.rank = rank
    def to_dict(self):
        return {"channel": self.channel, "user_id": self.user_id, "admin_rights": self.admin_rights, "rank": self.rank}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2593697128, signed=False)
        flags = 0
        if self.rank is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.channel))
        writer.write(bytes(self.user_id))
        writer.write(bytes(self.admin_rights))
        if flags & (1 << 0):
            writer.write_string(self.rank)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        channel = reader.tgread_object()
        user_id = reader.tgread_object()
        admin_rights = reader.tgread_object()
        if flags & (1 << 0):
            rank = reader.read_string()
        else:
            rank = None
        return cls(channel, user_id, admin_rights, rank)

@register
class ChannelsEditTitle(TLObject):
    CONSTRUCTOR_ID = 1450044624
    __slots__ = ('channel', 'title')
    def __init__(self, channel: 'InputChannel', title: str):
        self.channel = channel
        self.title = title
    def to_dict(self):
        return {"channel": self.channel, "title": self.title}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1450044624, signed=False)
        writer.write(bytes(self.channel))
        writer.write_string(self.title)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        channel = reader.tgread_object()
        title = reader.read_string()
        return cls(channel, title)

@register
class ChannelsEditPhoto(TLObject):
    CONSTRUCTOR_ID = 4046346185
    __slots__ = ('channel', 'photo')
    def __init__(self, channel: 'InputChannel', photo: 'InputChatPhoto'):
        self.channel = channel
        self.photo = photo
    def to_dict(self):
        return {"channel": self.channel, "photo": self.photo}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4046346185, signed=False)
        writer.write(bytes(self.channel))
        writer.write(bytes(self.photo))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        channel = reader.tgread_object()
        photo = reader.tgread_object()
        return cls(channel, photo)

@register
class ChannelsCheckUsername(TLObject):
    CONSTRUCTOR_ID = 283557164
    __slots__ = ('channel', 'username')
    def __init__(self, channel: 'InputChannel', username: str):
        self.channel = channel
        self.username = username
    def to_dict(self):
        return {"channel": self.channel, "username": self.username}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(283557164, signed=False)
        writer.write(bytes(self.channel))
        writer.write_string(self.username)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        channel = reader.tgread_object()
        username = reader.read_string()
        return cls(channel, username)

@register
class ChannelsUpdateUsername(TLObject):
    CONSTRUCTOR_ID = 890549214
    __slots__ = ('channel', 'username')
    def __init__(self, channel: 'InputChannel', username: str):
        self.channel = channel
        self.username = username
    def to_dict(self):
        return {"channel": self.channel, "username": self.username}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(890549214, signed=False)
        writer.write(bytes(self.channel))
        writer.write_string(self.username)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        channel = reader.tgread_object()
        username = reader.read_string()
        return cls(channel, username)

@register
class ChannelsJoinChannel(TLObject):
    CONSTRUCTOR_ID = 615851205
    __slots__ = ('channel')
    def __init__(self, channel: 'InputChannel'):
        self.channel = channel
    def to_dict(self):
        return {"channel": self.channel}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(615851205, signed=False)
        writer.write(bytes(self.channel))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        channel = reader.tgread_object()
        return cls(channel)

@register
class ChannelsLeaveChannel(TLObject):
    CONSTRUCTOR_ID = 4164332181
    __slots__ = ('channel')
    def __init__(self, channel: 'InputChannel'):
        self.channel = channel
    def to_dict(self):
        return {"channel": self.channel}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4164332181, signed=False)
        writer.write(bytes(self.channel))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        channel = reader.tgread_object()
        return cls(channel)

@register
class ChannelsInviteToChannel(TLObject):
    CONSTRUCTOR_ID = 3387112788
    __slots__ = ('channel', 'users')
    def __init__(self, channel: 'InputChannel', users: 'Vector'):
        self.channel = channel
        self.users = users
    def to_dict(self):
        return {"channel": self.channel, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3387112788, signed=False)
        writer.write(bytes(self.channel))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        channel = reader.tgread_object()
        users = reader.tgread_object()
        return cls(channel, users)

@register
class ChannelsDeleteChannel(TLObject):
    CONSTRUCTOR_ID = 3222347747
    __slots__ = ('channel')
    def __init__(self, channel: 'InputChannel'):
        self.channel = channel
    def to_dict(self):
        return {"channel": self.channel}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3222347747, signed=False)
        writer.write(bytes(self.channel))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        channel = reader.tgread_object()
        return cls(channel)

@register
class ChannelsExportMessageLink(TLObject):
    CONSTRUCTOR_ID = 3862932971
    __slots__ = ('grouped', 'thread', 'channel', 'id')
    def __init__(self, channel: 'InputChannel', id: int, grouped: bool = None, thread: bool = None):
        self.grouped = grouped
        self.thread = thread
        self.channel = channel
        self.id = id
    def to_dict(self):
        return {"grouped": self.grouped, "thread": self.thread, "channel": self.channel, "id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3862932971, signed=False)
        flags = 0
        if self.grouped: flags |= 1 << 0
        if self.thread: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.channel))
        writer.write_int(self.id, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        grouped = bool(flags & (1 << 0))
        thread = bool(flags & (1 << 1))
        channel = reader.tgread_object()
        id = reader.read_int()
        return cls(grouped, thread, channel, id)

@register
class ChannelsToggleSignatures(TLObject):
    CONSTRUCTOR_ID = 1099781276
    __slots__ = ('signatures_enabled', 'profiles_enabled', 'channel')
    def __init__(self, channel: 'InputChannel', signatures_enabled: bool = None, profiles_enabled: bool = None):
        self.signatures_enabled = signatures_enabled
        self.profiles_enabled = profiles_enabled
        self.channel = channel
    def to_dict(self):
        return {"signatures_enabled": self.signatures_enabled, "profiles_enabled": self.profiles_enabled, "channel": self.channel}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1099781276, signed=False)
        flags = 0
        if self.signatures_enabled: flags |= 1 << 0
        if self.profiles_enabled: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.channel))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        signatures_enabled = bool(flags & (1 << 0))
        profiles_enabled = bool(flags & (1 << 1))
        channel = reader.tgread_object()
        return cls(signatures_enabled, profiles_enabled, channel)

@register
class ChannelsGetAdminedPublicChannels(TLObject):
    CONSTRUCTOR_ID = 4172297903
    __slots__ = ('by_location', 'check_limit', 'for_personal')
    def __init__(self, by_location: bool = None, check_limit: bool = None, for_personal: bool = None):
        self.by_location = by_location
        self.check_limit = check_limit
        self.for_personal = for_personal
    def to_dict(self):
        return {"by_location": self.by_location, "check_limit": self.check_limit, "for_personal": self.for_personal}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4172297903, signed=False)
        flags = 0
        if self.by_location: flags |= 1 << 0
        if self.check_limit: flags |= 1 << 1
        if self.for_personal: flags |= 1 << 2
        writer.write_int(flags, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        by_location = bool(flags & (1 << 0))
        check_limit = bool(flags & (1 << 1))
        for_personal = bool(flags & (1 << 2))
        return cls(by_location, check_limit, for_personal)

@register
class ChannelsEditBanned(TLObject):
    CONSTRUCTOR_ID = 2531708289
    __slots__ = ('channel', 'participant', 'banned_rights')
    def __init__(self, channel: 'InputChannel', participant: 'InputPeer', banned_rights: 'ChatBannedRights'):
        self.channel = channel
        self.participant = participant
        self.banned_rights = banned_rights
    def to_dict(self):
        return {"channel": self.channel, "participant": self.participant, "banned_rights": self.banned_rights}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2531708289, signed=False)
        writer.write(bytes(self.channel))
        writer.write(bytes(self.participant))
        writer.write(bytes(self.banned_rights))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        channel = reader.tgread_object()
        participant = reader.tgread_object()
        banned_rights = reader.tgread_object()
        return cls(channel, participant, banned_rights)

@register
class ChannelsGetAdminLog(TLObject):
    CONSTRUCTOR_ID = 870184064
    __slots__ = ('channel', 'q', 'events_filter', 'admins', 'max_id', 'min_id', 'limit')
    def __init__(self, channel: 'InputChannel', q: str, max_id: int, min_id: int, limit: int, events_filter: 'ChannelAdminLogEventsFilter' = None, admins: 'Vector' = None):
        self.channel = channel
        self.q = q
        self.events_filter = events_filter
        self.admins = admins
        self.max_id = max_id
        self.min_id = min_id
        self.limit = limit
    def to_dict(self):
        return {"channel": self.channel, "q": self.q, "events_filter": self.events_filter, "admins": self.admins, "max_id": self.max_id, "min_id": self.min_id, "limit": self.limit}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(870184064, signed=False)
        flags = 0
        if self.events_filter is not None: flags |= 1 << 0
        if self.admins is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.channel))
        writer.write_string(self.q)
        if flags & (1 << 0):
            writer.write(bytes(self.events_filter))
        if flags & (1 << 1):
            writer.write(bytes(self.admins))
        writer.write_long(self.max_id, signed=False)
        writer.write_long(self.min_id, signed=False)
        writer.write_int(self.limit, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        channel = reader.tgread_object()
        q = reader.read_string()
        if flags & (1 << 0):
            events_filter = reader.tgread_object()
        else:
            events_filter = None
        if flags & (1 << 1):
            admins = reader.tgread_object()
        else:
            admins = None
        max_id = reader.read_long()
        min_id = reader.read_long()
        limit = reader.read_int()
        return cls(channel, q, events_filter, admins, max_id, min_id, limit)

@register
class ChannelsSetStickers(TLObject):
    CONSTRUCTOR_ID = 3935085817
    __slots__ = ('channel', 'stickerset')
    def __init__(self, channel: 'InputChannel', stickerset: 'InputStickerSet'):
        self.channel = channel
        self.stickerset = stickerset
    def to_dict(self):
        return {"channel": self.channel, "stickerset": self.stickerset}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3935085817, signed=False)
        writer.write(bytes(self.channel))
        writer.write(bytes(self.stickerset))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        channel = reader.tgread_object()
        stickerset = reader.tgread_object()
        return cls(channel, stickerset)

@register
class ChannelsReadMessageContents(TLObject):
    CONSTRUCTOR_ID = 3937786936
    __slots__ = ('channel', 'id')
    def __init__(self, channel: 'InputChannel', id: 'Vector'):
        self.channel = channel
        self.id = id
    def to_dict(self):
        return {"channel": self.channel, "id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3937786936, signed=False)
        writer.write(bytes(self.channel))
        writer.write(bytes(self.id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        channel = reader.tgread_object()
        id = reader.tgread_object()
        return cls(channel, id)

@register
class ChannelsDeleteHistory(TLObject):
    CONSTRUCTOR_ID = 2611648071
    __slots__ = ('for_everyone', 'channel', 'max_id')
    def __init__(self, channel: 'InputChannel', max_id: int, for_everyone: bool = None):
        self.for_everyone = for_everyone
        self.channel = channel
        self.max_id = max_id
    def to_dict(self):
        return {"for_everyone": self.for_everyone, "channel": self.channel, "max_id": self.max_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2611648071, signed=False)
        flags = 0
        if self.for_everyone: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.channel))
        writer.write_int(self.max_id, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        for_everyone = bool(flags & (1 << 0))
        channel = reader.tgread_object()
        max_id = reader.read_int()
        return cls(for_everyone, channel, max_id)

@register
class ChannelsTogglePreHistoryHidden(TLObject):
    CONSTRUCTOR_ID = 3938171212
    __slots__ = ('channel', 'enabled')
    def __init__(self, channel: 'InputChannel', enabled: bool):
        self.channel = channel
        self.enabled = enabled
    def to_dict(self):
        return {"channel": self.channel, "enabled": self.enabled}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3938171212, signed=False)
        writer.write(bytes(self.channel))
        writer.write(serialize_bool(self.enabled))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        channel = reader.tgread_object()
        enabled = reader.tgread_bool()
        return cls(channel, enabled)

@register
class ChannelsGetLeftChannels(TLObject):
    CONSTRUCTOR_ID = 2202135744
    __slots__ = ('offset')
    def __init__(self, offset: int):
        self.offset = offset
    def to_dict(self):
        return {"offset": self.offset}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2202135744, signed=False)
        writer.write_int(self.offset, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        offset = reader.read_int()
        return cls(offset)

@register
class ChannelsGetGroupsForDiscussion(TLObject):
    CONSTRUCTOR_ID = 4124758904
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4124758904, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class ChannelsSetDiscussionGroup(TLObject):
    CONSTRUCTOR_ID = 1079520178
    __slots__ = ('broadcast', 'group')
    def __init__(self, broadcast: 'InputChannel', group: 'InputChannel'):
        self.broadcast = broadcast
        self.group = group
    def to_dict(self):
        return {"broadcast": self.broadcast, "group": self.group}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1079520178, signed=False)
        writer.write(bytes(self.broadcast))
        writer.write(bytes(self.group))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        broadcast = reader.tgread_object()
        group = reader.tgread_object()
        return cls(broadcast, group)

@register
class ChannelsEditLocation(TLObject):
    CONSTRUCTOR_ID = 1491484525
    __slots__ = ('channel', 'geo_point', 'address')
    def __init__(self, channel: 'InputChannel', geo_point: 'InputGeoPoint', address: str):
        self.channel = channel
        self.geo_point = geo_point
        self.address = address
    def to_dict(self):
        return {"channel": self.channel, "geo_point": self.geo_point, "address": self.address}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1491484525, signed=False)
        writer.write(bytes(self.channel))
        writer.write(bytes(self.geo_point))
        writer.write_string(self.address)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        channel = reader.tgread_object()
        geo_point = reader.tgread_object()
        address = reader.read_string()
        return cls(channel, geo_point, address)

@register
class ChannelsToggleSlowMode(TLObject):
    CONSTRUCTOR_ID = 3990134512
    __slots__ = ('channel', 'seconds')
    def __init__(self, channel: 'InputChannel', seconds: int):
        self.channel = channel
        self.seconds = seconds
    def to_dict(self):
        return {"channel": self.channel, "seconds": self.seconds}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3990134512, signed=False)
        writer.write(bytes(self.channel))
        writer.write_int(self.seconds, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        channel = reader.tgread_object()
        seconds = reader.read_int()
        return cls(channel, seconds)

@register
class ChannelsGetInactiveChannels(TLObject):
    CONSTRUCTOR_ID = 300429806
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(300429806, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class ChannelsConvertToGigagroup(TLObject):
    CONSTRUCTOR_ID = 187239529
    __slots__ = ('channel')
    def __init__(self, channel: 'InputChannel'):
        self.channel = channel
    def to_dict(self):
        return {"channel": self.channel}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(187239529, signed=False)
        writer.write(bytes(self.channel))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        channel = reader.tgread_object()
        return cls(channel)

@register
class ChannelsGetSendAs(TLObject):
    CONSTRUCTOR_ID = 3884295231
    __slots__ = ('for_paid_reactions', 'for_live_stories', 'peer')
    def __init__(self, peer: 'InputPeer', for_paid_reactions: bool = None, for_live_stories: bool = None):
        self.for_paid_reactions = for_paid_reactions
        self.for_live_stories = for_live_stories
        self.peer = peer
    def to_dict(self):
        return {"for_paid_reactions": self.for_paid_reactions, "for_live_stories": self.for_live_stories, "peer": self.peer}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3884295231, signed=False)
        flags = 0
        if self.for_paid_reactions: flags |= 1 << 0
        if self.for_live_stories: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        for_paid_reactions = bool(flags & (1 << 0))
        for_live_stories = bool(flags & (1 << 1))
        peer = reader.tgread_object()
        return cls(for_paid_reactions, for_live_stories, peer)

@register
class ChannelsDeleteParticipantHistory(TLObject):
    CONSTRUCTOR_ID = 913655003
    __slots__ = ('channel', 'participant')
    def __init__(self, channel: 'InputChannel', participant: 'InputPeer'):
        self.channel = channel
        self.participant = participant
    def to_dict(self):
        return {"channel": self.channel, "participant": self.participant}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(913655003, signed=False)
        writer.write(bytes(self.channel))
        writer.write(bytes(self.participant))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        channel = reader.tgread_object()
        participant = reader.tgread_object()
        return cls(channel, participant)

@register
class ChannelsToggleJoinToSend(TLObject):
    CONSTRUCTOR_ID = 3838547328
    __slots__ = ('channel', 'enabled')
    def __init__(self, channel: 'InputChannel', enabled: bool):
        self.channel = channel
        self.enabled = enabled
    def to_dict(self):
        return {"channel": self.channel, "enabled": self.enabled}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3838547328, signed=False)
        writer.write(bytes(self.channel))
        writer.write(serialize_bool(self.enabled))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        channel = reader.tgread_object()
        enabled = reader.tgread_bool()
        return cls(channel, enabled)

@register
class ChannelsToggleJoinRequest(TLObject):
    CONSTRUCTOR_ID = 1277789622
    __slots__ = ('channel', 'enabled')
    def __init__(self, channel: 'InputChannel', enabled: bool):
        self.channel = channel
        self.enabled = enabled
    def to_dict(self):
        return {"channel": self.channel, "enabled": self.enabled}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1277789622, signed=False)
        writer.write(bytes(self.channel))
        writer.write(serialize_bool(self.enabled))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        channel = reader.tgread_object()
        enabled = reader.tgread_bool()
        return cls(channel, enabled)

@register
class ChannelsReorderUsernames(TLObject):
    CONSTRUCTOR_ID = 3025988893
    __slots__ = ('channel', 'order')
    def __init__(self, channel: 'InputChannel', order: 'Vector'):
        self.channel = channel
        self.order = order
    def to_dict(self):
        return {"channel": self.channel, "order": self.order}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3025988893, signed=False)
        writer.write(bytes(self.channel))
        writer.write(bytes(self.order))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        channel = reader.tgread_object()
        order = reader.tgread_object()
        return cls(channel, order)

@register
class ChannelsToggleUsername(TLObject):
    CONSTRUCTOR_ID = 1358053637
    __slots__ = ('channel', 'username', 'active')
    def __init__(self, channel: 'InputChannel', username: str, active: bool):
        self.channel = channel
        self.username = username
        self.active = active
    def to_dict(self):
        return {"channel": self.channel, "username": self.username, "active": self.active}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1358053637, signed=False)
        writer.write(bytes(self.channel))
        writer.write_string(self.username)
        writer.write(serialize_bool(self.active))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        channel = reader.tgread_object()
        username = reader.read_string()
        active = reader.tgread_bool()
        return cls(channel, username, active)

@register
class ChannelsDeactivateAllUsernames(TLObject):
    CONSTRUCTOR_ID = 170155475
    __slots__ = ('channel')
    def __init__(self, channel: 'InputChannel'):
        self.channel = channel
    def to_dict(self):
        return {"channel": self.channel}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(170155475, signed=False)
        writer.write(bytes(self.channel))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        channel = reader.tgread_object()
        return cls(channel)

@register
class ChannelsToggleForum(TLObject):
    CONSTRUCTOR_ID = 1073174324
    __slots__ = ('channel', 'enabled', 'tabs')
    def __init__(self, channel: 'InputChannel', enabled: bool, tabs: bool):
        self.channel = channel
        self.enabled = enabled
        self.tabs = tabs
    def to_dict(self):
        return {"channel": self.channel, "enabled": self.enabled, "tabs": self.tabs}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1073174324, signed=False)
        writer.write(bytes(self.channel))
        writer.write(serialize_bool(self.enabled))
        writer.write(serialize_bool(self.tabs))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        channel = reader.tgread_object()
        enabled = reader.tgread_bool()
        tabs = reader.tgread_bool()
        return cls(channel, enabled, tabs)

@register
class ChannelsToggleAntiSpam(TLObject):
    CONSTRUCTOR_ID = 1760814315
    __slots__ = ('channel', 'enabled')
    def __init__(self, channel: 'InputChannel', enabled: bool):
        self.channel = channel
        self.enabled = enabled
    def to_dict(self):
        return {"channel": self.channel, "enabled": self.enabled}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1760814315, signed=False)
        writer.write(bytes(self.channel))
        writer.write(serialize_bool(self.enabled))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        channel = reader.tgread_object()
        enabled = reader.tgread_bool()
        return cls(channel, enabled)

@register
class ChannelsReportAntiSpamFalsePositive(TLObject):
    CONSTRUCTOR_ID = 2823857811
    __slots__ = ('channel', 'msg_id')
    def __init__(self, channel: 'InputChannel', msg_id: int):
        self.channel = channel
        self.msg_id = msg_id
    def to_dict(self):
        return {"channel": self.channel, "msg_id": self.msg_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2823857811, signed=False)
        writer.write(bytes(self.channel))
        writer.write_int(self.msg_id, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        channel = reader.tgread_object()
        msg_id = reader.read_int()
        return cls(channel, msg_id)

@register
class ChannelsToggleParticipantsHidden(TLObject):
    CONSTRUCTOR_ID = 1785624660
    __slots__ = ('channel', 'enabled')
    def __init__(self, channel: 'InputChannel', enabled: bool):
        self.channel = channel
        self.enabled = enabled
    def to_dict(self):
        return {"channel": self.channel, "enabled": self.enabled}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1785624660, signed=False)
        writer.write(bytes(self.channel))
        writer.write(serialize_bool(self.enabled))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        channel = reader.tgread_object()
        enabled = reader.tgread_bool()
        return cls(channel, enabled)

@register
class ChannelsUpdateColor(TLObject):
    CONSTRUCTOR_ID = 3635033713
    __slots__ = ('for_profile', 'channel', 'color', 'background_emoji_id')
    def __init__(self, channel: 'InputChannel', for_profile: bool = None, color: int = None, background_emoji_id: int = None):
        self.for_profile = for_profile
        self.channel = channel
        self.color = color
        self.background_emoji_id = background_emoji_id
    def to_dict(self):
        return {"for_profile": self.for_profile, "channel": self.channel, "color": self.color, "background_emoji_id": self.background_emoji_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3635033713, signed=False)
        flags = 0
        if self.for_profile: flags |= 1 << 1
        if self.color is not None: flags |= 1 << 2
        if self.background_emoji_id is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.channel))
        if flags & (1 << 2):
            writer.write_int(self.color, signed=True)
        if flags & (1 << 0):
            writer.write_long(self.background_emoji_id, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        for_profile = bool(flags & (1 << 1))
        channel = reader.tgread_object()
        if flags & (1 << 2):
            color = reader.read_int()
        else:
            color = None
        if flags & (1 << 0):
            background_emoji_id = reader.read_long()
        else:
            background_emoji_id = None
        return cls(for_profile, channel, color, background_emoji_id)

@register
class ChannelsToggleViewForumAsMessages(TLObject):
    CONSTRUCTOR_ID = 2537077525
    __slots__ = ('channel', 'enabled')
    def __init__(self, channel: 'InputChannel', enabled: bool):
        self.channel = channel
        self.enabled = enabled
    def to_dict(self):
        return {"channel": self.channel, "enabled": self.enabled}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2537077525, signed=False)
        writer.write(bytes(self.channel))
        writer.write(serialize_bool(self.enabled))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        channel = reader.tgread_object()
        enabled = reader.tgread_bool()
        return cls(channel, enabled)

@register
class ChannelsGetChannelRecommendations(TLObject):
    CONSTRUCTOR_ID = 631707458
    __slots__ = ('channel')
    def __init__(self, channel: 'InputChannel' = None):
        self.channel = channel
    def to_dict(self):
        return {"channel": self.channel}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(631707458, signed=False)
        flags = 0
        if self.channel is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        if flags & (1 << 0):
            writer.write(bytes(self.channel))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        if flags & (1 << 0):
            channel = reader.tgread_object()
        else:
            channel = None
        return cls(channel)

@register
class ChannelsUpdateEmojiStatus(TLObject):
    CONSTRUCTOR_ID = 4040418984
    __slots__ = ('channel', 'emoji_status')
    def __init__(self, channel: 'InputChannel', emoji_status: 'EmojiStatus'):
        self.channel = channel
        self.emoji_status = emoji_status
    def to_dict(self):
        return {"channel": self.channel, "emoji_status": self.emoji_status}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4040418984, signed=False)
        writer.write(bytes(self.channel))
        writer.write(bytes(self.emoji_status))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        channel = reader.tgread_object()
        emoji_status = reader.tgread_object()
        return cls(channel, emoji_status)

@register
class ChannelsSetBoostsToUnblockRestrictions(TLObject):
    CONSTRUCTOR_ID = 2906234094
    __slots__ = ('channel', 'boosts')
    def __init__(self, channel: 'InputChannel', boosts: int):
        self.channel = channel
        self.boosts = boosts
    def to_dict(self):
        return {"channel": self.channel, "boosts": self.boosts}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2906234094, signed=False)
        writer.write(bytes(self.channel))
        writer.write_int(self.boosts, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        channel = reader.tgread_object()
        boosts = reader.read_int()
        return cls(channel, boosts)

@register
class ChannelsSetEmojiStickers(TLObject):
    CONSTRUCTOR_ID = 1020866743
    __slots__ = ('channel', 'stickerset')
    def __init__(self, channel: 'InputChannel', stickerset: 'InputStickerSet'):
        self.channel = channel
        self.stickerset = stickerset
    def to_dict(self):
        return {"channel": self.channel, "stickerset": self.stickerset}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1020866743, signed=False)
        writer.write(bytes(self.channel))
        writer.write(bytes(self.stickerset))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        channel = reader.tgread_object()
        stickerset = reader.tgread_object()
        return cls(channel, stickerset)

@register
class ChannelsRestrictSponsoredMessages(TLObject):
    CONSTRUCTOR_ID = 2598966553
    __slots__ = ('channel', 'restricted')
    def __init__(self, channel: 'InputChannel', restricted: bool):
        self.channel = channel
        self.restricted = restricted
    def to_dict(self):
        return {"channel": self.channel, "restricted": self.restricted}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2598966553, signed=False)
        writer.write(bytes(self.channel))
        writer.write(serialize_bool(self.restricted))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        channel = reader.tgread_object()
        restricted = reader.tgread_bool()
        return cls(channel, restricted)

@register
class ChannelsSearchPosts(TLObject):
    CONSTRUCTOR_ID = 4072993357
    __slots__ = ('hashtag', 'query', 'offset_rate', 'offset_peer', 'offset_id', 'limit', 'allow_paid_stars')
    def __init__(self, offset_rate: int, offset_peer: 'InputPeer', offset_id: int, limit: int, hashtag: str = None, query: str = None, allow_paid_stars: int = None):
        self.hashtag = hashtag
        self.query = query
        self.offset_rate = offset_rate
        self.offset_peer = offset_peer
        self.offset_id = offset_id
        self.limit = limit
        self.allow_paid_stars = allow_paid_stars
    def to_dict(self):
        return {"hashtag": self.hashtag, "query": self.query, "offset_rate": self.offset_rate, "offset_peer": self.offset_peer, "offset_id": self.offset_id, "limit": self.limit, "allow_paid_stars": self.allow_paid_stars}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4072993357, signed=False)
        flags = 0
        if self.hashtag is not None: flags |= 1 << 0
        if self.query is not None: flags |= 1 << 1
        if self.allow_paid_stars is not None: flags |= 1 << 2
        writer.write_int(flags, signed=False)
        if flags & (1 << 0):
            writer.write_string(self.hashtag)
        if flags & (1 << 1):
            writer.write_string(self.query)
        writer.write_int(self.offset_rate, signed=True)
        writer.write(bytes(self.offset_peer))
        writer.write_int(self.offset_id, signed=True)
        writer.write_int(self.limit, signed=True)
        if flags & (1 << 2):
            writer.write_long(self.allow_paid_stars, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        if flags & (1 << 0):
            hashtag = reader.read_string()
        else:
            hashtag = None
        if flags & (1 << 1):
            query = reader.read_string()
        else:
            query = None
        offset_rate = reader.read_int()
        offset_peer = reader.tgread_object()
        offset_id = reader.read_int()
        limit = reader.read_int()
        if flags & (1 << 2):
            allow_paid_stars = reader.read_long()
        else:
            allow_paid_stars = None
        return cls(hashtag, query, offset_rate, offset_peer, offset_id, limit, allow_paid_stars)

@register
class ChannelsUpdatePaidMessagesPrice(TLObject):
    CONSTRUCTOR_ID = 1259483771
    __slots__ = ('broadcast_messages_allowed', 'channel', 'send_paid_messages_stars')
    def __init__(self, channel: 'InputChannel', send_paid_messages_stars: int, broadcast_messages_allowed: bool = None):
        self.broadcast_messages_allowed = broadcast_messages_allowed
        self.channel = channel
        self.send_paid_messages_stars = send_paid_messages_stars
    def to_dict(self):
        return {"broadcast_messages_allowed": self.broadcast_messages_allowed, "channel": self.channel, "send_paid_messages_stars": self.send_paid_messages_stars}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1259483771, signed=False)
        flags = 0
        if self.broadcast_messages_allowed: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.channel))
        writer.write_long(self.send_paid_messages_stars, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        broadcast_messages_allowed = bool(flags & (1 << 0))
        channel = reader.tgread_object()
        send_paid_messages_stars = reader.read_long()
        return cls(broadcast_messages_allowed, channel, send_paid_messages_stars)

@register
class ChannelsToggleAutotranslation(TLObject):
    CONSTRUCTOR_ID = 377471137
    __slots__ = ('channel', 'enabled')
    def __init__(self, channel: 'InputChannel', enabled: bool):
        self.channel = channel
        self.enabled = enabled
    def to_dict(self):
        return {"channel": self.channel, "enabled": self.enabled}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(377471137, signed=False)
        writer.write(bytes(self.channel))
        writer.write(serialize_bool(self.enabled))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        channel = reader.tgread_object()
        enabled = reader.tgread_bool()
        return cls(channel, enabled)

@register
class ChannelsGetMessageAuthor(TLObject):
    CONSTRUCTOR_ID = 3974275302
    __slots__ = ('channel', 'id')
    def __init__(self, channel: 'InputChannel', id: int):
        self.channel = channel
        self.id = id
    def to_dict(self):
        return {"channel": self.channel, "id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3974275302, signed=False)
        writer.write(bytes(self.channel))
        writer.write_int(self.id, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        channel = reader.tgread_object()
        id = reader.read_int()
        return cls(channel, id)

@register
class ChannelsCheckSearchPostsFlood(TLObject):
    CONSTRUCTOR_ID = 576090389
    __slots__ = ('query')
    def __init__(self, query: str = None):
        self.query = query
    def to_dict(self):
        return {"query": self.query}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(576090389, signed=False)
        flags = 0
        if self.query is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        if flags & (1 << 0):
            writer.write_string(self.query)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        if flags & (1 << 0):
            query = reader.read_string()
        else:
            query = None
        return cls(query)

@register
class ChannelsSetMainProfileTab(TLObject):
    CONSTRUCTOR_ID = 897842353
    __slots__ = ('channel', 'tab')
    def __init__(self, channel: 'InputChannel', tab: 'ProfileTab'):
        self.channel = channel
        self.tab = tab
    def to_dict(self):
        return {"channel": self.channel, "tab": self.tab}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(897842353, signed=False)
        writer.write(bytes(self.channel))
        writer.write(bytes(self.tab))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        channel = reader.tgread_object()
        tab = reader.tgread_object()
        return cls(channel, tab)

