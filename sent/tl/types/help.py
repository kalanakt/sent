"""Auto-generated TL types. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional, TYPE_CHECKING
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

@register
class HelpConfigSimple(TLObject):
    CONSTRUCTOR_ID = 1515793004
    __slots__ = ('date', 'expires', 'rules')
    def __init__(self, date: int, expires: int, rules: 'Vector'):
        self.date = date
        self.expires = expires
        self.rules = rules
    def to_dict(self):
        return {"date": self.date, "expires": self.expires, "rules": self.rules}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1515793004, signed=False)
        writer.write_int(self.date, signed=True)
        writer.write_int(self.expires, signed=True)
        writer.write(bytes(self.rules))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        date = reader.read_int()
        expires = reader.read_int()
        rules = reader.tgread_object()
        return cls(date, expires, rules)

@register
class HelpAppUpdate(TLObject):
    CONSTRUCTOR_ID = 3434860080
    __slots__ = ('can_not_skip', 'id', 'version', 'text', 'entities', 'document', 'url', 'sticker')
    def __init__(self, id: int, version: str, text: str, entities: 'Vector', can_not_skip: bool = None, document: 'Document' = None, url: str = None, sticker: 'Document' = None):
        self.can_not_skip = can_not_skip
        self.id = id
        self.version = version
        self.text = text
        self.entities = entities
        self.document = document
        self.url = url
        self.sticker = sticker
    def to_dict(self):
        return {"can_not_skip": self.can_not_skip, "id": self.id, "version": self.version, "text": self.text, "entities": self.entities, "document": self.document, "url": self.url, "sticker": self.sticker}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3434860080, signed=False)
        flags = 0
        if self.can_not_skip: flags |= 1 << 0
        if self.document is not None: flags |= 1 << 1
        if self.url is not None: flags |= 1 << 2
        if self.sticker is not None: flags |= 1 << 3
        writer.write_int(flags, signed=False)
        writer.write_int(self.id, signed=True)
        writer.write_string(self.version)
        writer.write_string(self.text)
        writer.write(bytes(self.entities))
        if flags & (1 << 1):
            writer.write(bytes(self.document))
        if flags & (1 << 2):
            writer.write_string(self.url)
        if flags & (1 << 3):
            writer.write(bytes(self.sticker))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        can_not_skip = bool(flags & (1 << 0))
        id = reader.read_int()
        version = reader.read_string()
        text = reader.read_string()
        entities = reader.tgread_object()
        if flags & (1 << 1):
            document = reader.tgread_object()
        else:
            document = None
        if flags & (1 << 2):
            url = reader.read_string()
        else:
            url = None
        if flags & (1 << 3):
            sticker = reader.tgread_object()
        else:
            sticker = None
        return cls(can_not_skip, id, version, text, entities, document, url, sticker)

@register
class HelpNoAppUpdate(TLObject):
    CONSTRUCTOR_ID = 3294258486
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3294258486, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class HelpInviteText(TLObject):
    CONSTRUCTOR_ID = 415997816
    __slots__ = ('message')
    def __init__(self, message: str):
        self.message = message
    def to_dict(self):
        return {"message": self.message}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(415997816, signed=False)
        writer.write_string(self.message)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        message = reader.read_string()
        return cls(message)

@register
class HelpSupport(TLObject):
    CONSTRUCTOR_ID = 398898678
    __slots__ = ('phone_number', 'user')
    def __init__(self, phone_number: str, user: 'User'):
        self.phone_number = phone_number
        self.user = user
    def to_dict(self):
        return {"phone_number": self.phone_number, "user": self.user}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(398898678, signed=False)
        writer.write_string(self.phone_number)
        writer.write(bytes(self.user))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        phone_number = reader.read_string()
        user = reader.tgread_object()
        return cls(phone_number, user)

@register
class HelpTermsOfService(TLObject):
    CONSTRUCTOR_ID = 2013922064
    __slots__ = ('popup', 'id', 'text', 'entities', 'min_age_confirm')
    def __init__(self, id: 'DataJSON', text: str, entities: 'Vector', popup: bool = None, min_age_confirm: int = None):
        self.popup = popup
        self.id = id
        self.text = text
        self.entities = entities
        self.min_age_confirm = min_age_confirm
    def to_dict(self):
        return {"popup": self.popup, "id": self.id, "text": self.text, "entities": self.entities, "min_age_confirm": self.min_age_confirm}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2013922064, signed=False)
        flags = 0
        if self.popup: flags |= 1 << 0
        if self.min_age_confirm is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.id))
        writer.write_string(self.text)
        writer.write(bytes(self.entities))
        if flags & (1 << 1):
            writer.write_int(self.min_age_confirm, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        popup = bool(flags & (1 << 0))
        id = reader.tgread_object()
        text = reader.read_string()
        entities = reader.tgread_object()
        if flags & (1 << 1):
            min_age_confirm = reader.read_int()
        else:
            min_age_confirm = None
        return cls(popup, id, text, entities, min_age_confirm)

@register
class HelpRecentMeUrls(TLObject):
    CONSTRUCTOR_ID = 235081943
    __slots__ = ('urls', 'chats', 'users')
    def __init__(self, urls: 'Vector', chats: 'Vector', users: 'Vector'):
        self.urls = urls
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"urls": self.urls, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(235081943, signed=False)
        writer.write(bytes(self.urls))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        urls = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(urls, chats, users)

@register
class HelpTermsOfServiceUpdateEmpty(TLObject):
    CONSTRUCTOR_ID = 3811614591
    __slots__ = ('expires')
    def __init__(self, expires: int):
        self.expires = expires
    def to_dict(self):
        return {"expires": self.expires}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3811614591, signed=False)
        writer.write_int(self.expires, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        expires = reader.read_int()
        return cls(expires)

@register
class HelpTermsOfServiceUpdate(TLObject):
    CONSTRUCTOR_ID = 686618977
    __slots__ = ('expires', 'terms_of_service')
    def __init__(self, expires: int, terms_of_service: 'HelpTermsOfService'):
        self.expires = expires
        self.terms_of_service = terms_of_service
    def to_dict(self):
        return {"expires": self.expires, "terms_of_service": self.terms_of_service}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(686618977, signed=False)
        writer.write_int(self.expires, signed=True)
        writer.write(bytes(self.terms_of_service))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        expires = reader.read_int()
        terms_of_service = reader.tgread_object()
        return cls(expires, terms_of_service)

@register
class HelpDeepLinkInfoEmpty(TLObject):
    CONSTRUCTOR_ID = 1722786150
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1722786150, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class HelpDeepLinkInfo(TLObject):
    CONSTRUCTOR_ID = 1783556146
    __slots__ = ('update_app', 'message', 'entities')
    def __init__(self, message: str, update_app: bool = None, entities: 'Vector' = None):
        self.update_app = update_app
        self.message = message
        self.entities = entities
    def to_dict(self):
        return {"update_app": self.update_app, "message": self.message, "entities": self.entities}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1783556146, signed=False)
        flags = 0
        if self.update_app: flags |= 1 << 0
        if self.entities is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write_string(self.message)
        if flags & (1 << 1):
            writer.write(bytes(self.entities))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        update_app = bool(flags & (1 << 0))
        message = reader.read_string()
        if flags & (1 << 1):
            entities = reader.tgread_object()
        else:
            entities = None
        return cls(update_app, message, entities)

@register
class HelpPassportConfigNotModified(TLObject):
    CONSTRUCTOR_ID = 3216634967
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3216634967, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class HelpPassportConfig(TLObject):
    CONSTRUCTOR_ID = 2694370991
    __slots__ = ('hash', 'countries_langs')
    def __init__(self, hash: int, countries_langs: 'DataJSON'):
        self.hash = hash
        self.countries_langs = countries_langs
    def to_dict(self):
        return {"hash": self.hash, "countries_langs": self.countries_langs}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2694370991, signed=False)
        writer.write_int(self.hash, signed=True)
        writer.write(bytes(self.countries_langs))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_int()
        countries_langs = reader.tgread_object()
        return cls(hash, countries_langs)

@register
class HelpSupportName(TLObject):
    CONSTRUCTOR_ID = 2349199817
    __slots__ = ('name')
    def __init__(self, name: str):
        self.name = name
    def to_dict(self):
        return {"name": self.name}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2349199817, signed=False)
        writer.write_string(self.name)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        name = reader.read_string()
        return cls(name)

@register
class HelpUserInfoEmpty(TLObject):
    CONSTRUCTOR_ID = 4088278765
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4088278765, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class HelpUserInfo(TLObject):
    CONSTRUCTOR_ID = 32192344
    __slots__ = ('message', 'entities', 'author', 'date')
    def __init__(self, message: str, entities: 'Vector', author: str, date: int):
        self.message = message
        self.entities = entities
        self.author = author
        self.date = date
    def to_dict(self):
        return {"message": self.message, "entities": self.entities, "author": self.author, "date": self.date}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(32192344, signed=False)
        writer.write_string(self.message)
        writer.write(bytes(self.entities))
        writer.write_string(self.author)
        writer.write_int(self.date, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        message = reader.read_string()
        entities = reader.tgread_object()
        author = reader.read_string()
        date = reader.read_int()
        return cls(message, entities, author, date)

@register
class HelpPromoDataEmpty(TLObject):
    CONSTRUCTOR_ID = 2566302837
    __slots__ = ('expires')
    def __init__(self, expires: int):
        self.expires = expires
    def to_dict(self):
        return {"expires": self.expires}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2566302837, signed=False)
        writer.write_int(self.expires, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        expires = reader.read_int()
        return cls(expires)

@register
class HelpPromoData(TLObject):
    CONSTRUCTOR_ID = 145021050
    __slots__ = ('proxy', 'expires', 'peer', 'psa_type', 'psa_message', 'pending_suggestions', 'dismissed_suggestions', 'custom_pending_suggestion', 'chats', 'users')
    def __init__(self, expires: int, pending_suggestions: 'Vector', dismissed_suggestions: 'Vector', chats: 'Vector', users: 'Vector', proxy: bool = None, peer: 'Peer' = None, psa_type: str = None, psa_message: str = None, custom_pending_suggestion: 'PendingSuggestion' = None):
        self.proxy = proxy
        self.expires = expires
        self.peer = peer
        self.psa_type = psa_type
        self.psa_message = psa_message
        self.pending_suggestions = pending_suggestions
        self.dismissed_suggestions = dismissed_suggestions
        self.custom_pending_suggestion = custom_pending_suggestion
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"proxy": self.proxy, "expires": self.expires, "peer": self.peer, "psa_type": self.psa_type, "psa_message": self.psa_message, "pending_suggestions": self.pending_suggestions, "dismissed_suggestions": self.dismissed_suggestions, "custom_pending_suggestion": self.custom_pending_suggestion, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(145021050, signed=False)
        flags = 0
        if self.proxy: flags |= 1 << 0
        if self.peer is not None: flags |= 1 << 3
        if self.psa_type is not None: flags |= 1 << 1
        if self.psa_message is not None: flags |= 1 << 2
        if self.custom_pending_suggestion is not None: flags |= 1 << 4
        writer.write_int(flags, signed=False)
        writer.write_int(self.expires, signed=True)
        if flags & (1 << 3):
            writer.write(bytes(self.peer))
        if flags & (1 << 1):
            writer.write_string(self.psa_type)
        if flags & (1 << 2):
            writer.write_string(self.psa_message)
        writer.write(bytes(self.pending_suggestions))
        writer.write(bytes(self.dismissed_suggestions))
        if flags & (1 << 4):
            writer.write(bytes(self.custom_pending_suggestion))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        proxy = bool(flags & (1 << 0))
        expires = reader.read_int()
        if flags & (1 << 3):
            peer = reader.tgread_object()
        else:
            peer = None
        if flags & (1 << 1):
            psa_type = reader.read_string()
        else:
            psa_type = None
        if flags & (1 << 2):
            psa_message = reader.read_string()
        else:
            psa_message = None
        pending_suggestions = reader.tgread_object()
        dismissed_suggestions = reader.tgread_object()
        if flags & (1 << 4):
            custom_pending_suggestion = reader.tgread_object()
        else:
            custom_pending_suggestion = None
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(proxy, expires, peer, psa_type, psa_message, pending_suggestions, dismissed_suggestions, custom_pending_suggestion, chats, users)

@register
class HelpCountryCode(TLObject):
    CONSTRUCTOR_ID = 1107543535
    __slots__ = ('country_code', 'prefixes', 'patterns')
    def __init__(self, country_code: str, prefixes: 'Vector' = None, patterns: 'Vector' = None):
        self.country_code = country_code
        self.prefixes = prefixes
        self.patterns = patterns
    def to_dict(self):
        return {"country_code": self.country_code, "prefixes": self.prefixes, "patterns": self.patterns}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1107543535, signed=False)
        flags = 0
        if self.prefixes is not None: flags |= 1 << 0
        if self.patterns is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write_string(self.country_code)
        if flags & (1 << 0):
            writer.write(bytes(self.prefixes))
        if flags & (1 << 1):
            writer.write(bytes(self.patterns))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        country_code = reader.read_string()
        if flags & (1 << 0):
            prefixes = reader.tgread_object()
        else:
            prefixes = None
        if flags & (1 << 1):
            patterns = reader.tgread_object()
        else:
            patterns = None
        return cls(country_code, prefixes, patterns)

@register
class HelpCountry(TLObject):
    CONSTRUCTOR_ID = 3280440867
    __slots__ = ('hidden', 'iso2', 'default_name', 'name', 'country_codes')
    def __init__(self, iso2: str, default_name: str, country_codes: 'Vector', hidden: bool = None, name: str = None):
        self.hidden = hidden
        self.iso2 = iso2
        self.default_name = default_name
        self.name = name
        self.country_codes = country_codes
    def to_dict(self):
        return {"hidden": self.hidden, "iso2": self.iso2, "default_name": self.default_name, "name": self.name, "country_codes": self.country_codes}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3280440867, signed=False)
        flags = 0
        if self.hidden: flags |= 1 << 0
        if self.name is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write_string(self.iso2)
        writer.write_string(self.default_name)
        if flags & (1 << 1):
            writer.write_string(self.name)
        writer.write(bytes(self.country_codes))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        hidden = bool(flags & (1 << 0))
        iso2 = reader.read_string()
        default_name = reader.read_string()
        if flags & (1 << 1):
            name = reader.read_string()
        else:
            name = None
        country_codes = reader.tgread_object()
        return cls(hidden, iso2, default_name, name, country_codes)

@register
class HelpCountriesListNotModified(TLObject):
    CONSTRUCTOR_ID = 2479628082
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2479628082, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class HelpCountriesList(TLObject):
    CONSTRUCTOR_ID = 2278585758
    __slots__ = ('countries', 'hash')
    def __init__(self, countries: 'Vector', hash: int):
        self.countries = countries
        self.hash = hash
    def to_dict(self):
        return {"countries": self.countries, "hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2278585758, signed=False)
        writer.write(bytes(self.countries))
        writer.write_int(self.hash, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        countries = reader.tgread_object()
        hash = reader.read_int()
        return cls(countries, hash)

@register
class HelpPremiumPromo(TLObject):
    CONSTRUCTOR_ID = 1395946908
    __slots__ = ('status_text', 'status_entities', 'video_sections', 'videos', 'period_options', 'users')
    def __init__(self, status_text: str, status_entities: 'Vector', video_sections: 'Vector', videos: 'Vector', period_options: 'Vector', users: 'Vector'):
        self.status_text = status_text
        self.status_entities = status_entities
        self.video_sections = video_sections
        self.videos = videos
        self.period_options = period_options
        self.users = users
    def to_dict(self):
        return {"status_text": self.status_text, "status_entities": self.status_entities, "video_sections": self.video_sections, "videos": self.videos, "period_options": self.period_options, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1395946908, signed=False)
        writer.write_string(self.status_text)
        writer.write(bytes(self.status_entities))
        writer.write(bytes(self.video_sections))
        writer.write(bytes(self.videos))
        writer.write(bytes(self.period_options))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        status_text = reader.read_string()
        status_entities = reader.tgread_object()
        video_sections = reader.tgread_object()
        videos = reader.tgread_object()
        period_options = reader.tgread_object()
        users = reader.tgread_object()
        return cls(status_text, status_entities, video_sections, videos, period_options, users)

@register
class HelpAppConfigNotModified(TLObject):
    CONSTRUCTOR_ID = 2094949405
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2094949405, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class HelpAppConfig(TLObject):
    CONSTRUCTOR_ID = 3709368366
    __slots__ = ('hash', 'config')
    def __init__(self, hash: int, config: 'JSONValue'):
        self.hash = hash
        self.config = config
    def to_dict(self):
        return {"hash": self.hash, "config": self.config}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3709368366, signed=False)
        writer.write_int(self.hash, signed=True)
        writer.write(bytes(self.config))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_int()
        config = reader.tgread_object()
        return cls(hash, config)

@register
class HelpPeerColorSet(TLObject):
    CONSTRUCTOR_ID = 639736408
    __slots__ = ('colors')
    def __init__(self, colors: 'Vector'):
        self.colors = colors
    def to_dict(self):
        return {"colors": self.colors}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(639736408, signed=False)
        writer.write(bytes(self.colors))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        colors = reader.tgread_object()
        return cls(colors)

@register
class HelpPeerColorProfileSet(TLObject):
    CONSTRUCTOR_ID = 1987928555
    __slots__ = ('palette_colors', 'bg_colors', 'story_colors')
    def __init__(self, palette_colors: 'Vector', bg_colors: 'Vector', story_colors: 'Vector'):
        self.palette_colors = palette_colors
        self.bg_colors = bg_colors
        self.story_colors = story_colors
    def to_dict(self):
        return {"palette_colors": self.palette_colors, "bg_colors": self.bg_colors, "story_colors": self.story_colors}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1987928555, signed=False)
        writer.write(bytes(self.palette_colors))
        writer.write(bytes(self.bg_colors))
        writer.write(bytes(self.story_colors))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        palette_colors = reader.tgread_object()
        bg_colors = reader.tgread_object()
        story_colors = reader.tgread_object()
        return cls(palette_colors, bg_colors, story_colors)

@register
class HelpPeerColorOption(TLObject):
    CONSTRUCTOR_ID = 2917953214
    __slots__ = ('hidden', 'color_id', 'colors', 'dark_colors', 'channel_min_level', 'group_min_level')
    def __init__(self, color_id: int, hidden: bool = None, colors: 'HelpPeerColorSet' = None, dark_colors: 'HelpPeerColorSet' = None, channel_min_level: int = None, group_min_level: int = None):
        self.hidden = hidden
        self.color_id = color_id
        self.colors = colors
        self.dark_colors = dark_colors
        self.channel_min_level = channel_min_level
        self.group_min_level = group_min_level
    def to_dict(self):
        return {"hidden": self.hidden, "color_id": self.color_id, "colors": self.colors, "dark_colors": self.dark_colors, "channel_min_level": self.channel_min_level, "group_min_level": self.group_min_level}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2917953214, signed=False)
        flags = 0
        if self.hidden: flags |= 1 << 0
        if self.colors is not None: flags |= 1 << 1
        if self.dark_colors is not None: flags |= 1 << 2
        if self.channel_min_level is not None: flags |= 1 << 3
        if self.group_min_level is not None: flags |= 1 << 4
        writer.write_int(flags, signed=False)
        writer.write_int(self.color_id, signed=True)
        if flags & (1 << 1):
            writer.write(bytes(self.colors))
        if flags & (1 << 2):
            writer.write(bytes(self.dark_colors))
        if flags & (1 << 3):
            writer.write_int(self.channel_min_level, signed=True)
        if flags & (1 << 4):
            writer.write_int(self.group_min_level, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        hidden = bool(flags & (1 << 0))
        color_id = reader.read_int()
        if flags & (1 << 1):
            colors = reader.tgread_object()
        else:
            colors = None
        if flags & (1 << 2):
            dark_colors = reader.tgread_object()
        else:
            dark_colors = None
        if flags & (1 << 3):
            channel_min_level = reader.read_int()
        else:
            channel_min_level = None
        if flags & (1 << 4):
            group_min_level = reader.read_int()
        else:
            group_min_level = None
        return cls(hidden, color_id, colors, dark_colors, channel_min_level, group_min_level)

@register
class HelpPeerColorsNotModified(TLObject):
    CONSTRUCTOR_ID = 732034510
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(732034510, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class HelpPeerColors(TLObject):
    CONSTRUCTOR_ID = 16313608
    __slots__ = ('hash', 'colors')
    def __init__(self, hash: int, colors: 'Vector'):
        self.hash = hash
        self.colors = colors
    def to_dict(self):
        return {"hash": self.hash, "colors": self.colors}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(16313608, signed=False)
        writer.write_int(self.hash, signed=True)
        writer.write(bytes(self.colors))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_int()
        colors = reader.tgread_object()
        return cls(hash, colors)

@register
class HelpTimezonesListNotModified(TLObject):
    CONSTRUCTOR_ID = 2533820620
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2533820620, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class HelpTimezonesList(TLObject):
    CONSTRUCTOR_ID = 2071260529
    __slots__ = ('timezones', 'hash')
    def __init__(self, timezones: 'Vector', hash: int):
        self.timezones = timezones
        self.hash = hash
    def to_dict(self):
        return {"timezones": self.timezones, "hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2071260529, signed=False)
        writer.write(bytes(self.timezones))
        writer.write_int(self.hash, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        timezones = reader.tgread_object()
        hash = reader.read_int()
        return cls(timezones, hash)

