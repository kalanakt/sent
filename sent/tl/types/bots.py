"""Auto-generated TL types. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional, TYPE_CHECKING
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

@register
class BotsBotInfo(TLObject):
    CONSTRUCTOR_ID = 3903288752
    __slots__ = ('name', 'about', 'description')
    def __init__(self, name: str, about: str, description: str):
        self.name = name
        self.about = about
        self.description = description
    def to_dict(self):
        return {"name": self.name, "about": self.about, "description": self.description}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3903288752, signed=False)
        writer.write_string(self.name)
        writer.write_string(self.about)
        writer.write_string(self.description)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        name = reader.read_string()
        about = reader.read_string()
        description = reader.read_string()
        return cls(name, about, description)

@register
class BotsPopularAppBots(TLObject):
    CONSTRUCTOR_ID = 428978491
    __slots__ = ('next_offset', 'users')
    def __init__(self, users: 'Vector', next_offset: str = None):
        self.next_offset = next_offset
        self.users = users
    def to_dict(self):
        return {"next_offset": self.next_offset, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(428978491, signed=False)
        flags = 0
        if self.next_offset is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        if flags & (1 << 0):
            writer.write_string(self.next_offset)
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        if flags & (1 << 0):
            next_offset = reader.read_string()
        else:
            next_offset = None
        users = reader.tgread_object()
        return cls(next_offset, users)

@register
class BotsPreviewInfo(TLObject):
    CONSTRUCTOR_ID = 212278628
    __slots__ = ('media', 'lang_codes')
    def __init__(self, media: 'Vector', lang_codes: 'Vector'):
        self.media = media
        self.lang_codes = lang_codes
    def to_dict(self):
        return {"media": self.media, "lang_codes": self.lang_codes}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(212278628, signed=False)
        writer.write(bytes(self.media))
        writer.write(bytes(self.lang_codes))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        media = reader.tgread_object()
        lang_codes = reader.tgread_object()
        return cls(media, lang_codes)

@register
class BotsExportedBotToken(TLObject):
    CONSTRUCTOR_ID = 1012971041
    __slots__ = ('token')
    def __init__(self, token: str):
        self.token = token
    def to_dict(self):
        return {"token": self.token}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1012971041, signed=False)
        writer.write_string(self.token)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        token = reader.read_string()
        return cls(token)

@register
class BotsRequestedButton(TLObject):
    CONSTRUCTOR_ID = 4047224023
    __slots__ = ('webapp_req_id')
    def __init__(self, webapp_req_id: str):
        self.webapp_req_id = webapp_req_id
    def to_dict(self):
        return {"webapp_req_id": self.webapp_req_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4047224023, signed=False)
        writer.write_string(self.webapp_req_id)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        webapp_req_id = reader.read_string()
        return cls(webapp_req_id)

@register
class BotsAccessSettings(TLObject):
    CONSTRUCTOR_ID = 3709845395
    __slots__ = ('restricted', 'add_users')
    def __init__(self, restricted: bool = None, add_users: 'Vector' = None):
        self.restricted = restricted
        self.add_users = add_users
    def to_dict(self):
        return {"restricted": self.restricted, "add_users": self.add_users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3709845395, signed=False)
        flags = 0
        if self.restricted: flags |= 1 << 0
        if self.add_users is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        if flags & (1 << 1):
            writer.write(bytes(self.add_users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        restricted = bool(flags & (1 << 0))
        if flags & (1 << 1):
            add_users = reader.tgread_object()
        else:
            add_users = None
        return cls(restricted, add_users)

