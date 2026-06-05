"""Auto-generated TL types. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional, TYPE_CHECKING
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

@register
class MessagesDialogs(TLObject):
    CONSTRUCTOR_ID = 364538944
    __slots__ = ('dialogs', 'messages', 'chats', 'users')
    def __init__(self, dialogs: 'Vector', messages: 'Vector', chats: 'Vector', users: 'Vector'):
        self.dialogs = dialogs
        self.messages = messages
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"dialogs": self.dialogs, "messages": self.messages, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(364538944, signed=False)
        writer.write(bytes(self.dialogs))
        writer.write(bytes(self.messages))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        dialogs = reader.tgread_object()
        messages = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(dialogs, messages, chats, users)

@register
class MessagesDialogsSlice(TLObject):
    CONSTRUCTOR_ID = 1910543603
    __slots__ = ('count', 'dialogs', 'messages', 'chats', 'users')
    def __init__(self, count: int, dialogs: 'Vector', messages: 'Vector', chats: 'Vector', users: 'Vector'):
        self.count = count
        self.dialogs = dialogs
        self.messages = messages
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"count": self.count, "dialogs": self.dialogs, "messages": self.messages, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1910543603, signed=False)
        writer.write_int(self.count, signed=True)
        writer.write(bytes(self.dialogs))
        writer.write(bytes(self.messages))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        count = reader.read_int()
        dialogs = reader.tgread_object()
        messages = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(count, dialogs, messages, chats, users)

@register
class MessagesDialogsNotModified(TLObject):
    CONSTRUCTOR_ID = 4041467286
    __slots__ = ('count')
    def __init__(self, count: int):
        self.count = count
    def to_dict(self):
        return {"count": self.count}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4041467286, signed=False)
        writer.write_int(self.count, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        count = reader.read_int()
        return cls(count)

@register
class MessagesMessages(TLObject):
    CONSTRUCTOR_ID = 494135274
    __slots__ = ('messages', 'topics', 'chats', 'users')
    def __init__(self, messages: 'Vector', topics: 'Vector', chats: 'Vector', users: 'Vector'):
        self.messages = messages
        self.topics = topics
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"messages": self.messages, "topics": self.topics, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(494135274, signed=False)
        writer.write(bytes(self.messages))
        writer.write(bytes(self.topics))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        messages = reader.tgread_object()
        topics = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(messages, topics, chats, users)

@register
class MessagesMessagesSlice(TLObject):
    CONSTRUCTOR_ID = 1595959062
    __slots__ = ('inexact', 'count', 'next_rate', 'offset_id_offset', 'search_flood', 'messages', 'topics', 'chats', 'users')
    def __init__(self, count: int, messages: 'Vector', topics: 'Vector', chats: 'Vector', users: 'Vector', inexact: bool = None, next_rate: int = None, offset_id_offset: int = None, search_flood: 'SearchPostsFlood' = None):
        self.inexact = inexact
        self.count = count
        self.next_rate = next_rate
        self.offset_id_offset = offset_id_offset
        self.search_flood = search_flood
        self.messages = messages
        self.topics = topics
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"inexact": self.inexact, "count": self.count, "next_rate": self.next_rate, "offset_id_offset": self.offset_id_offset, "search_flood": self.search_flood, "messages": self.messages, "topics": self.topics, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1595959062, signed=False)
        flags = 0
        if self.inexact: flags |= 1 << 1
        if self.next_rate is not None: flags |= 1 << 0
        if self.offset_id_offset is not None: flags |= 1 << 2
        if self.search_flood is not None: flags |= 1 << 3
        writer.write_int(flags, signed=False)
        writer.write_int(self.count, signed=True)
        if flags & (1 << 0):
            writer.write_int(self.next_rate, signed=True)
        if flags & (1 << 2):
            writer.write_int(self.offset_id_offset, signed=True)
        if flags & (1 << 3):
            writer.write(bytes(self.search_flood))
        writer.write(bytes(self.messages))
        writer.write(bytes(self.topics))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        inexact = bool(flags & (1 << 1))
        count = reader.read_int()
        if flags & (1 << 0):
            next_rate = reader.read_int()
        else:
            next_rate = None
        if flags & (1 << 2):
            offset_id_offset = reader.read_int()
        else:
            offset_id_offset = None
        if flags & (1 << 3):
            search_flood = reader.tgread_object()
        else:
            search_flood = None
        messages = reader.tgread_object()
        topics = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(inexact, count, next_rate, offset_id_offset, search_flood, messages, topics, chats, users)

@register
class MessagesChannelMessages(TLObject):
    CONSTRUCTOR_ID = 3346446926
    __slots__ = ('inexact', 'pts', 'count', 'offset_id_offset', 'messages', 'topics', 'chats', 'users')
    def __init__(self, pts: int, count: int, messages: 'Vector', topics: 'Vector', chats: 'Vector', users: 'Vector', inexact: bool = None, offset_id_offset: int = None):
        self.inexact = inexact
        self.pts = pts
        self.count = count
        self.offset_id_offset = offset_id_offset
        self.messages = messages
        self.topics = topics
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"inexact": self.inexact, "pts": self.pts, "count": self.count, "offset_id_offset": self.offset_id_offset, "messages": self.messages, "topics": self.topics, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3346446926, signed=False)
        flags = 0
        if self.inexact: flags |= 1 << 1
        if self.offset_id_offset is not None: flags |= 1 << 2
        writer.write_int(flags, signed=False)
        writer.write_int(self.pts, signed=True)
        writer.write_int(self.count, signed=True)
        if flags & (1 << 2):
            writer.write_int(self.offset_id_offset, signed=True)
        writer.write(bytes(self.messages))
        writer.write(bytes(self.topics))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        inexact = bool(flags & (1 << 1))
        pts = reader.read_int()
        count = reader.read_int()
        if flags & (1 << 2):
            offset_id_offset = reader.read_int()
        else:
            offset_id_offset = None
        messages = reader.tgread_object()
        topics = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(inexact, pts, count, offset_id_offset, messages, topics, chats, users)

@register
class MessagesMessagesNotModified(TLObject):
    CONSTRUCTOR_ID = 1951620897
    __slots__ = ('count')
    def __init__(self, count: int):
        self.count = count
    def to_dict(self):
        return {"count": self.count}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1951620897, signed=False)
        writer.write_int(self.count, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        count = reader.read_int()
        return cls(count)

@register
class MessagesChats(TLObject):
    CONSTRUCTOR_ID = 1694474197
    __slots__ = ('chats')
    def __init__(self, chats: 'Vector'):
        self.chats = chats
    def to_dict(self):
        return {"chats": self.chats}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1694474197, signed=False)
        writer.write(bytes(self.chats))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        chats = reader.tgread_object()
        return cls(chats)

@register
class MessagesChatsSlice(TLObject):
    CONSTRUCTOR_ID = 2631405892
    __slots__ = ('count', 'chats')
    def __init__(self, count: int, chats: 'Vector'):
        self.count = count
        self.chats = chats
    def to_dict(self):
        return {"count": self.count, "chats": self.chats}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2631405892, signed=False)
        writer.write_int(self.count, signed=True)
        writer.write(bytes(self.chats))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        count = reader.read_int()
        chats = reader.tgread_object()
        return cls(count, chats)

@register
class MessagesChatFull(TLObject):
    CONSTRUCTOR_ID = 3856126364
    __slots__ = ('full_chat', 'chats', 'users')
    def __init__(self, full_chat: 'ChatFull', chats: 'Vector', users: 'Vector'):
        self.full_chat = full_chat
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"full_chat": self.full_chat, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3856126364, signed=False)
        writer.write(bytes(self.full_chat))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        full_chat = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(full_chat, chats, users)

@register
class MessagesAffectedHistory(TLObject):
    CONSTRUCTOR_ID = 3025955281
    __slots__ = ('pts', 'pts_count', 'offset')
    def __init__(self, pts: int, pts_count: int, offset: int):
        self.pts = pts
        self.pts_count = pts_count
        self.offset = offset
    def to_dict(self):
        return {"pts": self.pts, "pts_count": self.pts_count, "offset": self.offset}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3025955281, signed=False)
        writer.write_int(self.pts, signed=True)
        writer.write_int(self.pts_count, signed=True)
        writer.write_int(self.offset, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        pts = reader.read_int()
        pts_count = reader.read_int()
        offset = reader.read_int()
        return cls(pts, pts_count, offset)

@register
class MessagesDhConfigNotModified(TLObject):
    CONSTRUCTOR_ID = 3236054581
    __slots__ = ('random')
    def __init__(self, random: bytes):
        self.random = random
    def to_dict(self):
        return {"random": self.random}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3236054581, signed=False)
        writer.write_bytes(self.random)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        random = reader.read_bytes()
        return cls(random)

@register
class MessagesDhConfig(TLObject):
    CONSTRUCTOR_ID = 740433629
    __slots__ = ('g', 'p', 'version', 'random')
    def __init__(self, g: int, p: bytes, version: int, random: bytes):
        self.g = g
        self.p = p
        self.version = version
        self.random = random
    def to_dict(self):
        return {"g": self.g, "p": self.p, "version": self.version, "random": self.random}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(740433629, signed=False)
        writer.write_int(self.g, signed=True)
        writer.write_bytes(self.p)
        writer.write_int(self.version, signed=True)
        writer.write_bytes(self.random)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        g = reader.read_int()
        p = reader.read_bytes()
        version = reader.read_int()
        random = reader.read_bytes()
        return cls(g, p, version, random)

@register
class MessagesSentEncryptedMessage(TLObject):
    CONSTRUCTOR_ID = 1443858741
    __slots__ = ('date')
    def __init__(self, date: int):
        self.date = date
    def to_dict(self):
        return {"date": self.date}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1443858741, signed=False)
        writer.write_int(self.date, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        date = reader.read_int()
        return cls(date)

@register
class MessagesSentEncryptedFile(TLObject):
    CONSTRUCTOR_ID = 2492727090
    __slots__ = ('date', 'file')
    def __init__(self, date: int, file: 'EncryptedFile'):
        self.date = date
        self.file = file
    def to_dict(self):
        return {"date": self.date, "file": self.file}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2492727090, signed=False)
        writer.write_int(self.date, signed=True)
        writer.write(bytes(self.file))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        date = reader.read_int()
        file = reader.tgread_object()
        return cls(date, file)

@register
class MessagesStickersNotModified(TLObject):
    CONSTRUCTOR_ID = 4050950690
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4050950690, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class MessagesStickers(TLObject):
    CONSTRUCTOR_ID = 816245886
    __slots__ = ('hash', 'stickers')
    def __init__(self, hash: int, stickers: 'Vector'):
        self.hash = hash
        self.stickers = stickers
    def to_dict(self):
        return {"hash": self.hash, "stickers": self.stickers}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(816245886, signed=False)
        writer.write_long(self.hash, signed=False)
        writer.write(bytes(self.stickers))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_long()
        stickers = reader.tgread_object()
        return cls(hash, stickers)

@register
class MessagesAllStickersNotModified(TLObject):
    CONSTRUCTOR_ID = 3898999491
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3898999491, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class MessagesAllStickers(TLObject):
    CONSTRUCTOR_ID = 3451637435
    __slots__ = ('hash', 'sets')
    def __init__(self, hash: int, sets: 'Vector'):
        self.hash = hash
        self.sets = sets
    def to_dict(self):
        return {"hash": self.hash, "sets": self.sets}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3451637435, signed=False)
        writer.write_long(self.hash, signed=False)
        writer.write(bytes(self.sets))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_long()
        sets = reader.tgread_object()
        return cls(hash, sets)

@register
class MessagesAffectedMessages(TLObject):
    CONSTRUCTOR_ID = 2228326789
    __slots__ = ('pts', 'pts_count')
    def __init__(self, pts: int, pts_count: int):
        self.pts = pts
        self.pts_count = pts_count
    def to_dict(self):
        return {"pts": self.pts, "pts_count": self.pts_count}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2228326789, signed=False)
        writer.write_int(self.pts, signed=True)
        writer.write_int(self.pts_count, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        pts = reader.read_int()
        pts_count = reader.read_int()
        return cls(pts, pts_count)

@register
class MessagesStickerSet(TLObject):
    CONSTRUCTOR_ID = 1846886166
    __slots__ = ('set', 'packs', 'keywords', 'documents')
    def __init__(self, set: 'StickerSet', packs: 'Vector', keywords: 'Vector', documents: 'Vector'):
        self.set = set
        self.packs = packs
        self.keywords = keywords
        self.documents = documents
    def to_dict(self):
        return {"set": self.set, "packs": self.packs, "keywords": self.keywords, "documents": self.documents}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1846886166, signed=False)
        writer.write(bytes(self.set))
        writer.write(bytes(self.packs))
        writer.write(bytes(self.keywords))
        writer.write(bytes(self.documents))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        set = reader.tgread_object()
        packs = reader.tgread_object()
        keywords = reader.tgread_object()
        documents = reader.tgread_object()
        return cls(set, packs, keywords, documents)

@register
class MessagesStickerSetNotModified(TLObject):
    CONSTRUCTOR_ID = 3556320491
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3556320491, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class MessagesSavedGifsNotModified(TLObject):
    CONSTRUCTOR_ID = 3892468898
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3892468898, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class MessagesSavedGifs(TLObject):
    CONSTRUCTOR_ID = 2225089037
    __slots__ = ('hash', 'gifs')
    def __init__(self, hash: int, gifs: 'Vector'):
        self.hash = hash
        self.gifs = gifs
    def to_dict(self):
        return {"hash": self.hash, "gifs": self.gifs}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2225089037, signed=False)
        writer.write_long(self.hash, signed=False)
        writer.write(bytes(self.gifs))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_long()
        gifs = reader.tgread_object()
        return cls(hash, gifs)

@register
class MessagesBotResults(TLObject):
    CONSTRUCTOR_ID = 3760321270
    __slots__ = ('gallery', 'query_id', 'next_offset', 'switch_pm', 'switch_webview', 'results', 'cache_time', 'users')
    def __init__(self, query_id: int, results: 'Vector', cache_time: int, users: 'Vector', gallery: bool = None, next_offset: str = None, switch_pm: 'InlineBotSwitchPM' = None, switch_webview: 'InlineBotWebView' = None):
        self.gallery = gallery
        self.query_id = query_id
        self.next_offset = next_offset
        self.switch_pm = switch_pm
        self.switch_webview = switch_webview
        self.results = results
        self.cache_time = cache_time
        self.users = users
    def to_dict(self):
        return {"gallery": self.gallery, "query_id": self.query_id, "next_offset": self.next_offset, "switch_pm": self.switch_pm, "switch_webview": self.switch_webview, "results": self.results, "cache_time": self.cache_time, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3760321270, signed=False)
        flags = 0
        if self.gallery: flags |= 1 << 0
        if self.next_offset is not None: flags |= 1 << 1
        if self.switch_pm is not None: flags |= 1 << 2
        if self.switch_webview is not None: flags |= 1 << 3
        writer.write_int(flags, signed=False)
        writer.write_long(self.query_id, signed=False)
        if flags & (1 << 1):
            writer.write_string(self.next_offset)
        if flags & (1 << 2):
            writer.write(bytes(self.switch_pm))
        if flags & (1 << 3):
            writer.write(bytes(self.switch_webview))
        writer.write(bytes(self.results))
        writer.write_int(self.cache_time, signed=True)
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        gallery = bool(flags & (1 << 0))
        query_id = reader.read_long()
        if flags & (1 << 1):
            next_offset = reader.read_string()
        else:
            next_offset = None
        if flags & (1 << 2):
            switch_pm = reader.tgread_object()
        else:
            switch_pm = None
        if flags & (1 << 3):
            switch_webview = reader.tgread_object()
        else:
            switch_webview = None
        results = reader.tgread_object()
        cache_time = reader.read_int()
        users = reader.tgread_object()
        return cls(gallery, query_id, next_offset, switch_pm, switch_webview, results, cache_time, users)

@register
class MessagesBotCallbackAnswer(TLObject):
    CONSTRUCTOR_ID = 911761060
    __slots__ = ('alert', 'has_url', 'native_ui', 'message', 'url', 'cache_time')
    def __init__(self, cache_time: int, alert: bool = None, has_url: bool = None, native_ui: bool = None, message: str = None, url: str = None):
        self.alert = alert
        self.has_url = has_url
        self.native_ui = native_ui
        self.message = message
        self.url = url
        self.cache_time = cache_time
    def to_dict(self):
        return {"alert": self.alert, "has_url": self.has_url, "native_ui": self.native_ui, "message": self.message, "url": self.url, "cache_time": self.cache_time}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(911761060, signed=False)
        flags = 0
        if self.alert: flags |= 1 << 1
        if self.has_url: flags |= 1 << 3
        if self.native_ui: flags |= 1 << 4
        if self.message is not None: flags |= 1 << 0
        if self.url is not None: flags |= 1 << 2
        writer.write_int(flags, signed=False)
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
        has_url = bool(flags & (1 << 3))
        native_ui = bool(flags & (1 << 4))
        if flags & (1 << 0):
            message = reader.read_string()
        else:
            message = None
        if flags & (1 << 2):
            url = reader.read_string()
        else:
            url = None
        cache_time = reader.read_int()
        return cls(alert, has_url, native_ui, message, url, cache_time)

@register
class MessagesMessageEditData(TLObject):
    CONSTRUCTOR_ID = 649453030
    __slots__ = ('caption')
    def __init__(self, caption: bool = None):
        self.caption = caption
    def to_dict(self):
        return {"caption": self.caption}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(649453030, signed=False)
        flags = 0
        if self.caption: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        caption = bool(flags & (1 << 0))
        return cls(caption)

@register
class MessagesPeerDialogs(TLObject):
    CONSTRUCTOR_ID = 863093588
    __slots__ = ('dialogs', 'messages', 'chats', 'users', 'state')
    def __init__(self, dialogs: 'Vector', messages: 'Vector', chats: 'Vector', users: 'Vector', state: 'UpdatesState'):
        self.dialogs = dialogs
        self.messages = messages
        self.chats = chats
        self.users = users
        self.state = state
    def to_dict(self):
        return {"dialogs": self.dialogs, "messages": self.messages, "chats": self.chats, "users": self.users, "state": self.state}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(863093588, signed=False)
        writer.write(bytes(self.dialogs))
        writer.write(bytes(self.messages))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        writer.write(bytes(self.state))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        dialogs = reader.tgread_object()
        messages = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        state = reader.tgread_object()
        return cls(dialogs, messages, chats, users, state)

@register
class MessagesFeaturedStickersNotModified(TLObject):
    CONSTRUCTOR_ID = 3336309862
    __slots__ = ('count')
    def __init__(self, count: int):
        self.count = count
    def to_dict(self):
        return {"count": self.count}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3336309862, signed=False)
        writer.write_int(self.count, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        count = reader.read_int()
        return cls(count)

@register
class MessagesFeaturedStickers(TLObject):
    CONSTRUCTOR_ID = 3191351558
    __slots__ = ('premium', 'hash', 'count', 'sets', 'unread')
    def __init__(self, hash: int, count: int, sets: 'Vector', unread: 'Vector', premium: bool = None):
        self.premium = premium
        self.hash = hash
        self.count = count
        self.sets = sets
        self.unread = unread
    def to_dict(self):
        return {"premium": self.premium, "hash": self.hash, "count": self.count, "sets": self.sets, "unread": self.unread}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3191351558, signed=False)
        flags = 0
        if self.premium: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write_long(self.hash, signed=False)
        writer.write_int(self.count, signed=True)
        writer.write(bytes(self.sets))
        writer.write(bytes(self.unread))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        premium = bool(flags & (1 << 0))
        hash = reader.read_long()
        count = reader.read_int()
        sets = reader.tgread_object()
        unread = reader.tgread_object()
        return cls(premium, hash, count, sets, unread)

@register
class MessagesRecentStickersNotModified(TLObject):
    CONSTRUCTOR_ID = 186120336
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(186120336, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class MessagesRecentStickers(TLObject):
    CONSTRUCTOR_ID = 2295561302
    __slots__ = ('hash', 'packs', 'stickers', 'dates')
    def __init__(self, hash: int, packs: 'Vector', stickers: 'Vector', dates: 'Vector'):
        self.hash = hash
        self.packs = packs
        self.stickers = stickers
        self.dates = dates
    def to_dict(self):
        return {"hash": self.hash, "packs": self.packs, "stickers": self.stickers, "dates": self.dates}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2295561302, signed=False)
        writer.write_long(self.hash, signed=False)
        writer.write(bytes(self.packs))
        writer.write(bytes(self.stickers))
        writer.write(bytes(self.dates))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_long()
        packs = reader.tgread_object()
        stickers = reader.tgread_object()
        dates = reader.tgread_object()
        return cls(hash, packs, stickers, dates)

@register
class MessagesArchivedStickers(TLObject):
    CONSTRUCTOR_ID = 1338747336
    __slots__ = ('count', 'sets')
    def __init__(self, count: int, sets: 'Vector'):
        self.count = count
        self.sets = sets
    def to_dict(self):
        return {"count": self.count, "sets": self.sets}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1338747336, signed=False)
        writer.write_int(self.count, signed=True)
        writer.write(bytes(self.sets))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        count = reader.read_int()
        sets = reader.tgread_object()
        return cls(count, sets)

@register
class MessagesStickerSetInstallResultSuccess(TLObject):
    CONSTRUCTOR_ID = 946083368
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(946083368, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class MessagesStickerSetInstallResultArchive(TLObject):
    CONSTRUCTOR_ID = 904138920
    __slots__ = ('sets')
    def __init__(self, sets: 'Vector'):
        self.sets = sets
    def to_dict(self):
        return {"sets": self.sets}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(904138920, signed=False)
        writer.write(bytes(self.sets))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        sets = reader.tgread_object()
        return cls(sets)

@register
class MessagesHighScores(TLObject):
    CONSTRUCTOR_ID = 2587622809
    __slots__ = ('scores', 'users')
    def __init__(self, scores: 'Vector', users: 'Vector'):
        self.scores = scores
        self.users = users
    def to_dict(self):
        return {"scores": self.scores, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2587622809, signed=False)
        writer.write(bytes(self.scores))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        scores = reader.tgread_object()
        users = reader.tgread_object()
        return cls(scores, users)

@register
class MessagesFavedStickersNotModified(TLObject):
    CONSTRUCTOR_ID = 2660214483
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2660214483, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class MessagesFavedStickers(TLObject):
    CONSTRUCTOR_ID = 750063767
    __slots__ = ('hash', 'packs', 'stickers')
    def __init__(self, hash: int, packs: 'Vector', stickers: 'Vector'):
        self.hash = hash
        self.packs = packs
        self.stickers = stickers
    def to_dict(self):
        return {"hash": self.hash, "packs": self.packs, "stickers": self.stickers}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(750063767, signed=False)
        writer.write_long(self.hash, signed=False)
        writer.write(bytes(self.packs))
        writer.write(bytes(self.stickers))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_long()
        packs = reader.tgread_object()
        stickers = reader.tgread_object()
        return cls(hash, packs, stickers)

@register
class MessagesFoundStickerSetsNotModified(TLObject):
    CONSTRUCTOR_ID = 223655517
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(223655517, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class MessagesFoundStickerSets(TLObject):
    CONSTRUCTOR_ID = 2331024850
    __slots__ = ('hash', 'sets')
    def __init__(self, hash: int, sets: 'Vector'):
        self.hash = hash
        self.sets = sets
    def to_dict(self):
        return {"hash": self.hash, "sets": self.sets}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2331024850, signed=False)
        writer.write_long(self.hash, signed=False)
        writer.write(bytes(self.sets))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_long()
        sets = reader.tgread_object()
        return cls(hash, sets)

@register
class MessagesSearchCounter(TLObject):
    CONSTRUCTOR_ID = 3896830975
    __slots__ = ('inexact', 'filter', 'count')
    def __init__(self, filter: 'MessagesFilter', count: int, inexact: bool = None):
        self.inexact = inexact
        self.filter = filter
        self.count = count
    def to_dict(self):
        return {"inexact": self.inexact, "filter": self.filter, "count": self.count}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3896830975, signed=False)
        flags = 0
        if self.inexact: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.filter))
        writer.write_int(self.count, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        inexact = bool(flags & (1 << 1))
        filter = reader.tgread_object()
        count = reader.read_int()
        return cls(inexact, filter, count)

@register
class MessagesInactiveChats(TLObject):
    CONSTRUCTOR_ID = 2837970629
    __slots__ = ('dates', 'chats', 'users')
    def __init__(self, dates: 'Vector', chats: 'Vector', users: 'Vector'):
        self.dates = dates
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"dates": self.dates, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2837970629, signed=False)
        writer.write(bytes(self.dates))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        dates = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(dates, chats, users)

@register
class MessagesVotesList(TLObject):
    CONSTRUCTOR_ID = 1218005070
    __slots__ = ('count', 'votes', 'chats', 'users', 'next_offset')
    def __init__(self, count: int, votes: 'Vector', chats: 'Vector', users: 'Vector', next_offset: str = None):
        self.count = count
        self.votes = votes
        self.chats = chats
        self.users = users
        self.next_offset = next_offset
    def to_dict(self):
        return {"count": self.count, "votes": self.votes, "chats": self.chats, "users": self.users, "next_offset": self.next_offset}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1218005070, signed=False)
        flags = 0
        if self.next_offset is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write_int(self.count, signed=True)
        writer.write(bytes(self.votes))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        if flags & (1 << 0):
            writer.write_string(self.next_offset)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        count = reader.read_int()
        votes = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        if flags & (1 << 0):
            next_offset = reader.read_string()
        else:
            next_offset = None
        return cls(count, votes, chats, users, next_offset)

@register
class MessagesMessageViews(TLObject):
    CONSTRUCTOR_ID = 3066361155
    __slots__ = ('views', 'chats', 'users')
    def __init__(self, views: 'Vector', chats: 'Vector', users: 'Vector'):
        self.views = views
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"views": self.views, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3066361155, signed=False)
        writer.write(bytes(self.views))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        views = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(views, chats, users)

@register
class MessagesDiscussionMessage(TLObject):
    CONSTRUCTOR_ID = 2788431746
    __slots__ = ('messages', 'max_id', 'read_inbox_max_id', 'read_outbox_max_id', 'unread_count', 'chats', 'users')
    def __init__(self, messages: 'Vector', unread_count: int, chats: 'Vector', users: 'Vector', max_id: int = None, read_inbox_max_id: int = None, read_outbox_max_id: int = None):
        self.messages = messages
        self.max_id = max_id
        self.read_inbox_max_id = read_inbox_max_id
        self.read_outbox_max_id = read_outbox_max_id
        self.unread_count = unread_count
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"messages": self.messages, "max_id": self.max_id, "read_inbox_max_id": self.read_inbox_max_id, "read_outbox_max_id": self.read_outbox_max_id, "unread_count": self.unread_count, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2788431746, signed=False)
        flags = 0
        if self.max_id is not None: flags |= 1 << 0
        if self.read_inbox_max_id is not None: flags |= 1 << 1
        if self.read_outbox_max_id is not None: flags |= 1 << 2
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.messages))
        if flags & (1 << 0):
            writer.write_int(self.max_id, signed=True)
        if flags & (1 << 1):
            writer.write_int(self.read_inbox_max_id, signed=True)
        if flags & (1 << 2):
            writer.write_int(self.read_outbox_max_id, signed=True)
        writer.write_int(self.unread_count, signed=True)
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        messages = reader.tgread_object()
        if flags & (1 << 0):
            max_id = reader.read_int()
        else:
            max_id = None
        if flags & (1 << 1):
            read_inbox_max_id = reader.read_int()
        else:
            read_inbox_max_id = None
        if flags & (1 << 2):
            read_outbox_max_id = reader.read_int()
        else:
            read_outbox_max_id = None
        unread_count = reader.read_int()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(messages, max_id, read_inbox_max_id, read_outbox_max_id, unread_count, chats, users)

@register
class MessagesHistoryImport(TLObject):
    CONSTRUCTOR_ID = 375566091
    __slots__ = ('id')
    def __init__(self, id: int):
        self.id = id
    def to_dict(self):
        return {"id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(375566091, signed=False)
        writer.write_long(self.id, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        id = reader.read_long()
        return cls(id)

@register
class MessagesHistoryImportParsed(TLObject):
    CONSTRUCTOR_ID = 1578088377
    __slots__ = ('pm', 'group', 'title')
    def __init__(self, pm: bool = None, group: bool = None, title: str = None):
        self.pm = pm
        self.group = group
        self.title = title
    def to_dict(self):
        return {"pm": self.pm, "group": self.group, "title": self.title}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1578088377, signed=False)
        flags = 0
        if self.pm: flags |= 1 << 0
        if self.group: flags |= 1 << 1
        if self.title is not None: flags |= 1 << 2
        writer.write_int(flags, signed=False)
        if flags & (1 << 2):
            writer.write_string(self.title)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        pm = bool(flags & (1 << 0))
        group = bool(flags & (1 << 1))
        if flags & (1 << 2):
            title = reader.read_string()
        else:
            title = None
        return cls(pm, group, title)

@register
class MessagesAffectedFoundMessages(TLObject):
    CONSTRUCTOR_ID = 4019011180
    __slots__ = ('pts', 'pts_count', 'offset', 'messages')
    def __init__(self, pts: int, pts_count: int, offset: int, messages: 'Vector'):
        self.pts = pts
        self.pts_count = pts_count
        self.offset = offset
        self.messages = messages
    def to_dict(self):
        return {"pts": self.pts, "pts_count": self.pts_count, "offset": self.offset, "messages": self.messages}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4019011180, signed=False)
        writer.write_int(self.pts, signed=True)
        writer.write_int(self.pts_count, signed=True)
        writer.write_int(self.offset, signed=True)
        writer.write(bytes(self.messages))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        pts = reader.read_int()
        pts_count = reader.read_int()
        offset = reader.read_int()
        messages = reader.tgread_object()
        return cls(pts, pts_count, offset, messages)

@register
class MessagesExportedChatInvites(TLObject):
    CONSTRUCTOR_ID = 3183881676
    __slots__ = ('count', 'invites', 'users')
    def __init__(self, count: int, invites: 'Vector', users: 'Vector'):
        self.count = count
        self.invites = invites
        self.users = users
    def to_dict(self):
        return {"count": self.count, "invites": self.invites, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3183881676, signed=False)
        writer.write_int(self.count, signed=True)
        writer.write(bytes(self.invites))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        count = reader.read_int()
        invites = reader.tgread_object()
        users = reader.tgread_object()
        return cls(count, invites, users)

@register
class MessagesExportedChatInvite(TLObject):
    CONSTRUCTOR_ID = 410107472
    __slots__ = ('invite', 'users')
    def __init__(self, invite: 'ExportedChatInvite', users: 'Vector'):
        self.invite = invite
        self.users = users
    def to_dict(self):
        return {"invite": self.invite, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(410107472, signed=False)
        writer.write(bytes(self.invite))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        invite = reader.tgread_object()
        users = reader.tgread_object()
        return cls(invite, users)

@register
class MessagesExportedChatInviteReplaced(TLObject):
    CONSTRUCTOR_ID = 572915951
    __slots__ = ('invite', 'new_invite', 'users')
    def __init__(self, invite: 'ExportedChatInvite', new_invite: 'ExportedChatInvite', users: 'Vector'):
        self.invite = invite
        self.new_invite = new_invite
        self.users = users
    def to_dict(self):
        return {"invite": self.invite, "new_invite": self.new_invite, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(572915951, signed=False)
        writer.write(bytes(self.invite))
        writer.write(bytes(self.new_invite))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        invite = reader.tgread_object()
        new_invite = reader.tgread_object()
        users = reader.tgread_object()
        return cls(invite, new_invite, users)

@register
class MessagesChatInviteImporters(TLObject):
    CONSTRUCTOR_ID = 2176233482
    __slots__ = ('count', 'importers', 'users')
    def __init__(self, count: int, importers: 'Vector', users: 'Vector'):
        self.count = count
        self.importers = importers
        self.users = users
    def to_dict(self):
        return {"count": self.count, "importers": self.importers, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2176233482, signed=False)
        writer.write_int(self.count, signed=True)
        writer.write(bytes(self.importers))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        count = reader.read_int()
        importers = reader.tgread_object()
        users = reader.tgread_object()
        return cls(count, importers, users)

@register
class MessagesChatAdminsWithInvites(TLObject):
    CONSTRUCTOR_ID = 3063640791
    __slots__ = ('admins', 'users')
    def __init__(self, admins: 'Vector', users: 'Vector'):
        self.admins = admins
        self.users = users
    def to_dict(self):
        return {"admins": self.admins, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3063640791, signed=False)
        writer.write(bytes(self.admins))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        admins = reader.tgread_object()
        users = reader.tgread_object()
        return cls(admins, users)

@register
class MessagesCheckedHistoryImportPeer(TLObject):
    CONSTRUCTOR_ID = 2723014423
    __slots__ = ('confirm_text')
    def __init__(self, confirm_text: str):
        self.confirm_text = confirm_text
    def to_dict(self):
        return {"confirm_text": self.confirm_text}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2723014423, signed=False)
        writer.write_string(self.confirm_text)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        confirm_text = reader.read_string()
        return cls(confirm_text)

@register
class MessagesSponsoredMessages(TLObject):
    CONSTRUCTOR_ID = 4292502893
    __slots__ = ('posts_between', 'start_delay', 'between_delay', 'messages', 'chats', 'users')
    def __init__(self, messages: 'Vector', chats: 'Vector', users: 'Vector', posts_between: int = None, start_delay: int = None, between_delay: int = None):
        self.posts_between = posts_between
        self.start_delay = start_delay
        self.between_delay = between_delay
        self.messages = messages
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"posts_between": self.posts_between, "start_delay": self.start_delay, "between_delay": self.between_delay, "messages": self.messages, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4292502893, signed=False)
        flags = 0
        if self.posts_between is not None: flags |= 1 << 0
        if self.start_delay is not None: flags |= 1 << 1
        if self.between_delay is not None: flags |= 1 << 2
        writer.write_int(flags, signed=False)
        if flags & (1 << 0):
            writer.write_int(self.posts_between, signed=True)
        if flags & (1 << 1):
            writer.write_int(self.start_delay, signed=True)
        if flags & (1 << 2):
            writer.write_int(self.between_delay, signed=True)
        writer.write(bytes(self.messages))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        if flags & (1 << 0):
            posts_between = reader.read_int()
        else:
            posts_between = None
        if flags & (1 << 1):
            start_delay = reader.read_int()
        else:
            start_delay = None
        if flags & (1 << 2):
            between_delay = reader.read_int()
        else:
            between_delay = None
        messages = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(posts_between, start_delay, between_delay, messages, chats, users)

@register
class MessagesSponsoredMessagesEmpty(TLObject):
    CONSTRUCTOR_ID = 406407439
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(406407439, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class MessagesSearchResultsCalendar(TLObject):
    CONSTRUCTOR_ID = 343859772
    __slots__ = ('inexact', 'count', 'min_date', 'min_msg_id', 'offset_id_offset', 'periods', 'messages', 'chats', 'users')
    def __init__(self, count: int, min_date: int, min_msg_id: int, periods: 'Vector', messages: 'Vector', chats: 'Vector', users: 'Vector', inexact: bool = None, offset_id_offset: int = None):
        self.inexact = inexact
        self.count = count
        self.min_date = min_date
        self.min_msg_id = min_msg_id
        self.offset_id_offset = offset_id_offset
        self.periods = periods
        self.messages = messages
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"inexact": self.inexact, "count": self.count, "min_date": self.min_date, "min_msg_id": self.min_msg_id, "offset_id_offset": self.offset_id_offset, "periods": self.periods, "messages": self.messages, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(343859772, signed=False)
        flags = 0
        if self.inexact: flags |= 1 << 0
        if self.offset_id_offset is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write_int(self.count, signed=True)
        writer.write_int(self.min_date, signed=True)
        writer.write_int(self.min_msg_id, signed=True)
        if flags & (1 << 1):
            writer.write_int(self.offset_id_offset, signed=True)
        writer.write(bytes(self.periods))
        writer.write(bytes(self.messages))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        inexact = bool(flags & (1 << 0))
        count = reader.read_int()
        min_date = reader.read_int()
        min_msg_id = reader.read_int()
        if flags & (1 << 1):
            offset_id_offset = reader.read_int()
        else:
            offset_id_offset = None
        periods = reader.tgread_object()
        messages = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(inexact, count, min_date, min_msg_id, offset_id_offset, periods, messages, chats, users)

@register
class MessagesSearchResultsPositions(TLObject):
    CONSTRUCTOR_ID = 1404185519
    __slots__ = ('count', 'positions')
    def __init__(self, count: int, positions: 'Vector'):
        self.count = count
        self.positions = positions
    def to_dict(self):
        return {"count": self.count, "positions": self.positions}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1404185519, signed=False)
        writer.write_int(self.count, signed=True)
        writer.write(bytes(self.positions))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        count = reader.read_int()
        positions = reader.tgread_object()
        return cls(count, positions)

@register
class MessagesPeerSettings(TLObject):
    CONSTRUCTOR_ID = 1753266509
    __slots__ = ('settings', 'chats', 'users')
    def __init__(self, settings: 'PeerSettings', chats: 'Vector', users: 'Vector'):
        self.settings = settings
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"settings": self.settings, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1753266509, signed=False)
        writer.write(bytes(self.settings))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        settings = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(settings, chats, users)

@register
class MessagesMessageReactionsList(TLObject):
    CONSTRUCTOR_ID = 834488621
    __slots__ = ('count', 'reactions', 'chats', 'users', 'next_offset')
    def __init__(self, count: int, reactions: 'Vector', chats: 'Vector', users: 'Vector', next_offset: str = None):
        self.count = count
        self.reactions = reactions
        self.chats = chats
        self.users = users
        self.next_offset = next_offset
    def to_dict(self):
        return {"count": self.count, "reactions": self.reactions, "chats": self.chats, "users": self.users, "next_offset": self.next_offset}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(834488621, signed=False)
        flags = 0
        if self.next_offset is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write_int(self.count, signed=True)
        writer.write(bytes(self.reactions))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        if flags & (1 << 0):
            writer.write_string(self.next_offset)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        count = reader.read_int()
        reactions = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        if flags & (1 << 0):
            next_offset = reader.read_string()
        else:
            next_offset = None
        return cls(count, reactions, chats, users, next_offset)

@register
class MessagesAvailableReactionsNotModified(TLObject):
    CONSTRUCTOR_ID = 2668042583
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2668042583, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class MessagesAvailableReactions(TLObject):
    CONSTRUCTOR_ID = 1989032621
    __slots__ = ('hash', 'reactions')
    def __init__(self, hash: int, reactions: 'Vector'):
        self.hash = hash
        self.reactions = reactions
    def to_dict(self):
        return {"hash": self.hash, "reactions": self.reactions}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1989032621, signed=False)
        writer.write_int(self.hash, signed=True)
        writer.write(bytes(self.reactions))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_int()
        reactions = reader.tgread_object()
        return cls(hash, reactions)

@register
class MessagesTranscribedAudio(TLObject):
    CONSTRUCTOR_ID = 3485063511
    __slots__ = ('pending', 'transcription_id', 'text', 'trial_remains_num', 'trial_remains_until_date')
    def __init__(self, transcription_id: int, text: str, pending: bool = None, trial_remains_num: int = None, trial_remains_until_date: int = None):
        self.pending = pending
        self.transcription_id = transcription_id
        self.text = text
        self.trial_remains_num = trial_remains_num
        self.trial_remains_until_date = trial_remains_until_date
    def to_dict(self):
        return {"pending": self.pending, "transcription_id": self.transcription_id, "text": self.text, "trial_remains_num": self.trial_remains_num, "trial_remains_until_date": self.trial_remains_until_date}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3485063511, signed=False)
        flags = 0
        if self.pending: flags |= 1 << 0
        if self.trial_remains_num is not None: flags |= 1 << 1
        if self.trial_remains_until_date is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write_long(self.transcription_id, signed=False)
        writer.write_string(self.text)
        if flags & (1 << 1):
            writer.write_int(self.trial_remains_num, signed=True)
        if flags & (1 << 1):
            writer.write_int(self.trial_remains_until_date, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        pending = bool(flags & (1 << 0))
        transcription_id = reader.read_long()
        text = reader.read_string()
        if flags & (1 << 1):
            trial_remains_num = reader.read_int()
        else:
            trial_remains_num = None
        if flags & (1 << 1):
            trial_remains_until_date = reader.read_int()
        else:
            trial_remains_until_date = None
        return cls(pending, transcription_id, text, trial_remains_num, trial_remains_until_date)

@register
class MessagesReactionsNotModified(TLObject):
    CONSTRUCTOR_ID = 2960120799
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2960120799, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class MessagesReactions(TLObject):
    CONSTRUCTOR_ID = 3942512406
    __slots__ = ('hash', 'reactions')
    def __init__(self, hash: int, reactions: 'Vector'):
        self.hash = hash
        self.reactions = reactions
    def to_dict(self):
        return {"hash": self.hash, "reactions": self.reactions}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3942512406, signed=False)
        writer.write_long(self.hash, signed=False)
        writer.write(bytes(self.reactions))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_long()
        reactions = reader.tgread_object()
        return cls(hash, reactions)

@register
class MessagesForumTopics(TLObject):
    CONSTRUCTOR_ID = 913709011
    __slots__ = ('order_by_create_date', 'count', 'topics', 'messages', 'chats', 'users', 'pts')
    def __init__(self, count: int, topics: 'Vector', messages: 'Vector', chats: 'Vector', users: 'Vector', pts: int, order_by_create_date: bool = None):
        self.order_by_create_date = order_by_create_date
        self.count = count
        self.topics = topics
        self.messages = messages
        self.chats = chats
        self.users = users
        self.pts = pts
    def to_dict(self):
        return {"order_by_create_date": self.order_by_create_date, "count": self.count, "topics": self.topics, "messages": self.messages, "chats": self.chats, "users": self.users, "pts": self.pts}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(913709011, signed=False)
        flags = 0
        if self.order_by_create_date: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write_int(self.count, signed=True)
        writer.write(bytes(self.topics))
        writer.write(bytes(self.messages))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        writer.write_int(self.pts, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        order_by_create_date = bool(flags & (1 << 0))
        count = reader.read_int()
        topics = reader.tgread_object()
        messages = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        pts = reader.read_int()
        return cls(order_by_create_date, count, topics, messages, chats, users, pts)

@register
class MessagesEmojiGroupsNotModified(TLObject):
    CONSTRUCTOR_ID = 1874111879
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1874111879, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class MessagesEmojiGroups(TLObject):
    CONSTRUCTOR_ID = 2283780427
    __slots__ = ('hash', 'groups')
    def __init__(self, hash: int, groups: 'Vector'):
        self.hash = hash
        self.groups = groups
    def to_dict(self):
        return {"hash": self.hash, "groups": self.groups}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2283780427, signed=False)
        writer.write_int(self.hash, signed=True)
        writer.write(bytes(self.groups))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_int()
        groups = reader.tgread_object()
        return cls(hash, groups)

@register
class MessagesTranslateResult(TLObject):
    CONSTRUCTOR_ID = 870003448
    __slots__ = ('result')
    def __init__(self, result: 'Vector'):
        self.result = result
    def to_dict(self):
        return {"result": self.result}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(870003448, signed=False)
        writer.write(bytes(self.result))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        result = reader.tgread_object()
        return cls(result)

@register
class MessagesBotApp(TLObject):
    CONSTRUCTOR_ID = 3947933173
    __slots__ = ('inactive', 'request_write_access', 'has_settings', 'app')
    def __init__(self, app: 'BotApp', inactive: bool = None, request_write_access: bool = None, has_settings: bool = None):
        self.inactive = inactive
        self.request_write_access = request_write_access
        self.has_settings = has_settings
        self.app = app
    def to_dict(self):
        return {"inactive": self.inactive, "request_write_access": self.request_write_access, "has_settings": self.has_settings, "app": self.app}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3947933173, signed=False)
        flags = 0
        if self.inactive: flags |= 1 << 0
        if self.request_write_access: flags |= 1 << 1
        if self.has_settings: flags |= 1 << 2
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.app))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        inactive = bool(flags & (1 << 0))
        request_write_access = bool(flags & (1 << 1))
        has_settings = bool(flags & (1 << 2))
        app = reader.tgread_object()
        return cls(inactive, request_write_access, has_settings, app)

@register
class MessagesWebPage(TLObject):
    CONSTRUCTOR_ID = 4250800829
    __slots__ = ('webpage', 'chats', 'users')
    def __init__(self, webpage: 'WebPage', chats: 'Vector', users: 'Vector'):
        self.webpage = webpage
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"webpage": self.webpage, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4250800829, signed=False)
        writer.write(bytes(self.webpage))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        webpage = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(webpage, chats, users)

@register
class MessagesSavedDialogs(TLObject):
    CONSTRUCTOR_ID = 4164608545
    __slots__ = ('dialogs', 'messages', 'chats', 'users')
    def __init__(self, dialogs: 'Vector', messages: 'Vector', chats: 'Vector', users: 'Vector'):
        self.dialogs = dialogs
        self.messages = messages
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"dialogs": self.dialogs, "messages": self.messages, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4164608545, signed=False)
        writer.write(bytes(self.dialogs))
        writer.write(bytes(self.messages))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        dialogs = reader.tgread_object()
        messages = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(dialogs, messages, chats, users)

@register
class MessagesSavedDialogsSlice(TLObject):
    CONSTRUCTOR_ID = 1153080793
    __slots__ = ('count', 'dialogs', 'messages', 'chats', 'users')
    def __init__(self, count: int, dialogs: 'Vector', messages: 'Vector', chats: 'Vector', users: 'Vector'):
        self.count = count
        self.dialogs = dialogs
        self.messages = messages
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"count": self.count, "dialogs": self.dialogs, "messages": self.messages, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1153080793, signed=False)
        writer.write_int(self.count, signed=True)
        writer.write(bytes(self.dialogs))
        writer.write(bytes(self.messages))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        count = reader.read_int()
        dialogs = reader.tgread_object()
        messages = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(count, dialogs, messages, chats, users)

@register
class MessagesSavedDialogsNotModified(TLObject):
    CONSTRUCTOR_ID = 3223285736
    __slots__ = ('count')
    def __init__(self, count: int):
        self.count = count
    def to_dict(self):
        return {"count": self.count}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3223285736, signed=False)
        writer.write_int(self.count, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        count = reader.read_int()
        return cls(count)

@register
class MessagesSavedReactionTagsNotModified(TLObject):
    CONSTRUCTOR_ID = 2291882479
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2291882479, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class MessagesSavedReactionTags(TLObject):
    CONSTRUCTOR_ID = 844731658
    __slots__ = ('tags', 'hash')
    def __init__(self, tags: 'Vector', hash: int):
        self.tags = tags
        self.hash = hash
    def to_dict(self):
        return {"tags": self.tags, "hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(844731658, signed=False)
        writer.write(bytes(self.tags))
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        tags = reader.tgread_object()
        hash = reader.read_long()
        return cls(tags, hash)

@register
class MessagesQuickReplies(TLObject):
    CONSTRUCTOR_ID = 3331155605
    __slots__ = ('quick_replies', 'messages', 'chats', 'users')
    def __init__(self, quick_replies: 'Vector', messages: 'Vector', chats: 'Vector', users: 'Vector'):
        self.quick_replies = quick_replies
        self.messages = messages
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"quick_replies": self.quick_replies, "messages": self.messages, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3331155605, signed=False)
        writer.write(bytes(self.quick_replies))
        writer.write(bytes(self.messages))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        quick_replies = reader.tgread_object()
        messages = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(quick_replies, messages, chats, users)

@register
class MessagesQuickRepliesNotModified(TLObject):
    CONSTRUCTOR_ID = 1603398491
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1603398491, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class MessagesDialogFilters(TLObject):
    CONSTRUCTOR_ID = 718878489
    __slots__ = ('tags_enabled', 'filters')
    def __init__(self, filters: 'Vector', tags_enabled: bool = None):
        self.tags_enabled = tags_enabled
        self.filters = filters
    def to_dict(self):
        return {"tags_enabled": self.tags_enabled, "filters": self.filters}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(718878489, signed=False)
        flags = 0
        if self.tags_enabled: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.filters))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        tags_enabled = bool(flags & (1 << 0))
        filters = reader.tgread_object()
        return cls(tags_enabled, filters)

@register
class MessagesMyStickers(TLObject):
    CONSTRUCTOR_ID = 4211040925
    __slots__ = ('count', 'sets')
    def __init__(self, count: int, sets: 'Vector'):
        self.count = count
        self.sets = sets
    def to_dict(self):
        return {"count": self.count, "sets": self.sets}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4211040925, signed=False)
        writer.write_int(self.count, signed=True)
        writer.write(bytes(self.sets))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        count = reader.read_int()
        sets = reader.tgread_object()
        return cls(count, sets)

@register
class MessagesInvitedUsers(TLObject):
    CONSTRUCTOR_ID = 2136862630
    __slots__ = ('updates', 'missing_invitees')
    def __init__(self, updates: 'Updates', missing_invitees: 'Vector'):
        self.updates = updates
        self.missing_invitees = missing_invitees
    def to_dict(self):
        return {"updates": self.updates, "missing_invitees": self.missing_invitees}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2136862630, signed=False)
        writer.write(bytes(self.updates))
        writer.write(bytes(self.missing_invitees))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        updates = reader.tgread_object()
        missing_invitees = reader.tgread_object()
        return cls(updates, missing_invitees)

@register
class MessagesAvailableEffectsNotModified(TLObject):
    CONSTRUCTOR_ID = 3522009691
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3522009691, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class MessagesAvailableEffects(TLObject):
    CONSTRUCTOR_ID = 3185271150
    __slots__ = ('hash', 'effects', 'documents')
    def __init__(self, hash: int, effects: 'Vector', documents: 'Vector'):
        self.hash = hash
        self.effects = effects
        self.documents = documents
    def to_dict(self):
        return {"hash": self.hash, "effects": self.effects, "documents": self.documents}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3185271150, signed=False)
        writer.write_int(self.hash, signed=True)
        writer.write(bytes(self.effects))
        writer.write(bytes(self.documents))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_int()
        effects = reader.tgread_object()
        documents = reader.tgread_object()
        return cls(hash, effects, documents)

@register
class MessagesBotPreparedInlineMessage(TLObject):
    CONSTRUCTOR_ID = 2395931921
    __slots__ = ('id', 'expire_date')
    def __init__(self, id: str, expire_date: int):
        self.id = id
        self.expire_date = expire_date
    def to_dict(self):
        return {"id": self.id, "expire_date": self.expire_date}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2395931921, signed=False)
        writer.write_string(self.id)
        writer.write_int(self.expire_date, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        id = reader.read_string()
        expire_date = reader.read_int()
        return cls(id, expire_date)

@register
class MessagesPreparedInlineMessage(TLObject):
    CONSTRUCTOR_ID = 4283920525
    __slots__ = ('query_id', 'result', 'peer_types', 'cache_time', 'users')
    def __init__(self, query_id: int, result: 'BotInlineResult', peer_types: 'Vector', cache_time: int, users: 'Vector'):
        self.query_id = query_id
        self.result = result
        self.peer_types = peer_types
        self.cache_time = cache_time
        self.users = users
    def to_dict(self):
        return {"query_id": self.query_id, "result": self.result, "peer_types": self.peer_types, "cache_time": self.cache_time, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4283920525, signed=False)
        writer.write_long(self.query_id, signed=False)
        writer.write(bytes(self.result))
        writer.write(bytes(self.peer_types))
        writer.write_int(self.cache_time, signed=True)
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        query_id = reader.read_long()
        result = reader.tgread_object()
        peer_types = reader.tgread_object()
        cache_time = reader.read_int()
        users = reader.tgread_object()
        return cls(query_id, result, peer_types, cache_time, users)

@register
class MessagesFoundStickersNotModified(TLObject):
    CONSTRUCTOR_ID = 1611711796
    __slots__ = ('next_offset')
    def __init__(self, next_offset: int = None):
        self.next_offset = next_offset
    def to_dict(self):
        return {"next_offset": self.next_offset}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1611711796, signed=False)
        flags = 0
        if self.next_offset is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        if flags & (1 << 0):
            writer.write_int(self.next_offset, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        if flags & (1 << 0):
            next_offset = reader.read_int()
        else:
            next_offset = None
        return cls(next_offset)

@register
class MessagesFoundStickers(TLObject):
    CONSTRUCTOR_ID = 2194268816
    __slots__ = ('next_offset', 'hash', 'stickers')
    def __init__(self, hash: int, stickers: 'Vector', next_offset: int = None):
        self.next_offset = next_offset
        self.hash = hash
        self.stickers = stickers
    def to_dict(self):
        return {"next_offset": self.next_offset, "hash": self.hash, "stickers": self.stickers}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2194268816, signed=False)
        flags = 0
        if self.next_offset is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        if flags & (1 << 0):
            writer.write_int(self.next_offset, signed=True)
        writer.write_long(self.hash, signed=False)
        writer.write(bytes(self.stickers))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        if flags & (1 << 0):
            next_offset = reader.read_int()
        else:
            next_offset = None
        hash = reader.read_long()
        stickers = reader.tgread_object()
        return cls(next_offset, hash, stickers)

@register
class MessagesWebPagePreview(TLObject):
    CONSTRUCTOR_ID = 2358937772
    __slots__ = ('media', 'chats', 'users')
    def __init__(self, media: 'MessageMedia', chats: 'Vector', users: 'Vector'):
        self.media = media
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"media": self.media, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2358937772, signed=False)
        writer.write(bytes(self.media))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        media = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(media, chats, users)

@register
class MessagesEmojiGameOutcome(TLObject):
    CONSTRUCTOR_ID = 3660240455
    __slots__ = ('seed', 'stake_ton_amount', 'ton_amount')
    def __init__(self, seed: bytes, stake_ton_amount: int, ton_amount: int):
        self.seed = seed
        self.stake_ton_amount = stake_ton_amount
        self.ton_amount = ton_amount
    def to_dict(self):
        return {"seed": self.seed, "stake_ton_amount": self.stake_ton_amount, "ton_amount": self.ton_amount}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3660240455, signed=False)
        writer.write_bytes(self.seed)
        writer.write_long(self.stake_ton_amount, signed=False)
        writer.write_long(self.ton_amount, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        seed = reader.read_bytes()
        stake_ton_amount = reader.read_long()
        ton_amount = reader.read_long()
        return cls(seed, stake_ton_amount, ton_amount)

@register
class MessagesEmojiGameUnavailable(TLObject):
    CONSTRUCTOR_ID = 1508266805
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1508266805, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class MessagesEmojiGameDiceInfo(TLObject):
    CONSTRUCTOR_ID = 1155883043
    __slots__ = ('game_hash', 'prev_stake', 'current_streak', 'params', 'plays_left')
    def __init__(self, game_hash: str, prev_stake: int, current_streak: int, params: 'Vector', plays_left: int = None):
        self.game_hash = game_hash
        self.prev_stake = prev_stake
        self.current_streak = current_streak
        self.params = params
        self.plays_left = plays_left
    def to_dict(self):
        return {"game_hash": self.game_hash, "prev_stake": self.prev_stake, "current_streak": self.current_streak, "params": self.params, "plays_left": self.plays_left}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1155883043, signed=False)
        flags = 0
        if self.plays_left is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write_string(self.game_hash)
        writer.write_long(self.prev_stake, signed=False)
        writer.write_int(self.current_streak, signed=True)
        writer.write(bytes(self.params))
        if flags & (1 << 0):
            writer.write_int(self.plays_left, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        game_hash = reader.read_string()
        prev_stake = reader.read_long()
        current_streak = reader.read_int()
        params = reader.tgread_object()
        if flags & (1 << 0):
            plays_left = reader.read_int()
        else:
            plays_left = None
        return cls(game_hash, prev_stake, current_streak, params, plays_left)

@register
class MessagesComposedMessageWithAI(TLObject):
    CONSTRUCTOR_ID = 2430053882
    __slots__ = ('result_text', 'diff_text')
    def __init__(self, result_text: 'TextWithEntities', diff_text: 'TextWithEntities' = None):
        self.result_text = result_text
        self.diff_text = diff_text
    def to_dict(self):
        return {"result_text": self.result_text, "diff_text": self.diff_text}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2430053882, signed=False)
        flags = 0
        if self.diff_text is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.result_text))
        if flags & (1 << 0):
            writer.write(bytes(self.diff_text))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        result_text = reader.tgread_object()
        if flags & (1 << 0):
            diff_text = reader.tgread_object()
        else:
            diff_text = None
        return cls(result_text, diff_text)

