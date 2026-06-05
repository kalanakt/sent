"""Auto-generated TL functions. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

@register
class PhotosUpdateProfilePhoto(TLObject):
    CONSTRUCTOR_ID = 166207545
    __slots__ = ('fallback', 'bot', 'id')
    def __init__(self, id: 'InputPhoto', fallback: bool = None, bot: 'InputUser' = None):
        self.fallback = fallback
        self.bot = bot
        self.id = id
    def to_dict(self):
        return {"fallback": self.fallback, "bot": self.bot, "id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(166207545, signed=False)
        flags = 0
        if self.fallback: flags |= 1 << 0
        if self.bot is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        if flags & (1 << 1):
            writer.write(bytes(self.bot))
        writer.write(bytes(self.id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        fallback = bool(flags & (1 << 0))
        if flags & (1 << 1):
            bot = reader.tgread_object()
        else:
            bot = None
        id = reader.tgread_object()
        return cls(fallback, bot, id)

@register
class PhotosUploadProfilePhoto(TLObject):
    CONSTRUCTOR_ID = 59286453
    __slots__ = ('fallback', 'bot', 'file', 'video', 'video_start_ts', 'video_emoji_markup')
    def __init__(self, fallback: bool = None, bot: 'InputUser' = None, file: 'InputFile' = None, video: 'InputFile' = None, video_start_ts: float = None, video_emoji_markup: 'VideoSize' = None):
        self.fallback = fallback
        self.bot = bot
        self.file = file
        self.video = video
        self.video_start_ts = video_start_ts
        self.video_emoji_markup = video_emoji_markup
    def to_dict(self):
        return {"fallback": self.fallback, "bot": self.bot, "file": self.file, "video": self.video, "video_start_ts": self.video_start_ts, "video_emoji_markup": self.video_emoji_markup}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(59286453, signed=False)
        flags = 0
        if self.fallback: flags |= 1 << 3
        if self.bot is not None: flags |= 1 << 5
        if self.file is not None: flags |= 1 << 0
        if self.video is not None: flags |= 1 << 1
        if self.video_start_ts is not None: flags |= 1 << 2
        if self.video_emoji_markup is not None: flags |= 1 << 4
        writer.write_int(flags, signed=False)
        if flags & (1 << 5):
            writer.write(bytes(self.bot))
        if flags & (1 << 0):
            writer.write(bytes(self.file))
        if flags & (1 << 1):
            writer.write(bytes(self.video))
        if flags & (1 << 2):
            writer.write_double(self.video_start_ts)
        if flags & (1 << 4):
            writer.write(bytes(self.video_emoji_markup))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        fallback = bool(flags & (1 << 3))
        if flags & (1 << 5):
            bot = reader.tgread_object()
        else:
            bot = None
        if flags & (1 << 0):
            file = reader.tgread_object()
        else:
            file = None
        if flags & (1 << 1):
            video = reader.tgread_object()
        else:
            video = None
        if flags & (1 << 2):
            video_start_ts = reader.read_double()
        else:
            video_start_ts = None
        if flags & (1 << 4):
            video_emoji_markup = reader.tgread_object()
        else:
            video_emoji_markup = None
        return cls(fallback, bot, file, video, video_start_ts, video_emoji_markup)

@register
class PhotosDeletePhotos(TLObject):
    CONSTRUCTOR_ID = 2278522671
    __slots__ = ('id')
    def __init__(self, id: 'Vector'):
        self.id = id
    def to_dict(self):
        return {"id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2278522671, signed=False)
        writer.write(bytes(self.id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        id = reader.tgread_object()
        return cls(id)

@register
class PhotosGetUserPhotos(TLObject):
    CONSTRUCTOR_ID = 2446144168
    __slots__ = ('user_id', 'offset', 'max_id', 'limit')
    def __init__(self, user_id: 'InputUser', offset: int, max_id: int, limit: int):
        self.user_id = user_id
        self.offset = offset
        self.max_id = max_id
        self.limit = limit
    def to_dict(self):
        return {"user_id": self.user_id, "offset": self.offset, "max_id": self.max_id, "limit": self.limit}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2446144168, signed=False)
        writer.write(bytes(self.user_id))
        writer.write_int(self.offset, signed=True)
        writer.write_long(self.max_id, signed=False)
        writer.write_int(self.limit, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        user_id = reader.tgread_object()
        offset = reader.read_int()
        max_id = reader.read_long()
        limit = reader.read_int()
        return cls(user_id, offset, max_id, limit)

@register
class PhotosUploadContactProfilePhoto(TLObject):
    CONSTRUCTOR_ID = 3779873393
    __slots__ = ('suggest', 'save', 'user_id', 'file', 'video', 'video_start_ts', 'video_emoji_markup')
    def __init__(self, user_id: 'InputUser', suggest: bool = None, save: bool = None, file: 'InputFile' = None, video: 'InputFile' = None, video_start_ts: float = None, video_emoji_markup: 'VideoSize' = None):
        self.suggest = suggest
        self.save = save
        self.user_id = user_id
        self.file = file
        self.video = video
        self.video_start_ts = video_start_ts
        self.video_emoji_markup = video_emoji_markup
    def to_dict(self):
        return {"suggest": self.suggest, "save": self.save, "user_id": self.user_id, "file": self.file, "video": self.video, "video_start_ts": self.video_start_ts, "video_emoji_markup": self.video_emoji_markup}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3779873393, signed=False)
        flags = 0
        if self.suggest: flags |= 1 << 3
        if self.save: flags |= 1 << 4
        if self.file is not None: flags |= 1 << 0
        if self.video is not None: flags |= 1 << 1
        if self.video_start_ts is not None: flags |= 1 << 2
        if self.video_emoji_markup is not None: flags |= 1 << 5
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.user_id))
        if flags & (1 << 0):
            writer.write(bytes(self.file))
        if flags & (1 << 1):
            writer.write(bytes(self.video))
        if flags & (1 << 2):
            writer.write_double(self.video_start_ts)
        if flags & (1 << 5):
            writer.write(bytes(self.video_emoji_markup))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        suggest = bool(flags & (1 << 3))
        save = bool(flags & (1 << 4))
        user_id = reader.tgread_object()
        if flags & (1 << 0):
            file = reader.tgread_object()
        else:
            file = None
        if flags & (1 << 1):
            video = reader.tgread_object()
        else:
            video = None
        if flags & (1 << 2):
            video_start_ts = reader.read_double()
        else:
            video_start_ts = None
        if flags & (1 << 5):
            video_emoji_markup = reader.tgread_object()
        else:
            video_emoji_markup = None
        return cls(suggest, save, user_id, file, video, video_start_ts, video_emoji_markup)

