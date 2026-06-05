"""Auto-generated TL functions. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

@register
class HelpGetConfig(TLObject):
    CONSTRUCTOR_ID = 3304659051
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3304659051, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class HelpGetNearestDc(TLObject):
    CONSTRUCTOR_ID = 531836966
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(531836966, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class HelpGetAppUpdate(TLObject):
    CONSTRUCTOR_ID = 1378703997
    __slots__ = ('source')
    def __init__(self, source: str):
        self.source = source
    def to_dict(self):
        return {"source": self.source}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1378703997, signed=False)
        writer.write_string(self.source)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        source = reader.read_string()
        return cls(source)

@register
class HelpGetInviteText(TLObject):
    CONSTRUCTOR_ID = 1295590211
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1295590211, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class HelpGetSupport(TLObject):
    CONSTRUCTOR_ID = 2631862477
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2631862477, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class HelpSetBotUpdatesStatus(TLObject):
    CONSTRUCTOR_ID = 3961704397
    __slots__ = ('pending_updates_count', 'message')
    def __init__(self, pending_updates_count: int, message: str):
        self.pending_updates_count = pending_updates_count
        self.message = message
    def to_dict(self):
        return {"pending_updates_count": self.pending_updates_count, "message": self.message}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3961704397, signed=False)
        writer.write_int(self.pending_updates_count, signed=True)
        writer.write_string(self.message)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        pending_updates_count = reader.read_int()
        message = reader.read_string()
        return cls(pending_updates_count, message)

@register
class HelpGetCdnConfig(TLObject):
    CONSTRUCTOR_ID = 1375900482
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1375900482, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class HelpGetRecentMeUrls(TLObject):
    CONSTRUCTOR_ID = 1036054804
    __slots__ = ('referer')
    def __init__(self, referer: str):
        self.referer = referer
    def to_dict(self):
        return {"referer": self.referer}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1036054804, signed=False)
        writer.write_string(self.referer)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        referer = reader.read_string()
        return cls(referer)

@register
class HelpGetTermsOfServiceUpdate(TLObject):
    CONSTRUCTOR_ID = 749019089
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(749019089, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class HelpAcceptTermsOfService(TLObject):
    CONSTRUCTOR_ID = 4000511898
    __slots__ = ('id')
    def __init__(self, id: 'DataJSON'):
        self.id = id
    def to_dict(self):
        return {"id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4000511898, signed=False)
        writer.write(bytes(self.id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        id = reader.tgread_object()
        return cls(id)

@register
class HelpGetDeepLinkInfo(TLObject):
    CONSTRUCTOR_ID = 1072547679
    __slots__ = ('path')
    def __init__(self, path: str):
        self.path = path
    def to_dict(self):
        return {"path": self.path}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1072547679, signed=False)
        writer.write_string(self.path)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        path = reader.read_string()
        return cls(path)

@register
class HelpGetAppConfig(TLObject):
    CONSTRUCTOR_ID = 1642330196
    __slots__ = ('hash')
    def __init__(self, hash: int):
        self.hash = hash
    def to_dict(self):
        return {"hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1642330196, signed=False)
        writer.write_int(self.hash, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_int()
        return cls(hash)

@register
class HelpSaveAppLog(TLObject):
    CONSTRUCTOR_ID = 1862465352
    __slots__ = ('events')
    def __init__(self, events: 'Vector'):
        self.events = events
    def to_dict(self):
        return {"events": self.events}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1862465352, signed=False)
        writer.write(bytes(self.events))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        events = reader.tgread_object()
        return cls(events)

@register
class HelpGetPassportConfig(TLObject):
    CONSTRUCTOR_ID = 3328290056
    __slots__ = ('hash')
    def __init__(self, hash: int):
        self.hash = hash
    def to_dict(self):
        return {"hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3328290056, signed=False)
        writer.write_int(self.hash, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_int()
        return cls(hash)

@register
class HelpGetSupportName(TLObject):
    CONSTRUCTOR_ID = 3546343212
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3546343212, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class HelpGetUserInfo(TLObject):
    CONSTRUCTOR_ID = 59377875
    __slots__ = ('user_id')
    def __init__(self, user_id: 'InputUser'):
        self.user_id = user_id
    def to_dict(self):
        return {"user_id": self.user_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(59377875, signed=False)
        writer.write(bytes(self.user_id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        user_id = reader.tgread_object()
        return cls(user_id)

@register
class HelpEditUserInfo(TLObject):
    CONSTRUCTOR_ID = 1723407216
    __slots__ = ('user_id', 'message', 'entities')
    def __init__(self, user_id: 'InputUser', message: str, entities: 'Vector'):
        self.user_id = user_id
        self.message = message
        self.entities = entities
    def to_dict(self):
        return {"user_id": self.user_id, "message": self.message, "entities": self.entities}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1723407216, signed=False)
        writer.write(bytes(self.user_id))
        writer.write_string(self.message)
        writer.write(bytes(self.entities))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        user_id = reader.tgread_object()
        message = reader.read_string()
        entities = reader.tgread_object()
        return cls(user_id, message, entities)

@register
class HelpGetPromoData(TLObject):
    CONSTRUCTOR_ID = 3231151137
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3231151137, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class HelpHidePromoData(TLObject):
    CONSTRUCTOR_ID = 505748629
    __slots__ = ('peer')
    def __init__(self, peer: 'InputPeer'):
        self.peer = peer
    def to_dict(self):
        return {"peer": self.peer}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(505748629, signed=False)
        writer.write(bytes(self.peer))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        return cls(peer)

@register
class HelpDismissSuggestion(TLObject):
    CONSTRUCTOR_ID = 4111317665
    __slots__ = ('peer', 'suggestion')
    def __init__(self, peer: 'InputPeer', suggestion: str):
        self.peer = peer
        self.suggestion = suggestion
    def to_dict(self):
        return {"peer": self.peer, "suggestion": self.suggestion}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4111317665, signed=False)
        writer.write(bytes(self.peer))
        writer.write_string(self.suggestion)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        suggestion = reader.read_string()
        return cls(peer, suggestion)

@register
class HelpGetCountriesList(TLObject):
    CONSTRUCTOR_ID = 1935116200
    __slots__ = ('lang_code', 'hash')
    def __init__(self, lang_code: str, hash: int):
        self.lang_code = lang_code
        self.hash = hash
    def to_dict(self):
        return {"lang_code": self.lang_code, "hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1935116200, signed=False)
        writer.write_string(self.lang_code)
        writer.write_int(self.hash, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        lang_code = reader.read_string()
        hash = reader.read_int()
        return cls(lang_code, hash)

@register
class HelpGetPremiumPromo(TLObject):
    CONSTRUCTOR_ID = 3088815060
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3088815060, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class HelpGetPeerColors(TLObject):
    CONSTRUCTOR_ID = 3665884207
    __slots__ = ('hash')
    def __init__(self, hash: int):
        self.hash = hash
    def to_dict(self):
        return {"hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3665884207, signed=False)
        writer.write_int(self.hash, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_int()
        return cls(hash)

@register
class HelpGetPeerProfileColors(TLObject):
    CONSTRUCTOR_ID = 2882513405
    __slots__ = ('hash')
    def __init__(self, hash: int):
        self.hash = hash
    def to_dict(self):
        return {"hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2882513405, signed=False)
        writer.write_int(self.hash, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_int()
        return cls(hash)

@register
class HelpGetTimezonesList(TLObject):
    CONSTRUCTOR_ID = 1236468288
    __slots__ = ('hash')
    def __init__(self, hash: int):
        self.hash = hash
    def to_dict(self):
        return {"hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1236468288, signed=False)
        writer.write_int(self.hash, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_int()
        return cls(hash)

