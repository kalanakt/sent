"""Auto-generated TL functions. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

@register
class MessagesGetMessages(TLObject):
    CONSTRUCTOR_ID = 1673946374
    __slots__ = ('id')
    def __init__(self, id: 'Vector'):
        self.id = id
    def to_dict(self):
        return {"id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1673946374, signed=False)
        writer.write(bytes(self.id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        id = reader.tgread_object()
        return cls(id)

@register
class MessagesGetDialogs(TLObject):
    CONSTRUCTOR_ID = 2700397391
    __slots__ = ('exclude_pinned', 'folder_id', 'offset_date', 'offset_id', 'offset_peer', 'limit', 'hash')
    def __init__(self, offset_date: int, offset_id: int, offset_peer: 'InputPeer', limit: int, hash: int, exclude_pinned: bool = None, folder_id: int = None):
        self.exclude_pinned = exclude_pinned
        self.folder_id = folder_id
        self.offset_date = offset_date
        self.offset_id = offset_id
        self.offset_peer = offset_peer
        self.limit = limit
        self.hash = hash
    def to_dict(self):
        return {"exclude_pinned": self.exclude_pinned, "folder_id": self.folder_id, "offset_date": self.offset_date, "offset_id": self.offset_id, "offset_peer": self.offset_peer, "limit": self.limit, "hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2700397391, signed=False)
        flags = 0
        if self.exclude_pinned: flags |= 1 << 0
        if self.folder_id is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        if flags & (1 << 1):
            writer.write_int(self.folder_id, signed=True)
        writer.write_int(self.offset_date, signed=True)
        writer.write_int(self.offset_id, signed=True)
        writer.write(bytes(self.offset_peer))
        writer.write_int(self.limit, signed=True)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        exclude_pinned = bool(flags & (1 << 0))
        if flags & (1 << 1):
            folder_id = reader.read_int()
        else:
            folder_id = None
        offset_date = reader.read_int()
        offset_id = reader.read_int()
        offset_peer = reader.tgread_object()
        limit = reader.read_int()
        hash = reader.read_long()
        return cls(exclude_pinned, folder_id, offset_date, offset_id, offset_peer, limit, hash)

@register
class MessagesGetHistory(TLObject):
    CONSTRUCTOR_ID = 1143203525
    __slots__ = ('peer', 'offset_id', 'offset_date', 'add_offset', 'limit', 'max_id', 'min_id', 'hash')
    def __init__(self, peer: 'InputPeer', offset_id: int, offset_date: int, add_offset: int, limit: int, max_id: int, min_id: int, hash: int):
        self.peer = peer
        self.offset_id = offset_id
        self.offset_date = offset_date
        self.add_offset = add_offset
        self.limit = limit
        self.max_id = max_id
        self.min_id = min_id
        self.hash = hash
    def to_dict(self):
        return {"peer": self.peer, "offset_id": self.offset_id, "offset_date": self.offset_date, "add_offset": self.add_offset, "limit": self.limit, "max_id": self.max_id, "min_id": self.min_id, "hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1143203525, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.offset_id, signed=True)
        writer.write_int(self.offset_date, signed=True)
        writer.write_int(self.add_offset, signed=True)
        writer.write_int(self.limit, signed=True)
        writer.write_int(self.max_id, signed=True)
        writer.write_int(self.min_id, signed=True)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        offset_id = reader.read_int()
        offset_date = reader.read_int()
        add_offset = reader.read_int()
        limit = reader.read_int()
        max_id = reader.read_int()
        min_id = reader.read_int()
        hash = reader.read_long()
        return cls(peer, offset_id, offset_date, add_offset, limit, max_id, min_id, hash)

@register
class MessagesSearch(TLObject):
    CONSTRUCTOR_ID = 703497338
    __slots__ = ('peer', 'q', 'from_id', 'saved_peer_id', 'saved_reaction', 'top_msg_id', 'filter', 'min_date', 'max_date', 'offset_id', 'add_offset', 'limit', 'max_id', 'min_id', 'hash')
    def __init__(self, peer: 'InputPeer', q: str, filter: 'MessagesFilter', min_date: int, max_date: int, offset_id: int, add_offset: int, limit: int, max_id: int, min_id: int, hash: int, from_id: 'InputPeer' = None, saved_peer_id: 'InputPeer' = None, saved_reaction: 'Vector' = None, top_msg_id: int = None):
        self.peer = peer
        self.q = q
        self.from_id = from_id
        self.saved_peer_id = saved_peer_id
        self.saved_reaction = saved_reaction
        self.top_msg_id = top_msg_id
        self.filter = filter
        self.min_date = min_date
        self.max_date = max_date
        self.offset_id = offset_id
        self.add_offset = add_offset
        self.limit = limit
        self.max_id = max_id
        self.min_id = min_id
        self.hash = hash
    def to_dict(self):
        return {"peer": self.peer, "q": self.q, "from_id": self.from_id, "saved_peer_id": self.saved_peer_id, "saved_reaction": self.saved_reaction, "top_msg_id": self.top_msg_id, "filter": self.filter, "min_date": self.min_date, "max_date": self.max_date, "offset_id": self.offset_id, "add_offset": self.add_offset, "limit": self.limit, "max_id": self.max_id, "min_id": self.min_id, "hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(703497338, signed=False)
        flags = 0
        if self.from_id is not None: flags |= 1 << 0
        if self.saved_peer_id is not None: flags |= 1 << 2
        if self.saved_reaction is not None: flags |= 1 << 3
        if self.top_msg_id is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write_string(self.q)
        if flags & (1 << 0):
            writer.write(bytes(self.from_id))
        if flags & (1 << 2):
            writer.write(bytes(self.saved_peer_id))
        if flags & (1 << 3):
            writer.write(bytes(self.saved_reaction))
        if flags & (1 << 1):
            writer.write_int(self.top_msg_id, signed=True)
        writer.write(bytes(self.filter))
        writer.write_int(self.min_date, signed=True)
        writer.write_int(self.max_date, signed=True)
        writer.write_int(self.offset_id, signed=True)
        writer.write_int(self.add_offset, signed=True)
        writer.write_int(self.limit, signed=True)
        writer.write_int(self.max_id, signed=True)
        writer.write_int(self.min_id, signed=True)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        peer = reader.tgread_object()
        q = reader.read_string()
        if flags & (1 << 0):
            from_id = reader.tgread_object()
        else:
            from_id = None
        if flags & (1 << 2):
            saved_peer_id = reader.tgread_object()
        else:
            saved_peer_id = None
        if flags & (1 << 3):
            saved_reaction = reader.tgread_object()
        else:
            saved_reaction = None
        if flags & (1 << 1):
            top_msg_id = reader.read_int()
        else:
            top_msg_id = None
        filter = reader.tgread_object()
        min_date = reader.read_int()
        max_date = reader.read_int()
        offset_id = reader.read_int()
        add_offset = reader.read_int()
        limit = reader.read_int()
        max_id = reader.read_int()
        min_id = reader.read_int()
        hash = reader.read_long()
        return cls(peer, q, from_id, saved_peer_id, saved_reaction, top_msg_id, filter, min_date, max_date, offset_id, add_offset, limit, max_id, min_id, hash)

@register
class MessagesReadHistory(TLObject):
    CONSTRUCTOR_ID = 238054714
    __slots__ = ('peer', 'max_id')
    def __init__(self, peer: 'InputPeer', max_id: int):
        self.peer = peer
        self.max_id = max_id
    def to_dict(self):
        return {"peer": self.peer, "max_id": self.max_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(238054714, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.max_id, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        max_id = reader.read_int()
        return cls(peer, max_id)

@register
class MessagesDeleteHistory(TLObject):
    CONSTRUCTOR_ID = 2962199082
    __slots__ = ('just_clear', 'revoke', 'peer', 'max_id', 'min_date', 'max_date')
    def __init__(self, peer: 'InputPeer', max_id: int, just_clear: bool = None, revoke: bool = None, min_date: int = None, max_date: int = None):
        self.just_clear = just_clear
        self.revoke = revoke
        self.peer = peer
        self.max_id = max_id
        self.min_date = min_date
        self.max_date = max_date
    def to_dict(self):
        return {"just_clear": self.just_clear, "revoke": self.revoke, "peer": self.peer, "max_id": self.max_id, "min_date": self.min_date, "max_date": self.max_date}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2962199082, signed=False)
        flags = 0
        if self.just_clear: flags |= 1 << 0
        if self.revoke: flags |= 1 << 1
        if self.min_date is not None: flags |= 1 << 2
        if self.max_date is not None: flags |= 1 << 3
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.max_id, signed=True)
        if flags & (1 << 2):
            writer.write_int(self.min_date, signed=True)
        if flags & (1 << 3):
            writer.write_int(self.max_date, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        just_clear = bool(flags & (1 << 0))
        revoke = bool(flags & (1 << 1))
        peer = reader.tgread_object()
        max_id = reader.read_int()
        if flags & (1 << 2):
            min_date = reader.read_int()
        else:
            min_date = None
        if flags & (1 << 3):
            max_date = reader.read_int()
        else:
            max_date = None
        return cls(just_clear, revoke, peer, max_id, min_date, max_date)

@register
class MessagesDeleteMessages(TLObject):
    CONSTRUCTOR_ID = 3851326930
    __slots__ = ('revoke', 'id')
    def __init__(self, id: 'Vector', revoke: bool = None):
        self.revoke = revoke
        self.id = id
    def to_dict(self):
        return {"revoke": self.revoke, "id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3851326930, signed=False)
        flags = 0
        if self.revoke: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        revoke = bool(flags & (1 << 0))
        id = reader.tgread_object()
        return cls(revoke, id)

@register
class MessagesReceivedMessages(TLObject):
    CONSTRUCTOR_ID = 94983360
    __slots__ = ('max_id')
    def __init__(self, max_id: int):
        self.max_id = max_id
    def to_dict(self):
        return {"max_id": self.max_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(94983360, signed=False)
        writer.write_int(self.max_id, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        max_id = reader.read_int()
        return cls(max_id)

@register
class MessagesSetTyping(TLObject):
    CONSTRUCTOR_ID = 1486110434
    __slots__ = ('peer', 'top_msg_id', 'action')
    def __init__(self, peer: 'InputPeer', action: 'SendMessageAction', top_msg_id: int = None):
        self.peer = peer
        self.top_msg_id = top_msg_id
        self.action = action
    def to_dict(self):
        return {"peer": self.peer, "top_msg_id": self.top_msg_id, "action": self.action}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1486110434, signed=False)
        flags = 0
        if self.top_msg_id is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        if flags & (1 << 0):
            writer.write_int(self.top_msg_id, signed=True)
        writer.write(bytes(self.action))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        peer = reader.tgread_object()
        if flags & (1 << 0):
            top_msg_id = reader.read_int()
        else:
            top_msg_id = None
        action = reader.tgread_object()
        return cls(peer, top_msg_id, action)

@register
class MessagesSendMessage(TLObject):
    CONSTRUCTOR_ID = 1415369050
    __slots__ = ('no_webpage', 'silent', 'background', 'clear_draft', 'noforwards', 'update_stickersets_order', 'invert_media', 'allow_paid_floodskip', 'peer', 'reply_to', 'message', 'random_id', 'reply_markup', 'entities', 'schedule_date', 'schedule_repeat_period', 'send_as', 'quick_reply_shortcut', 'effect', 'allow_paid_stars', 'suggested_post')
    def __init__(self, peer: 'InputPeer', message: str, random_id: int, no_webpage: bool = None, silent: bool = None, background: bool = None, clear_draft: bool = None, noforwards: bool = None, update_stickersets_order: bool = None, invert_media: bool = None, allow_paid_floodskip: bool = None, reply_to: 'InputReplyTo' = None, reply_markup: 'ReplyMarkup' = None, entities: 'Vector' = None, schedule_date: int = None, schedule_repeat_period: int = None, send_as: 'InputPeer' = None, quick_reply_shortcut: 'InputQuickReplyShortcut' = None, effect: int = None, allow_paid_stars: int = None, suggested_post: 'SuggestedPost' = None):
        self.no_webpage = no_webpage
        self.silent = silent
        self.background = background
        self.clear_draft = clear_draft
        self.noforwards = noforwards
        self.update_stickersets_order = update_stickersets_order
        self.invert_media = invert_media
        self.allow_paid_floodskip = allow_paid_floodskip
        self.peer = peer
        self.reply_to = reply_to
        self.message = message
        self.random_id = random_id
        self.reply_markup = reply_markup
        self.entities = entities
        self.schedule_date = schedule_date
        self.schedule_repeat_period = schedule_repeat_period
        self.send_as = send_as
        self.quick_reply_shortcut = quick_reply_shortcut
        self.effect = effect
        self.allow_paid_stars = allow_paid_stars
        self.suggested_post = suggested_post
    def to_dict(self):
        return {"no_webpage": self.no_webpage, "silent": self.silent, "background": self.background, "clear_draft": self.clear_draft, "noforwards": self.noforwards, "update_stickersets_order": self.update_stickersets_order, "invert_media": self.invert_media, "allow_paid_floodskip": self.allow_paid_floodskip, "peer": self.peer, "reply_to": self.reply_to, "message": self.message, "random_id": self.random_id, "reply_markup": self.reply_markup, "entities": self.entities, "schedule_date": self.schedule_date, "schedule_repeat_period": self.schedule_repeat_period, "send_as": self.send_as, "quick_reply_shortcut": self.quick_reply_shortcut, "effect": self.effect, "allow_paid_stars": self.allow_paid_stars, "suggested_post": self.suggested_post}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1415369050, signed=False)
        flags = 0
        if self.no_webpage: flags |= 1 << 1
        if self.silent: flags |= 1 << 5
        if self.background: flags |= 1 << 6
        if self.clear_draft: flags |= 1 << 7
        if self.noforwards: flags |= 1 << 14
        if self.update_stickersets_order: flags |= 1 << 15
        if self.invert_media: flags |= 1 << 16
        if self.allow_paid_floodskip: flags |= 1 << 19
        if self.reply_to is not None: flags |= 1 << 0
        if self.reply_markup is not None: flags |= 1 << 2
        if self.entities is not None: flags |= 1 << 3
        if self.schedule_date is not None: flags |= 1 << 10
        if self.schedule_repeat_period is not None: flags |= 1 << 24
        if self.send_as is not None: flags |= 1 << 13
        if self.quick_reply_shortcut is not None: flags |= 1 << 17
        if self.effect is not None: flags |= 1 << 18
        if self.allow_paid_stars is not None: flags |= 1 << 21
        if self.suggested_post is not None: flags |= 1 << 22
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        if flags & (1 << 0):
            writer.write(bytes(self.reply_to))
        writer.write_string(self.message)
        writer.write_long(self.random_id, signed=False)
        if flags & (1 << 2):
            writer.write(bytes(self.reply_markup))
        if flags & (1 << 3):
            writer.write(bytes(self.entities))
        if flags & (1 << 10):
            writer.write_int(self.schedule_date, signed=True)
        if flags & (1 << 24):
            writer.write_int(self.schedule_repeat_period, signed=True)
        if flags & (1 << 13):
            writer.write(bytes(self.send_as))
        if flags & (1 << 17):
            writer.write(bytes(self.quick_reply_shortcut))
        if flags & (1 << 18):
            writer.write_long(self.effect, signed=False)
        if flags & (1 << 21):
            writer.write_long(self.allow_paid_stars, signed=False)
        if flags & (1 << 22):
            writer.write(bytes(self.suggested_post))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        no_webpage = bool(flags & (1 << 1))
        silent = bool(flags & (1 << 5))
        background = bool(flags & (1 << 6))
        clear_draft = bool(flags & (1 << 7))
        noforwards = bool(flags & (1 << 14))
        update_stickersets_order = bool(flags & (1 << 15))
        invert_media = bool(flags & (1 << 16))
        allow_paid_floodskip = bool(flags & (1 << 19))
        peer = reader.tgread_object()
        if flags & (1 << 0):
            reply_to = reader.tgread_object()
        else:
            reply_to = None
        message = reader.read_string()
        random_id = reader.read_long()
        if flags & (1 << 2):
            reply_markup = reader.tgread_object()
        else:
            reply_markup = None
        if flags & (1 << 3):
            entities = reader.tgread_object()
        else:
            entities = None
        if flags & (1 << 10):
            schedule_date = reader.read_int()
        else:
            schedule_date = None
        if flags & (1 << 24):
            schedule_repeat_period = reader.read_int()
        else:
            schedule_repeat_period = None
        if flags & (1 << 13):
            send_as = reader.tgread_object()
        else:
            send_as = None
        if flags & (1 << 17):
            quick_reply_shortcut = reader.tgread_object()
        else:
            quick_reply_shortcut = None
        if flags & (1 << 18):
            effect = reader.read_long()
        else:
            effect = None
        if flags & (1 << 21):
            allow_paid_stars = reader.read_long()
        else:
            allow_paid_stars = None
        if flags & (1 << 22):
            suggested_post = reader.tgread_object()
        else:
            suggested_post = None
        return cls(no_webpage, silent, background, clear_draft, noforwards, update_stickersets_order, invert_media, allow_paid_floodskip, peer, reply_to, message, random_id, reply_markup, entities, schedule_date, schedule_repeat_period, send_as, quick_reply_shortcut, effect, allow_paid_stars, suggested_post)

@register
class MessagesSendMedia(TLObject):
    CONSTRUCTOR_ID = 53536639
    __slots__ = ('silent', 'background', 'clear_draft', 'noforwards', 'update_stickersets_order', 'invert_media', 'allow_paid_floodskip', 'peer', 'reply_to', 'media', 'message', 'random_id', 'reply_markup', 'entities', 'schedule_date', 'schedule_repeat_period', 'send_as', 'quick_reply_shortcut', 'effect', 'allow_paid_stars', 'suggested_post')
    def __init__(self, peer: 'InputPeer', media: 'InputMedia', message: str, random_id: int, silent: bool = None, background: bool = None, clear_draft: bool = None, noforwards: bool = None, update_stickersets_order: bool = None, invert_media: bool = None, allow_paid_floodskip: bool = None, reply_to: 'InputReplyTo' = None, reply_markup: 'ReplyMarkup' = None, entities: 'Vector' = None, schedule_date: int = None, schedule_repeat_period: int = None, send_as: 'InputPeer' = None, quick_reply_shortcut: 'InputQuickReplyShortcut' = None, effect: int = None, allow_paid_stars: int = None, suggested_post: 'SuggestedPost' = None):
        self.silent = silent
        self.background = background
        self.clear_draft = clear_draft
        self.noforwards = noforwards
        self.update_stickersets_order = update_stickersets_order
        self.invert_media = invert_media
        self.allow_paid_floodskip = allow_paid_floodskip
        self.peer = peer
        self.reply_to = reply_to
        self.media = media
        self.message = message
        self.random_id = random_id
        self.reply_markup = reply_markup
        self.entities = entities
        self.schedule_date = schedule_date
        self.schedule_repeat_period = schedule_repeat_period
        self.send_as = send_as
        self.quick_reply_shortcut = quick_reply_shortcut
        self.effect = effect
        self.allow_paid_stars = allow_paid_stars
        self.suggested_post = suggested_post
    def to_dict(self):
        return {"silent": self.silent, "background": self.background, "clear_draft": self.clear_draft, "noforwards": self.noforwards, "update_stickersets_order": self.update_stickersets_order, "invert_media": self.invert_media, "allow_paid_floodskip": self.allow_paid_floodskip, "peer": self.peer, "reply_to": self.reply_to, "media": self.media, "message": self.message, "random_id": self.random_id, "reply_markup": self.reply_markup, "entities": self.entities, "schedule_date": self.schedule_date, "schedule_repeat_period": self.schedule_repeat_period, "send_as": self.send_as, "quick_reply_shortcut": self.quick_reply_shortcut, "effect": self.effect, "allow_paid_stars": self.allow_paid_stars, "suggested_post": self.suggested_post}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(53536639, signed=False)
        flags = 0
        if self.silent: flags |= 1 << 5
        if self.background: flags |= 1 << 6
        if self.clear_draft: flags |= 1 << 7
        if self.noforwards: flags |= 1 << 14
        if self.update_stickersets_order: flags |= 1 << 15
        if self.invert_media: flags |= 1 << 16
        if self.allow_paid_floodskip: flags |= 1 << 19
        if self.reply_to is not None: flags |= 1 << 0
        if self.reply_markup is not None: flags |= 1 << 2
        if self.entities is not None: flags |= 1 << 3
        if self.schedule_date is not None: flags |= 1 << 10
        if self.schedule_repeat_period is not None: flags |= 1 << 24
        if self.send_as is not None: flags |= 1 << 13
        if self.quick_reply_shortcut is not None: flags |= 1 << 17
        if self.effect is not None: flags |= 1 << 18
        if self.allow_paid_stars is not None: flags |= 1 << 21
        if self.suggested_post is not None: flags |= 1 << 22
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        if flags & (1 << 0):
            writer.write(bytes(self.reply_to))
        writer.write(bytes(self.media))
        writer.write_string(self.message)
        writer.write_long(self.random_id, signed=False)
        if flags & (1 << 2):
            writer.write(bytes(self.reply_markup))
        if flags & (1 << 3):
            writer.write(bytes(self.entities))
        if flags & (1 << 10):
            writer.write_int(self.schedule_date, signed=True)
        if flags & (1 << 24):
            writer.write_int(self.schedule_repeat_period, signed=True)
        if flags & (1 << 13):
            writer.write(bytes(self.send_as))
        if flags & (1 << 17):
            writer.write(bytes(self.quick_reply_shortcut))
        if flags & (1 << 18):
            writer.write_long(self.effect, signed=False)
        if flags & (1 << 21):
            writer.write_long(self.allow_paid_stars, signed=False)
        if flags & (1 << 22):
            writer.write(bytes(self.suggested_post))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        silent = bool(flags & (1 << 5))
        background = bool(flags & (1 << 6))
        clear_draft = bool(flags & (1 << 7))
        noforwards = bool(flags & (1 << 14))
        update_stickersets_order = bool(flags & (1 << 15))
        invert_media = bool(flags & (1 << 16))
        allow_paid_floodskip = bool(flags & (1 << 19))
        peer = reader.tgread_object()
        if flags & (1 << 0):
            reply_to = reader.tgread_object()
        else:
            reply_to = None
        media = reader.tgread_object()
        message = reader.read_string()
        random_id = reader.read_long()
        if flags & (1 << 2):
            reply_markup = reader.tgread_object()
        else:
            reply_markup = None
        if flags & (1 << 3):
            entities = reader.tgread_object()
        else:
            entities = None
        if flags & (1 << 10):
            schedule_date = reader.read_int()
        else:
            schedule_date = None
        if flags & (1 << 24):
            schedule_repeat_period = reader.read_int()
        else:
            schedule_repeat_period = None
        if flags & (1 << 13):
            send_as = reader.tgread_object()
        else:
            send_as = None
        if flags & (1 << 17):
            quick_reply_shortcut = reader.tgread_object()
        else:
            quick_reply_shortcut = None
        if flags & (1 << 18):
            effect = reader.read_long()
        else:
            effect = None
        if flags & (1 << 21):
            allow_paid_stars = reader.read_long()
        else:
            allow_paid_stars = None
        if flags & (1 << 22):
            suggested_post = reader.tgread_object()
        else:
            suggested_post = None
        return cls(silent, background, clear_draft, noforwards, update_stickersets_order, invert_media, allow_paid_floodskip, peer, reply_to, media, message, random_id, reply_markup, entities, schedule_date, schedule_repeat_period, send_as, quick_reply_shortcut, effect, allow_paid_stars, suggested_post)

@register
class MessagesForwardMessages(TLObject):
    CONSTRUCTOR_ID = 326126204
    __slots__ = ('silent', 'background', 'with_my_score', 'drop_author', 'drop_media_captions', 'noforwards', 'allow_paid_floodskip', 'from_peer', 'id', 'random_id', 'to_peer', 'top_msg_id', 'reply_to', 'schedule_date', 'schedule_repeat_period', 'send_as', 'quick_reply_shortcut', 'effect', 'video_timestamp', 'allow_paid_stars', 'suggested_post')
    def __init__(self, from_peer: 'InputPeer', id: 'Vector', random_id: 'Vector', to_peer: 'InputPeer', silent: bool = None, background: bool = None, with_my_score: bool = None, drop_author: bool = None, drop_media_captions: bool = None, noforwards: bool = None, allow_paid_floodskip: bool = None, top_msg_id: int = None, reply_to: 'InputReplyTo' = None, schedule_date: int = None, schedule_repeat_period: int = None, send_as: 'InputPeer' = None, quick_reply_shortcut: 'InputQuickReplyShortcut' = None, effect: int = None, video_timestamp: int = None, allow_paid_stars: int = None, suggested_post: 'SuggestedPost' = None):
        self.silent = silent
        self.background = background
        self.with_my_score = with_my_score
        self.drop_author = drop_author
        self.drop_media_captions = drop_media_captions
        self.noforwards = noforwards
        self.allow_paid_floodskip = allow_paid_floodskip
        self.from_peer = from_peer
        self.id = id
        self.random_id = random_id
        self.to_peer = to_peer
        self.top_msg_id = top_msg_id
        self.reply_to = reply_to
        self.schedule_date = schedule_date
        self.schedule_repeat_period = schedule_repeat_period
        self.send_as = send_as
        self.quick_reply_shortcut = quick_reply_shortcut
        self.effect = effect
        self.video_timestamp = video_timestamp
        self.allow_paid_stars = allow_paid_stars
        self.suggested_post = suggested_post
    def to_dict(self):
        return {"silent": self.silent, "background": self.background, "with_my_score": self.with_my_score, "drop_author": self.drop_author, "drop_media_captions": self.drop_media_captions, "noforwards": self.noforwards, "allow_paid_floodskip": self.allow_paid_floodskip, "from_peer": self.from_peer, "id": self.id, "random_id": self.random_id, "to_peer": self.to_peer, "top_msg_id": self.top_msg_id, "reply_to": self.reply_to, "schedule_date": self.schedule_date, "schedule_repeat_period": self.schedule_repeat_period, "send_as": self.send_as, "quick_reply_shortcut": self.quick_reply_shortcut, "effect": self.effect, "video_timestamp": self.video_timestamp, "allow_paid_stars": self.allow_paid_stars, "suggested_post": self.suggested_post}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(326126204, signed=False)
        flags = 0
        if self.silent: flags |= 1 << 5
        if self.background: flags |= 1 << 6
        if self.with_my_score: flags |= 1 << 8
        if self.drop_author: flags |= 1 << 11
        if self.drop_media_captions: flags |= 1 << 12
        if self.noforwards: flags |= 1 << 14
        if self.allow_paid_floodskip: flags |= 1 << 19
        if self.top_msg_id is not None: flags |= 1 << 9
        if self.reply_to is not None: flags |= 1 << 22
        if self.schedule_date is not None: flags |= 1 << 10
        if self.schedule_repeat_period is not None: flags |= 1 << 24
        if self.send_as is not None: flags |= 1 << 13
        if self.quick_reply_shortcut is not None: flags |= 1 << 17
        if self.effect is not None: flags |= 1 << 18
        if self.video_timestamp is not None: flags |= 1 << 20
        if self.allow_paid_stars is not None: flags |= 1 << 21
        if self.suggested_post is not None: flags |= 1 << 23
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.from_peer))
        writer.write(bytes(self.id))
        writer.write(bytes(self.random_id))
        writer.write(bytes(self.to_peer))
        if flags & (1 << 9):
            writer.write_int(self.top_msg_id, signed=True)
        if flags & (1 << 22):
            writer.write(bytes(self.reply_to))
        if flags & (1 << 10):
            writer.write_int(self.schedule_date, signed=True)
        if flags & (1 << 24):
            writer.write_int(self.schedule_repeat_period, signed=True)
        if flags & (1 << 13):
            writer.write(bytes(self.send_as))
        if flags & (1 << 17):
            writer.write(bytes(self.quick_reply_shortcut))
        if flags & (1 << 18):
            writer.write_long(self.effect, signed=False)
        if flags & (1 << 20):
            writer.write_int(self.video_timestamp, signed=True)
        if flags & (1 << 21):
            writer.write_long(self.allow_paid_stars, signed=False)
        if flags & (1 << 23):
            writer.write(bytes(self.suggested_post))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        silent = bool(flags & (1 << 5))
        background = bool(flags & (1 << 6))
        with_my_score = bool(flags & (1 << 8))
        drop_author = bool(flags & (1 << 11))
        drop_media_captions = bool(flags & (1 << 12))
        noforwards = bool(flags & (1 << 14))
        allow_paid_floodskip = bool(flags & (1 << 19))
        from_peer = reader.tgread_object()
        id = reader.tgread_object()
        random_id = reader.tgread_object()
        to_peer = reader.tgread_object()
        if flags & (1 << 9):
            top_msg_id = reader.read_int()
        else:
            top_msg_id = None
        if flags & (1 << 22):
            reply_to = reader.tgread_object()
        else:
            reply_to = None
        if flags & (1 << 10):
            schedule_date = reader.read_int()
        else:
            schedule_date = None
        if flags & (1 << 24):
            schedule_repeat_period = reader.read_int()
        else:
            schedule_repeat_period = None
        if flags & (1 << 13):
            send_as = reader.tgread_object()
        else:
            send_as = None
        if flags & (1 << 17):
            quick_reply_shortcut = reader.tgread_object()
        else:
            quick_reply_shortcut = None
        if flags & (1 << 18):
            effect = reader.read_long()
        else:
            effect = None
        if flags & (1 << 20):
            video_timestamp = reader.read_int()
        else:
            video_timestamp = None
        if flags & (1 << 21):
            allow_paid_stars = reader.read_long()
        else:
            allow_paid_stars = None
        if flags & (1 << 23):
            suggested_post = reader.tgread_object()
        else:
            suggested_post = None
        return cls(silent, background, with_my_score, drop_author, drop_media_captions, noforwards, allow_paid_floodskip, from_peer, id, random_id, to_peer, top_msg_id, reply_to, schedule_date, schedule_repeat_period, send_as, quick_reply_shortcut, effect, video_timestamp, allow_paid_stars, suggested_post)

@register
class MessagesReportSpam(TLObject):
    CONSTRUCTOR_ID = 3474297563
    __slots__ = ('peer')
    def __init__(self, peer: 'InputPeer'):
        self.peer = peer
    def to_dict(self):
        return {"peer": self.peer}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3474297563, signed=False)
        writer.write(bytes(self.peer))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        return cls(peer)

@register
class MessagesGetPeerSettings(TLObject):
    CONSTRUCTOR_ID = 4024018594
    __slots__ = ('peer')
    def __init__(self, peer: 'InputPeer'):
        self.peer = peer
    def to_dict(self):
        return {"peer": self.peer}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4024018594, signed=False)
        writer.write(bytes(self.peer))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        return cls(peer)

@register
class MessagesReport(TLObject):
    CONSTRUCTOR_ID = 4235767707
    __slots__ = ('peer', 'id', 'option', 'message')
    def __init__(self, peer: 'InputPeer', id: 'Vector', option: bytes, message: str):
        self.peer = peer
        self.id = id
        self.option = option
        self.message = message
    def to_dict(self):
        return {"peer": self.peer, "id": self.id, "option": self.option, "message": self.message}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4235767707, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.id))
        writer.write_bytes(self.option)
        writer.write_string(self.message)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        id = reader.tgread_object()
        option = reader.read_bytes()
        message = reader.read_string()
        return cls(peer, id, option, message)

@register
class MessagesGetChats(TLObject):
    CONSTRUCTOR_ID = 1240027791
    __slots__ = ('id')
    def __init__(self, id: 'Vector'):
        self.id = id
    def to_dict(self):
        return {"id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1240027791, signed=False)
        writer.write(bytes(self.id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        id = reader.tgread_object()
        return cls(id)

@register
class MessagesGetFullChat(TLObject):
    CONSTRUCTOR_ID = 2930772788
    __slots__ = ('chat_id')
    def __init__(self, chat_id: int):
        self.chat_id = chat_id
    def to_dict(self):
        return {"chat_id": self.chat_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2930772788, signed=False)
        writer.write_long(self.chat_id, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        chat_id = reader.read_long()
        return cls(chat_id)

@register
class MessagesEditChatTitle(TLObject):
    CONSTRUCTOR_ID = 1937260541
    __slots__ = ('chat_id', 'title')
    def __init__(self, chat_id: int, title: str):
        self.chat_id = chat_id
        self.title = title
    def to_dict(self):
        return {"chat_id": self.chat_id, "title": self.title}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1937260541, signed=False)
        writer.write_long(self.chat_id, signed=False)
        writer.write_string(self.title)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        chat_id = reader.read_long()
        title = reader.read_string()
        return cls(chat_id, title)

@register
class MessagesEditChatPhoto(TLObject):
    CONSTRUCTOR_ID = 903730804
    __slots__ = ('chat_id', 'photo')
    def __init__(self, chat_id: int, photo: 'InputChatPhoto'):
        self.chat_id = chat_id
        self.photo = photo
    def to_dict(self):
        return {"chat_id": self.chat_id, "photo": self.photo}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(903730804, signed=False)
        writer.write_long(self.chat_id, signed=False)
        writer.write(bytes(self.photo))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        chat_id = reader.read_long()
        photo = reader.tgread_object()
        return cls(chat_id, photo)

@register
class MessagesAddChatUser(TLObject):
    CONSTRUCTOR_ID = 3418804487
    __slots__ = ('chat_id', 'user_id', 'fwd_limit')
    def __init__(self, chat_id: int, user_id: 'InputUser', fwd_limit: int):
        self.chat_id = chat_id
        self.user_id = user_id
        self.fwd_limit = fwd_limit
    def to_dict(self):
        return {"chat_id": self.chat_id, "user_id": self.user_id, "fwd_limit": self.fwd_limit}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3418804487, signed=False)
        writer.write_long(self.chat_id, signed=False)
        writer.write(bytes(self.user_id))
        writer.write_int(self.fwd_limit, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        chat_id = reader.read_long()
        user_id = reader.tgread_object()
        fwd_limit = reader.read_int()
        return cls(chat_id, user_id, fwd_limit)

@register
class MessagesDeleteChatUser(TLObject):
    CONSTRUCTOR_ID = 2719505579
    __slots__ = ('revoke_history', 'chat_id', 'user_id')
    def __init__(self, chat_id: int, user_id: 'InputUser', revoke_history: bool = None):
        self.revoke_history = revoke_history
        self.chat_id = chat_id
        self.user_id = user_id
    def to_dict(self):
        return {"revoke_history": self.revoke_history, "chat_id": self.chat_id, "user_id": self.user_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2719505579, signed=False)
        flags = 0
        if self.revoke_history: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write_long(self.chat_id, signed=False)
        writer.write(bytes(self.user_id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        revoke_history = bool(flags & (1 << 0))
        chat_id = reader.read_long()
        user_id = reader.tgread_object()
        return cls(revoke_history, chat_id, user_id)

@register
class MessagesCreateChat(TLObject):
    CONSTRUCTOR_ID = 2463030740
    __slots__ = ('users', 'title', 'ttl_period')
    def __init__(self, users: 'Vector', title: str, ttl_period: int = None):
        self.users = users
        self.title = title
        self.ttl_period = ttl_period
    def to_dict(self):
        return {"users": self.users, "title": self.title, "ttl_period": self.ttl_period}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2463030740, signed=False)
        flags = 0
        if self.ttl_period is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.users))
        writer.write_string(self.title)
        if flags & (1 << 0):
            writer.write_int(self.ttl_period, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        users = reader.tgread_object()
        title = reader.read_string()
        if flags & (1 << 0):
            ttl_period = reader.read_int()
        else:
            ttl_period = None
        return cls(users, title, ttl_period)

@register
class MessagesGetDhConfig(TLObject):
    CONSTRUCTOR_ID = 651135312
    __slots__ = ('version', 'random_length')
    def __init__(self, version: int, random_length: int):
        self.version = version
        self.random_length = random_length
    def to_dict(self):
        return {"version": self.version, "random_length": self.random_length}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(651135312, signed=False)
        writer.write_int(self.version, signed=True)
        writer.write_int(self.random_length, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        version = reader.read_int()
        random_length = reader.read_int()
        return cls(version, random_length)

@register
class MessagesRequestEncryption(TLObject):
    CONSTRUCTOR_ID = 4132286275
    __slots__ = ('user_id', 'random_id', 'g_a')
    def __init__(self, user_id: 'InputUser', random_id: int, g_a: bytes):
        self.user_id = user_id
        self.random_id = random_id
        self.g_a = g_a
    def to_dict(self):
        return {"user_id": self.user_id, "random_id": self.random_id, "g_a": self.g_a}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4132286275, signed=False)
        writer.write(bytes(self.user_id))
        writer.write_int(self.random_id, signed=True)
        writer.write_bytes(self.g_a)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        user_id = reader.tgread_object()
        random_id = reader.read_int()
        g_a = reader.read_bytes()
        return cls(user_id, random_id, g_a)

@register
class MessagesAcceptEncryption(TLObject):
    CONSTRUCTOR_ID = 1035731989
    __slots__ = ('peer', 'g_b', 'key_fingerprint')
    def __init__(self, peer: 'InputEncryptedChat', g_b: bytes, key_fingerprint: int):
        self.peer = peer
        self.g_b = g_b
        self.key_fingerprint = key_fingerprint
    def to_dict(self):
        return {"peer": self.peer, "g_b": self.g_b, "key_fingerprint": self.key_fingerprint}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1035731989, signed=False)
        writer.write(bytes(self.peer))
        writer.write_bytes(self.g_b)
        writer.write_long(self.key_fingerprint, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        g_b = reader.read_bytes()
        key_fingerprint = reader.read_long()
        return cls(peer, g_b, key_fingerprint)

@register
class MessagesDiscardEncryption(TLObject):
    CONSTRUCTOR_ID = 4086541984
    __slots__ = ('delete_history', 'chat_id')
    def __init__(self, chat_id: int, delete_history: bool = None):
        self.delete_history = delete_history
        self.chat_id = chat_id
    def to_dict(self):
        return {"delete_history": self.delete_history, "chat_id": self.chat_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4086541984, signed=False)
        flags = 0
        if self.delete_history: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write_int(self.chat_id, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        delete_history = bool(flags & (1 << 0))
        chat_id = reader.read_int()
        return cls(delete_history, chat_id)

@register
class MessagesSetEncryptedTyping(TLObject):
    CONSTRUCTOR_ID = 2031374829
    __slots__ = ('peer', 'typing')
    def __init__(self, peer: 'InputEncryptedChat', typing: bool):
        self.peer = peer
        self.typing = typing
    def to_dict(self):
        return {"peer": self.peer, "typing": self.typing}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2031374829, signed=False)
        writer.write(bytes(self.peer))
        writer.write(serialize_bool(self.typing))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        typing = reader.tgread_bool()
        return cls(peer, typing)

@register
class MessagesReadEncryptedHistory(TLObject):
    CONSTRUCTOR_ID = 2135648522
    __slots__ = ('peer', 'max_date')
    def __init__(self, peer: 'InputEncryptedChat', max_date: int):
        self.peer = peer
        self.max_date = max_date
    def to_dict(self):
        return {"peer": self.peer, "max_date": self.max_date}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2135648522, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.max_date, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        max_date = reader.read_int()
        return cls(peer, max_date)

@register
class MessagesSendEncrypted(TLObject):
    CONSTRUCTOR_ID = 1157265941
    __slots__ = ('silent', 'peer', 'random_id', 'data')
    def __init__(self, peer: 'InputEncryptedChat', random_id: int, data: bytes, silent: bool = None):
        self.silent = silent
        self.peer = peer
        self.random_id = random_id
        self.data = data
    def to_dict(self):
        return {"silent": self.silent, "peer": self.peer, "random_id": self.random_id, "data": self.data}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1157265941, signed=False)
        flags = 0
        if self.silent: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write_long(self.random_id, signed=False)
        writer.write_bytes(self.data)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        silent = bool(flags & (1 << 0))
        peer = reader.tgread_object()
        random_id = reader.read_long()
        data = reader.read_bytes()
        return cls(silent, peer, random_id, data)

@register
class MessagesSendEncryptedFile(TLObject):
    CONSTRUCTOR_ID = 1431914525
    __slots__ = ('silent', 'peer', 'random_id', 'data', 'file')
    def __init__(self, peer: 'InputEncryptedChat', random_id: int, data: bytes, file: 'InputEncryptedFile', silent: bool = None):
        self.silent = silent
        self.peer = peer
        self.random_id = random_id
        self.data = data
        self.file = file
    def to_dict(self):
        return {"silent": self.silent, "peer": self.peer, "random_id": self.random_id, "data": self.data, "file": self.file}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1431914525, signed=False)
        flags = 0
        if self.silent: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write_long(self.random_id, signed=False)
        writer.write_bytes(self.data)
        writer.write(bytes(self.file))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        silent = bool(flags & (1 << 0))
        peer = reader.tgread_object()
        random_id = reader.read_long()
        data = reader.read_bytes()
        file = reader.tgread_object()
        return cls(silent, peer, random_id, data, file)

@register
class MessagesSendEncryptedService(TLObject):
    CONSTRUCTOR_ID = 852769188
    __slots__ = ('peer', 'random_id', 'data')
    def __init__(self, peer: 'InputEncryptedChat', random_id: int, data: bytes):
        self.peer = peer
        self.random_id = random_id
        self.data = data
    def to_dict(self):
        return {"peer": self.peer, "random_id": self.random_id, "data": self.data}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(852769188, signed=False)
        writer.write(bytes(self.peer))
        writer.write_long(self.random_id, signed=False)
        writer.write_bytes(self.data)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        random_id = reader.read_long()
        data = reader.read_bytes()
        return cls(peer, random_id, data)

@register
class MessagesReceivedQueue(TLObject):
    CONSTRUCTOR_ID = 1436924774
    __slots__ = ('max_qts')
    def __init__(self, max_qts: int):
        self.max_qts = max_qts
    def to_dict(self):
        return {"max_qts": self.max_qts}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1436924774, signed=False)
        writer.write_int(self.max_qts, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        max_qts = reader.read_int()
        return cls(max_qts)

@register
class MessagesReportEncryptedSpam(TLObject):
    CONSTRUCTOR_ID = 1259113487
    __slots__ = ('peer')
    def __init__(self, peer: 'InputEncryptedChat'):
        self.peer = peer
    def to_dict(self):
        return {"peer": self.peer}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1259113487, signed=False)
        writer.write(bytes(self.peer))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        return cls(peer)

@register
class MessagesReadMessageContents(TLObject):
    CONSTRUCTOR_ID = 916930423
    __slots__ = ('id')
    def __init__(self, id: 'Vector'):
        self.id = id
    def to_dict(self):
        return {"id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(916930423, signed=False)
        writer.write(bytes(self.id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        id = reader.tgread_object()
        return cls(id)

@register
class MessagesGetStickers(TLObject):
    CONSTRUCTOR_ID = 3584414625
    __slots__ = ('emoticon', 'hash')
    def __init__(self, emoticon: str, hash: int):
        self.emoticon = emoticon
        self.hash = hash
    def to_dict(self):
        return {"emoticon": self.emoticon, "hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3584414625, signed=False)
        writer.write_string(self.emoticon)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        emoticon = reader.read_string()
        hash = reader.read_long()
        return cls(emoticon, hash)

@register
class MessagesGetAllStickers(TLObject):
    CONSTRUCTOR_ID = 3097534888
    __slots__ = ('hash')
    def __init__(self, hash: int):
        self.hash = hash
    def to_dict(self):
        return {"hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3097534888, signed=False)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_long()
        return cls(hash)

@register
class MessagesGetWebPagePreview(TLObject):
    CONSTRUCTOR_ID = 1460498287
    __slots__ = ('message', 'entities')
    def __init__(self, message: str, entities: 'Vector' = None):
        self.message = message
        self.entities = entities
    def to_dict(self):
        return {"message": self.message, "entities": self.entities}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1460498287, signed=False)
        flags = 0
        if self.entities is not None: flags |= 1 << 3
        writer.write_int(flags, signed=False)
        writer.write_string(self.message)
        if flags & (1 << 3):
            writer.write(bytes(self.entities))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        message = reader.read_string()
        if flags & (1 << 3):
            entities = reader.tgread_object()
        else:
            entities = None
        return cls(message, entities)

@register
class MessagesExportChatInvite(TLObject):
    CONSTRUCTOR_ID = 2757090960
    __slots__ = ('legacy_revoke_permanent', 'request_needed', 'peer', 'expire_date', 'usage_limit', 'title', 'subscription_pricing')
    def __init__(self, peer: 'InputPeer', legacy_revoke_permanent: bool = None, request_needed: bool = None, expire_date: int = None, usage_limit: int = None, title: str = None, subscription_pricing: 'StarsSubscriptionPricing' = None):
        self.legacy_revoke_permanent = legacy_revoke_permanent
        self.request_needed = request_needed
        self.peer = peer
        self.expire_date = expire_date
        self.usage_limit = usage_limit
        self.title = title
        self.subscription_pricing = subscription_pricing
    def to_dict(self):
        return {"legacy_revoke_permanent": self.legacy_revoke_permanent, "request_needed": self.request_needed, "peer": self.peer, "expire_date": self.expire_date, "usage_limit": self.usage_limit, "title": self.title, "subscription_pricing": self.subscription_pricing}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2757090960, signed=False)
        flags = 0
        if self.legacy_revoke_permanent: flags |= 1 << 2
        if self.request_needed: flags |= 1 << 3
        if self.expire_date is not None: flags |= 1 << 0
        if self.usage_limit is not None: flags |= 1 << 1
        if self.title is not None: flags |= 1 << 4
        if self.subscription_pricing is not None: flags |= 1 << 5
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        if flags & (1 << 0):
            writer.write_int(self.expire_date, signed=True)
        if flags & (1 << 1):
            writer.write_int(self.usage_limit, signed=True)
        if flags & (1 << 4):
            writer.write_string(self.title)
        if flags & (1 << 5):
            writer.write(bytes(self.subscription_pricing))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        legacy_revoke_permanent = bool(flags & (1 << 2))
        request_needed = bool(flags & (1 << 3))
        peer = reader.tgread_object()
        if flags & (1 << 0):
            expire_date = reader.read_int()
        else:
            expire_date = None
        if flags & (1 << 1):
            usage_limit = reader.read_int()
        else:
            usage_limit = None
        if flags & (1 << 4):
            title = reader.read_string()
        else:
            title = None
        if flags & (1 << 5):
            subscription_pricing = reader.tgread_object()
        else:
            subscription_pricing = None
        return cls(legacy_revoke_permanent, request_needed, peer, expire_date, usage_limit, title, subscription_pricing)

@register
class MessagesCheckChatInvite(TLObject):
    CONSTRUCTOR_ID = 1051570619
    __slots__ = ('hash')
    def __init__(self, hash: str):
        self.hash = hash
    def to_dict(self):
        return {"hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1051570619, signed=False)
        writer.write_string(self.hash)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_string()
        return cls(hash)

@register
class MessagesImportChatInvite(TLObject):
    CONSTRUCTOR_ID = 1817183516
    __slots__ = ('hash')
    def __init__(self, hash: str):
        self.hash = hash
    def to_dict(self):
        return {"hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1817183516, signed=False)
        writer.write_string(self.hash)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_string()
        return cls(hash)

@register
class MessagesGetStickerSet(TLObject):
    CONSTRUCTOR_ID = 3365989492
    __slots__ = ('stickerset', 'hash')
    def __init__(self, stickerset: 'InputStickerSet', hash: int):
        self.stickerset = stickerset
        self.hash = hash
    def to_dict(self):
        return {"stickerset": self.stickerset, "hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3365989492, signed=False)
        writer.write(bytes(self.stickerset))
        writer.write_int(self.hash, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        stickerset = reader.tgread_object()
        hash = reader.read_int()
        return cls(stickerset, hash)

@register
class MessagesInstallStickerSet(TLObject):
    CONSTRUCTOR_ID = 3348096096
    __slots__ = ('stickerset', 'archived')
    def __init__(self, stickerset: 'InputStickerSet', archived: bool):
        self.stickerset = stickerset
        self.archived = archived
    def to_dict(self):
        return {"stickerset": self.stickerset, "archived": self.archived}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3348096096, signed=False)
        writer.write(bytes(self.stickerset))
        writer.write(serialize_bool(self.archived))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        stickerset = reader.tgread_object()
        archived = reader.tgread_bool()
        return cls(stickerset, archived)

@register
class MessagesUninstallStickerSet(TLObject):
    CONSTRUCTOR_ID = 4184757726
    __slots__ = ('stickerset')
    def __init__(self, stickerset: 'InputStickerSet'):
        self.stickerset = stickerset
    def to_dict(self):
        return {"stickerset": self.stickerset}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4184757726, signed=False)
        writer.write(bytes(self.stickerset))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        stickerset = reader.tgread_object()
        return cls(stickerset)

@register
class MessagesStartBot(TLObject):
    CONSTRUCTOR_ID = 3873403768
    __slots__ = ('bot', 'peer', 'random_id', 'start_param')
    def __init__(self, bot: 'InputUser', peer: 'InputPeer', random_id: int, start_param: str):
        self.bot = bot
        self.peer = peer
        self.random_id = random_id
        self.start_param = start_param
    def to_dict(self):
        return {"bot": self.bot, "peer": self.peer, "random_id": self.random_id, "start_param": self.start_param}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3873403768, signed=False)
        writer.write(bytes(self.bot))
        writer.write(bytes(self.peer))
        writer.write_long(self.random_id, signed=False)
        writer.write_string(self.start_param)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        bot = reader.tgread_object()
        peer = reader.tgread_object()
        random_id = reader.read_long()
        start_param = reader.read_string()
        return cls(bot, peer, random_id, start_param)

@register
class MessagesGetMessagesViews(TLObject):
    CONSTRUCTOR_ID = 1468322785
    __slots__ = ('peer', 'id', 'increment')
    def __init__(self, peer: 'InputPeer', id: 'Vector', increment: bool):
        self.peer = peer
        self.id = id
        self.increment = increment
    def to_dict(self):
        return {"peer": self.peer, "id": self.id, "increment": self.increment}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1468322785, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.id))
        writer.write(serialize_bool(self.increment))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        id = reader.tgread_object()
        increment = reader.tgread_bool()
        return cls(peer, id, increment)

@register
class MessagesEditChatAdmin(TLObject):
    CONSTRUCTOR_ID = 2824589762
    __slots__ = ('chat_id', 'user_id', 'is_admin')
    def __init__(self, chat_id: int, user_id: 'InputUser', is_admin: bool):
        self.chat_id = chat_id
        self.user_id = user_id
        self.is_admin = is_admin
    def to_dict(self):
        return {"chat_id": self.chat_id, "user_id": self.user_id, "is_admin": self.is_admin}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2824589762, signed=False)
        writer.write_long(self.chat_id, signed=False)
        writer.write(bytes(self.user_id))
        writer.write(serialize_bool(self.is_admin))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        chat_id = reader.read_long()
        user_id = reader.tgread_object()
        is_admin = reader.tgread_bool()
        return cls(chat_id, user_id, is_admin)

@register
class MessagesMigrateChat(TLObject):
    CONSTRUCTOR_ID = 2726777625
    __slots__ = ('chat_id')
    def __init__(self, chat_id: int):
        self.chat_id = chat_id
    def to_dict(self):
        return {"chat_id": self.chat_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2726777625, signed=False)
        writer.write_long(self.chat_id, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        chat_id = reader.read_long()
        return cls(chat_id)

@register
class MessagesSearchGlobal(TLObject):
    CONSTRUCTOR_ID = 1271290010
    __slots__ = ('broadcasts_only', 'groups_only', 'users_only', 'folder_id', 'q', 'filter', 'min_date', 'max_date', 'offset_rate', 'offset_peer', 'offset_id', 'limit')
    def __init__(self, q: str, filter: 'MessagesFilter', min_date: int, max_date: int, offset_rate: int, offset_peer: 'InputPeer', offset_id: int, limit: int, broadcasts_only: bool = None, groups_only: bool = None, users_only: bool = None, folder_id: int = None):
        self.broadcasts_only = broadcasts_only
        self.groups_only = groups_only
        self.users_only = users_only
        self.folder_id = folder_id
        self.q = q
        self.filter = filter
        self.min_date = min_date
        self.max_date = max_date
        self.offset_rate = offset_rate
        self.offset_peer = offset_peer
        self.offset_id = offset_id
        self.limit = limit
    def to_dict(self):
        return {"broadcasts_only": self.broadcasts_only, "groups_only": self.groups_only, "users_only": self.users_only, "folder_id": self.folder_id, "q": self.q, "filter": self.filter, "min_date": self.min_date, "max_date": self.max_date, "offset_rate": self.offset_rate, "offset_peer": self.offset_peer, "offset_id": self.offset_id, "limit": self.limit}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1271290010, signed=False)
        flags = 0
        if self.broadcasts_only: flags |= 1 << 1
        if self.groups_only: flags |= 1 << 2
        if self.users_only: flags |= 1 << 3
        if self.folder_id is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        if flags & (1 << 0):
            writer.write_int(self.folder_id, signed=True)
        writer.write_string(self.q)
        writer.write(bytes(self.filter))
        writer.write_int(self.min_date, signed=True)
        writer.write_int(self.max_date, signed=True)
        writer.write_int(self.offset_rate, signed=True)
        writer.write(bytes(self.offset_peer))
        writer.write_int(self.offset_id, signed=True)
        writer.write_int(self.limit, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        broadcasts_only = bool(flags & (1 << 1))
        groups_only = bool(flags & (1 << 2))
        users_only = bool(flags & (1 << 3))
        if flags & (1 << 0):
            folder_id = reader.read_int()
        else:
            folder_id = None
        q = reader.read_string()
        filter = reader.tgread_object()
        min_date = reader.read_int()
        max_date = reader.read_int()
        offset_rate = reader.read_int()
        offset_peer = reader.tgread_object()
        offset_id = reader.read_int()
        limit = reader.read_int()
        return cls(broadcasts_only, groups_only, users_only, folder_id, q, filter, min_date, max_date, offset_rate, offset_peer, offset_id, limit)

@register
class MessagesReorderStickerSets(TLObject):
    CONSTRUCTOR_ID = 2016638777
    __slots__ = ('masks', 'emojis', 'order')
    def __init__(self, order: 'Vector', masks: bool = None, emojis: bool = None):
        self.masks = masks
        self.emojis = emojis
        self.order = order
    def to_dict(self):
        return {"masks": self.masks, "emojis": self.emojis, "order": self.order}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2016638777, signed=False)
        flags = 0
        if self.masks: flags |= 1 << 0
        if self.emojis: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.order))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        masks = bool(flags & (1 << 0))
        emojis = bool(flags & (1 << 1))
        order = reader.tgread_object()
        return cls(masks, emojis, order)

@register
class MessagesGetDocumentByHash(TLObject):
    CONSTRUCTOR_ID = 2985428511
    __slots__ = ('sha256', 'size', 'mime_type')
    def __init__(self, sha256: bytes, size: int, mime_type: str):
        self.sha256 = sha256
        self.size = size
        self.mime_type = mime_type
    def to_dict(self):
        return {"sha256": self.sha256, "size": self.size, "mime_type": self.mime_type}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2985428511, signed=False)
        writer.write_bytes(self.sha256)
        writer.write_long(self.size, signed=False)
        writer.write_string(self.mime_type)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        sha256 = reader.read_bytes()
        size = reader.read_long()
        mime_type = reader.read_string()
        return cls(sha256, size, mime_type)

@register
class MessagesGetSavedGifs(TLObject):
    CONSTRUCTOR_ID = 1559270965
    __slots__ = ('hash')
    def __init__(self, hash: int):
        self.hash = hash
    def to_dict(self):
        return {"hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1559270965, signed=False)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_long()
        return cls(hash)

@register
class MessagesSaveGif(TLObject):
    CONSTRUCTOR_ID = 846868683
    __slots__ = ('id', 'unsave')
    def __init__(self, id: 'InputDocument', unsave: bool):
        self.id = id
        self.unsave = unsave
    def to_dict(self):
        return {"id": self.id, "unsave": self.unsave}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(846868683, signed=False)
        writer.write(bytes(self.id))
        writer.write(serialize_bool(self.unsave))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        id = reader.tgread_object()
        unsave = reader.tgread_bool()
        return cls(id, unsave)

@register
class MessagesGetInlineBotResults(TLObject):
    CONSTRUCTOR_ID = 1364105629
    __slots__ = ('bot', 'peer', 'geo_point', 'query', 'offset')
    def __init__(self, bot: 'InputUser', peer: 'InputPeer', query: str, offset: str, geo_point: 'InputGeoPoint' = None):
        self.bot = bot
        self.peer = peer
        self.geo_point = geo_point
        self.query = query
        self.offset = offset
    def to_dict(self):
        return {"bot": self.bot, "peer": self.peer, "geo_point": self.geo_point, "query": self.query, "offset": self.offset}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1364105629, signed=False)
        flags = 0
        if self.geo_point is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.bot))
        writer.write(bytes(self.peer))
        if flags & (1 << 0):
            writer.write(bytes(self.geo_point))
        writer.write_string(self.query)
        writer.write_string(self.offset)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        bot = reader.tgread_object()
        peer = reader.tgread_object()
        if flags & (1 << 0):
            geo_point = reader.tgread_object()
        else:
            geo_point = None
        query = reader.read_string()
        offset = reader.read_string()
        return cls(bot, peer, geo_point, query, offset)

@register
class MessagesSetInlineBotResults(TLObject):
    CONSTRUCTOR_ID = 3138561049
    __slots__ = ('gallery', 'private', 'query_id', 'results', 'cache_time', 'next_offset', 'switch_pm', 'switch_webview')
    def __init__(self, query_id: int, results: 'Vector', cache_time: int, gallery: bool = None, private: bool = None, next_offset: str = None, switch_pm: 'InlineBotSwitchPM' = None, switch_webview: 'InlineBotWebView' = None):
        self.gallery = gallery
        self.private = private
        self.query_id = query_id
        self.results = results
        self.cache_time = cache_time
        self.next_offset = next_offset
        self.switch_pm = switch_pm
        self.switch_webview = switch_webview
    def to_dict(self):
        return {"gallery": self.gallery, "private": self.private, "query_id": self.query_id, "results": self.results, "cache_time": self.cache_time, "next_offset": self.next_offset, "switch_pm": self.switch_pm, "switch_webview": self.switch_webview}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3138561049, signed=False)
        flags = 0
        if self.gallery: flags |= 1 << 0
        if self.private: flags |= 1 << 1
        if self.next_offset is not None: flags |= 1 << 2
        if self.switch_pm is not None: flags |= 1 << 3
        if self.switch_webview is not None: flags |= 1 << 4
        writer.write_int(flags, signed=False)
        writer.write_long(self.query_id, signed=False)
        writer.write(bytes(self.results))
        writer.write_int(self.cache_time, signed=True)
        if flags & (1 << 2):
            writer.write_string(self.next_offset)
        if flags & (1 << 3):
            writer.write(bytes(self.switch_pm))
        if flags & (1 << 4):
            writer.write(bytes(self.switch_webview))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        gallery = bool(flags & (1 << 0))
        private = bool(flags & (1 << 1))
        query_id = reader.read_long()
        results = reader.tgread_object()
        cache_time = reader.read_int()
        if flags & (1 << 2):
            next_offset = reader.read_string()
        else:
            next_offset = None
        if flags & (1 << 3):
            switch_pm = reader.tgread_object()
        else:
            switch_pm = None
        if flags & (1 << 4):
            switch_webview = reader.tgread_object()
        else:
            switch_webview = None
        return cls(gallery, private, query_id, results, cache_time, next_offset, switch_pm, switch_webview)

@register
class MessagesSendInlineBotResult(TLObject):
    CONSTRUCTOR_ID = 3234821702
    __slots__ = ('silent', 'background', 'clear_draft', 'hide_via', 'peer', 'reply_to', 'random_id', 'query_id', 'id', 'schedule_date', 'send_as', 'quick_reply_shortcut', 'allow_paid_stars')
    def __init__(self, peer: 'InputPeer', random_id: int, query_id: int, id: str, silent: bool = None, background: bool = None, clear_draft: bool = None, hide_via: bool = None, reply_to: 'InputReplyTo' = None, schedule_date: int = None, send_as: 'InputPeer' = None, quick_reply_shortcut: 'InputQuickReplyShortcut' = None, allow_paid_stars: int = None):
        self.silent = silent
        self.background = background
        self.clear_draft = clear_draft
        self.hide_via = hide_via
        self.peer = peer
        self.reply_to = reply_to
        self.random_id = random_id
        self.query_id = query_id
        self.id = id
        self.schedule_date = schedule_date
        self.send_as = send_as
        self.quick_reply_shortcut = quick_reply_shortcut
        self.allow_paid_stars = allow_paid_stars
    def to_dict(self):
        return {"silent": self.silent, "background": self.background, "clear_draft": self.clear_draft, "hide_via": self.hide_via, "peer": self.peer, "reply_to": self.reply_to, "random_id": self.random_id, "query_id": self.query_id, "id": self.id, "schedule_date": self.schedule_date, "send_as": self.send_as, "quick_reply_shortcut": self.quick_reply_shortcut, "allow_paid_stars": self.allow_paid_stars}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3234821702, signed=False)
        flags = 0
        if self.silent: flags |= 1 << 5
        if self.background: flags |= 1 << 6
        if self.clear_draft: flags |= 1 << 7
        if self.hide_via: flags |= 1 << 11
        if self.reply_to is not None: flags |= 1 << 0
        if self.schedule_date is not None: flags |= 1 << 10
        if self.send_as is not None: flags |= 1 << 13
        if self.quick_reply_shortcut is not None: flags |= 1 << 17
        if self.allow_paid_stars is not None: flags |= 1 << 21
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        if flags & (1 << 0):
            writer.write(bytes(self.reply_to))
        writer.write_long(self.random_id, signed=False)
        writer.write_long(self.query_id, signed=False)
        writer.write_string(self.id)
        if flags & (1 << 10):
            writer.write_int(self.schedule_date, signed=True)
        if flags & (1 << 13):
            writer.write(bytes(self.send_as))
        if flags & (1 << 17):
            writer.write(bytes(self.quick_reply_shortcut))
        if flags & (1 << 21):
            writer.write_long(self.allow_paid_stars, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        silent = bool(flags & (1 << 5))
        background = bool(flags & (1 << 6))
        clear_draft = bool(flags & (1 << 7))
        hide_via = bool(flags & (1 << 11))
        peer = reader.tgread_object()
        if flags & (1 << 0):
            reply_to = reader.tgread_object()
        else:
            reply_to = None
        random_id = reader.read_long()
        query_id = reader.read_long()
        id = reader.read_string()
        if flags & (1 << 10):
            schedule_date = reader.read_int()
        else:
            schedule_date = None
        if flags & (1 << 13):
            send_as = reader.tgread_object()
        else:
            send_as = None
        if flags & (1 << 17):
            quick_reply_shortcut = reader.tgread_object()
        else:
            quick_reply_shortcut = None
        if flags & (1 << 21):
            allow_paid_stars = reader.read_long()
        else:
            allow_paid_stars = None
        return cls(silent, background, clear_draft, hide_via, peer, reply_to, random_id, query_id, id, schedule_date, send_as, quick_reply_shortcut, allow_paid_stars)

@register
class MessagesGetMessageEditData(TLObject):
    CONSTRUCTOR_ID = 4255550774
    __slots__ = ('peer', 'id')
    def __init__(self, peer: 'InputPeer', id: int):
        self.peer = peer
        self.id = id
    def to_dict(self):
        return {"peer": self.peer, "id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4255550774, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.id, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        id = reader.read_int()
        return cls(peer, id)

@register
class MessagesEditMessage(TLObject):
    CONSTRUCTOR_ID = 1374175969
    __slots__ = ('no_webpage', 'invert_media', 'peer', 'id', 'message', 'media', 'reply_markup', 'entities', 'schedule_date', 'schedule_repeat_period', 'quick_reply_shortcut_id')
    def __init__(self, peer: 'InputPeer', id: int, no_webpage: bool = None, invert_media: bool = None, message: str = None, media: 'InputMedia' = None, reply_markup: 'ReplyMarkup' = None, entities: 'Vector' = None, schedule_date: int = None, schedule_repeat_period: int = None, quick_reply_shortcut_id: int = None):
        self.no_webpage = no_webpage
        self.invert_media = invert_media
        self.peer = peer
        self.id = id
        self.message = message
        self.media = media
        self.reply_markup = reply_markup
        self.entities = entities
        self.schedule_date = schedule_date
        self.schedule_repeat_period = schedule_repeat_period
        self.quick_reply_shortcut_id = quick_reply_shortcut_id
    def to_dict(self):
        return {"no_webpage": self.no_webpage, "invert_media": self.invert_media, "peer": self.peer, "id": self.id, "message": self.message, "media": self.media, "reply_markup": self.reply_markup, "entities": self.entities, "schedule_date": self.schedule_date, "schedule_repeat_period": self.schedule_repeat_period, "quick_reply_shortcut_id": self.quick_reply_shortcut_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1374175969, signed=False)
        flags = 0
        if self.no_webpage: flags |= 1 << 1
        if self.invert_media: flags |= 1 << 16
        if self.message is not None: flags |= 1 << 11
        if self.media is not None: flags |= 1 << 14
        if self.reply_markup is not None: flags |= 1 << 2
        if self.entities is not None: flags |= 1 << 3
        if self.schedule_date is not None: flags |= 1 << 15
        if self.schedule_repeat_period is not None: flags |= 1 << 18
        if self.quick_reply_shortcut_id is not None: flags |= 1 << 17
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.id, signed=True)
        if flags & (1 << 11):
            writer.write_string(self.message)
        if flags & (1 << 14):
            writer.write(bytes(self.media))
        if flags & (1 << 2):
            writer.write(bytes(self.reply_markup))
        if flags & (1 << 3):
            writer.write(bytes(self.entities))
        if flags & (1 << 15):
            writer.write_int(self.schedule_date, signed=True)
        if flags & (1 << 18):
            writer.write_int(self.schedule_repeat_period, signed=True)
        if flags & (1 << 17):
            writer.write_int(self.quick_reply_shortcut_id, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        no_webpage = bool(flags & (1 << 1))
        invert_media = bool(flags & (1 << 16))
        peer = reader.tgread_object()
        id = reader.read_int()
        if flags & (1 << 11):
            message = reader.read_string()
        else:
            message = None
        if flags & (1 << 14):
            media = reader.tgread_object()
        else:
            media = None
        if flags & (1 << 2):
            reply_markup = reader.tgread_object()
        else:
            reply_markup = None
        if flags & (1 << 3):
            entities = reader.tgread_object()
        else:
            entities = None
        if flags & (1 << 15):
            schedule_date = reader.read_int()
        else:
            schedule_date = None
        if flags & (1 << 18):
            schedule_repeat_period = reader.read_int()
        else:
            schedule_repeat_period = None
        if flags & (1 << 17):
            quick_reply_shortcut_id = reader.read_int()
        else:
            quick_reply_shortcut_id = None
        return cls(no_webpage, invert_media, peer, id, message, media, reply_markup, entities, schedule_date, schedule_repeat_period, quick_reply_shortcut_id)

@register
class MessagesEditInlineBotMessage(TLObject):
    CONSTRUCTOR_ID = 2203418042
    __slots__ = ('no_webpage', 'invert_media', 'id', 'message', 'media', 'reply_markup', 'entities')
    def __init__(self, id: 'InputBotInlineMessageID', no_webpage: bool = None, invert_media: bool = None, message: str = None, media: 'InputMedia' = None, reply_markup: 'ReplyMarkup' = None, entities: 'Vector' = None):
        self.no_webpage = no_webpage
        self.invert_media = invert_media
        self.id = id
        self.message = message
        self.media = media
        self.reply_markup = reply_markup
        self.entities = entities
    def to_dict(self):
        return {"no_webpage": self.no_webpage, "invert_media": self.invert_media, "id": self.id, "message": self.message, "media": self.media, "reply_markup": self.reply_markup, "entities": self.entities}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2203418042, signed=False)
        flags = 0
        if self.no_webpage: flags |= 1 << 1
        if self.invert_media: flags |= 1 << 16
        if self.message is not None: flags |= 1 << 11
        if self.media is not None: flags |= 1 << 14
        if self.reply_markup is not None: flags |= 1 << 2
        if self.entities is not None: flags |= 1 << 3
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.id))
        if flags & (1 << 11):
            writer.write_string(self.message)
        if flags & (1 << 14):
            writer.write(bytes(self.media))
        if flags & (1 << 2):
            writer.write(bytes(self.reply_markup))
        if flags & (1 << 3):
            writer.write(bytes(self.entities))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        no_webpage = bool(flags & (1 << 1))
        invert_media = bool(flags & (1 << 16))
        id = reader.tgread_object()
        if flags & (1 << 11):
            message = reader.read_string()
        else:
            message = None
        if flags & (1 << 14):
            media = reader.tgread_object()
        else:
            media = None
        if flags & (1 << 2):
            reply_markup = reader.tgread_object()
        else:
            reply_markup = None
        if flags & (1 << 3):
            entities = reader.tgread_object()
        else:
            entities = None
        return cls(no_webpage, invert_media, id, message, media, reply_markup, entities)

@register
class MessagesGetBotCallbackAnswer(TLObject):
    CONSTRUCTOR_ID = 2470627847
    __slots__ = ('game', 'peer', 'msg_id', 'data', 'password')
    def __init__(self, peer: 'InputPeer', msg_id: int, game: bool = None, data: bytes = None, password: 'InputCheckPasswordSRP' = None):
        self.game = game
        self.peer = peer
        self.msg_id = msg_id
        self.data = data
        self.password = password
    def to_dict(self):
        return {"game": self.game, "peer": self.peer, "msg_id": self.msg_id, "data": self.data, "password": self.password}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2470627847, signed=False)
        flags = 0
        if self.game: flags |= 1 << 1
        if self.data is not None: flags |= 1 << 0
        if self.password is not None: flags |= 1 << 2
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.msg_id, signed=True)
        if flags & (1 << 0):
            writer.write_bytes(self.data)
        if flags & (1 << 2):
            writer.write(bytes(self.password))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        game = bool(flags & (1 << 1))
        peer = reader.tgread_object()
        msg_id = reader.read_int()
        if flags & (1 << 0):
            data = reader.read_bytes()
        else:
            data = None
        if flags & (1 << 2):
            password = reader.tgread_object()
        else:
            password = None
        return cls(game, peer, msg_id, data, password)

@register
class MessagesSetBotCallbackAnswer(TLObject):
    CONSTRUCTOR_ID = 3582923530
    __slots__ = ('alert', 'query_id', 'message', 'url', 'cache_time')
    def __init__(self, query_id: int, cache_time: int, alert: bool = None, message: str = None, url: str = None):
        self.alert = alert
        self.query_id = query_id
        self.message = message
        self.url = url
        self.cache_time = cache_time
    def to_dict(self):
        return {"alert": self.alert, "query_id": self.query_id, "message": self.message, "url": self.url, "cache_time": self.cache_time}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3582923530, signed=False)
        flags = 0
        if self.alert: flags |= 1 << 1
        if self.message is not None: flags |= 1 << 0
        if self.url is not None: flags |= 1 << 2
        writer.write_int(flags, signed=False)
        writer.write_long(self.query_id, signed=False)
        if flags & (1 << 0):
            writer.write_string(self.message)
        if flags & (1 << 2):
            writer.write_string(self.url)
        writer.write_int(self.cache_time, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        alert = bool(flags & (1 << 1))
        query_id = reader.read_long()
        if flags & (1 << 0):
            message = reader.read_string()
        else:
            message = None
        if flags & (1 << 2):
            url = reader.read_string()
        else:
            url = None
        cache_time = reader.read_int()
        return cls(alert, query_id, message, url, cache_time)

@register
class MessagesGetPeerDialogs(TLObject):
    CONSTRUCTOR_ID = 3832593661
    __slots__ = ('peers')
    def __init__(self, peers: 'Vector'):
        self.peers = peers
    def to_dict(self):
        return {"peers": self.peers}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3832593661, signed=False)
        writer.write(bytes(self.peers))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peers = reader.tgread_object()
        return cls(peers)

@register
class MessagesSaveDraft(TLObject):
    CONSTRUCTOR_ID = 1420701838
    __slots__ = ('no_webpage', 'invert_media', 'reply_to', 'peer', 'message', 'entities', 'media', 'effect', 'suggested_post')
    def __init__(self, peer: 'InputPeer', message: str, no_webpage: bool = None, invert_media: bool = None, reply_to: 'InputReplyTo' = None, entities: 'Vector' = None, media: 'InputMedia' = None, effect: int = None, suggested_post: 'SuggestedPost' = None):
        self.no_webpage = no_webpage
        self.invert_media = invert_media
        self.reply_to = reply_to
        self.peer = peer
        self.message = message
        self.entities = entities
        self.media = media
        self.effect = effect
        self.suggested_post = suggested_post
    def to_dict(self):
        return {"no_webpage": self.no_webpage, "invert_media": self.invert_media, "reply_to": self.reply_to, "peer": self.peer, "message": self.message, "entities": self.entities, "media": self.media, "effect": self.effect, "suggested_post": self.suggested_post}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1420701838, signed=False)
        flags = 0
        if self.no_webpage: flags |= 1 << 1
        if self.invert_media: flags |= 1 << 6
        if self.reply_to is not None: flags |= 1 << 4
        if self.entities is not None: flags |= 1 << 3
        if self.media is not None: flags |= 1 << 5
        if self.effect is not None: flags |= 1 << 7
        if self.suggested_post is not None: flags |= 1 << 8
        writer.write_int(flags, signed=False)
        if flags & (1 << 4):
            writer.write(bytes(self.reply_to))
        writer.write(bytes(self.peer))
        writer.write_string(self.message)
        if flags & (1 << 3):
            writer.write(bytes(self.entities))
        if flags & (1 << 5):
            writer.write(bytes(self.media))
        if flags & (1 << 7):
            writer.write_long(self.effect, signed=False)
        if flags & (1 << 8):
            writer.write(bytes(self.suggested_post))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        no_webpage = bool(flags & (1 << 1))
        invert_media = bool(flags & (1 << 6))
        if flags & (1 << 4):
            reply_to = reader.tgread_object()
        else:
            reply_to = None
        peer = reader.tgread_object()
        message = reader.read_string()
        if flags & (1 << 3):
            entities = reader.tgread_object()
        else:
            entities = None
        if flags & (1 << 5):
            media = reader.tgread_object()
        else:
            media = None
        if flags & (1 << 7):
            effect = reader.read_long()
        else:
            effect = None
        if flags & (1 << 8):
            suggested_post = reader.tgread_object()
        else:
            suggested_post = None
        return cls(no_webpage, invert_media, reply_to, peer, message, entities, media, effect, suggested_post)

@register
class MessagesGetAllDrafts(TLObject):
    CONSTRUCTOR_ID = 1782549861
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1782549861, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class MessagesGetFeaturedStickers(TLObject):
    CONSTRUCTOR_ID = 1685588756
    __slots__ = ('hash')
    def __init__(self, hash: int):
        self.hash = hash
    def to_dict(self):
        return {"hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1685588756, signed=False)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_long()
        return cls(hash)

@register
class MessagesReadFeaturedStickers(TLObject):
    CONSTRUCTOR_ID = 1527873830
    __slots__ = ('id')
    def __init__(self, id: 'Vector'):
        self.id = id
    def to_dict(self):
        return {"id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1527873830, signed=False)
        writer.write(bytes(self.id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        id = reader.tgread_object()
        return cls(id)

@register
class MessagesGetRecentStickers(TLObject):
    CONSTRUCTOR_ID = 2645114939
    __slots__ = ('attached', 'hash')
    def __init__(self, hash: int, attached: bool = None):
        self.attached = attached
        self.hash = hash
    def to_dict(self):
        return {"attached": self.attached, "hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2645114939, signed=False)
        flags = 0
        if self.attached: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        attached = bool(flags & (1 << 0))
        hash = reader.read_long()
        return cls(attached, hash)

@register
class MessagesSaveRecentSticker(TLObject):
    CONSTRUCTOR_ID = 958863608
    __slots__ = ('attached', 'id', 'unsave')
    def __init__(self, id: 'InputDocument', unsave: bool, attached: bool = None):
        self.attached = attached
        self.id = id
        self.unsave = unsave
    def to_dict(self):
        return {"attached": self.attached, "id": self.id, "unsave": self.unsave}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(958863608, signed=False)
        flags = 0
        if self.attached: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.id))
        writer.write(serialize_bool(self.unsave))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        attached = bool(flags & (1 << 0))
        id = reader.tgread_object()
        unsave = reader.tgread_bool()
        return cls(attached, id, unsave)

@register
class MessagesClearRecentStickers(TLObject):
    CONSTRUCTOR_ID = 2308530221
    __slots__ = ('attached')
    def __init__(self, attached: bool = None):
        self.attached = attached
    def to_dict(self):
        return {"attached": self.attached}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2308530221, signed=False)
        flags = 0
        if self.attached: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        attached = bool(flags & (1 << 0))
        return cls(attached)

@register
class MessagesGetArchivedStickers(TLObject):
    CONSTRUCTOR_ID = 1475442322
    __slots__ = ('masks', 'emojis', 'offset_id', 'limit')
    def __init__(self, offset_id: int, limit: int, masks: bool = None, emojis: bool = None):
        self.masks = masks
        self.emojis = emojis
        self.offset_id = offset_id
        self.limit = limit
    def to_dict(self):
        return {"masks": self.masks, "emojis": self.emojis, "offset_id": self.offset_id, "limit": self.limit}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1475442322, signed=False)
        flags = 0
        if self.masks: flags |= 1 << 0
        if self.emojis: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write_long(self.offset_id, signed=False)
        writer.write_int(self.limit, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        masks = bool(flags & (1 << 0))
        emojis = bool(flags & (1 << 1))
        offset_id = reader.read_long()
        limit = reader.read_int()
        return cls(masks, emojis, offset_id, limit)

@register
class MessagesGetMaskStickers(TLObject):
    CONSTRUCTOR_ID = 1678738104
    __slots__ = ('hash')
    def __init__(self, hash: int):
        self.hash = hash
    def to_dict(self):
        return {"hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1678738104, signed=False)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_long()
        return cls(hash)

@register
class MessagesGetAttachedStickers(TLObject):
    CONSTRUCTOR_ID = 3428542412
    __slots__ = ('media')
    def __init__(self, media: 'InputStickeredMedia'):
        self.media = media
    def to_dict(self):
        return {"media": self.media}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3428542412, signed=False)
        writer.write(bytes(self.media))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        media = reader.tgread_object()
        return cls(media)

@register
class MessagesSetGameScore(TLObject):
    CONSTRUCTOR_ID = 2398678208
    __slots__ = ('edit_message', 'force', 'peer', 'id', 'user_id', 'score')
    def __init__(self, peer: 'InputPeer', id: int, user_id: 'InputUser', score: int, edit_message: bool = None, force: bool = None):
        self.edit_message = edit_message
        self.force = force
        self.peer = peer
        self.id = id
        self.user_id = user_id
        self.score = score
    def to_dict(self):
        return {"edit_message": self.edit_message, "force": self.force, "peer": self.peer, "id": self.id, "user_id": self.user_id, "score": self.score}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2398678208, signed=False)
        flags = 0
        if self.edit_message: flags |= 1 << 0
        if self.force: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.id, signed=True)
        writer.write(bytes(self.user_id))
        writer.write_int(self.score, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        edit_message = bool(flags & (1 << 0))
        force = bool(flags & (1 << 1))
        peer = reader.tgread_object()
        id = reader.read_int()
        user_id = reader.tgread_object()
        score = reader.read_int()
        return cls(edit_message, force, peer, id, user_id, score)

@register
class MessagesSetInlineGameScore(TLObject):
    CONSTRUCTOR_ID = 363700068
    __slots__ = ('edit_message', 'force', 'id', 'user_id', 'score')
    def __init__(self, id: 'InputBotInlineMessageID', user_id: 'InputUser', score: int, edit_message: bool = None, force: bool = None):
        self.edit_message = edit_message
        self.force = force
        self.id = id
        self.user_id = user_id
        self.score = score
    def to_dict(self):
        return {"edit_message": self.edit_message, "force": self.force, "id": self.id, "user_id": self.user_id, "score": self.score}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(363700068, signed=False)
        flags = 0
        if self.edit_message: flags |= 1 << 0
        if self.force: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.id))
        writer.write(bytes(self.user_id))
        writer.write_int(self.score, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        edit_message = bool(flags & (1 << 0))
        force = bool(flags & (1 << 1))
        id = reader.tgread_object()
        user_id = reader.tgread_object()
        score = reader.read_int()
        return cls(edit_message, force, id, user_id, score)

@register
class MessagesGetGameHighScores(TLObject):
    CONSTRUCTOR_ID = 3894568093
    __slots__ = ('peer', 'id', 'user_id')
    def __init__(self, peer: 'InputPeer', id: int, user_id: 'InputUser'):
        self.peer = peer
        self.id = id
        self.user_id = user_id
    def to_dict(self):
        return {"peer": self.peer, "id": self.id, "user_id": self.user_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3894568093, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.id, signed=True)
        writer.write(bytes(self.user_id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        id = reader.read_int()
        user_id = reader.tgread_object()
        return cls(peer, id, user_id)

@register
class MessagesGetInlineGameHighScores(TLObject):
    CONSTRUCTOR_ID = 258170395
    __slots__ = ('id', 'user_id')
    def __init__(self, id: 'InputBotInlineMessageID', user_id: 'InputUser'):
        self.id = id
        self.user_id = user_id
    def to_dict(self):
        return {"id": self.id, "user_id": self.user_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(258170395, signed=False)
        writer.write(bytes(self.id))
        writer.write(bytes(self.user_id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        id = reader.tgread_object()
        user_id = reader.tgread_object()
        return cls(id, user_id)

@register
class MessagesGetCommonChats(TLObject):
    CONSTRUCTOR_ID = 3826032900
    __slots__ = ('user_id', 'max_id', 'limit')
    def __init__(self, user_id: 'InputUser', max_id: int, limit: int):
        self.user_id = user_id
        self.max_id = max_id
        self.limit = limit
    def to_dict(self):
        return {"user_id": self.user_id, "max_id": self.max_id, "limit": self.limit}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3826032900, signed=False)
        writer.write(bytes(self.user_id))
        writer.write_long(self.max_id, signed=False)
        writer.write_int(self.limit, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        user_id = reader.tgread_object()
        max_id = reader.read_long()
        limit = reader.read_int()
        return cls(user_id, max_id, limit)

@register
class MessagesGetWebPage(TLObject):
    CONSTRUCTOR_ID = 2375455395
    __slots__ = ('url', 'hash')
    def __init__(self, url: str, hash: int):
        self.url = url
        self.hash = hash
    def to_dict(self):
        return {"url": self.url, "hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2375455395, signed=False)
        writer.write_string(self.url)
        writer.write_int(self.hash, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        url = reader.read_string()
        hash = reader.read_int()
        return cls(url, hash)

@register
class MessagesToggleDialogPin(TLObject):
    CONSTRUCTOR_ID = 2805064279
    __slots__ = ('pinned', 'peer')
    def __init__(self, peer: 'InputDialogPeer', pinned: bool = None):
        self.pinned = pinned
        self.peer = peer
    def to_dict(self):
        return {"pinned": self.pinned, "peer": self.peer}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2805064279, signed=False)
        flags = 0
        if self.pinned: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        pinned = bool(flags & (1 << 0))
        peer = reader.tgread_object()
        return cls(pinned, peer)

@register
class MessagesReorderPinnedDialogs(TLObject):
    CONSTRUCTOR_ID = 991616823
    __slots__ = ('force', 'folder_id', 'order')
    def __init__(self, folder_id: int, order: 'Vector', force: bool = None):
        self.force = force
        self.folder_id = folder_id
        self.order = order
    def to_dict(self):
        return {"force": self.force, "folder_id": self.folder_id, "order": self.order}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(991616823, signed=False)
        flags = 0
        if self.force: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write_int(self.folder_id, signed=True)
        writer.write(bytes(self.order))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        force = bool(flags & (1 << 0))
        folder_id = reader.read_int()
        order = reader.tgread_object()
        return cls(force, folder_id, order)

@register
class MessagesGetPinnedDialogs(TLObject):
    CONSTRUCTOR_ID = 3602468338
    __slots__ = ('folder_id')
    def __init__(self, folder_id: int):
        self.folder_id = folder_id
    def to_dict(self):
        return {"folder_id": self.folder_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3602468338, signed=False)
        writer.write_int(self.folder_id, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        folder_id = reader.read_int()
        return cls(folder_id)

@register
class MessagesSetBotShippingResults(TLObject):
    CONSTRUCTOR_ID = 3858133754
    __slots__ = ('query_id', 'error', 'shipping_options')
    def __init__(self, query_id: int, error: str = None, shipping_options: 'Vector' = None):
        self.query_id = query_id
        self.error = error
        self.shipping_options = shipping_options
    def to_dict(self):
        return {"query_id": self.query_id, "error": self.error, "shipping_options": self.shipping_options}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3858133754, signed=False)
        flags = 0
        if self.error is not None: flags |= 1 << 0
        if self.shipping_options is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write_long(self.query_id, signed=False)
        if flags & (1 << 0):
            writer.write_string(self.error)
        if flags & (1 << 1):
            writer.write(bytes(self.shipping_options))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        query_id = reader.read_long()
        if flags & (1 << 0):
            error = reader.read_string()
        else:
            error = None
        if flags & (1 << 1):
            shipping_options = reader.tgread_object()
        else:
            shipping_options = None
        return cls(query_id, error, shipping_options)

@register
class MessagesSetBotPrecheckoutResults(TLObject):
    CONSTRUCTOR_ID = 163765653
    __slots__ = ('success', 'query_id', 'error')
    def __init__(self, query_id: int, success: bool = None, error: str = None):
        self.success = success
        self.query_id = query_id
        self.error = error
    def to_dict(self):
        return {"success": self.success, "query_id": self.query_id, "error": self.error}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(163765653, signed=False)
        flags = 0
        if self.success: flags |= 1 << 1
        if self.error is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write_long(self.query_id, signed=False)
        if flags & (1 << 0):
            writer.write_string(self.error)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        success = bool(flags & (1 << 1))
        query_id = reader.read_long()
        if flags & (1 << 0):
            error = reader.read_string()
        else:
            error = None
        return cls(success, query_id, error)

@register
class MessagesUploadMedia(TLObject):
    CONSTRUCTOR_ID = 345405816
    __slots__ = ('business_connection_id', 'peer', 'media')
    def __init__(self, peer: 'InputPeer', media: 'InputMedia', business_connection_id: str = None):
        self.business_connection_id = business_connection_id
        self.peer = peer
        self.media = media
    def to_dict(self):
        return {"business_connection_id": self.business_connection_id, "peer": self.peer, "media": self.media}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(345405816, signed=False)
        flags = 0
        if self.business_connection_id is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        if flags & (1 << 0):
            writer.write_string(self.business_connection_id)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.media))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        if flags & (1 << 0):
            business_connection_id = reader.read_string()
        else:
            business_connection_id = None
        peer = reader.tgread_object()
        media = reader.tgread_object()
        return cls(business_connection_id, peer, media)

@register
class MessagesSendScreenshotNotification(TLObject):
    CONSTRUCTOR_ID = 2705348631
    __slots__ = ('peer', 'reply_to', 'random_id')
    def __init__(self, peer: 'InputPeer', reply_to: 'InputReplyTo', random_id: int):
        self.peer = peer
        self.reply_to = reply_to
        self.random_id = random_id
    def to_dict(self):
        return {"peer": self.peer, "reply_to": self.reply_to, "random_id": self.random_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2705348631, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.reply_to))
        writer.write_long(self.random_id, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        reply_to = reader.tgread_object()
        random_id = reader.read_long()
        return cls(peer, reply_to, random_id)

@register
class MessagesGetFavedStickers(TLObject):
    CONSTRUCTOR_ID = 82946729
    __slots__ = ('hash')
    def __init__(self, hash: int):
        self.hash = hash
    def to_dict(self):
        return {"hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(82946729, signed=False)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_long()
        return cls(hash)

@register
class MessagesFaveSticker(TLObject):
    CONSTRUCTOR_ID = 3120547163
    __slots__ = ('id', 'unfave')
    def __init__(self, id: 'InputDocument', unfave: bool):
        self.id = id
        self.unfave = unfave
    def to_dict(self):
        return {"id": self.id, "unfave": self.unfave}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3120547163, signed=False)
        writer.write(bytes(self.id))
        writer.write(serialize_bool(self.unfave))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        id = reader.tgread_object()
        unfave = reader.tgread_bool()
        return cls(id, unfave)

@register
class MessagesGetUnreadMentions(TLObject):
    CONSTRUCTOR_ID = 4043827088
    __slots__ = ('peer', 'top_msg_id', 'offset_id', 'add_offset', 'limit', 'max_id', 'min_id')
    def __init__(self, peer: 'InputPeer', offset_id: int, add_offset: int, limit: int, max_id: int, min_id: int, top_msg_id: int = None):
        self.peer = peer
        self.top_msg_id = top_msg_id
        self.offset_id = offset_id
        self.add_offset = add_offset
        self.limit = limit
        self.max_id = max_id
        self.min_id = min_id
    def to_dict(self):
        return {"peer": self.peer, "top_msg_id": self.top_msg_id, "offset_id": self.offset_id, "add_offset": self.add_offset, "limit": self.limit, "max_id": self.max_id, "min_id": self.min_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4043827088, signed=False)
        flags = 0
        if self.top_msg_id is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        if flags & (1 << 0):
            writer.write_int(self.top_msg_id, signed=True)
        writer.write_int(self.offset_id, signed=True)
        writer.write_int(self.add_offset, signed=True)
        writer.write_int(self.limit, signed=True)
        writer.write_int(self.max_id, signed=True)
        writer.write_int(self.min_id, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        peer = reader.tgread_object()
        if flags & (1 << 0):
            top_msg_id = reader.read_int()
        else:
            top_msg_id = None
        offset_id = reader.read_int()
        add_offset = reader.read_int()
        limit = reader.read_int()
        max_id = reader.read_int()
        min_id = reader.read_int()
        return cls(peer, top_msg_id, offset_id, add_offset, limit, max_id, min_id)

@register
class MessagesReadMentions(TLObject):
    CONSTRUCTOR_ID = 921026381
    __slots__ = ('peer', 'top_msg_id')
    def __init__(self, peer: 'InputPeer', top_msg_id: int = None):
        self.peer = peer
        self.top_msg_id = top_msg_id
    def to_dict(self):
        return {"peer": self.peer, "top_msg_id": self.top_msg_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(921026381, signed=False)
        flags = 0
        if self.top_msg_id is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        if flags & (1 << 0):
            writer.write_int(self.top_msg_id, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        peer = reader.tgread_object()
        if flags & (1 << 0):
            top_msg_id = reader.read_int()
        else:
            top_msg_id = None
        return cls(peer, top_msg_id)

@register
class MessagesGetRecentLocations(TLObject):
    CONSTRUCTOR_ID = 1881817312
    __slots__ = ('peer', 'limit', 'hash')
    def __init__(self, peer: 'InputPeer', limit: int, hash: int):
        self.peer = peer
        self.limit = limit
        self.hash = hash
    def to_dict(self):
        return {"peer": self.peer, "limit": self.limit, "hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1881817312, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.limit, signed=True)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        limit = reader.read_int()
        hash = reader.read_long()
        return cls(peer, limit, hash)

@register
class MessagesSendMultiMedia(TLObject):
    CONSTRUCTOR_ID = 469278068
    __slots__ = ('silent', 'background', 'clear_draft', 'noforwards', 'update_stickersets_order', 'invert_media', 'allow_paid_floodskip', 'peer', 'reply_to', 'multi_media', 'schedule_date', 'send_as', 'quick_reply_shortcut', 'effect', 'allow_paid_stars')
    def __init__(self, peer: 'InputPeer', multi_media: 'Vector', silent: bool = None, background: bool = None, clear_draft: bool = None, noforwards: bool = None, update_stickersets_order: bool = None, invert_media: bool = None, allow_paid_floodskip: bool = None, reply_to: 'InputReplyTo' = None, schedule_date: int = None, send_as: 'InputPeer' = None, quick_reply_shortcut: 'InputQuickReplyShortcut' = None, effect: int = None, allow_paid_stars: int = None):
        self.silent = silent
        self.background = background
        self.clear_draft = clear_draft
        self.noforwards = noforwards
        self.update_stickersets_order = update_stickersets_order
        self.invert_media = invert_media
        self.allow_paid_floodskip = allow_paid_floodskip
        self.peer = peer
        self.reply_to = reply_to
        self.multi_media = multi_media
        self.schedule_date = schedule_date
        self.send_as = send_as
        self.quick_reply_shortcut = quick_reply_shortcut
        self.effect = effect
        self.allow_paid_stars = allow_paid_stars
    def to_dict(self):
        return {"silent": self.silent, "background": self.background, "clear_draft": self.clear_draft, "noforwards": self.noforwards, "update_stickersets_order": self.update_stickersets_order, "invert_media": self.invert_media, "allow_paid_floodskip": self.allow_paid_floodskip, "peer": self.peer, "reply_to": self.reply_to, "multi_media": self.multi_media, "schedule_date": self.schedule_date, "send_as": self.send_as, "quick_reply_shortcut": self.quick_reply_shortcut, "effect": self.effect, "allow_paid_stars": self.allow_paid_stars}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(469278068, signed=False)
        flags = 0
        if self.silent: flags |= 1 << 5
        if self.background: flags |= 1 << 6
        if self.clear_draft: flags |= 1 << 7
        if self.noforwards: flags |= 1 << 14
        if self.update_stickersets_order: flags |= 1 << 15
        if self.invert_media: flags |= 1 << 16
        if self.allow_paid_floodskip: flags |= 1 << 19
        if self.reply_to is not None: flags |= 1 << 0
        if self.schedule_date is not None: flags |= 1 << 10
        if self.send_as is not None: flags |= 1 << 13
        if self.quick_reply_shortcut is not None: flags |= 1 << 17
        if self.effect is not None: flags |= 1 << 18
        if self.allow_paid_stars is not None: flags |= 1 << 21
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        if flags & (1 << 0):
            writer.write(bytes(self.reply_to))
        writer.write(bytes(self.multi_media))
        if flags & (1 << 10):
            writer.write_int(self.schedule_date, signed=True)
        if flags & (1 << 13):
            writer.write(bytes(self.send_as))
        if flags & (1 << 17):
            writer.write(bytes(self.quick_reply_shortcut))
        if flags & (1 << 18):
            writer.write_long(self.effect, signed=False)
        if flags & (1 << 21):
            writer.write_long(self.allow_paid_stars, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        silent = bool(flags & (1 << 5))
        background = bool(flags & (1 << 6))
        clear_draft = bool(flags & (1 << 7))
        noforwards = bool(flags & (1 << 14))
        update_stickersets_order = bool(flags & (1 << 15))
        invert_media = bool(flags & (1 << 16))
        allow_paid_floodskip = bool(flags & (1 << 19))
        peer = reader.tgread_object()
        if flags & (1 << 0):
            reply_to = reader.tgread_object()
        else:
            reply_to = None
        multi_media = reader.tgread_object()
        if flags & (1 << 10):
            schedule_date = reader.read_int()
        else:
            schedule_date = None
        if flags & (1 << 13):
            send_as = reader.tgread_object()
        else:
            send_as = None
        if flags & (1 << 17):
            quick_reply_shortcut = reader.tgread_object()
        else:
            quick_reply_shortcut = None
        if flags & (1 << 18):
            effect = reader.read_long()
        else:
            effect = None
        if flags & (1 << 21):
            allow_paid_stars = reader.read_long()
        else:
            allow_paid_stars = None
        return cls(silent, background, clear_draft, noforwards, update_stickersets_order, invert_media, allow_paid_floodskip, peer, reply_to, multi_media, schedule_date, send_as, quick_reply_shortcut, effect, allow_paid_stars)

@register
class MessagesUploadEncryptedFile(TLObject):
    CONSTRUCTOR_ID = 1347929239
    __slots__ = ('peer', 'file')
    def __init__(self, peer: 'InputEncryptedChat', file: 'InputEncryptedFile'):
        self.peer = peer
        self.file = file
    def to_dict(self):
        return {"peer": self.peer, "file": self.file}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1347929239, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.file))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        file = reader.tgread_object()
        return cls(peer, file)

@register
class MessagesSearchStickerSets(TLObject):
    CONSTRUCTOR_ID = 896555914
    __slots__ = ('exclude_featured', 'q', 'hash')
    def __init__(self, q: str, hash: int, exclude_featured: bool = None):
        self.exclude_featured = exclude_featured
        self.q = q
        self.hash = hash
    def to_dict(self):
        return {"exclude_featured": self.exclude_featured, "q": self.q, "hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(896555914, signed=False)
        flags = 0
        if self.exclude_featured: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write_string(self.q)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        exclude_featured = bool(flags & (1 << 0))
        q = reader.read_string()
        hash = reader.read_long()
        return cls(exclude_featured, q, hash)

@register
class MessagesGetSplitRanges(TLObject):
    CONSTRUCTOR_ID = 486505992
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(486505992, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class MessagesMarkDialogUnread(TLObject):
    CONSTRUCTOR_ID = 2354054904
    __slots__ = ('unread', 'parent_peer', 'peer')
    def __init__(self, peer: 'InputDialogPeer', unread: bool = None, parent_peer: 'InputPeer' = None):
        self.unread = unread
        self.parent_peer = parent_peer
        self.peer = peer
    def to_dict(self):
        return {"unread": self.unread, "parent_peer": self.parent_peer, "peer": self.peer}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2354054904, signed=False)
        flags = 0
        if self.unread: flags |= 1 << 0
        if self.parent_peer is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        if flags & (1 << 1):
            writer.write(bytes(self.parent_peer))
        writer.write(bytes(self.peer))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        unread = bool(flags & (1 << 0))
        if flags & (1 << 1):
            parent_peer = reader.tgread_object()
        else:
            parent_peer = None
        peer = reader.tgread_object()
        return cls(unread, parent_peer, peer)

@register
class MessagesGetDialogUnreadMarks(TLObject):
    CONSTRUCTOR_ID = 555754018
    __slots__ = ('parent_peer')
    def __init__(self, parent_peer: 'InputPeer' = None):
        self.parent_peer = parent_peer
    def to_dict(self):
        return {"parent_peer": self.parent_peer}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(555754018, signed=False)
        flags = 0
        if self.parent_peer is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        if flags & (1 << 0):
            writer.write(bytes(self.parent_peer))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        if flags & (1 << 0):
            parent_peer = reader.tgread_object()
        else:
            parent_peer = None
        return cls(parent_peer)

@register
class MessagesClearAllDrafts(TLObject):
    CONSTRUCTOR_ID = 2119757468
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2119757468, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class MessagesUpdatePinnedMessage(TLObject):
    CONSTRUCTOR_ID = 3534419948
    __slots__ = ('silent', 'unpin', 'pm_oneside', 'peer', 'id')
    def __init__(self, peer: 'InputPeer', id: int, silent: bool = None, unpin: bool = None, pm_oneside: bool = None):
        self.silent = silent
        self.unpin = unpin
        self.pm_oneside = pm_oneside
        self.peer = peer
        self.id = id
    def to_dict(self):
        return {"silent": self.silent, "unpin": self.unpin, "pm_oneside": self.pm_oneside, "peer": self.peer, "id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3534419948, signed=False)
        flags = 0
        if self.silent: flags |= 1 << 0
        if self.unpin: flags |= 1 << 1
        if self.pm_oneside: flags |= 1 << 2
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.id, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        silent = bool(flags & (1 << 0))
        unpin = bool(flags & (1 << 1))
        pm_oneside = bool(flags & (1 << 2))
        peer = reader.tgread_object()
        id = reader.read_int()
        return cls(silent, unpin, pm_oneside, peer, id)

@register
class MessagesSendVote(TLObject):
    CONSTRUCTOR_ID = 283795844
    __slots__ = ('peer', 'msg_id', 'options')
    def __init__(self, peer: 'InputPeer', msg_id: int, options: 'Vector'):
        self.peer = peer
        self.msg_id = msg_id
        self.options = options
    def to_dict(self):
        return {"peer": self.peer, "msg_id": self.msg_id, "options": self.options}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(283795844, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.msg_id, signed=True)
        writer.write(bytes(self.options))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        msg_id = reader.read_int()
        options = reader.tgread_object()
        return cls(peer, msg_id, options)

@register
class MessagesGetPollResults(TLObject):
    CONSTRUCTOR_ID = 3986940731
    __slots__ = ('peer', 'msg_id', 'poll_hash')
    def __init__(self, peer: 'InputPeer', msg_id: int, poll_hash: int):
        self.peer = peer
        self.msg_id = msg_id
        self.poll_hash = poll_hash
    def to_dict(self):
        return {"peer": self.peer, "msg_id": self.msg_id, "poll_hash": self.poll_hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3986940731, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.msg_id, signed=True)
        writer.write_long(self.poll_hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        msg_id = reader.read_int()
        poll_hash = reader.read_long()
        return cls(peer, msg_id, poll_hash)

@register
class MessagesGetOnlines(TLObject):
    CONSTRUCTOR_ID = 1848369232
    __slots__ = ('peer')
    def __init__(self, peer: 'InputPeer'):
        self.peer = peer
    def to_dict(self):
        return {"peer": self.peer}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1848369232, signed=False)
        writer.write(bytes(self.peer))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        return cls(peer)

@register
class MessagesEditChatAbout(TLObject):
    CONSTRUCTOR_ID = 3740665751
    __slots__ = ('peer', 'about')
    def __init__(self, peer: 'InputPeer', about: str):
        self.peer = peer
        self.about = about
    def to_dict(self):
        return {"peer": self.peer, "about": self.about}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3740665751, signed=False)
        writer.write(bytes(self.peer))
        writer.write_string(self.about)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        about = reader.read_string()
        return cls(peer, about)

@register
class MessagesEditChatDefaultBannedRights(TLObject):
    CONSTRUCTOR_ID = 2777049921
    __slots__ = ('peer', 'banned_rights')
    def __init__(self, peer: 'InputPeer', banned_rights: 'ChatBannedRights'):
        self.peer = peer
        self.banned_rights = banned_rights
    def to_dict(self):
        return {"peer": self.peer, "banned_rights": self.banned_rights}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2777049921, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.banned_rights))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        banned_rights = reader.tgread_object()
        return cls(peer, banned_rights)

@register
class MessagesGetEmojiKeywords(TLObject):
    CONSTRUCTOR_ID = 899735650
    __slots__ = ('lang_code')
    def __init__(self, lang_code: str):
        self.lang_code = lang_code
    def to_dict(self):
        return {"lang_code": self.lang_code}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(899735650, signed=False)
        writer.write_string(self.lang_code)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        lang_code = reader.read_string()
        return cls(lang_code)

@register
class MessagesGetEmojiKeywordsDifference(TLObject):
    CONSTRUCTOR_ID = 352892591
    __slots__ = ('lang_code', 'from_version')
    def __init__(self, lang_code: str, from_version: int):
        self.lang_code = lang_code
        self.from_version = from_version
    def to_dict(self):
        return {"lang_code": self.lang_code, "from_version": self.from_version}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(352892591, signed=False)
        writer.write_string(self.lang_code)
        writer.write_int(self.from_version, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        lang_code = reader.read_string()
        from_version = reader.read_int()
        return cls(lang_code, from_version)

@register
class MessagesGetEmojiKeywordsLanguages(TLObject):
    CONSTRUCTOR_ID = 1318675378
    __slots__ = ('lang_codes')
    def __init__(self, lang_codes: 'Vector'):
        self.lang_codes = lang_codes
    def to_dict(self):
        return {"lang_codes": self.lang_codes}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1318675378, signed=False)
        writer.write(bytes(self.lang_codes))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        lang_codes = reader.tgread_object()
        return cls(lang_codes)

@register
class MessagesGetEmojiURL(TLObject):
    CONSTRUCTOR_ID = 3585149990
    __slots__ = ('lang_code')
    def __init__(self, lang_code: str):
        self.lang_code = lang_code
    def to_dict(self):
        return {"lang_code": self.lang_code}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3585149990, signed=False)
        writer.write_string(self.lang_code)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        lang_code = reader.read_string()
        return cls(lang_code)

@register
class MessagesGetSearchCounters(TLObject):
    CONSTRUCTOR_ID = 465367808
    __slots__ = ('peer', 'saved_peer_id', 'top_msg_id', 'filters')
    def __init__(self, peer: 'InputPeer', filters: 'Vector', saved_peer_id: 'InputPeer' = None, top_msg_id: int = None):
        self.peer = peer
        self.saved_peer_id = saved_peer_id
        self.top_msg_id = top_msg_id
        self.filters = filters
    def to_dict(self):
        return {"peer": self.peer, "saved_peer_id": self.saved_peer_id, "top_msg_id": self.top_msg_id, "filters": self.filters}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(465367808, signed=False)
        flags = 0
        if self.saved_peer_id is not None: flags |= 1 << 2
        if self.top_msg_id is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        if flags & (1 << 2):
            writer.write(bytes(self.saved_peer_id))
        if flags & (1 << 0):
            writer.write_int(self.top_msg_id, signed=True)
        writer.write(bytes(self.filters))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        peer = reader.tgread_object()
        if flags & (1 << 2):
            saved_peer_id = reader.tgread_object()
        else:
            saved_peer_id = None
        if flags & (1 << 0):
            top_msg_id = reader.read_int()
        else:
            top_msg_id = None
        filters = reader.tgread_object()
        return cls(peer, saved_peer_id, top_msg_id, filters)

@register
class MessagesRequestUrlAuth(TLObject):
    CONSTRUCTOR_ID = 2303510940
    __slots__ = ('peer', 'msg_id', 'button_id', 'url', 'in_app_origin')
    def __init__(self, peer: 'InputPeer' = None, msg_id: int = None, button_id: int = None, url: str = None, in_app_origin: str = None):
        self.peer = peer
        self.msg_id = msg_id
        self.button_id = button_id
        self.url = url
        self.in_app_origin = in_app_origin
    def to_dict(self):
        return {"peer": self.peer, "msg_id": self.msg_id, "button_id": self.button_id, "url": self.url, "in_app_origin": self.in_app_origin}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2303510940, signed=False)
        flags = 0
        if self.peer is not None: flags |= 1 << 1
        if self.msg_id is not None: flags |= 1 << 1
        if self.button_id is not None: flags |= 1 << 1
        if self.url is not None: flags |= 1 << 2
        if self.in_app_origin is not None: flags |= 1 << 3
        writer.write_int(flags, signed=False)
        if flags & (1 << 1):
            writer.write(bytes(self.peer))
        if flags & (1 << 1):
            writer.write_int(self.msg_id, signed=True)
        if flags & (1 << 1):
            writer.write_int(self.button_id, signed=True)
        if flags & (1 << 2):
            writer.write_string(self.url)
        if flags & (1 << 3):
            writer.write_string(self.in_app_origin)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        if flags & (1 << 1):
            peer = reader.tgread_object()
        else:
            peer = None
        if flags & (1 << 1):
            msg_id = reader.read_int()
        else:
            msg_id = None
        if flags & (1 << 1):
            button_id = reader.read_int()
        else:
            button_id = None
        if flags & (1 << 2):
            url = reader.read_string()
        else:
            url = None
        if flags & (1 << 3):
            in_app_origin = reader.read_string()
        else:
            in_app_origin = None
        return cls(peer, msg_id, button_id, url, in_app_origin)

@register
class MessagesAcceptUrlAuth(TLObject):
    CONSTRUCTOR_ID = 1738797278
    __slots__ = ('write_allowed', 'share_phone_number', 'peer', 'msg_id', 'button_id', 'url', 'match_code')
    def __init__(self, write_allowed: bool = None, share_phone_number: bool = None, peer: 'InputPeer' = None, msg_id: int = None, button_id: int = None, url: str = None, match_code: str = None):
        self.write_allowed = write_allowed
        self.share_phone_number = share_phone_number
        self.peer = peer
        self.msg_id = msg_id
        self.button_id = button_id
        self.url = url
        self.match_code = match_code
    def to_dict(self):
        return {"write_allowed": self.write_allowed, "share_phone_number": self.share_phone_number, "peer": self.peer, "msg_id": self.msg_id, "button_id": self.button_id, "url": self.url, "match_code": self.match_code}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1738797278, signed=False)
        flags = 0
        if self.write_allowed: flags |= 1 << 0
        if self.share_phone_number: flags |= 1 << 3
        if self.peer is not None: flags |= 1 << 1
        if self.msg_id is not None: flags |= 1 << 1
        if self.button_id is not None: flags |= 1 << 1
        if self.url is not None: flags |= 1 << 2
        if self.match_code is not None: flags |= 1 << 4
        writer.write_int(flags, signed=False)
        if flags & (1 << 1):
            writer.write(bytes(self.peer))
        if flags & (1 << 1):
            writer.write_int(self.msg_id, signed=True)
        if flags & (1 << 1):
            writer.write_int(self.button_id, signed=True)
        if flags & (1 << 2):
            writer.write_string(self.url)
        if flags & (1 << 4):
            writer.write_string(self.match_code)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        write_allowed = bool(flags & (1 << 0))
        share_phone_number = bool(flags & (1 << 3))
        if flags & (1 << 1):
            peer = reader.tgread_object()
        else:
            peer = None
        if flags & (1 << 1):
            msg_id = reader.read_int()
        else:
            msg_id = None
        if flags & (1 << 1):
            button_id = reader.read_int()
        else:
            button_id = None
        if flags & (1 << 2):
            url = reader.read_string()
        else:
            url = None
        if flags & (1 << 4):
            match_code = reader.read_string()
        else:
            match_code = None
        return cls(write_allowed, share_phone_number, peer, msg_id, button_id, url, match_code)

@register
class MessagesHidePeerSettingsBar(TLObject):
    CONSTRUCTOR_ID = 1336717624
    __slots__ = ('peer')
    def __init__(self, peer: 'InputPeer'):
        self.peer = peer
    def to_dict(self):
        return {"peer": self.peer}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1336717624, signed=False)
        writer.write(bytes(self.peer))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        return cls(peer)

@register
class MessagesGetScheduledHistory(TLObject):
    CONSTRUCTOR_ID = 4111889931
    __slots__ = ('peer', 'hash')
    def __init__(self, peer: 'InputPeer', hash: int):
        self.peer = peer
        self.hash = hash
    def to_dict(self):
        return {"peer": self.peer, "hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4111889931, signed=False)
        writer.write(bytes(self.peer))
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        hash = reader.read_long()
        return cls(peer, hash)

@register
class MessagesGetScheduledMessages(TLObject):
    CONSTRUCTOR_ID = 3183150180
    __slots__ = ('peer', 'id')
    def __init__(self, peer: 'InputPeer', id: 'Vector'):
        self.peer = peer
        self.id = id
    def to_dict(self):
        return {"peer": self.peer, "id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3183150180, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        id = reader.tgread_object()
        return cls(peer, id)

@register
class MessagesSendScheduledMessages(TLObject):
    CONSTRUCTOR_ID = 3174597898
    __slots__ = ('peer', 'id')
    def __init__(self, peer: 'InputPeer', id: 'Vector'):
        self.peer = peer
        self.id = id
    def to_dict(self):
        return {"peer": self.peer, "id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3174597898, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        id = reader.tgread_object()
        return cls(peer, id)

@register
class MessagesDeleteScheduledMessages(TLObject):
    CONSTRUCTOR_ID = 1504586518
    __slots__ = ('peer', 'id')
    def __init__(self, peer: 'InputPeer', id: 'Vector'):
        self.peer = peer
        self.id = id
    def to_dict(self):
        return {"peer": self.peer, "id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1504586518, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        id = reader.tgread_object()
        return cls(peer, id)

@register
class MessagesGetPollVotes(TLObject):
    CONSTRUCTOR_ID = 3094231054
    __slots__ = ('peer', 'id', 'option', 'offset', 'limit')
    def __init__(self, peer: 'InputPeer', id: int, limit: int, option: bytes = None, offset: str = None):
        self.peer = peer
        self.id = id
        self.option = option
        self.offset = offset
        self.limit = limit
    def to_dict(self):
        return {"peer": self.peer, "id": self.id, "option": self.option, "offset": self.offset, "limit": self.limit}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3094231054, signed=False)
        flags = 0
        if self.option is not None: flags |= 1 << 0
        if self.offset is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.id, signed=True)
        if flags & (1 << 0):
            writer.write_bytes(self.option)
        if flags & (1 << 1):
            writer.write_string(self.offset)
        writer.write_int(self.limit, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        peer = reader.tgread_object()
        id = reader.read_int()
        if flags & (1 << 0):
            option = reader.read_bytes()
        else:
            option = None
        if flags & (1 << 1):
            offset = reader.read_string()
        else:
            offset = None
        limit = reader.read_int()
        return cls(peer, id, option, offset, limit)

@register
class MessagesToggleStickerSets(TLObject):
    CONSTRUCTOR_ID = 3037016042
    __slots__ = ('uninstall', 'archive', 'unarchive', 'stickersets')
    def __init__(self, stickersets: 'Vector', uninstall: bool = None, archive: bool = None, unarchive: bool = None):
        self.uninstall = uninstall
        self.archive = archive
        self.unarchive = unarchive
        self.stickersets = stickersets
    def to_dict(self):
        return {"uninstall": self.uninstall, "archive": self.archive, "unarchive": self.unarchive, "stickersets": self.stickersets}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3037016042, signed=False)
        flags = 0
        if self.uninstall: flags |= 1 << 0
        if self.archive: flags |= 1 << 1
        if self.unarchive: flags |= 1 << 2
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.stickersets))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        uninstall = bool(flags & (1 << 0))
        archive = bool(flags & (1 << 1))
        unarchive = bool(flags & (1 << 2))
        stickersets = reader.tgread_object()
        return cls(uninstall, archive, unarchive, stickersets)

@register
class MessagesGetDialogFilters(TLObject):
    CONSTRUCTOR_ID = 4023684233
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4023684233, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class MessagesGetSuggestedDialogFilters(TLObject):
    CONSTRUCTOR_ID = 2728186924
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2728186924, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class MessagesUpdateDialogFilter(TLObject):
    CONSTRUCTOR_ID = 450142282
    __slots__ = ('id', 'filter')
    def __init__(self, id: int, filter: 'DialogFilter' = None):
        self.id = id
        self.filter = filter
    def to_dict(self):
        return {"id": self.id, "filter": self.filter}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(450142282, signed=False)
        flags = 0
        if self.filter is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write_int(self.id, signed=True)
        if flags & (1 << 0):
            writer.write(bytes(self.filter))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        id = reader.read_int()
        if flags & (1 << 0):
            filter = reader.tgread_object()
        else:
            filter = None
        return cls(id, filter)

@register
class MessagesUpdateDialogFiltersOrder(TLObject):
    CONSTRUCTOR_ID = 3311649252
    __slots__ = ('order')
    def __init__(self, order: 'Vector'):
        self.order = order
    def to_dict(self):
        return {"order": self.order}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3311649252, signed=False)
        writer.write(bytes(self.order))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        order = reader.tgread_object()
        return cls(order)

@register
class MessagesGetOldFeaturedStickers(TLObject):
    CONSTRUCTOR_ID = 2127598753
    __slots__ = ('offset', 'limit', 'hash')
    def __init__(self, offset: int, limit: int, hash: int):
        self.offset = offset
        self.limit = limit
        self.hash = hash
    def to_dict(self):
        return {"offset": self.offset, "limit": self.limit, "hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2127598753, signed=False)
        writer.write_int(self.offset, signed=True)
        writer.write_int(self.limit, signed=True)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        offset = reader.read_int()
        limit = reader.read_int()
        hash = reader.read_long()
        return cls(offset, limit, hash)

@register
class MessagesGetReplies(TLObject):
    CONSTRUCTOR_ID = 584962828
    __slots__ = ('peer', 'msg_id', 'offset_id', 'offset_date', 'add_offset', 'limit', 'max_id', 'min_id', 'hash')
    def __init__(self, peer: 'InputPeer', msg_id: int, offset_id: int, offset_date: int, add_offset: int, limit: int, max_id: int, min_id: int, hash: int):
        self.peer = peer
        self.msg_id = msg_id
        self.offset_id = offset_id
        self.offset_date = offset_date
        self.add_offset = add_offset
        self.limit = limit
        self.max_id = max_id
        self.min_id = min_id
        self.hash = hash
    def to_dict(self):
        return {"peer": self.peer, "msg_id": self.msg_id, "offset_id": self.offset_id, "offset_date": self.offset_date, "add_offset": self.add_offset, "limit": self.limit, "max_id": self.max_id, "min_id": self.min_id, "hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(584962828, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.msg_id, signed=True)
        writer.write_int(self.offset_id, signed=True)
        writer.write_int(self.offset_date, signed=True)
        writer.write_int(self.add_offset, signed=True)
        writer.write_int(self.limit, signed=True)
        writer.write_int(self.max_id, signed=True)
        writer.write_int(self.min_id, signed=True)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        msg_id = reader.read_int()
        offset_id = reader.read_int()
        offset_date = reader.read_int()
        add_offset = reader.read_int()
        limit = reader.read_int()
        max_id = reader.read_int()
        min_id = reader.read_int()
        hash = reader.read_long()
        return cls(peer, msg_id, offset_id, offset_date, add_offset, limit, max_id, min_id, hash)

@register
class MessagesGetDiscussionMessage(TLObject):
    CONSTRUCTOR_ID = 1147761405
    __slots__ = ('peer', 'msg_id')
    def __init__(self, peer: 'InputPeer', msg_id: int):
        self.peer = peer
        self.msg_id = msg_id
    def to_dict(self):
        return {"peer": self.peer, "msg_id": self.msg_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1147761405, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.msg_id, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        msg_id = reader.read_int()
        return cls(peer, msg_id)

@register
class MessagesReadDiscussion(TLObject):
    CONSTRUCTOR_ID = 4147227124
    __slots__ = ('peer', 'msg_id', 'read_max_id')
    def __init__(self, peer: 'InputPeer', msg_id: int, read_max_id: int):
        self.peer = peer
        self.msg_id = msg_id
        self.read_max_id = read_max_id
    def to_dict(self):
        return {"peer": self.peer, "msg_id": self.msg_id, "read_max_id": self.read_max_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4147227124, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.msg_id, signed=True)
        writer.write_int(self.read_max_id, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        msg_id = reader.read_int()
        read_max_id = reader.read_int()
        return cls(peer, msg_id, read_max_id)

@register
class MessagesUnpinAllMessages(TLObject):
    CONSTRUCTOR_ID = 103667527
    __slots__ = ('peer', 'top_msg_id', 'saved_peer_id')
    def __init__(self, peer: 'InputPeer', top_msg_id: int = None, saved_peer_id: 'InputPeer' = None):
        self.peer = peer
        self.top_msg_id = top_msg_id
        self.saved_peer_id = saved_peer_id
    def to_dict(self):
        return {"peer": self.peer, "top_msg_id": self.top_msg_id, "saved_peer_id": self.saved_peer_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(103667527, signed=False)
        flags = 0
        if self.top_msg_id is not None: flags |= 1 << 0
        if self.saved_peer_id is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        if flags & (1 << 0):
            writer.write_int(self.top_msg_id, signed=True)
        if flags & (1 << 1):
            writer.write(bytes(self.saved_peer_id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        peer = reader.tgread_object()
        if flags & (1 << 0):
            top_msg_id = reader.read_int()
        else:
            top_msg_id = None
        if flags & (1 << 1):
            saved_peer_id = reader.tgread_object()
        else:
            saved_peer_id = None
        return cls(peer, top_msg_id, saved_peer_id)

@register
class MessagesDeleteChat(TLObject):
    CONSTRUCTOR_ID = 1540419152
    __slots__ = ('chat_id')
    def __init__(self, chat_id: int):
        self.chat_id = chat_id
    def to_dict(self):
        return {"chat_id": self.chat_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1540419152, signed=False)
        writer.write_long(self.chat_id, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        chat_id = reader.read_long()
        return cls(chat_id)

@register
class MessagesDeletePhoneCallHistory(TLObject):
    CONSTRUCTOR_ID = 4190888969
    __slots__ = ('revoke')
    def __init__(self, revoke: bool = None):
        self.revoke = revoke
    def to_dict(self):
        return {"revoke": self.revoke}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4190888969, signed=False)
        flags = 0
        if self.revoke: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        revoke = bool(flags & (1 << 0))
        return cls(revoke)

@register
class MessagesCheckHistoryImport(TLObject):
    CONSTRUCTOR_ID = 1140726259
    __slots__ = ('import_head')
    def __init__(self, import_head: str):
        self.import_head = import_head
    def to_dict(self):
        return {"import_head": self.import_head}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1140726259, signed=False)
        writer.write_string(self.import_head)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        import_head = reader.read_string()
        return cls(import_head)

@register
class MessagesInitHistoryImport(TLObject):
    CONSTRUCTOR_ID = 873008187
    __slots__ = ('peer', 'file', 'media_count')
    def __init__(self, peer: 'InputPeer', file: 'InputFile', media_count: int):
        self.peer = peer
        self.file = file
        self.media_count = media_count
    def to_dict(self):
        return {"peer": self.peer, "file": self.file, "media_count": self.media_count}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(873008187, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.file))
        writer.write_int(self.media_count, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        file = reader.tgread_object()
        media_count = reader.read_int()
        return cls(peer, file, media_count)

@register
class MessagesUploadImportedMedia(TLObject):
    CONSTRUCTOR_ID = 713433234
    __slots__ = ('peer', 'import_id', 'file_name', 'media')
    def __init__(self, peer: 'InputPeer', import_id: int, file_name: str, media: 'InputMedia'):
        self.peer = peer
        self.import_id = import_id
        self.file_name = file_name
        self.media = media
    def to_dict(self):
        return {"peer": self.peer, "import_id": self.import_id, "file_name": self.file_name, "media": self.media}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(713433234, signed=False)
        writer.write(bytes(self.peer))
        writer.write_long(self.import_id, signed=False)
        writer.write_string(self.file_name)
        writer.write(bytes(self.media))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        import_id = reader.read_long()
        file_name = reader.read_string()
        media = reader.tgread_object()
        return cls(peer, import_id, file_name, media)

@register
class MessagesStartHistoryImport(TLObject):
    CONSTRUCTOR_ID = 3023958852
    __slots__ = ('peer', 'import_id')
    def __init__(self, peer: 'InputPeer', import_id: int):
        self.peer = peer
        self.import_id = import_id
    def to_dict(self):
        return {"peer": self.peer, "import_id": self.import_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3023958852, signed=False)
        writer.write(bytes(self.peer))
        writer.write_long(self.import_id, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        import_id = reader.read_long()
        return cls(peer, import_id)

@register
class MessagesGetExportedChatInvites(TLObject):
    CONSTRUCTOR_ID = 2729812982
    __slots__ = ('revoked', 'peer', 'admin_id', 'offset_date', 'offset_link', 'limit')
    def __init__(self, peer: 'InputPeer', admin_id: 'InputUser', limit: int, revoked: bool = None, offset_date: int = None, offset_link: str = None):
        self.revoked = revoked
        self.peer = peer
        self.admin_id = admin_id
        self.offset_date = offset_date
        self.offset_link = offset_link
        self.limit = limit
    def to_dict(self):
        return {"revoked": self.revoked, "peer": self.peer, "admin_id": self.admin_id, "offset_date": self.offset_date, "offset_link": self.offset_link, "limit": self.limit}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2729812982, signed=False)
        flags = 0
        if self.revoked: flags |= 1 << 3
        if self.offset_date is not None: flags |= 1 << 2
        if self.offset_link is not None: flags |= 1 << 2
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.admin_id))
        if flags & (1 << 2):
            writer.write_int(self.offset_date, signed=True)
        if flags & (1 << 2):
            writer.write_string(self.offset_link)
        writer.write_int(self.limit, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        revoked = bool(flags & (1 << 3))
        peer = reader.tgread_object()
        admin_id = reader.tgread_object()
        if flags & (1 << 2):
            offset_date = reader.read_int()
        else:
            offset_date = None
        if flags & (1 << 2):
            offset_link = reader.read_string()
        else:
            offset_link = None
        limit = reader.read_int()
        return cls(revoked, peer, admin_id, offset_date, offset_link, limit)

@register
class MessagesGetExportedChatInvite(TLObject):
    CONSTRUCTOR_ID = 1937010524
    __slots__ = ('peer', 'link')
    def __init__(self, peer: 'InputPeer', link: str):
        self.peer = peer
        self.link = link
    def to_dict(self):
        return {"peer": self.peer, "link": self.link}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1937010524, signed=False)
        writer.write(bytes(self.peer))
        writer.write_string(self.link)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        link = reader.read_string()
        return cls(peer, link)

@register
class MessagesEditExportedChatInvite(TLObject):
    CONSTRUCTOR_ID = 3184144245
    __slots__ = ('revoked', 'peer', 'link', 'expire_date', 'usage_limit', 'request_needed', 'title')
    def __init__(self, peer: 'InputPeer', link: str, revoked: bool = None, expire_date: int = None, usage_limit: int = None, request_needed: bool = None, title: str = None):
        self.revoked = revoked
        self.peer = peer
        self.link = link
        self.expire_date = expire_date
        self.usage_limit = usage_limit
        self.request_needed = request_needed
        self.title = title
    def to_dict(self):
        return {"revoked": self.revoked, "peer": self.peer, "link": self.link, "expire_date": self.expire_date, "usage_limit": self.usage_limit, "request_needed": self.request_needed, "title": self.title}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3184144245, signed=False)
        flags = 0
        if self.revoked: flags |= 1 << 2
        if self.expire_date is not None: flags |= 1 << 0
        if self.usage_limit is not None: flags |= 1 << 1
        if self.request_needed is not None: flags |= 1 << 3
        if self.title is not None: flags |= 1 << 4
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write_string(self.link)
        if flags & (1 << 0):
            writer.write_int(self.expire_date, signed=True)
        if flags & (1 << 1):
            writer.write_int(self.usage_limit, signed=True)
        if flags & (1 << 3):
            writer.write(serialize_bool(self.request_needed))
        if flags & (1 << 4):
            writer.write_string(self.title)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        revoked = bool(flags & (1 << 2))
        peer = reader.tgread_object()
        link = reader.read_string()
        if flags & (1 << 0):
            expire_date = reader.read_int()
        else:
            expire_date = None
        if flags & (1 << 1):
            usage_limit = reader.read_int()
        else:
            usage_limit = None
        if flags & (1 << 3):
            request_needed = reader.tgread_bool()
        else:
            request_needed = None
        if flags & (1 << 4):
            title = reader.read_string()
        else:
            title = None
        return cls(revoked, peer, link, expire_date, usage_limit, request_needed, title)

@register
class MessagesDeleteRevokedExportedChatInvites(TLObject):
    CONSTRUCTOR_ID = 1452833749
    __slots__ = ('peer', 'admin_id')
    def __init__(self, peer: 'InputPeer', admin_id: 'InputUser'):
        self.peer = peer
        self.admin_id = admin_id
    def to_dict(self):
        return {"peer": self.peer, "admin_id": self.admin_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1452833749, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.admin_id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        admin_id = reader.tgread_object()
        return cls(peer, admin_id)

@register
class MessagesDeleteExportedChatInvite(TLObject):
    CONSTRUCTOR_ID = 3563365419
    __slots__ = ('peer', 'link')
    def __init__(self, peer: 'InputPeer', link: str):
        self.peer = peer
        self.link = link
    def to_dict(self):
        return {"peer": self.peer, "link": self.link}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3563365419, signed=False)
        writer.write(bytes(self.peer))
        writer.write_string(self.link)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        link = reader.read_string()
        return cls(peer, link)

@register
class MessagesGetAdminsWithInvites(TLObject):
    CONSTRUCTOR_ID = 958457583
    __slots__ = ('peer')
    def __init__(self, peer: 'InputPeer'):
        self.peer = peer
    def to_dict(self):
        return {"peer": self.peer}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(958457583, signed=False)
        writer.write(bytes(self.peer))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        return cls(peer)

@register
class MessagesGetChatInviteImporters(TLObject):
    CONSTRUCTOR_ID = 3741637966
    __slots__ = ('requested', 'subscription_expired', 'peer', 'link', 'q', 'offset_date', 'offset_user', 'limit')
    def __init__(self, peer: 'InputPeer', offset_date: int, offset_user: 'InputUser', limit: int, requested: bool = None, subscription_expired: bool = None, link: str = None, q: str = None):
        self.requested = requested
        self.subscription_expired = subscription_expired
        self.peer = peer
        self.link = link
        self.q = q
        self.offset_date = offset_date
        self.offset_user = offset_user
        self.limit = limit
    def to_dict(self):
        return {"requested": self.requested, "subscription_expired": self.subscription_expired, "peer": self.peer, "link": self.link, "q": self.q, "offset_date": self.offset_date, "offset_user": self.offset_user, "limit": self.limit}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3741637966, signed=False)
        flags = 0
        if self.requested: flags |= 1 << 0
        if self.subscription_expired: flags |= 1 << 3
        if self.link is not None: flags |= 1 << 1
        if self.q is not None: flags |= 1 << 2
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        if flags & (1 << 1):
            writer.write_string(self.link)
        if flags & (1 << 2):
            writer.write_string(self.q)
        writer.write_int(self.offset_date, signed=True)
        writer.write(bytes(self.offset_user))
        writer.write_int(self.limit, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        requested = bool(flags & (1 << 0))
        subscription_expired = bool(flags & (1 << 3))
        peer = reader.tgread_object()
        if flags & (1 << 1):
            link = reader.read_string()
        else:
            link = None
        if flags & (1 << 2):
            q = reader.read_string()
        else:
            q = None
        offset_date = reader.read_int()
        offset_user = reader.tgread_object()
        limit = reader.read_int()
        return cls(requested, subscription_expired, peer, link, q, offset_date, offset_user, limit)

@register
class MessagesSetHistoryTTL(TLObject):
    CONSTRUCTOR_ID = 3087949796
    __slots__ = ('peer', 'period')
    def __init__(self, peer: 'InputPeer', period: int):
        self.peer = peer
        self.period = period
    def to_dict(self):
        return {"peer": self.peer, "period": self.period}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3087949796, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.period, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        period = reader.read_int()
        return cls(peer, period)

@register
class MessagesCheckHistoryImportPeer(TLObject):
    CONSTRUCTOR_ID = 1573261059
    __slots__ = ('peer')
    def __init__(self, peer: 'InputPeer'):
        self.peer = peer
    def to_dict(self):
        return {"peer": self.peer}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1573261059, signed=False)
        writer.write(bytes(self.peer))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        return cls(peer)

@register
class MessagesSetChatTheme(TLObject):
    CONSTRUCTOR_ID = 135398089
    __slots__ = ('peer', 'theme')
    def __init__(self, peer: 'InputPeer', theme: 'InputChatTheme'):
        self.peer = peer
        self.theme = theme
    def to_dict(self):
        return {"peer": self.peer, "theme": self.theme}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(135398089, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.theme))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        theme = reader.tgread_object()
        return cls(peer, theme)

@register
class MessagesGetMessageReadParticipants(TLObject):
    CONSTRUCTOR_ID = 834782287
    __slots__ = ('peer', 'msg_id')
    def __init__(self, peer: 'InputPeer', msg_id: int):
        self.peer = peer
        self.msg_id = msg_id
    def to_dict(self):
        return {"peer": self.peer, "msg_id": self.msg_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(834782287, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.msg_id, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        msg_id = reader.read_int()
        return cls(peer, msg_id)

@register
class MessagesGetSearchResultsCalendar(TLObject):
    CONSTRUCTOR_ID = 1789130429
    __slots__ = ('peer', 'saved_peer_id', 'filter', 'offset_id', 'offset_date')
    def __init__(self, peer: 'InputPeer', filter: 'MessagesFilter', offset_id: int, offset_date: int, saved_peer_id: 'InputPeer' = None):
        self.peer = peer
        self.saved_peer_id = saved_peer_id
        self.filter = filter
        self.offset_id = offset_id
        self.offset_date = offset_date
    def to_dict(self):
        return {"peer": self.peer, "saved_peer_id": self.saved_peer_id, "filter": self.filter, "offset_id": self.offset_id, "offset_date": self.offset_date}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1789130429, signed=False)
        flags = 0
        if self.saved_peer_id is not None: flags |= 1 << 2
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        if flags & (1 << 2):
            writer.write(bytes(self.saved_peer_id))
        writer.write(bytes(self.filter))
        writer.write_int(self.offset_id, signed=True)
        writer.write_int(self.offset_date, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        peer = reader.tgread_object()
        if flags & (1 << 2):
            saved_peer_id = reader.tgread_object()
        else:
            saved_peer_id = None
        filter = reader.tgread_object()
        offset_id = reader.read_int()
        offset_date = reader.read_int()
        return cls(peer, saved_peer_id, filter, offset_id, offset_date)

@register
class MessagesGetSearchResultsPositions(TLObject):
    CONSTRUCTOR_ID = 2625580816
    __slots__ = ('peer', 'saved_peer_id', 'filter', 'offset_id', 'limit')
    def __init__(self, peer: 'InputPeer', filter: 'MessagesFilter', offset_id: int, limit: int, saved_peer_id: 'InputPeer' = None):
        self.peer = peer
        self.saved_peer_id = saved_peer_id
        self.filter = filter
        self.offset_id = offset_id
        self.limit = limit
    def to_dict(self):
        return {"peer": self.peer, "saved_peer_id": self.saved_peer_id, "filter": self.filter, "offset_id": self.offset_id, "limit": self.limit}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2625580816, signed=False)
        flags = 0
        if self.saved_peer_id is not None: flags |= 1 << 2
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        if flags & (1 << 2):
            writer.write(bytes(self.saved_peer_id))
        writer.write(bytes(self.filter))
        writer.write_int(self.offset_id, signed=True)
        writer.write_int(self.limit, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        peer = reader.tgread_object()
        if flags & (1 << 2):
            saved_peer_id = reader.tgread_object()
        else:
            saved_peer_id = None
        filter = reader.tgread_object()
        offset_id = reader.read_int()
        limit = reader.read_int()
        return cls(peer, saved_peer_id, filter, offset_id, limit)

@register
class MessagesHideChatJoinRequest(TLObject):
    CONSTRUCTOR_ID = 2145904661
    __slots__ = ('approved', 'peer', 'user_id')
    def __init__(self, peer: 'InputPeer', user_id: 'InputUser', approved: bool = None):
        self.approved = approved
        self.peer = peer
        self.user_id = user_id
    def to_dict(self):
        return {"approved": self.approved, "peer": self.peer, "user_id": self.user_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2145904661, signed=False)
        flags = 0
        if self.approved: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.user_id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        approved = bool(flags & (1 << 0))
        peer = reader.tgread_object()
        user_id = reader.tgread_object()
        return cls(approved, peer, user_id)

@register
class MessagesHideAllChatJoinRequests(TLObject):
    CONSTRUCTOR_ID = 3766875370
    __slots__ = ('approved', 'peer', 'link')
    def __init__(self, peer: 'InputPeer', approved: bool = None, link: str = None):
        self.approved = approved
        self.peer = peer
        self.link = link
    def to_dict(self):
        return {"approved": self.approved, "peer": self.peer, "link": self.link}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3766875370, signed=False)
        flags = 0
        if self.approved: flags |= 1 << 0
        if self.link is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        if flags & (1 << 1):
            writer.write_string(self.link)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        approved = bool(flags & (1 << 0))
        peer = reader.tgread_object()
        if flags & (1 << 1):
            link = reader.read_string()
        else:
            link = None
        return cls(approved, peer, link)

@register
class MessagesToggleNoForwards(TLObject):
    CONSTRUCTOR_ID = 2986875445
    __slots__ = ('peer', 'enabled', 'request_msg_id')
    def __init__(self, peer: 'InputPeer', enabled: bool, request_msg_id: int = None):
        self.peer = peer
        self.enabled = enabled
        self.request_msg_id = request_msg_id
    def to_dict(self):
        return {"peer": self.peer, "enabled": self.enabled, "request_msg_id": self.request_msg_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2986875445, signed=False)
        flags = 0
        if self.request_msg_id is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write(serialize_bool(self.enabled))
        if flags & (1 << 0):
            writer.write_int(self.request_msg_id, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        peer = reader.tgread_object()
        enabled = reader.tgread_bool()
        if flags & (1 << 0):
            request_msg_id = reader.read_int()
        else:
            request_msg_id = None
        return cls(peer, enabled, request_msg_id)

@register
class MessagesSaveDefaultSendAs(TLObject):
    CONSTRUCTOR_ID = 3439189910
    __slots__ = ('peer', 'send_as')
    def __init__(self, peer: 'InputPeer', send_as: 'InputPeer'):
        self.peer = peer
        self.send_as = send_as
    def to_dict(self):
        return {"peer": self.peer, "send_as": self.send_as}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3439189910, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.send_as))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        send_as = reader.tgread_object()
        return cls(peer, send_as)

@register
class MessagesSendReaction(TLObject):
    CONSTRUCTOR_ID = 3540875476
    __slots__ = ('big', 'add_to_recent', 'peer', 'msg_id', 'reaction')
    def __init__(self, peer: 'InputPeer', msg_id: int, big: bool = None, add_to_recent: bool = None, reaction: 'Vector' = None):
        self.big = big
        self.add_to_recent = add_to_recent
        self.peer = peer
        self.msg_id = msg_id
        self.reaction = reaction
    def to_dict(self):
        return {"big": self.big, "add_to_recent": self.add_to_recent, "peer": self.peer, "msg_id": self.msg_id, "reaction": self.reaction}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3540875476, signed=False)
        flags = 0
        if self.big: flags |= 1 << 1
        if self.add_to_recent: flags |= 1 << 2
        if self.reaction is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.msg_id, signed=True)
        if flags & (1 << 0):
            writer.write(bytes(self.reaction))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        big = bool(flags & (1 << 1))
        add_to_recent = bool(flags & (1 << 2))
        peer = reader.tgread_object()
        msg_id = reader.read_int()
        if flags & (1 << 0):
            reaction = reader.tgread_object()
        else:
            reaction = None
        return cls(big, add_to_recent, peer, msg_id, reaction)

@register
class MessagesGetMessagesReactions(TLObject):
    CONSTRUCTOR_ID = 2344259814
    __slots__ = ('peer', 'id')
    def __init__(self, peer: 'InputPeer', id: 'Vector'):
        self.peer = peer
        self.id = id
    def to_dict(self):
        return {"peer": self.peer, "id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2344259814, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        id = reader.tgread_object()
        return cls(peer, id)

@register
class MessagesGetMessageReactionsList(TLObject):
    CONSTRUCTOR_ID = 1176190792
    __slots__ = ('peer', 'id', 'reaction', 'offset', 'limit')
    def __init__(self, peer: 'InputPeer', id: int, limit: int, reaction: 'Reaction' = None, offset: str = None):
        self.peer = peer
        self.id = id
        self.reaction = reaction
        self.offset = offset
        self.limit = limit
    def to_dict(self):
        return {"peer": self.peer, "id": self.id, "reaction": self.reaction, "offset": self.offset, "limit": self.limit}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1176190792, signed=False)
        flags = 0
        if self.reaction is not None: flags |= 1 << 0
        if self.offset is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.id, signed=True)
        if flags & (1 << 0):
            writer.write(bytes(self.reaction))
        if flags & (1 << 1):
            writer.write_string(self.offset)
        writer.write_int(self.limit, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        peer = reader.tgread_object()
        id = reader.read_int()
        if flags & (1 << 0):
            reaction = reader.tgread_object()
        else:
            reaction = None
        if flags & (1 << 1):
            offset = reader.read_string()
        else:
            offset = None
        limit = reader.read_int()
        return cls(peer, id, reaction, offset, limit)

@register
class MessagesSetChatAvailableReactions(TLObject):
    CONSTRUCTOR_ID = 2253071745
    __slots__ = ('peer', 'available_reactions', 'reactions_limit', 'paid_enabled')
    def __init__(self, peer: 'InputPeer', available_reactions: 'ChatReactions', reactions_limit: int = None, paid_enabled: bool = None):
        self.peer = peer
        self.available_reactions = available_reactions
        self.reactions_limit = reactions_limit
        self.paid_enabled = paid_enabled
    def to_dict(self):
        return {"peer": self.peer, "available_reactions": self.available_reactions, "reactions_limit": self.reactions_limit, "paid_enabled": self.paid_enabled}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2253071745, signed=False)
        flags = 0
        if self.reactions_limit is not None: flags |= 1 << 0
        if self.paid_enabled is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.available_reactions))
        if flags & (1 << 0):
            writer.write_int(self.reactions_limit, signed=True)
        if flags & (1 << 1):
            writer.write(serialize_bool(self.paid_enabled))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        peer = reader.tgread_object()
        available_reactions = reader.tgread_object()
        if flags & (1 << 0):
            reactions_limit = reader.read_int()
        else:
            reactions_limit = None
        if flags & (1 << 1):
            paid_enabled = reader.tgread_bool()
        else:
            paid_enabled = None
        return cls(peer, available_reactions, reactions_limit, paid_enabled)

@register
class MessagesGetAvailableReactions(TLObject):
    CONSTRUCTOR_ID = 417243308
    __slots__ = ('hash')
    def __init__(self, hash: int):
        self.hash = hash
    def to_dict(self):
        return {"hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(417243308, signed=False)
        writer.write_int(self.hash, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_int()
        return cls(hash)

@register
class MessagesSetDefaultReaction(TLObject):
    CONSTRUCTOR_ID = 1330094102
    __slots__ = ('reaction')
    def __init__(self, reaction: 'Reaction'):
        self.reaction = reaction
    def to_dict(self):
        return {"reaction": self.reaction}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1330094102, signed=False)
        writer.write(bytes(self.reaction))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        reaction = reader.tgread_object()
        return cls(reaction)

@register
class MessagesTranslateText(TLObject):
    CONSTRUCTOR_ID = 2783888197
    __slots__ = ('peer', 'id', 'text', 'to_lang', 'tone')
    def __init__(self, to_lang: str, peer: 'InputPeer' = None, id: 'Vector' = None, text: 'Vector' = None, tone: str = None):
        self.peer = peer
        self.id = id
        self.text = text
        self.to_lang = to_lang
        self.tone = tone
    def to_dict(self):
        return {"peer": self.peer, "id": self.id, "text": self.text, "to_lang": self.to_lang, "tone": self.tone}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2783888197, signed=False)
        flags = 0
        if self.peer is not None: flags |= 1 << 0
        if self.id is not None: flags |= 1 << 0
        if self.text is not None: flags |= 1 << 1
        if self.tone is not None: flags |= 1 << 2
        writer.write_int(flags, signed=False)
        if flags & (1 << 0):
            writer.write(bytes(self.peer))
        if flags & (1 << 0):
            writer.write(bytes(self.id))
        if flags & (1 << 1):
            writer.write(bytes(self.text))
        writer.write_string(self.to_lang)
        if flags & (1 << 2):
            writer.write_string(self.tone)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        if flags & (1 << 0):
            peer = reader.tgread_object()
        else:
            peer = None
        if flags & (1 << 0):
            id = reader.tgread_object()
        else:
            id = None
        if flags & (1 << 1):
            text = reader.tgread_object()
        else:
            text = None
        to_lang = reader.read_string()
        if flags & (1 << 2):
            tone = reader.read_string()
        else:
            tone = None
        return cls(peer, id, text, to_lang, tone)

@register
class MessagesGetUnreadReactions(TLObject):
    CONSTRUCTOR_ID = 3179253932
    __slots__ = ('peer', 'top_msg_id', 'saved_peer_id', 'offset_id', 'add_offset', 'limit', 'max_id', 'min_id')
    def __init__(self, peer: 'InputPeer', offset_id: int, add_offset: int, limit: int, max_id: int, min_id: int, top_msg_id: int = None, saved_peer_id: 'InputPeer' = None):
        self.peer = peer
        self.top_msg_id = top_msg_id
        self.saved_peer_id = saved_peer_id
        self.offset_id = offset_id
        self.add_offset = add_offset
        self.limit = limit
        self.max_id = max_id
        self.min_id = min_id
    def to_dict(self):
        return {"peer": self.peer, "top_msg_id": self.top_msg_id, "saved_peer_id": self.saved_peer_id, "offset_id": self.offset_id, "add_offset": self.add_offset, "limit": self.limit, "max_id": self.max_id, "min_id": self.min_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3179253932, signed=False)
        flags = 0
        if self.top_msg_id is not None: flags |= 1 << 0
        if self.saved_peer_id is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        if flags & (1 << 0):
            writer.write_int(self.top_msg_id, signed=True)
        if flags & (1 << 1):
            writer.write(bytes(self.saved_peer_id))
        writer.write_int(self.offset_id, signed=True)
        writer.write_int(self.add_offset, signed=True)
        writer.write_int(self.limit, signed=True)
        writer.write_int(self.max_id, signed=True)
        writer.write_int(self.min_id, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        peer = reader.tgread_object()
        if flags & (1 << 0):
            top_msg_id = reader.read_int()
        else:
            top_msg_id = None
        if flags & (1 << 1):
            saved_peer_id = reader.tgread_object()
        else:
            saved_peer_id = None
        offset_id = reader.read_int()
        add_offset = reader.read_int()
        limit = reader.read_int()
        max_id = reader.read_int()
        min_id = reader.read_int()
        return cls(peer, top_msg_id, saved_peer_id, offset_id, add_offset, limit, max_id, min_id)

@register
class MessagesReadReactions(TLObject):
    CONSTRUCTOR_ID = 2663665555
    __slots__ = ('peer', 'top_msg_id', 'saved_peer_id')
    def __init__(self, peer: 'InputPeer', top_msg_id: int = None, saved_peer_id: 'InputPeer' = None):
        self.peer = peer
        self.top_msg_id = top_msg_id
        self.saved_peer_id = saved_peer_id
    def to_dict(self):
        return {"peer": self.peer, "top_msg_id": self.top_msg_id, "saved_peer_id": self.saved_peer_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2663665555, signed=False)
        flags = 0
        if self.top_msg_id is not None: flags |= 1 << 0
        if self.saved_peer_id is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        if flags & (1 << 0):
            writer.write_int(self.top_msg_id, signed=True)
        if flags & (1 << 1):
            writer.write(bytes(self.saved_peer_id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        peer = reader.tgread_object()
        if flags & (1 << 0):
            top_msg_id = reader.read_int()
        else:
            top_msg_id = None
        if flags & (1 << 1):
            saved_peer_id = reader.tgread_object()
        else:
            saved_peer_id = None
        return cls(peer, top_msg_id, saved_peer_id)

@register
class MessagesSearchSentMedia(TLObject):
    CONSTRUCTOR_ID = 276705696
    __slots__ = ('q', 'filter', 'limit')
    def __init__(self, q: str, filter: 'MessagesFilter', limit: int):
        self.q = q
        self.filter = filter
        self.limit = limit
    def to_dict(self):
        return {"q": self.q, "filter": self.filter, "limit": self.limit}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(276705696, signed=False)
        writer.write_string(self.q)
        writer.write(bytes(self.filter))
        writer.write_int(self.limit, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        q = reader.read_string()
        filter = reader.tgread_object()
        limit = reader.read_int()
        return cls(q, filter, limit)

@register
class MessagesGetAttachMenuBots(TLObject):
    CONSTRUCTOR_ID = 385663691
    __slots__ = ('hash')
    def __init__(self, hash: int):
        self.hash = hash
    def to_dict(self):
        return {"hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(385663691, signed=False)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_long()
        return cls(hash)

@register
class MessagesGetAttachMenuBot(TLObject):
    CONSTRUCTOR_ID = 1998676370
    __slots__ = ('bot')
    def __init__(self, bot: 'InputUser'):
        self.bot = bot
    def to_dict(self):
        return {"bot": self.bot}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1998676370, signed=False)
        writer.write(bytes(self.bot))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        bot = reader.tgread_object()
        return cls(bot)

@register
class MessagesToggleBotInAttachMenu(TLObject):
    CONSTRUCTOR_ID = 1777704297
    __slots__ = ('write_allowed', 'bot', 'enabled')
    def __init__(self, bot: 'InputUser', enabled: bool, write_allowed: bool = None):
        self.write_allowed = write_allowed
        self.bot = bot
        self.enabled = enabled
    def to_dict(self):
        return {"write_allowed": self.write_allowed, "bot": self.bot, "enabled": self.enabled}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1777704297, signed=False)
        flags = 0
        if self.write_allowed: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.bot))
        writer.write(serialize_bool(self.enabled))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        write_allowed = bool(flags & (1 << 0))
        bot = reader.tgread_object()
        enabled = reader.tgread_bool()
        return cls(write_allowed, bot, enabled)

@register
class MessagesRequestWebView(TLObject):
    CONSTRUCTOR_ID = 647873217
    __slots__ = ('from_bot_menu', 'silent', 'compact', 'fullscreen', 'peer', 'bot', 'url', 'start_param', 'theme_params', 'platform', 'reply_to', 'send_as')
    def __init__(self, peer: 'InputPeer', bot: 'InputUser', platform: str, from_bot_menu: bool = None, silent: bool = None, compact: bool = None, fullscreen: bool = None, url: str = None, start_param: str = None, theme_params: 'DataJSON' = None, reply_to: 'InputReplyTo' = None, send_as: 'InputPeer' = None):
        self.from_bot_menu = from_bot_menu
        self.silent = silent
        self.compact = compact
        self.fullscreen = fullscreen
        self.peer = peer
        self.bot = bot
        self.url = url
        self.start_param = start_param
        self.theme_params = theme_params
        self.platform = platform
        self.reply_to = reply_to
        self.send_as = send_as
    def to_dict(self):
        return {"from_bot_menu": self.from_bot_menu, "silent": self.silent, "compact": self.compact, "fullscreen": self.fullscreen, "peer": self.peer, "bot": self.bot, "url": self.url, "start_param": self.start_param, "theme_params": self.theme_params, "platform": self.platform, "reply_to": self.reply_to, "send_as": self.send_as}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(647873217, signed=False)
        flags = 0
        if self.from_bot_menu: flags |= 1 << 4
        if self.silent: flags |= 1 << 5
        if self.compact: flags |= 1 << 7
        if self.fullscreen: flags |= 1 << 8
        if self.url is not None: flags |= 1 << 1
        if self.start_param is not None: flags |= 1 << 3
        if self.theme_params is not None: flags |= 1 << 2
        if self.reply_to is not None: flags |= 1 << 0
        if self.send_as is not None: flags |= 1 << 13
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.bot))
        if flags & (1 << 1):
            writer.write_string(self.url)
        if flags & (1 << 3):
            writer.write_string(self.start_param)
        if flags & (1 << 2):
            writer.write(bytes(self.theme_params))
        writer.write_string(self.platform)
        if flags & (1 << 0):
            writer.write(bytes(self.reply_to))
        if flags & (1 << 13):
            writer.write(bytes(self.send_as))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        from_bot_menu = bool(flags & (1 << 4))
        silent = bool(flags & (1 << 5))
        compact = bool(flags & (1 << 7))
        fullscreen = bool(flags & (1 << 8))
        peer = reader.tgread_object()
        bot = reader.tgread_object()
        if flags & (1 << 1):
            url = reader.read_string()
        else:
            url = None
        if flags & (1 << 3):
            start_param = reader.read_string()
        else:
            start_param = None
        if flags & (1 << 2):
            theme_params = reader.tgread_object()
        else:
            theme_params = None
        platform = reader.read_string()
        if flags & (1 << 0):
            reply_to = reader.tgread_object()
        else:
            reply_to = None
        if flags & (1 << 13):
            send_as = reader.tgread_object()
        else:
            send_as = None
        return cls(from_bot_menu, silent, compact, fullscreen, peer, bot, url, start_param, theme_params, platform, reply_to, send_as)

@register
class MessagesProlongWebView(TLObject):
    CONSTRUCTOR_ID = 2966952579
    __slots__ = ('silent', 'peer', 'bot', 'query_id', 'reply_to', 'send_as')
    def __init__(self, peer: 'InputPeer', bot: 'InputUser', query_id: int, silent: bool = None, reply_to: 'InputReplyTo' = None, send_as: 'InputPeer' = None):
        self.silent = silent
        self.peer = peer
        self.bot = bot
        self.query_id = query_id
        self.reply_to = reply_to
        self.send_as = send_as
    def to_dict(self):
        return {"silent": self.silent, "peer": self.peer, "bot": self.bot, "query_id": self.query_id, "reply_to": self.reply_to, "send_as": self.send_as}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2966952579, signed=False)
        flags = 0
        if self.silent: flags |= 1 << 5
        if self.reply_to is not None: flags |= 1 << 0
        if self.send_as is not None: flags |= 1 << 13
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.bot))
        writer.write_long(self.query_id, signed=False)
        if flags & (1 << 0):
            writer.write(bytes(self.reply_to))
        if flags & (1 << 13):
            writer.write(bytes(self.send_as))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        silent = bool(flags & (1 << 5))
        peer = reader.tgread_object()
        bot = reader.tgread_object()
        query_id = reader.read_long()
        if flags & (1 << 0):
            reply_to = reader.tgread_object()
        else:
            reply_to = None
        if flags & (1 << 13):
            send_as = reader.tgread_object()
        else:
            send_as = None
        return cls(silent, peer, bot, query_id, reply_to, send_as)

@register
class MessagesRequestSimpleWebView(TLObject):
    CONSTRUCTOR_ID = 1094336115
    __slots__ = ('from_switch_webview', 'from_side_menu', 'compact', 'fullscreen', 'bot', 'url', 'start_param', 'theme_params', 'platform')
    def __init__(self, bot: 'InputUser', platform: str, from_switch_webview: bool = None, from_side_menu: bool = None, compact: bool = None, fullscreen: bool = None, url: str = None, start_param: str = None, theme_params: 'DataJSON' = None):
        self.from_switch_webview = from_switch_webview
        self.from_side_menu = from_side_menu
        self.compact = compact
        self.fullscreen = fullscreen
        self.bot = bot
        self.url = url
        self.start_param = start_param
        self.theme_params = theme_params
        self.platform = platform
    def to_dict(self):
        return {"from_switch_webview": self.from_switch_webview, "from_side_menu": self.from_side_menu, "compact": self.compact, "fullscreen": self.fullscreen, "bot": self.bot, "url": self.url, "start_param": self.start_param, "theme_params": self.theme_params, "platform": self.platform}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1094336115, signed=False)
        flags = 0
        if self.from_switch_webview: flags |= 1 << 1
        if self.from_side_menu: flags |= 1 << 2
        if self.compact: flags |= 1 << 7
        if self.fullscreen: flags |= 1 << 8
        if self.url is not None: flags |= 1 << 3
        if self.start_param is not None: flags |= 1 << 4
        if self.theme_params is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.bot))
        if flags & (1 << 3):
            writer.write_string(self.url)
        if flags & (1 << 4):
            writer.write_string(self.start_param)
        if flags & (1 << 0):
            writer.write(bytes(self.theme_params))
        writer.write_string(self.platform)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        from_switch_webview = bool(flags & (1 << 1))
        from_side_menu = bool(flags & (1 << 2))
        compact = bool(flags & (1 << 7))
        fullscreen = bool(flags & (1 << 8))
        bot = reader.tgread_object()
        if flags & (1 << 3):
            url = reader.read_string()
        else:
            url = None
        if flags & (1 << 4):
            start_param = reader.read_string()
        else:
            start_param = None
        if flags & (1 << 0):
            theme_params = reader.tgread_object()
        else:
            theme_params = None
        platform = reader.read_string()
        return cls(from_switch_webview, from_side_menu, compact, fullscreen, bot, url, start_param, theme_params, platform)

@register
class MessagesSendWebViewResultMessage(TLObject):
    CONSTRUCTOR_ID = 172168437
    __slots__ = ('bot_query_id', 'result')
    def __init__(self, bot_query_id: str, result: 'InputBotInlineResult'):
        self.bot_query_id = bot_query_id
        self.result = result
    def to_dict(self):
        return {"bot_query_id": self.bot_query_id, "result": self.result}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(172168437, signed=False)
        writer.write_string(self.bot_query_id)
        writer.write(bytes(self.result))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        bot_query_id = reader.read_string()
        result = reader.tgread_object()
        return cls(bot_query_id, result)

@register
class MessagesSendWebViewData(TLObject):
    CONSTRUCTOR_ID = 3691135688
    __slots__ = ('bot', 'random_id', 'button_text', 'data')
    def __init__(self, bot: 'InputUser', random_id: int, button_text: str, data: str):
        self.bot = bot
        self.random_id = random_id
        self.button_text = button_text
        self.data = data
    def to_dict(self):
        return {"bot": self.bot, "random_id": self.random_id, "button_text": self.button_text, "data": self.data}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3691135688, signed=False)
        writer.write(bytes(self.bot))
        writer.write_long(self.random_id, signed=False)
        writer.write_string(self.button_text)
        writer.write_string(self.data)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        bot = reader.tgread_object()
        random_id = reader.read_long()
        button_text = reader.read_string()
        data = reader.read_string()
        return cls(bot, random_id, button_text, data)

@register
class MessagesTranscribeAudio(TLObject):
    CONSTRUCTOR_ID = 647928393
    __slots__ = ('peer', 'msg_id')
    def __init__(self, peer: 'InputPeer', msg_id: int):
        self.peer = peer
        self.msg_id = msg_id
    def to_dict(self):
        return {"peer": self.peer, "msg_id": self.msg_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(647928393, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.msg_id, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        msg_id = reader.read_int()
        return cls(peer, msg_id)

@register
class MessagesRateTranscribedAudio(TLObject):
    CONSTRUCTOR_ID = 2132608815
    __slots__ = ('peer', 'msg_id', 'transcription_id', 'good')
    def __init__(self, peer: 'InputPeer', msg_id: int, transcription_id: int, good: bool):
        self.peer = peer
        self.msg_id = msg_id
        self.transcription_id = transcription_id
        self.good = good
    def to_dict(self):
        return {"peer": self.peer, "msg_id": self.msg_id, "transcription_id": self.transcription_id, "good": self.good}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2132608815, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.msg_id, signed=True)
        writer.write_long(self.transcription_id, signed=False)
        writer.write(serialize_bool(self.good))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        msg_id = reader.read_int()
        transcription_id = reader.read_long()
        good = reader.tgread_bool()
        return cls(peer, msg_id, transcription_id, good)

@register
class MessagesGetCustomEmojiDocuments(TLObject):
    CONSTRUCTOR_ID = 3651866452
    __slots__ = ('document_id')
    def __init__(self, document_id: 'Vector'):
        self.document_id = document_id
    def to_dict(self):
        return {"document_id": self.document_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3651866452, signed=False)
        writer.write(bytes(self.document_id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        document_id = reader.tgread_object()
        return cls(document_id)

@register
class MessagesGetEmojiStickers(TLObject):
    CONSTRUCTOR_ID = 4227637647
    __slots__ = ('hash')
    def __init__(self, hash: int):
        self.hash = hash
    def to_dict(self):
        return {"hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4227637647, signed=False)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_long()
        return cls(hash)

@register
class MessagesGetFeaturedEmojiStickers(TLObject):
    CONSTRUCTOR_ID = 248473398
    __slots__ = ('hash')
    def __init__(self, hash: int):
        self.hash = hash
    def to_dict(self):
        return {"hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(248473398, signed=False)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_long()
        return cls(hash)

@register
class MessagesReportReaction(TLObject):
    CONSTRUCTOR_ID = 1063567478
    __slots__ = ('peer', 'id', 'reaction_peer')
    def __init__(self, peer: 'InputPeer', id: int, reaction_peer: 'InputPeer'):
        self.peer = peer
        self.id = id
        self.reaction_peer = reaction_peer
    def to_dict(self):
        return {"peer": self.peer, "id": self.id, "reaction_peer": self.reaction_peer}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1063567478, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.id, signed=True)
        writer.write(bytes(self.reaction_peer))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        id = reader.read_int()
        reaction_peer = reader.tgread_object()
        return cls(peer, id, reaction_peer)

@register
class MessagesGetTopReactions(TLObject):
    CONSTRUCTOR_ID = 3145803194
    __slots__ = ('limit', 'hash')
    def __init__(self, limit: int, hash: int):
        self.limit = limit
        self.hash = hash
    def to_dict(self):
        return {"limit": self.limit, "hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3145803194, signed=False)
        writer.write_int(self.limit, signed=True)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        limit = reader.read_int()
        hash = reader.read_long()
        return cls(limit, hash)

@register
class MessagesGetRecentReactions(TLObject):
    CONSTRUCTOR_ID = 960896434
    __slots__ = ('limit', 'hash')
    def __init__(self, limit: int, hash: int):
        self.limit = limit
        self.hash = hash
    def to_dict(self):
        return {"limit": self.limit, "hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(960896434, signed=False)
        writer.write_int(self.limit, signed=True)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        limit = reader.read_int()
        hash = reader.read_long()
        return cls(limit, hash)

@register
class MessagesClearRecentReactions(TLObject):
    CONSTRUCTOR_ID = 2650730420
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2650730420, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class MessagesGetExtendedMedia(TLObject):
    CONSTRUCTOR_ID = 2230847508
    __slots__ = ('peer', 'id')
    def __init__(self, peer: 'InputPeer', id: 'Vector'):
        self.peer = peer
        self.id = id
    def to_dict(self):
        return {"peer": self.peer, "id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2230847508, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        id = reader.tgread_object()
        return cls(peer, id)

@register
class MessagesSetDefaultHistoryTTL(TLObject):
    CONSTRUCTOR_ID = 2662667333
    __slots__ = ('period')
    def __init__(self, period: int):
        self.period = period
    def to_dict(self):
        return {"period": self.period}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2662667333, signed=False)
        writer.write_int(self.period, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        period = reader.read_int()
        return cls(period)

@register
class MessagesGetDefaultHistoryTTL(TLObject):
    CONSTRUCTOR_ID = 1703637384
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1703637384, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class MessagesSendBotRequestedPeer(TLObject):
    CONSTRUCTOR_ID = 1818030759
    __slots__ = ('peer', 'msg_id', 'webapp_req_id', 'button_id', 'requested_peers')
    def __init__(self, peer: 'InputPeer', button_id: int, requested_peers: 'Vector', msg_id: int = None, webapp_req_id: str = None):
        self.peer = peer
        self.msg_id = msg_id
        self.webapp_req_id = webapp_req_id
        self.button_id = button_id
        self.requested_peers = requested_peers
    def to_dict(self):
        return {"peer": self.peer, "msg_id": self.msg_id, "webapp_req_id": self.webapp_req_id, "button_id": self.button_id, "requested_peers": self.requested_peers}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1818030759, signed=False)
        flags = 0
        if self.msg_id is not None: flags |= 1 << 0
        if self.webapp_req_id is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        if flags & (1 << 0):
            writer.write_int(self.msg_id, signed=True)
        if flags & (1 << 1):
            writer.write_string(self.webapp_req_id)
        writer.write_int(self.button_id, signed=True)
        writer.write(bytes(self.requested_peers))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        peer = reader.tgread_object()
        if flags & (1 << 0):
            msg_id = reader.read_int()
        else:
            msg_id = None
        if flags & (1 << 1):
            webapp_req_id = reader.read_string()
        else:
            webapp_req_id = None
        button_id = reader.read_int()
        requested_peers = reader.tgread_object()
        return cls(peer, msg_id, webapp_req_id, button_id, requested_peers)

@register
class MessagesGetEmojiGroups(TLObject):
    CONSTRUCTOR_ID = 1955122779
    __slots__ = ('hash')
    def __init__(self, hash: int):
        self.hash = hash
    def to_dict(self):
        return {"hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1955122779, signed=False)
        writer.write_int(self.hash, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_int()
        return cls(hash)

@register
class MessagesGetEmojiStatusGroups(TLObject):
    CONSTRUCTOR_ID = 785209037
    __slots__ = ('hash')
    def __init__(self, hash: int):
        self.hash = hash
    def to_dict(self):
        return {"hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(785209037, signed=False)
        writer.write_int(self.hash, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_int()
        return cls(hash)

@register
class MessagesGetEmojiProfilePhotoGroups(TLObject):
    CONSTRUCTOR_ID = 564480243
    __slots__ = ('hash')
    def __init__(self, hash: int):
        self.hash = hash
    def to_dict(self):
        return {"hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(564480243, signed=False)
        writer.write_int(self.hash, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_int()
        return cls(hash)

@register
class MessagesSearchCustomEmoji(TLObject):
    CONSTRUCTOR_ID = 739360983
    __slots__ = ('emoticon', 'hash')
    def __init__(self, emoticon: str, hash: int):
        self.emoticon = emoticon
        self.hash = hash
    def to_dict(self):
        return {"emoticon": self.emoticon, "hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(739360983, signed=False)
        writer.write_string(self.emoticon)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        emoticon = reader.read_string()
        hash = reader.read_long()
        return cls(emoticon, hash)

@register
class MessagesTogglePeerTranslations(TLObject):
    CONSTRUCTOR_ID = 3833378169
    __slots__ = ('disabled', 'peer')
    def __init__(self, peer: 'InputPeer', disabled: bool = None):
        self.disabled = disabled
        self.peer = peer
    def to_dict(self):
        return {"disabled": self.disabled, "peer": self.peer}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3833378169, signed=False)
        flags = 0
        if self.disabled: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        disabled = bool(flags & (1 << 0))
        peer = reader.tgread_object()
        return cls(disabled, peer)

@register
class MessagesGetBotApp(TLObject):
    CONSTRUCTOR_ID = 889046467
    __slots__ = ('app', 'hash')
    def __init__(self, app: 'InputBotApp', hash: int):
        self.app = app
        self.hash = hash
    def to_dict(self):
        return {"app": self.app, "hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(889046467, signed=False)
        writer.write(bytes(self.app))
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        app = reader.tgread_object()
        hash = reader.read_long()
        return cls(app, hash)

@register
class MessagesRequestAppWebView(TLObject):
    CONSTRUCTOR_ID = 1398901710
    __slots__ = ('write_allowed', 'compact', 'fullscreen', 'peer', 'app', 'start_param', 'theme_params', 'platform')
    def __init__(self, peer: 'InputPeer', app: 'InputBotApp', platform: str, write_allowed: bool = None, compact: bool = None, fullscreen: bool = None, start_param: str = None, theme_params: 'DataJSON' = None):
        self.write_allowed = write_allowed
        self.compact = compact
        self.fullscreen = fullscreen
        self.peer = peer
        self.app = app
        self.start_param = start_param
        self.theme_params = theme_params
        self.platform = platform
    def to_dict(self):
        return {"write_allowed": self.write_allowed, "compact": self.compact, "fullscreen": self.fullscreen, "peer": self.peer, "app": self.app, "start_param": self.start_param, "theme_params": self.theme_params, "platform": self.platform}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1398901710, signed=False)
        flags = 0
        if self.write_allowed: flags |= 1 << 0
        if self.compact: flags |= 1 << 7
        if self.fullscreen: flags |= 1 << 8
        if self.start_param is not None: flags |= 1 << 1
        if self.theme_params is not None: flags |= 1 << 2
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.app))
        if flags & (1 << 1):
            writer.write_string(self.start_param)
        if flags & (1 << 2):
            writer.write(bytes(self.theme_params))
        writer.write_string(self.platform)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        write_allowed = bool(flags & (1 << 0))
        compact = bool(flags & (1 << 7))
        fullscreen = bool(flags & (1 << 8))
        peer = reader.tgread_object()
        app = reader.tgread_object()
        if flags & (1 << 1):
            start_param = reader.read_string()
        else:
            start_param = None
        if flags & (1 << 2):
            theme_params = reader.tgread_object()
        else:
            theme_params = None
        platform = reader.read_string()
        return cls(write_allowed, compact, fullscreen, peer, app, start_param, theme_params, platform)

@register
class MessagesSetChatWallPaper(TLObject):
    CONSTRUCTOR_ID = 2415577825
    __slots__ = ('for_both', 'revert', 'peer', 'wallpaper', 'settings', 'id')
    def __init__(self, peer: 'InputPeer', for_both: bool = None, revert: bool = None, wallpaper: 'InputWallPaper' = None, settings: 'WallPaperSettings' = None, id: int = None):
        self.for_both = for_both
        self.revert = revert
        self.peer = peer
        self.wallpaper = wallpaper
        self.settings = settings
        self.id = id
    def to_dict(self):
        return {"for_both": self.for_both, "revert": self.revert, "peer": self.peer, "wallpaper": self.wallpaper, "settings": self.settings, "id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2415577825, signed=False)
        flags = 0
        if self.for_both: flags |= 1 << 3
        if self.revert: flags |= 1 << 4
        if self.wallpaper is not None: flags |= 1 << 0
        if self.settings is not None: flags |= 1 << 2
        if self.id is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        if flags & (1 << 0):
            writer.write(bytes(self.wallpaper))
        if flags & (1 << 2):
            writer.write(bytes(self.settings))
        if flags & (1 << 1):
            writer.write_int(self.id, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        for_both = bool(flags & (1 << 3))
        revert = bool(flags & (1 << 4))
        peer = reader.tgread_object()
        if flags & (1 << 0):
            wallpaper = reader.tgread_object()
        else:
            wallpaper = None
        if flags & (1 << 2):
            settings = reader.tgread_object()
        else:
            settings = None
        if flags & (1 << 1):
            id = reader.read_int()
        else:
            id = None
        return cls(for_both, revert, peer, wallpaper, settings, id)

@register
class MessagesSearchEmojiStickerSets(TLObject):
    CONSTRUCTOR_ID = 2461288780
    __slots__ = ('exclude_featured', 'q', 'hash')
    def __init__(self, q: str, hash: int, exclude_featured: bool = None):
        self.exclude_featured = exclude_featured
        self.q = q
        self.hash = hash
    def to_dict(self):
        return {"exclude_featured": self.exclude_featured, "q": self.q, "hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2461288780, signed=False)
        flags = 0
        if self.exclude_featured: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write_string(self.q)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        exclude_featured = bool(flags & (1 << 0))
        q = reader.read_string()
        hash = reader.read_long()
        return cls(exclude_featured, q, hash)

@register
class MessagesGetSavedDialogs(TLObject):
    CONSTRUCTOR_ID = 512883865
    __slots__ = ('exclude_pinned', 'parent_peer', 'offset_date', 'offset_id', 'offset_peer', 'limit', 'hash')
    def __init__(self, offset_date: int, offset_id: int, offset_peer: 'InputPeer', limit: int, hash: int, exclude_pinned: bool = None, parent_peer: 'InputPeer' = None):
        self.exclude_pinned = exclude_pinned
        self.parent_peer = parent_peer
        self.offset_date = offset_date
        self.offset_id = offset_id
        self.offset_peer = offset_peer
        self.limit = limit
        self.hash = hash
    def to_dict(self):
        return {"exclude_pinned": self.exclude_pinned, "parent_peer": self.parent_peer, "offset_date": self.offset_date, "offset_id": self.offset_id, "offset_peer": self.offset_peer, "limit": self.limit, "hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(512883865, signed=False)
        flags = 0
        if self.exclude_pinned: flags |= 1 << 0
        if self.parent_peer is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        if flags & (1 << 1):
            writer.write(bytes(self.parent_peer))
        writer.write_int(self.offset_date, signed=True)
        writer.write_int(self.offset_id, signed=True)
        writer.write(bytes(self.offset_peer))
        writer.write_int(self.limit, signed=True)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        exclude_pinned = bool(flags & (1 << 0))
        if flags & (1 << 1):
            parent_peer = reader.tgread_object()
        else:
            parent_peer = None
        offset_date = reader.read_int()
        offset_id = reader.read_int()
        offset_peer = reader.tgread_object()
        limit = reader.read_int()
        hash = reader.read_long()
        return cls(exclude_pinned, parent_peer, offset_date, offset_id, offset_peer, limit, hash)

@register
class MessagesGetSavedHistory(TLObject):
    CONSTRUCTOR_ID = 2576003081
    __slots__ = ('parent_peer', 'peer', 'offset_id', 'offset_date', 'add_offset', 'limit', 'max_id', 'min_id', 'hash')
    def __init__(self, peer: 'InputPeer', offset_id: int, offset_date: int, add_offset: int, limit: int, max_id: int, min_id: int, hash: int, parent_peer: 'InputPeer' = None):
        self.parent_peer = parent_peer
        self.peer = peer
        self.offset_id = offset_id
        self.offset_date = offset_date
        self.add_offset = add_offset
        self.limit = limit
        self.max_id = max_id
        self.min_id = min_id
        self.hash = hash
    def to_dict(self):
        return {"parent_peer": self.parent_peer, "peer": self.peer, "offset_id": self.offset_id, "offset_date": self.offset_date, "add_offset": self.add_offset, "limit": self.limit, "max_id": self.max_id, "min_id": self.min_id, "hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2576003081, signed=False)
        flags = 0
        if self.parent_peer is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        if flags & (1 << 0):
            writer.write(bytes(self.parent_peer))
        writer.write(bytes(self.peer))
        writer.write_int(self.offset_id, signed=True)
        writer.write_int(self.offset_date, signed=True)
        writer.write_int(self.add_offset, signed=True)
        writer.write_int(self.limit, signed=True)
        writer.write_int(self.max_id, signed=True)
        writer.write_int(self.min_id, signed=True)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        if flags & (1 << 0):
            parent_peer = reader.tgread_object()
        else:
            parent_peer = None
        peer = reader.tgread_object()
        offset_id = reader.read_int()
        offset_date = reader.read_int()
        add_offset = reader.read_int()
        limit = reader.read_int()
        max_id = reader.read_int()
        min_id = reader.read_int()
        hash = reader.read_long()
        return cls(parent_peer, peer, offset_id, offset_date, add_offset, limit, max_id, min_id, hash)

@register
class MessagesDeleteSavedHistory(TLObject):
    CONSTRUCTOR_ID = 1304758367
    __slots__ = ('parent_peer', 'peer', 'max_id', 'min_date', 'max_date')
    def __init__(self, peer: 'InputPeer', max_id: int, parent_peer: 'InputPeer' = None, min_date: int = None, max_date: int = None):
        self.parent_peer = parent_peer
        self.peer = peer
        self.max_id = max_id
        self.min_date = min_date
        self.max_date = max_date
    def to_dict(self):
        return {"parent_peer": self.parent_peer, "peer": self.peer, "max_id": self.max_id, "min_date": self.min_date, "max_date": self.max_date}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1304758367, signed=False)
        flags = 0
        if self.parent_peer is not None: flags |= 1 << 0
        if self.min_date is not None: flags |= 1 << 2
        if self.max_date is not None: flags |= 1 << 3
        writer.write_int(flags, signed=False)
        if flags & (1 << 0):
            writer.write(bytes(self.parent_peer))
        writer.write(bytes(self.peer))
        writer.write_int(self.max_id, signed=True)
        if flags & (1 << 2):
            writer.write_int(self.min_date, signed=True)
        if flags & (1 << 3):
            writer.write_int(self.max_date, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        if flags & (1 << 0):
            parent_peer = reader.tgread_object()
        else:
            parent_peer = None
        peer = reader.tgread_object()
        max_id = reader.read_int()
        if flags & (1 << 2):
            min_date = reader.read_int()
        else:
            min_date = None
        if flags & (1 << 3):
            max_date = reader.read_int()
        else:
            max_date = None
        return cls(parent_peer, peer, max_id, min_date, max_date)

@register
class MessagesGetPinnedSavedDialogs(TLObject):
    CONSTRUCTOR_ID = 3594360032
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3594360032, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class MessagesToggleSavedDialogPin(TLObject):
    CONSTRUCTOR_ID = 2894183390
    __slots__ = ('pinned', 'peer')
    def __init__(self, peer: 'InputDialogPeer', pinned: bool = None):
        self.pinned = pinned
        self.peer = peer
    def to_dict(self):
        return {"pinned": self.pinned, "peer": self.peer}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2894183390, signed=False)
        flags = 0
        if self.pinned: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        pinned = bool(flags & (1 << 0))
        peer = reader.tgread_object()
        return cls(pinned, peer)

@register
class MessagesReorderPinnedSavedDialogs(TLObject):
    CONSTRUCTOR_ID = 2339464583
    __slots__ = ('force', 'order')
    def __init__(self, order: 'Vector', force: bool = None):
        self.force = force
        self.order = order
    def to_dict(self):
        return {"force": self.force, "order": self.order}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2339464583, signed=False)
        flags = 0
        if self.force: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.order))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        force = bool(flags & (1 << 0))
        order = reader.tgread_object()
        return cls(force, order)

@register
class MessagesGetSavedReactionTags(TLObject):
    CONSTRUCTOR_ID = 909631579
    __slots__ = ('peer', 'hash')
    def __init__(self, hash: int, peer: 'InputPeer' = None):
        self.peer = peer
        self.hash = hash
    def to_dict(self):
        return {"peer": self.peer, "hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(909631579, signed=False)
        flags = 0
        if self.peer is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        if flags & (1 << 0):
            writer.write(bytes(self.peer))
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        if flags & (1 << 0):
            peer = reader.tgread_object()
        else:
            peer = None
        hash = reader.read_long()
        return cls(peer, hash)

@register
class MessagesUpdateSavedReactionTag(TLObject):
    CONSTRUCTOR_ID = 1613331948
    __slots__ = ('reaction', 'title')
    def __init__(self, reaction: 'Reaction', title: str = None):
        self.reaction = reaction
        self.title = title
    def to_dict(self):
        return {"reaction": self.reaction, "title": self.title}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1613331948, signed=False)
        flags = 0
        if self.title is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.reaction))
        if flags & (1 << 0):
            writer.write_string(self.title)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        reaction = reader.tgread_object()
        if flags & (1 << 0):
            title = reader.read_string()
        else:
            title = None
        return cls(reaction, title)

@register
class MessagesGetDefaultTagReactions(TLObject):
    CONSTRUCTOR_ID = 3187225640
    __slots__ = ('hash')
    def __init__(self, hash: int):
        self.hash = hash
    def to_dict(self):
        return {"hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3187225640, signed=False)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_long()
        return cls(hash)

@register
class MessagesGetOutboxReadDate(TLObject):
    CONSTRUCTOR_ID = 2353790557
    __slots__ = ('peer', 'msg_id')
    def __init__(self, peer: 'InputPeer', msg_id: int):
        self.peer = peer
        self.msg_id = msg_id
    def to_dict(self):
        return {"peer": self.peer, "msg_id": self.msg_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2353790557, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.msg_id, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        msg_id = reader.read_int()
        return cls(peer, msg_id)

@register
class MessagesGetQuickReplies(TLObject):
    CONSTRUCTOR_ID = 3565417128
    __slots__ = ('hash')
    def __init__(self, hash: int):
        self.hash = hash
    def to_dict(self):
        return {"hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3565417128, signed=False)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_long()
        return cls(hash)

@register
class MessagesReorderQuickReplies(TLObject):
    CONSTRUCTOR_ID = 1613961479
    __slots__ = ('order')
    def __init__(self, order: 'Vector'):
        self.order = order
    def to_dict(self):
        return {"order": self.order}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1613961479, signed=False)
        writer.write(bytes(self.order))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        order = reader.tgread_object()
        return cls(order)

@register
class MessagesCheckQuickReplyShortcut(TLObject):
    CONSTRUCTOR_ID = 4057005011
    __slots__ = ('shortcut')
    def __init__(self, shortcut: str):
        self.shortcut = shortcut
    def to_dict(self):
        return {"shortcut": self.shortcut}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4057005011, signed=False)
        writer.write_string(self.shortcut)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        shortcut = reader.read_string()
        return cls(shortcut)

@register
class MessagesEditQuickReplyShortcut(TLObject):
    CONSTRUCTOR_ID = 1543519471
    __slots__ = ('shortcut_id', 'shortcut')
    def __init__(self, shortcut_id: int, shortcut: str):
        self.shortcut_id = shortcut_id
        self.shortcut = shortcut
    def to_dict(self):
        return {"shortcut_id": self.shortcut_id, "shortcut": self.shortcut}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1543519471, signed=False)
        writer.write_int(self.shortcut_id, signed=True)
        writer.write_string(self.shortcut)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        shortcut_id = reader.read_int()
        shortcut = reader.read_string()
        return cls(shortcut_id, shortcut)

@register
class MessagesDeleteQuickReplyShortcut(TLObject):
    CONSTRUCTOR_ID = 1019234112
    __slots__ = ('shortcut_id')
    def __init__(self, shortcut_id: int):
        self.shortcut_id = shortcut_id
    def to_dict(self):
        return {"shortcut_id": self.shortcut_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1019234112, signed=False)
        writer.write_int(self.shortcut_id, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        shortcut_id = reader.read_int()
        return cls(shortcut_id)

@register
class MessagesGetQuickReplyMessages(TLObject):
    CONSTRUCTOR_ID = 2493814211
    __slots__ = ('shortcut_id', 'id', 'hash')
    def __init__(self, shortcut_id: int, hash: int, id: 'Vector' = None):
        self.shortcut_id = shortcut_id
        self.id = id
        self.hash = hash
    def to_dict(self):
        return {"shortcut_id": self.shortcut_id, "id": self.id, "hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2493814211, signed=False)
        flags = 0
        if self.id is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write_int(self.shortcut_id, signed=True)
        if flags & (1 << 0):
            writer.write(bytes(self.id))
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        shortcut_id = reader.read_int()
        if flags & (1 << 0):
            id = reader.tgread_object()
        else:
            id = None
        hash = reader.read_long()
        return cls(shortcut_id, id, hash)

@register
class MessagesSendQuickReplyMessages(TLObject):
    CONSTRUCTOR_ID = 1819610593
    __slots__ = ('peer', 'shortcut_id', 'id', 'random_id')
    def __init__(self, peer: 'InputPeer', shortcut_id: int, id: 'Vector', random_id: 'Vector'):
        self.peer = peer
        self.shortcut_id = shortcut_id
        self.id = id
        self.random_id = random_id
    def to_dict(self):
        return {"peer": self.peer, "shortcut_id": self.shortcut_id, "id": self.id, "random_id": self.random_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1819610593, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.shortcut_id, signed=True)
        writer.write(bytes(self.id))
        writer.write(bytes(self.random_id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        shortcut_id = reader.read_int()
        id = reader.tgread_object()
        random_id = reader.tgread_object()
        return cls(peer, shortcut_id, id, random_id)

@register
class MessagesDeleteQuickReplyMessages(TLObject):
    CONSTRUCTOR_ID = 3775260944
    __slots__ = ('shortcut_id', 'id')
    def __init__(self, shortcut_id: int, id: 'Vector'):
        self.shortcut_id = shortcut_id
        self.id = id
    def to_dict(self):
        return {"shortcut_id": self.shortcut_id, "id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3775260944, signed=False)
        writer.write_int(self.shortcut_id, signed=True)
        writer.write(bytes(self.id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        shortcut_id = reader.read_int()
        id = reader.tgread_object()
        return cls(shortcut_id, id)

@register
class MessagesToggleDialogFilterTags(TLObject):
    CONSTRUCTOR_ID = 4247640649
    __slots__ = ('enabled')
    def __init__(self, enabled: bool):
        self.enabled = enabled
    def to_dict(self):
        return {"enabled": self.enabled}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4247640649, signed=False)
        writer.write(serialize_bool(self.enabled))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        enabled = reader.tgread_bool()
        return cls(enabled)

@register
class MessagesGetMyStickers(TLObject):
    CONSTRUCTOR_ID = 3501580796
    __slots__ = ('offset_id', 'limit')
    def __init__(self, offset_id: int, limit: int):
        self.offset_id = offset_id
        self.limit = limit
    def to_dict(self):
        return {"offset_id": self.offset_id, "limit": self.limit}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3501580796, signed=False)
        writer.write_long(self.offset_id, signed=False)
        writer.write_int(self.limit, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        offset_id = reader.read_long()
        limit = reader.read_int()
        return cls(offset_id, limit)

@register
class MessagesGetEmojiStickerGroups(TLObject):
    CONSTRUCTOR_ID = 500711669
    __slots__ = ('hash')
    def __init__(self, hash: int):
        self.hash = hash
    def to_dict(self):
        return {"hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(500711669, signed=False)
        writer.write_int(self.hash, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_int()
        return cls(hash)

@register
class MessagesGetAvailableEffects(TLObject):
    CONSTRUCTOR_ID = 3735161401
    __slots__ = ('hash')
    def __init__(self, hash: int):
        self.hash = hash
    def to_dict(self):
        return {"hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3735161401, signed=False)
        writer.write_int(self.hash, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_int()
        return cls(hash)

@register
class MessagesEditFactCheck(TLObject):
    CONSTRUCTOR_ID = 92925557
    __slots__ = ('peer', 'msg_id', 'text')
    def __init__(self, peer: 'InputPeer', msg_id: int, text: 'TextWithEntities'):
        self.peer = peer
        self.msg_id = msg_id
        self.text = text
    def to_dict(self):
        return {"peer": self.peer, "msg_id": self.msg_id, "text": self.text}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(92925557, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.msg_id, signed=True)
        writer.write(bytes(self.text))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        msg_id = reader.read_int()
        text = reader.tgread_object()
        return cls(peer, msg_id, text)

@register
class MessagesDeleteFactCheck(TLObject):
    CONSTRUCTOR_ID = 3520762892
    __slots__ = ('peer', 'msg_id')
    def __init__(self, peer: 'InputPeer', msg_id: int):
        self.peer = peer
        self.msg_id = msg_id
    def to_dict(self):
        return {"peer": self.peer, "msg_id": self.msg_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3520762892, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.msg_id, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        msg_id = reader.read_int()
        return cls(peer, msg_id)

@register
class MessagesGetFactCheck(TLObject):
    CONSTRUCTOR_ID = 3117270510
    __slots__ = ('peer', 'msg_id')
    def __init__(self, peer: 'InputPeer', msg_id: 'Vector'):
        self.peer = peer
        self.msg_id = msg_id
    def to_dict(self):
        return {"peer": self.peer, "msg_id": self.msg_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3117270510, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.msg_id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        msg_id = reader.tgread_object()
        return cls(peer, msg_id)

@register
class MessagesRequestMainWebView(TLObject):
    CONSTRUCTOR_ID = 3386908283
    __slots__ = ('compact', 'fullscreen', 'peer', 'bot', 'start_param', 'theme_params', 'platform')
    def __init__(self, peer: 'InputPeer', bot: 'InputUser', platform: str, compact: bool = None, fullscreen: bool = None, start_param: str = None, theme_params: 'DataJSON' = None):
        self.compact = compact
        self.fullscreen = fullscreen
        self.peer = peer
        self.bot = bot
        self.start_param = start_param
        self.theme_params = theme_params
        self.platform = platform
    def to_dict(self):
        return {"compact": self.compact, "fullscreen": self.fullscreen, "peer": self.peer, "bot": self.bot, "start_param": self.start_param, "theme_params": self.theme_params, "platform": self.platform}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3386908283, signed=False)
        flags = 0
        if self.compact: flags |= 1 << 7
        if self.fullscreen: flags |= 1 << 8
        if self.start_param is not None: flags |= 1 << 1
        if self.theme_params is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.bot))
        if flags & (1 << 1):
            writer.write_string(self.start_param)
        if flags & (1 << 0):
            writer.write(bytes(self.theme_params))
        writer.write_string(self.platform)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        compact = bool(flags & (1 << 7))
        fullscreen = bool(flags & (1 << 8))
        peer = reader.tgread_object()
        bot = reader.tgread_object()
        if flags & (1 << 1):
            start_param = reader.read_string()
        else:
            start_param = None
        if flags & (1 << 0):
            theme_params = reader.tgread_object()
        else:
            theme_params = None
        platform = reader.read_string()
        return cls(compact, fullscreen, peer, bot, start_param, theme_params, platform)

@register
class MessagesSendPaidReaction(TLObject):
    CONSTRUCTOR_ID = 1488702288
    __slots__ = ('peer', 'msg_id', 'count', 'random_id', 'private')
    def __init__(self, peer: 'InputPeer', msg_id: int, count: int, random_id: int, private: 'PaidReactionPrivacy' = None):
        self.peer = peer
        self.msg_id = msg_id
        self.count = count
        self.random_id = random_id
        self.private = private
    def to_dict(self):
        return {"peer": self.peer, "msg_id": self.msg_id, "count": self.count, "random_id": self.random_id, "private": self.private}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1488702288, signed=False)
        flags = 0
        if self.private is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.msg_id, signed=True)
        writer.write_int(self.count, signed=True)
        writer.write_long(self.random_id, signed=False)
        if flags & (1 << 0):
            writer.write(bytes(self.private))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        peer = reader.tgread_object()
        msg_id = reader.read_int()
        count = reader.read_int()
        random_id = reader.read_long()
        if flags & (1 << 0):
            private = reader.tgread_object()
        else:
            private = None
        return cls(peer, msg_id, count, random_id, private)

@register
class MessagesTogglePaidReactionPrivacy(TLObject):
    CONSTRUCTOR_ID = 1129874869
    __slots__ = ('peer', 'msg_id', 'private')
    def __init__(self, peer: 'InputPeer', msg_id: int, private: 'PaidReactionPrivacy'):
        self.peer = peer
        self.msg_id = msg_id
        self.private = private
    def to_dict(self):
        return {"peer": self.peer, "msg_id": self.msg_id, "private": self.private}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1129874869, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.msg_id, signed=True)
        writer.write(bytes(self.private))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        msg_id = reader.read_int()
        private = reader.tgread_object()
        return cls(peer, msg_id, private)

@register
class MessagesGetPaidReactionPrivacy(TLObject):
    CONSTRUCTOR_ID = 1193563562
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1193563562, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class MessagesViewSponsoredMessage(TLObject):
    CONSTRUCTOR_ID = 647902787
    __slots__ = ('random_id')
    def __init__(self, random_id: bytes):
        self.random_id = random_id
    def to_dict(self):
        return {"random_id": self.random_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(647902787, signed=False)
        writer.write_bytes(self.random_id)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        random_id = reader.read_bytes()
        return cls(random_id)

@register
class MessagesClickSponsoredMessage(TLObject):
    CONSTRUCTOR_ID = 2184512894
    __slots__ = ('media', 'fullscreen', 'random_id')
    def __init__(self, random_id: bytes, media: bool = None, fullscreen: bool = None):
        self.media = media
        self.fullscreen = fullscreen
        self.random_id = random_id
    def to_dict(self):
        return {"media": self.media, "fullscreen": self.fullscreen, "random_id": self.random_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2184512894, signed=False)
        flags = 0
        if self.media: flags |= 1 << 0
        if self.fullscreen: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write_bytes(self.random_id)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        media = bool(flags & (1 << 0))
        fullscreen = bool(flags & (1 << 1))
        random_id = reader.read_bytes()
        return cls(media, fullscreen, random_id)

@register
class MessagesReportSponsoredMessage(TLObject):
    CONSTRUCTOR_ID = 315355332
    __slots__ = ('random_id', 'option')
    def __init__(self, random_id: bytes, option: bytes):
        self.random_id = random_id
        self.option = option
    def to_dict(self):
        return {"random_id": self.random_id, "option": self.option}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(315355332, signed=False)
        writer.write_bytes(self.random_id)
        writer.write_bytes(self.option)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        random_id = reader.read_bytes()
        option = reader.read_bytes()
        return cls(random_id, option)

@register
class MessagesGetSponsoredMessages(TLObject):
    CONSTRUCTOR_ID = 1030547536
    __slots__ = ('peer', 'msg_id')
    def __init__(self, peer: 'InputPeer', msg_id: int = None):
        self.peer = peer
        self.msg_id = msg_id
    def to_dict(self):
        return {"peer": self.peer, "msg_id": self.msg_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1030547536, signed=False)
        flags = 0
        if self.msg_id is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        if flags & (1 << 0):
            writer.write_int(self.msg_id, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        peer = reader.tgread_object()
        if flags & (1 << 0):
            msg_id = reader.read_int()
        else:
            msg_id = None
        return cls(peer, msg_id)

@register
class MessagesSavePreparedInlineMessage(TLObject):
    CONSTRUCTOR_ID = 4062150447
    __slots__ = ('result', 'user_id', 'peer_types')
    def __init__(self, result: 'InputBotInlineResult', user_id: 'InputUser', peer_types: 'Vector' = None):
        self.result = result
        self.user_id = user_id
        self.peer_types = peer_types
    def to_dict(self):
        return {"result": self.result, "user_id": self.user_id, "peer_types": self.peer_types}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4062150447, signed=False)
        flags = 0
        if self.peer_types is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.result))
        writer.write(bytes(self.user_id))
        if flags & (1 << 0):
            writer.write(bytes(self.peer_types))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        result = reader.tgread_object()
        user_id = reader.tgread_object()
        if flags & (1 << 0):
            peer_types = reader.tgread_object()
        else:
            peer_types = None
        return cls(result, user_id, peer_types)

@register
class MessagesGetPreparedInlineMessage(TLObject):
    CONSTRUCTOR_ID = 2239675832
    __slots__ = ('bot', 'id')
    def __init__(self, bot: 'InputUser', id: str):
        self.bot = bot
        self.id = id
    def to_dict(self):
        return {"bot": self.bot, "id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2239675832, signed=False)
        writer.write(bytes(self.bot))
        writer.write_string(self.id)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        bot = reader.tgread_object()
        id = reader.read_string()
        return cls(bot, id)

@register
class MessagesSearchStickers(TLObject):
    CONSTRUCTOR_ID = 699516522
    __slots__ = ('emojis', 'q', 'emoticon', 'lang_code', 'offset', 'limit', 'hash')
    def __init__(self, q: str, emoticon: str, lang_code: 'Vector', offset: int, limit: int, hash: int, emojis: bool = None):
        self.emojis = emojis
        self.q = q
        self.emoticon = emoticon
        self.lang_code = lang_code
        self.offset = offset
        self.limit = limit
        self.hash = hash
    def to_dict(self):
        return {"emojis": self.emojis, "q": self.q, "emoticon": self.emoticon, "lang_code": self.lang_code, "offset": self.offset, "limit": self.limit, "hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(699516522, signed=False)
        flags = 0
        if self.emojis: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write_string(self.q)
        writer.write_string(self.emoticon)
        writer.write(bytes(self.lang_code))
        writer.write_int(self.offset, signed=True)
        writer.write_int(self.limit, signed=True)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        emojis = bool(flags & (1 << 0))
        q = reader.read_string()
        emoticon = reader.read_string()
        lang_code = reader.tgread_object()
        offset = reader.read_int()
        limit = reader.read_int()
        hash = reader.read_long()
        return cls(emojis, q, emoticon, lang_code, offset, limit, hash)

@register
class MessagesReportMessagesDelivery(TLObject):
    CONSTRUCTOR_ID = 1517122453
    __slots__ = ('push', 'peer', 'id')
    def __init__(self, peer: 'InputPeer', id: 'Vector', push: bool = None):
        self.push = push
        self.peer = peer
        self.id = id
    def to_dict(self):
        return {"push": self.push, "peer": self.peer, "id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1517122453, signed=False)
        flags = 0
        if self.push: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        push = bool(flags & (1 << 0))
        peer = reader.tgread_object()
        id = reader.tgread_object()
        return cls(push, peer, id)

@register
class MessagesGetSavedDialogsByID(TLObject):
    CONSTRUCTOR_ID = 1869585558
    __slots__ = ('parent_peer', 'ids')
    def __init__(self, ids: 'Vector', parent_peer: 'InputPeer' = None):
        self.parent_peer = parent_peer
        self.ids = ids
    def to_dict(self):
        return {"parent_peer": self.parent_peer, "ids": self.ids}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1869585558, signed=False)
        flags = 0
        if self.parent_peer is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        if flags & (1 << 1):
            writer.write(bytes(self.parent_peer))
        writer.write(bytes(self.ids))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        if flags & (1 << 1):
            parent_peer = reader.tgread_object()
        else:
            parent_peer = None
        ids = reader.tgread_object()
        return cls(parent_peer, ids)

@register
class MessagesReadSavedHistory(TLObject):
    CONSTRUCTOR_ID = 3125427035
    __slots__ = ('parent_peer', 'peer', 'max_id')
    def __init__(self, parent_peer: 'InputPeer', peer: 'InputPeer', max_id: int):
        self.parent_peer = parent_peer
        self.peer = peer
        self.max_id = max_id
    def to_dict(self):
        return {"parent_peer": self.parent_peer, "peer": self.peer, "max_id": self.max_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3125427035, signed=False)
        writer.write(bytes(self.parent_peer))
        writer.write(bytes(self.peer))
        writer.write_int(self.max_id, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        parent_peer = reader.tgread_object()
        peer = reader.tgread_object()
        max_id = reader.read_int()
        return cls(parent_peer, peer, max_id)

@register
class MessagesToggleTodoCompleted(TLObject):
    CONSTRUCTOR_ID = 3554685220
    __slots__ = ('peer', 'msg_id', 'completed', 'incompleted')
    def __init__(self, peer: 'InputPeer', msg_id: int, completed: 'Vector', incompleted: 'Vector'):
        self.peer = peer
        self.msg_id = msg_id
        self.completed = completed
        self.incompleted = incompleted
    def to_dict(self):
        return {"peer": self.peer, "msg_id": self.msg_id, "completed": self.completed, "incompleted": self.incompleted}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3554685220, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.msg_id, signed=True)
        writer.write(bytes(self.completed))
        writer.write(bytes(self.incompleted))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        msg_id = reader.read_int()
        completed = reader.tgread_object()
        incompleted = reader.tgread_object()
        return cls(peer, msg_id, completed, incompleted)

@register
class MessagesAppendTodoList(TLObject):
    CONSTRUCTOR_ID = 564531287
    __slots__ = ('peer', 'msg_id', 'list')
    def __init__(self, peer: 'InputPeer', msg_id: int, list: 'Vector'):
        self.peer = peer
        self.msg_id = msg_id
        self.list = list
    def to_dict(self):
        return {"peer": self.peer, "msg_id": self.msg_id, "list": self.list}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(564531287, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.msg_id, signed=True)
        writer.write(bytes(self.list))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        msg_id = reader.read_int()
        list = reader.tgread_object()
        return cls(peer, msg_id, list)

@register
class MessagesToggleSuggestedPostApproval(TLObject):
    CONSTRUCTOR_ID = 2164737372
    __slots__ = ('reject', 'peer', 'msg_id', 'schedule_date', 'reject_comment')
    def __init__(self, peer: 'InputPeer', msg_id: int, reject: bool = None, schedule_date: int = None, reject_comment: str = None):
        self.reject = reject
        self.peer = peer
        self.msg_id = msg_id
        self.schedule_date = schedule_date
        self.reject_comment = reject_comment
    def to_dict(self):
        return {"reject": self.reject, "peer": self.peer, "msg_id": self.msg_id, "schedule_date": self.schedule_date, "reject_comment": self.reject_comment}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2164737372, signed=False)
        flags = 0
        if self.reject: flags |= 1 << 1
        if self.schedule_date is not None: flags |= 1 << 0
        if self.reject_comment is not None: flags |= 1 << 2
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.msg_id, signed=True)
        if flags & (1 << 0):
            writer.write_int(self.schedule_date, signed=True)
        if flags & (1 << 2):
            writer.write_string(self.reject_comment)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        reject = bool(flags & (1 << 1))
        peer = reader.tgread_object()
        msg_id = reader.read_int()
        if flags & (1 << 0):
            schedule_date = reader.read_int()
        else:
            schedule_date = None
        if flags & (1 << 2):
            reject_comment = reader.read_string()
        else:
            reject_comment = None
        return cls(reject, peer, msg_id, schedule_date, reject_comment)

@register
class MessagesGetForumTopics(TLObject):
    CONSTRUCTOR_ID = 1000635391
    __slots__ = ('peer', 'q', 'offset_date', 'offset_id', 'offset_topic', 'limit')
    def __init__(self, peer: 'InputPeer', offset_date: int, offset_id: int, offset_topic: int, limit: int, q: str = None):
        self.peer = peer
        self.q = q
        self.offset_date = offset_date
        self.offset_id = offset_id
        self.offset_topic = offset_topic
        self.limit = limit
    def to_dict(self):
        return {"peer": self.peer, "q": self.q, "offset_date": self.offset_date, "offset_id": self.offset_id, "offset_topic": self.offset_topic, "limit": self.limit}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1000635391, signed=False)
        flags = 0
        if self.q is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        if flags & (1 << 0):
            writer.write_string(self.q)
        writer.write_int(self.offset_date, signed=True)
        writer.write_int(self.offset_id, signed=True)
        writer.write_int(self.offset_topic, signed=True)
        writer.write_int(self.limit, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        peer = reader.tgread_object()
        if flags & (1 << 0):
            q = reader.read_string()
        else:
            q = None
        offset_date = reader.read_int()
        offset_id = reader.read_int()
        offset_topic = reader.read_int()
        limit = reader.read_int()
        return cls(peer, q, offset_date, offset_id, offset_topic, limit)

@register
class MessagesGetForumTopicsByID(TLObject):
    CONSTRUCTOR_ID = 2936687112
    __slots__ = ('peer', 'topics')
    def __init__(self, peer: 'InputPeer', topics: 'Vector'):
        self.peer = peer
        self.topics = topics
    def to_dict(self):
        return {"peer": self.peer, "topics": self.topics}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2936687112, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.topics))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        topics = reader.tgread_object()
        return cls(peer, topics)

@register
class MessagesEditForumTopic(TLObject):
    CONSTRUCTOR_ID = 3469480244
    __slots__ = ('peer', 'topic_id', 'title', 'icon_emoji_id', 'closed', 'hidden')
    def __init__(self, peer: 'InputPeer', topic_id: int, title: str = None, icon_emoji_id: int = None, closed: bool = None, hidden: bool = None):
        self.peer = peer
        self.topic_id = topic_id
        self.title = title
        self.icon_emoji_id = icon_emoji_id
        self.closed = closed
        self.hidden = hidden
    def to_dict(self):
        return {"peer": self.peer, "topic_id": self.topic_id, "title": self.title, "icon_emoji_id": self.icon_emoji_id, "closed": self.closed, "hidden": self.hidden}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3469480244, signed=False)
        flags = 0
        if self.title is not None: flags |= 1 << 0
        if self.icon_emoji_id is not None: flags |= 1 << 1
        if self.closed is not None: flags |= 1 << 2
        if self.hidden is not None: flags |= 1 << 3
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.topic_id, signed=True)
        if flags & (1 << 0):
            writer.write_string(self.title)
        if flags & (1 << 1):
            writer.write_long(self.icon_emoji_id, signed=False)
        if flags & (1 << 2):
            writer.write(serialize_bool(self.closed))
        if flags & (1 << 3):
            writer.write(serialize_bool(self.hidden))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        peer = reader.tgread_object()
        topic_id = reader.read_int()
        if flags & (1 << 0):
            title = reader.read_string()
        else:
            title = None
        if flags & (1 << 1):
            icon_emoji_id = reader.read_long()
        else:
            icon_emoji_id = None
        if flags & (1 << 2):
            closed = reader.tgread_bool()
        else:
            closed = None
        if flags & (1 << 3):
            hidden = reader.tgread_bool()
        else:
            hidden = None
        return cls(peer, topic_id, title, icon_emoji_id, closed, hidden)

@register
class MessagesUpdatePinnedForumTopic(TLObject):
    CONSTRUCTOR_ID = 392032849
    __slots__ = ('peer', 'topic_id', 'pinned')
    def __init__(self, peer: 'InputPeer', topic_id: int, pinned: bool):
        self.peer = peer
        self.topic_id = topic_id
        self.pinned = pinned
    def to_dict(self):
        return {"peer": self.peer, "topic_id": self.topic_id, "pinned": self.pinned}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(392032849, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.topic_id, signed=True)
        writer.write(serialize_bool(self.pinned))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        topic_id = reader.read_int()
        pinned = reader.tgread_bool()
        return cls(peer, topic_id, pinned)

@register
class MessagesReorderPinnedForumTopics(TLObject):
    CONSTRUCTOR_ID = 242762224
    __slots__ = ('force', 'peer', 'order')
    def __init__(self, peer: 'InputPeer', order: 'Vector', force: bool = None):
        self.force = force
        self.peer = peer
        self.order = order
    def to_dict(self):
        return {"force": self.force, "peer": self.peer, "order": self.order}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(242762224, signed=False)
        flags = 0
        if self.force: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.order))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        force = bool(flags & (1 << 0))
        peer = reader.tgread_object()
        order = reader.tgread_object()
        return cls(force, peer, order)

@register
class MessagesCreateForumTopic(TLObject):
    CONSTRUCTOR_ID = 798540757
    __slots__ = ('title_missing', 'peer', 'title', 'icon_color', 'icon_emoji_id', 'random_id', 'send_as')
    def __init__(self, peer: 'InputPeer', title: str, random_id: int, title_missing: bool = None, icon_color: int = None, icon_emoji_id: int = None, send_as: 'InputPeer' = None):
        self.title_missing = title_missing
        self.peer = peer
        self.title = title
        self.icon_color = icon_color
        self.icon_emoji_id = icon_emoji_id
        self.random_id = random_id
        self.send_as = send_as
    def to_dict(self):
        return {"title_missing": self.title_missing, "peer": self.peer, "title": self.title, "icon_color": self.icon_color, "icon_emoji_id": self.icon_emoji_id, "random_id": self.random_id, "send_as": self.send_as}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(798540757, signed=False)
        flags = 0
        if self.title_missing: flags |= 1 << 4
        if self.icon_color is not None: flags |= 1 << 0
        if self.icon_emoji_id is not None: flags |= 1 << 3
        if self.send_as is not None: flags |= 1 << 2
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write_string(self.title)
        if flags & (1 << 0):
            writer.write_int(self.icon_color, signed=True)
        if flags & (1 << 3):
            writer.write_long(self.icon_emoji_id, signed=False)
        writer.write_long(self.random_id, signed=False)
        if flags & (1 << 2):
            writer.write(bytes(self.send_as))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        title_missing = bool(flags & (1 << 4))
        peer = reader.tgread_object()
        title = reader.read_string()
        if flags & (1 << 0):
            icon_color = reader.read_int()
        else:
            icon_color = None
        if flags & (1 << 3):
            icon_emoji_id = reader.read_long()
        else:
            icon_emoji_id = None
        random_id = reader.read_long()
        if flags & (1 << 2):
            send_as = reader.tgread_object()
        else:
            send_as = None
        return cls(title_missing, peer, title, icon_color, icon_emoji_id, random_id, send_as)

@register
class MessagesDeleteTopicHistory(TLObject):
    CONSTRUCTOR_ID = 3531697936
    __slots__ = ('peer', 'top_msg_id')
    def __init__(self, peer: 'InputPeer', top_msg_id: int):
        self.peer = peer
        self.top_msg_id = top_msg_id
    def to_dict(self):
        return {"peer": self.peer, "top_msg_id": self.top_msg_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3531697936, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.top_msg_id, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        top_msg_id = reader.read_int()
        return cls(peer, top_msg_id)

@register
class MessagesGetEmojiGameInfo(TLObject):
    CONSTRUCTOR_ID = 4219374759
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4219374759, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class MessagesSummarizeText(TLObject):
    CONSTRUCTOR_ID = 2881213254
    __slots__ = ('peer', 'id', 'to_lang', 'tone')
    def __init__(self, peer: 'InputPeer', id: int, to_lang: str = None, tone: str = None):
        self.peer = peer
        self.id = id
        self.to_lang = to_lang
        self.tone = tone
    def to_dict(self):
        return {"peer": self.peer, "id": self.id, "to_lang": self.to_lang, "tone": self.tone}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2881213254, signed=False)
        flags = 0
        if self.to_lang is not None: flags |= 1 << 0
        if self.tone is not None: flags |= 1 << 2
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.id, signed=True)
        if flags & (1 << 0):
            writer.write_string(self.to_lang)
        if flags & (1 << 2):
            writer.write_string(self.tone)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        peer = reader.tgread_object()
        id = reader.read_int()
        if flags & (1 << 0):
            to_lang = reader.read_string()
        else:
            to_lang = None
        if flags & (1 << 2):
            tone = reader.read_string()
        else:
            tone = None
        return cls(peer, id, to_lang, tone)

@register
class MessagesEditChatCreator(TLObject):
    CONSTRUCTOR_ID = 4148410455
    __slots__ = ('peer', 'user_id', 'password')
    def __init__(self, peer: 'InputPeer', user_id: 'InputUser', password: 'InputCheckPasswordSRP'):
        self.peer = peer
        self.user_id = user_id
        self.password = password
    def to_dict(self):
        return {"peer": self.peer, "user_id": self.user_id, "password": self.password}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4148410455, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.user_id))
        writer.write(bytes(self.password))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        user_id = reader.tgread_object()
        password = reader.tgread_object()
        return cls(peer, user_id, password)

@register
class MessagesGetFutureChatCreatorAfterLeave(TLObject):
    CONSTRUCTOR_ID = 998051494
    __slots__ = ('peer')
    def __init__(self, peer: 'InputPeer'):
        self.peer = peer
    def to_dict(self):
        return {"peer": self.peer}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(998051494, signed=False)
        writer.write(bytes(self.peer))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        return cls(peer)

@register
class MessagesEditChatParticipantRank(TLObject):
    CONSTRUCTOR_ID = 2685350576
    __slots__ = ('peer', 'participant', 'rank')
    def __init__(self, peer: 'InputPeer', participant: 'InputPeer', rank: str):
        self.peer = peer
        self.participant = participant
        self.rank = rank
    def to_dict(self):
        return {"peer": self.peer, "participant": self.participant, "rank": self.rank}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2685350576, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.participant))
        writer.write_string(self.rank)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        participant = reader.tgread_object()
        rank = reader.read_string()
        return cls(peer, participant, rank)

@register
class MessagesDeclineUrlAuth(TLObject):
    CONSTRUCTOR_ID = 893610940
    __slots__ = ('url')
    def __init__(self, url: str):
        self.url = url
    def to_dict(self):
        return {"url": self.url}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(893610940, signed=False)
        writer.write_string(self.url)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        url = reader.read_string()
        return cls(url)

@register
class MessagesCheckUrlAuthMatchCode(TLObject):
    CONSTRUCTOR_ID = 3382999819
    __slots__ = ('url', 'match_code')
    def __init__(self, url: str, match_code: str):
        self.url = url
        self.match_code = match_code
    def to_dict(self):
        return {"url": self.url, "match_code": self.match_code}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3382999819, signed=False)
        writer.write_string(self.url)
        writer.write_string(self.match_code)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        url = reader.read_string()
        match_code = reader.read_string()
        return cls(url, match_code)

@register
class MessagesComposeMessageWithAI(TLObject):
    CONSTRUCTOR_ID = 3672950153
    __slots__ = ('proofread', 'emojify', 'text', 'translate_to_lang', 'tone')
    def __init__(self, text: 'TextWithEntities', proofread: bool = None, emojify: bool = None, translate_to_lang: str = None, tone: 'InputAiComposeTone' = None):
        self.proofread = proofread
        self.emojify = emojify
        self.text = text
        self.translate_to_lang = translate_to_lang
        self.tone = tone
    def to_dict(self):
        return {"proofread": self.proofread, "emojify": self.emojify, "text": self.text, "translate_to_lang": self.translate_to_lang, "tone": self.tone}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3672950153, signed=False)
        flags = 0
        if self.proofread: flags |= 1 << 0
        if self.emojify: flags |= 1 << 3
        if self.translate_to_lang is not None: flags |= 1 << 1
        if self.tone is not None: flags |= 1 << 2
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.text))
        if flags & (1 << 1):
            writer.write_string(self.translate_to_lang)
        if flags & (1 << 2):
            writer.write(bytes(self.tone))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        proofread = bool(flags & (1 << 0))
        emojify = bool(flags & (1 << 3))
        text = reader.tgread_object()
        if flags & (1 << 1):
            translate_to_lang = reader.read_string()
        else:
            translate_to_lang = None
        if flags & (1 << 2):
            tone = reader.tgread_object()
        else:
            tone = None
        return cls(proofread, emojify, text, translate_to_lang, tone)

@register
class MessagesReportReadMetrics(TLObject):
    CONSTRUCTOR_ID = 1080542694
    __slots__ = ('peer', 'metrics')
    def __init__(self, peer: 'InputPeer', metrics: 'Vector'):
        self.peer = peer
        self.metrics = metrics
    def to_dict(self):
        return {"peer": self.peer, "metrics": self.metrics}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1080542694, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.metrics))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        metrics = reader.tgread_object()
        return cls(peer, metrics)

@register
class MessagesReportMusicListen(TLObject):
    CONSTRUCTOR_ID = 3720140825
    __slots__ = ('id', 'listened_duration')
    def __init__(self, id: 'InputDocument', listened_duration: int):
        self.id = id
        self.listened_duration = listened_duration
    def to_dict(self):
        return {"id": self.id, "listened_duration": self.listened_duration}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3720140825, signed=False)
        writer.write(bytes(self.id))
        writer.write_int(self.listened_duration, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        id = reader.tgread_object()
        listened_duration = reader.read_int()
        return cls(id, listened_duration)

@register
class MessagesAddPollAnswer(TLObject):
    CONSTRUCTOR_ID = 431770477
    __slots__ = ('peer', 'msg_id', 'answer')
    def __init__(self, peer: 'InputPeer', msg_id: int, answer: 'PollAnswer'):
        self.peer = peer
        self.msg_id = msg_id
        self.answer = answer
    def to_dict(self):
        return {"peer": self.peer, "msg_id": self.msg_id, "answer": self.answer}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(431770477, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.msg_id, signed=True)
        writer.write(bytes(self.answer))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        msg_id = reader.read_int()
        answer = reader.tgread_object()
        return cls(peer, msg_id, answer)

@register
class MessagesDeletePollAnswer(TLObject):
    CONSTRUCTOR_ID = 2894398885
    __slots__ = ('peer', 'msg_id', 'option')
    def __init__(self, peer: 'InputPeer', msg_id: int, option: bytes):
        self.peer = peer
        self.msg_id = msg_id
        self.option = option
    def to_dict(self):
        return {"peer": self.peer, "msg_id": self.msg_id, "option": self.option}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2894398885, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.msg_id, signed=True)
        writer.write_bytes(self.option)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        msg_id = reader.read_int()
        option = reader.read_bytes()
        return cls(peer, msg_id, option)

@register
class MessagesGetUnreadPollVotes(TLObject):
    CONSTRUCTOR_ID = 1126722802
    __slots__ = ('peer', 'top_msg_id', 'offset_id', 'add_offset', 'limit', 'max_id', 'min_id')
    def __init__(self, peer: 'InputPeer', offset_id: int, add_offset: int, limit: int, max_id: int, min_id: int, top_msg_id: int = None):
        self.peer = peer
        self.top_msg_id = top_msg_id
        self.offset_id = offset_id
        self.add_offset = add_offset
        self.limit = limit
        self.max_id = max_id
        self.min_id = min_id
    def to_dict(self):
        return {"peer": self.peer, "top_msg_id": self.top_msg_id, "offset_id": self.offset_id, "add_offset": self.add_offset, "limit": self.limit, "max_id": self.max_id, "min_id": self.min_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1126722802, signed=False)
        flags = 0
        if self.top_msg_id is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        if flags & (1 << 0):
            writer.write_int(self.top_msg_id, signed=True)
        writer.write_int(self.offset_id, signed=True)
        writer.write_int(self.add_offset, signed=True)
        writer.write_int(self.limit, signed=True)
        writer.write_int(self.max_id, signed=True)
        writer.write_int(self.min_id, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        peer = reader.tgread_object()
        if flags & (1 << 0):
            top_msg_id = reader.read_int()
        else:
            top_msg_id = None
        offset_id = reader.read_int()
        add_offset = reader.read_int()
        limit = reader.read_int()
        max_id = reader.read_int()
        min_id = reader.read_int()
        return cls(peer, top_msg_id, offset_id, add_offset, limit, max_id, min_id)

@register
class MessagesReadPollVotes(TLObject):
    CONSTRUCTOR_ID = 388019416
    __slots__ = ('peer', 'top_msg_id')
    def __init__(self, peer: 'InputPeer', top_msg_id: int = None):
        self.peer = peer
        self.top_msg_id = top_msg_id
    def to_dict(self):
        return {"peer": self.peer, "top_msg_id": self.top_msg_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(388019416, signed=False)
        flags = 0
        if self.top_msg_id is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        if flags & (1 << 0):
            writer.write_int(self.top_msg_id, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        peer = reader.tgread_object()
        if flags & (1 << 0):
            top_msg_id = reader.read_int()
        else:
            top_msg_id = None
        return cls(peer, top_msg_id)

@register
class MessagesSetBotGuestChatResult(TLObject):
    CONSTRUCTOR_ID = 3102803683
    __slots__ = ('query_id', 'result')
    def __init__(self, query_id: int, result: 'InputBotInlineResult'):
        self.query_id = query_id
        self.result = result
    def to_dict(self):
        return {"query_id": self.query_id, "result": self.result}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3102803683, signed=False)
        writer.write_long(self.query_id, signed=False)
        writer.write(bytes(self.result))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        query_id = reader.read_long()
        result = reader.tgread_object()
        return cls(query_id, result)

@register
class MessagesDeleteParticipantReactions(TLObject):
    CONSTRUCTOR_ID = 2696416504
    __slots__ = ('peer', 'participant')
    def __init__(self, peer: 'InputPeer', participant: 'InputPeer'):
        self.peer = peer
        self.participant = participant
    def to_dict(self):
        return {"peer": self.peer, "participant": self.participant}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2696416504, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.participant))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        participant = reader.tgread_object()
        return cls(peer, participant)

@register
class MessagesDeleteParticipantReaction(TLObject):
    CONSTRUCTOR_ID = 3820484652
    __slots__ = ('peer', 'msg_id', 'participant')
    def __init__(self, peer: 'InputPeer', msg_id: int, participant: 'InputPeer'):
        self.peer = peer
        self.msg_id = msg_id
        self.participant = participant
    def to_dict(self):
        return {"peer": self.peer, "msg_id": self.msg_id, "participant": self.participant}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3820484652, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.msg_id, signed=True)
        writer.write(bytes(self.participant))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        msg_id = reader.read_int()
        participant = reader.tgread_object()
        return cls(peer, msg_id, participant)

@register
class MessagesGetPersonalChannelHistory(TLObject):
    CONSTRUCTOR_ID = 1442515350
    __slots__ = ('user_id', 'limit', 'max_id', 'min_id', 'hash')
    def __init__(self, user_id: 'InputUser', limit: int, max_id: int, min_id: int, hash: int):
        self.user_id = user_id
        self.limit = limit
        self.max_id = max_id
        self.min_id = min_id
        self.hash = hash
    def to_dict(self):
        return {"user_id": self.user_id, "limit": self.limit, "max_id": self.max_id, "min_id": self.min_id, "hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1442515350, signed=False)
        writer.write(bytes(self.user_id))
        writer.write_int(self.limit, signed=True)
        writer.write_int(self.max_id, signed=True)
        writer.write_int(self.min_id, signed=True)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        user_id = reader.tgread_object()
        limit = reader.read_int()
        max_id = reader.read_int()
        min_id = reader.read_int()
        hash = reader.read_long()
        return cls(user_id, limit, max_id, min_id, hash)

