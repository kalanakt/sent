"""Auto-generated TL functions. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

@register
class BotsSendCustomRequest(TLObject):
    CONSTRUCTOR_ID = 2854709741
    __slots__ = ('custom_method', 'params')
    def __init__(self, custom_method: str, params: 'DataJSON'):
        self.custom_method = custom_method
        self.params = params
    def to_dict(self):
        return {"custom_method": self.custom_method, "params": self.params}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2854709741, signed=False)
        writer.write_string(self.custom_method)
        writer.write(bytes(self.params))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        custom_method = reader.read_string()
        params = reader.tgread_object()
        return cls(custom_method, params)

@register
class BotsAnswerWebhookJSONQuery(TLObject):
    CONSTRUCTOR_ID = 3860938573
    __slots__ = ('query_id', 'data')
    def __init__(self, query_id: int, data: 'DataJSON'):
        self.query_id = query_id
        self.data = data
    def to_dict(self):
        return {"query_id": self.query_id, "data": self.data}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3860938573, signed=False)
        writer.write_long(self.query_id, signed=False)
        writer.write(bytes(self.data))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        query_id = reader.read_long()
        data = reader.tgread_object()
        return cls(query_id, data)

@register
class BotsSetBotCommands(TLObject):
    CONSTRUCTOR_ID = 85399130
    __slots__ = ('scope', 'lang_code', 'commands')
    def __init__(self, scope: 'BotCommandScope', lang_code: str, commands: 'Vector'):
        self.scope = scope
        self.lang_code = lang_code
        self.commands = commands
    def to_dict(self):
        return {"scope": self.scope, "lang_code": self.lang_code, "commands": self.commands}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(85399130, signed=False)
        writer.write(bytes(self.scope))
        writer.write_string(self.lang_code)
        writer.write(bytes(self.commands))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        scope = reader.tgread_object()
        lang_code = reader.read_string()
        commands = reader.tgread_object()
        return cls(scope, lang_code, commands)

@register
class BotsResetBotCommands(TLObject):
    CONSTRUCTOR_ID = 1032708345
    __slots__ = ('scope', 'lang_code')
    def __init__(self, scope: 'BotCommandScope', lang_code: str):
        self.scope = scope
        self.lang_code = lang_code
    def to_dict(self):
        return {"scope": self.scope, "lang_code": self.lang_code}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1032708345, signed=False)
        writer.write(bytes(self.scope))
        writer.write_string(self.lang_code)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        scope = reader.tgread_object()
        lang_code = reader.read_string()
        return cls(scope, lang_code)

@register
class BotsGetBotCommands(TLObject):
    CONSTRUCTOR_ID = 3813412310
    __slots__ = ('scope', 'lang_code')
    def __init__(self, scope: 'BotCommandScope', lang_code: str):
        self.scope = scope
        self.lang_code = lang_code
    def to_dict(self):
        return {"scope": self.scope, "lang_code": self.lang_code}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3813412310, signed=False)
        writer.write(bytes(self.scope))
        writer.write_string(self.lang_code)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        scope = reader.tgread_object()
        lang_code = reader.read_string()
        return cls(scope, lang_code)

@register
class BotsSetBotMenuButton(TLObject):
    CONSTRUCTOR_ID = 1157944655
    __slots__ = ('user_id', 'button')
    def __init__(self, user_id: 'InputUser', button: 'BotMenuButton'):
        self.user_id = user_id
        self.button = button
    def to_dict(self):
        return {"user_id": self.user_id, "button": self.button}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1157944655, signed=False)
        writer.write(bytes(self.user_id))
        writer.write(bytes(self.button))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        user_id = reader.tgread_object()
        button = reader.tgread_object()
        return cls(user_id, button)

@register
class BotsGetBotMenuButton(TLObject):
    CONSTRUCTOR_ID = 2623597352
    __slots__ = ('user_id')
    def __init__(self, user_id: 'InputUser'):
        self.user_id = user_id
    def to_dict(self):
        return {"user_id": self.user_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2623597352, signed=False)
        writer.write(bytes(self.user_id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        user_id = reader.tgread_object()
        return cls(user_id)

@register
class BotsSetBotBroadcastDefaultAdminRights(TLObject):
    CONSTRUCTOR_ID = 2021942497
    __slots__ = ('admin_rights')
    def __init__(self, admin_rights: 'ChatAdminRights'):
        self.admin_rights = admin_rights
    def to_dict(self):
        return {"admin_rights": self.admin_rights}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2021942497, signed=False)
        writer.write(bytes(self.admin_rights))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        admin_rights = reader.tgread_object()
        return cls(admin_rights)

@register
class BotsSetBotGroupDefaultAdminRights(TLObject):
    CONSTRUCTOR_ID = 2455685610
    __slots__ = ('admin_rights')
    def __init__(self, admin_rights: 'ChatAdminRights'):
        self.admin_rights = admin_rights
    def to_dict(self):
        return {"admin_rights": self.admin_rights}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2455685610, signed=False)
        writer.write(bytes(self.admin_rights))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        admin_rights = reader.tgread_object()
        return cls(admin_rights)

@register
class BotsSetBotInfo(TLObject):
    CONSTRUCTOR_ID = 282013987
    __slots__ = ('bot', 'lang_code', 'name', 'about', 'description')
    def __init__(self, lang_code: str, bot: 'InputUser' = None, name: str = None, about: str = None, description: str = None):
        self.bot = bot
        self.lang_code = lang_code
        self.name = name
        self.about = about
        self.description = description
    def to_dict(self):
        return {"bot": self.bot, "lang_code": self.lang_code, "name": self.name, "about": self.about, "description": self.description}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(282013987, signed=False)
        flags = 0
        if self.bot is not None: flags |= 1 << 2
        if self.name is not None: flags |= 1 << 3
        if self.about is not None: flags |= 1 << 0
        if self.description is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        if flags & (1 << 2):
            writer.write(bytes(self.bot))
        writer.write_string(self.lang_code)
        if flags & (1 << 3):
            writer.write_string(self.name)
        if flags & (1 << 0):
            writer.write_string(self.about)
        if flags & (1 << 1):
            writer.write_string(self.description)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        if flags & (1 << 2):
            bot = reader.tgread_object()
        else:
            bot = None
        lang_code = reader.read_string()
        if flags & (1 << 3):
            name = reader.read_string()
        else:
            name = None
        if flags & (1 << 0):
            about = reader.read_string()
        else:
            about = None
        if flags & (1 << 1):
            description = reader.read_string()
        else:
            description = None
        return cls(bot, lang_code, name, about, description)

@register
class BotsGetBotInfo(TLObject):
    CONSTRUCTOR_ID = 3705214205
    __slots__ = ('bot', 'lang_code')
    def __init__(self, lang_code: str, bot: 'InputUser' = None):
        self.bot = bot
        self.lang_code = lang_code
    def to_dict(self):
        return {"bot": self.bot, "lang_code": self.lang_code}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3705214205, signed=False)
        flags = 0
        if self.bot is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        if flags & (1 << 0):
            writer.write(bytes(self.bot))
        writer.write_string(self.lang_code)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        if flags & (1 << 0):
            bot = reader.tgread_object()
        else:
            bot = None
        lang_code = reader.read_string()
        return cls(bot, lang_code)

@register
class BotsReorderUsernames(TLObject):
    CONSTRUCTOR_ID = 2533994946
    __slots__ = ('bot', 'order')
    def __init__(self, bot: 'InputUser', order: 'Vector'):
        self.bot = bot
        self.order = order
    def to_dict(self):
        return {"bot": self.bot, "order": self.order}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2533994946, signed=False)
        writer.write(bytes(self.bot))
        writer.write(bytes(self.order))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        bot = reader.tgread_object()
        order = reader.tgread_object()
        return cls(bot, order)

@register
class BotsToggleUsername(TLObject):
    CONSTRUCTOR_ID = 87861619
    __slots__ = ('bot', 'username', 'active')
    def __init__(self, bot: 'InputUser', username: str, active: bool):
        self.bot = bot
        self.username = username
        self.active = active
    def to_dict(self):
        return {"bot": self.bot, "username": self.username, "active": self.active}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(87861619, signed=False)
        writer.write(bytes(self.bot))
        writer.write_string(self.username)
        writer.write(serialize_bool(self.active))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        bot = reader.tgread_object()
        username = reader.read_string()
        active = reader.tgread_bool()
        return cls(bot, username, active)

@register
class BotsCanSendMessage(TLObject):
    CONSTRUCTOR_ID = 324662502
    __slots__ = ('bot')
    def __init__(self, bot: 'InputUser'):
        self.bot = bot
    def to_dict(self):
        return {"bot": self.bot}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(324662502, signed=False)
        writer.write(bytes(self.bot))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        bot = reader.tgread_object()
        return cls(bot)

@register
class BotsAllowSendMessage(TLObject):
    CONSTRUCTOR_ID = 4046644207
    __slots__ = ('bot')
    def __init__(self, bot: 'InputUser'):
        self.bot = bot
    def to_dict(self):
        return {"bot": self.bot}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4046644207, signed=False)
        writer.write(bytes(self.bot))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        bot = reader.tgread_object()
        return cls(bot)

@register
class BotsInvokeWebViewCustomMethod(TLObject):
    CONSTRUCTOR_ID = 142591463
    __slots__ = ('bot', 'custom_method', 'params')
    def __init__(self, bot: 'InputUser', custom_method: str, params: 'DataJSON'):
        self.bot = bot
        self.custom_method = custom_method
        self.params = params
    def to_dict(self):
        return {"bot": self.bot, "custom_method": self.custom_method, "params": self.params}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(142591463, signed=False)
        writer.write(bytes(self.bot))
        writer.write_string(self.custom_method)
        writer.write(bytes(self.params))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        bot = reader.tgread_object()
        custom_method = reader.read_string()
        params = reader.tgread_object()
        return cls(bot, custom_method, params)

@register
class BotsGetPopularAppBots(TLObject):
    CONSTRUCTOR_ID = 3260088722
    __slots__ = ('offset', 'limit')
    def __init__(self, offset: str, limit: int):
        self.offset = offset
        self.limit = limit
    def to_dict(self):
        return {"offset": self.offset, "limit": self.limit}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3260088722, signed=False)
        writer.write_string(self.offset)
        writer.write_int(self.limit, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        offset = reader.read_string()
        limit = reader.read_int()
        return cls(offset, limit)

@register
class BotsAddPreviewMedia(TLObject):
    CONSTRUCTOR_ID = 397326170
    __slots__ = ('bot', 'lang_code', 'media')
    def __init__(self, bot: 'InputUser', lang_code: str, media: 'InputMedia'):
        self.bot = bot
        self.lang_code = lang_code
        self.media = media
    def to_dict(self):
        return {"bot": self.bot, "lang_code": self.lang_code, "media": self.media}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(397326170, signed=False)
        writer.write(bytes(self.bot))
        writer.write_string(self.lang_code)
        writer.write(bytes(self.media))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        bot = reader.tgread_object()
        lang_code = reader.read_string()
        media = reader.tgread_object()
        return cls(bot, lang_code, media)

@register
class BotsEditPreviewMedia(TLObject):
    CONSTRUCTOR_ID = 2233819247
    __slots__ = ('bot', 'lang_code', 'media', 'new_media')
    def __init__(self, bot: 'InputUser', lang_code: str, media: 'InputMedia', new_media: 'InputMedia'):
        self.bot = bot
        self.lang_code = lang_code
        self.media = media
        self.new_media = new_media
    def to_dict(self):
        return {"bot": self.bot, "lang_code": self.lang_code, "media": self.media, "new_media": self.new_media}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2233819247, signed=False)
        writer.write(bytes(self.bot))
        writer.write_string(self.lang_code)
        writer.write(bytes(self.media))
        writer.write(bytes(self.new_media))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        bot = reader.tgread_object()
        lang_code = reader.read_string()
        media = reader.tgread_object()
        new_media = reader.tgread_object()
        return cls(bot, lang_code, media, new_media)

@register
class BotsDeletePreviewMedia(TLObject):
    CONSTRUCTOR_ID = 755054003
    __slots__ = ('bot', 'lang_code', 'media')
    def __init__(self, bot: 'InputUser', lang_code: str, media: 'Vector'):
        self.bot = bot
        self.lang_code = lang_code
        self.media = media
    def to_dict(self):
        return {"bot": self.bot, "lang_code": self.lang_code, "media": self.media}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(755054003, signed=False)
        writer.write(bytes(self.bot))
        writer.write_string(self.lang_code)
        writer.write(bytes(self.media))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        bot = reader.tgread_object()
        lang_code = reader.read_string()
        media = reader.tgread_object()
        return cls(bot, lang_code, media)

@register
class BotsReorderPreviewMedias(TLObject):
    CONSTRUCTOR_ID = 3056071594
    __slots__ = ('bot', 'lang_code', 'order')
    def __init__(self, bot: 'InputUser', lang_code: str, order: 'Vector'):
        self.bot = bot
        self.lang_code = lang_code
        self.order = order
    def to_dict(self):
        return {"bot": self.bot, "lang_code": self.lang_code, "order": self.order}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3056071594, signed=False)
        writer.write(bytes(self.bot))
        writer.write_string(self.lang_code)
        writer.write(bytes(self.order))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        bot = reader.tgread_object()
        lang_code = reader.read_string()
        order = reader.tgread_object()
        return cls(bot, lang_code, order)

@register
class BotsGetPreviewInfo(TLObject):
    CONSTRUCTOR_ID = 1111143341
    __slots__ = ('bot', 'lang_code')
    def __init__(self, bot: 'InputUser', lang_code: str):
        self.bot = bot
        self.lang_code = lang_code
    def to_dict(self):
        return {"bot": self.bot, "lang_code": self.lang_code}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1111143341, signed=False)
        writer.write(bytes(self.bot))
        writer.write_string(self.lang_code)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        bot = reader.tgread_object()
        lang_code = reader.read_string()
        return cls(bot, lang_code)

@register
class BotsGetPreviewMedias(TLObject):
    CONSTRUCTOR_ID = 2728745293
    __slots__ = ('bot')
    def __init__(self, bot: 'InputUser'):
        self.bot = bot
    def to_dict(self):
        return {"bot": self.bot}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2728745293, signed=False)
        writer.write(bytes(self.bot))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        bot = reader.tgread_object()
        return cls(bot)

@register
class BotsUpdateUserEmojiStatus(TLObject):
    CONSTRUCTOR_ID = 3986632901
    __slots__ = ('user_id', 'emoji_status')
    def __init__(self, user_id: 'InputUser', emoji_status: 'EmojiStatus'):
        self.user_id = user_id
        self.emoji_status = emoji_status
    def to_dict(self):
        return {"user_id": self.user_id, "emoji_status": self.emoji_status}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3986632901, signed=False)
        writer.write(bytes(self.user_id))
        writer.write(bytes(self.emoji_status))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        user_id = reader.tgread_object()
        emoji_status = reader.tgread_object()
        return cls(user_id, emoji_status)

@register
class BotsToggleUserEmojiStatusPermission(TLObject):
    CONSTRUCTOR_ID = 115237778
    __slots__ = ('bot', 'enabled')
    def __init__(self, bot: 'InputUser', enabled: bool):
        self.bot = bot
        self.enabled = enabled
    def to_dict(self):
        return {"bot": self.bot, "enabled": self.enabled}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(115237778, signed=False)
        writer.write(bytes(self.bot))
        writer.write(serialize_bool(self.enabled))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        bot = reader.tgread_object()
        enabled = reader.tgread_bool()
        return cls(bot, enabled)

@register
class BotsCheckDownloadFileParams(TLObject):
    CONSTRUCTOR_ID = 1342666121
    __slots__ = ('bot', 'file_name', 'url')
    def __init__(self, bot: 'InputUser', file_name: str, url: str):
        self.bot = bot
        self.file_name = file_name
        self.url = url
    def to_dict(self):
        return {"bot": self.bot, "file_name": self.file_name, "url": self.url}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1342666121, signed=False)
        writer.write(bytes(self.bot))
        writer.write_string(self.file_name)
        writer.write_string(self.url)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        bot = reader.tgread_object()
        file_name = reader.read_string()
        url = reader.read_string()
        return cls(bot, file_name, url)

@register
class BotsGetAdminedBots(TLObject):
    CONSTRUCTOR_ID = 2960203139
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2960203139, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class BotsUpdateStarRefProgram(TLObject):
    CONSTRUCTOR_ID = 2005621427
    __slots__ = ('bot', 'commission_permille', 'duration_months')
    def __init__(self, bot: 'InputUser', commission_permille: int, duration_months: int = None):
        self.bot = bot
        self.commission_permille = commission_permille
        self.duration_months = duration_months
    def to_dict(self):
        return {"bot": self.bot, "commission_permille": self.commission_permille, "duration_months": self.duration_months}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2005621427, signed=False)
        flags = 0
        if self.duration_months is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.bot))
        writer.write_int(self.commission_permille, signed=True)
        if flags & (1 << 0):
            writer.write_int(self.duration_months, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        bot = reader.tgread_object()
        commission_permille = reader.read_int()
        if flags & (1 << 0):
            duration_months = reader.read_int()
        else:
            duration_months = None
        return cls(bot, commission_permille, duration_months)

@register
class BotsSetCustomVerification(TLObject):
    CONSTRUCTOR_ID = 2341068733
    __slots__ = ('enabled', 'bot', 'peer', 'custom_description')
    def __init__(self, peer: 'InputPeer', enabled: bool = None, bot: 'InputUser' = None, custom_description: str = None):
        self.enabled = enabled
        self.bot = bot
        self.peer = peer
        self.custom_description = custom_description
    def to_dict(self):
        return {"enabled": self.enabled, "bot": self.bot, "peer": self.peer, "custom_description": self.custom_description}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2341068733, signed=False)
        flags = 0
        if self.enabled: flags |= 1 << 1
        if self.bot is not None: flags |= 1 << 0
        if self.custom_description is not None: flags |= 1 << 2
        writer.write_int(flags, signed=False)
        if flags & (1 << 0):
            writer.write(bytes(self.bot))
        writer.write(bytes(self.peer))
        if flags & (1 << 2):
            writer.write_string(self.custom_description)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        enabled = bool(flags & (1 << 1))
        if flags & (1 << 0):
            bot = reader.tgread_object()
        else:
            bot = None
        peer = reader.tgread_object()
        if flags & (1 << 2):
            custom_description = reader.read_string()
        else:
            custom_description = None
        return cls(enabled, bot, peer, custom_description)

@register
class BotsGetBotRecommendations(TLObject):
    CONSTRUCTOR_ID = 2713126933
    __slots__ = ('bot')
    def __init__(self, bot: 'InputUser'):
        self.bot = bot
    def to_dict(self):
        return {"bot": self.bot}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2713126933, signed=False)
        writer.write(bytes(self.bot))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        bot = reader.tgread_object()
        return cls(bot)

@register
class BotsCheckUsername(TLObject):
    CONSTRUCTOR_ID = 2280792475
    __slots__ = ('username')
    def __init__(self, username: str):
        self.username = username
    def to_dict(self):
        return {"username": self.username}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2280792475, signed=False)
        writer.write_string(self.username)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        username = reader.read_string()
        return cls(username)

@register
class BotsCreateBot(TLObject):
    CONSTRUCTOR_ID = 3853614891
    __slots__ = ('via_deeplink', 'name', 'username', 'manager_id')
    def __init__(self, name: str, username: str, manager_id: 'InputUser', via_deeplink: bool = None):
        self.via_deeplink = via_deeplink
        self.name = name
        self.username = username
        self.manager_id = manager_id
    def to_dict(self):
        return {"via_deeplink": self.via_deeplink, "name": self.name, "username": self.username, "manager_id": self.manager_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3853614891, signed=False)
        flags = 0
        if self.via_deeplink: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write_string(self.name)
        writer.write_string(self.username)
        writer.write(bytes(self.manager_id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        via_deeplink = bool(flags & (1 << 0))
        name = reader.read_string()
        username = reader.read_string()
        manager_id = reader.tgread_object()
        return cls(via_deeplink, name, username, manager_id)

@register
class BotsExportBotToken(TLObject):
    CONSTRUCTOR_ID = 3171785195
    __slots__ = ('bot', 'revoke')
    def __init__(self, bot: 'InputUser', revoke: bool):
        self.bot = bot
        self.revoke = revoke
    def to_dict(self):
        return {"bot": self.bot, "revoke": self.revoke}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3171785195, signed=False)
        writer.write(bytes(self.bot))
        writer.write(serialize_bool(self.revoke))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        bot = reader.tgread_object()
        revoke = reader.tgread_bool()
        return cls(bot, revoke)

@register
class BotsRequestWebViewButton(TLObject):
    CONSTRUCTOR_ID = 832742238
    __slots__ = ('user_id', 'button')
    def __init__(self, user_id: 'InputUser', button: 'KeyboardButton'):
        self.user_id = user_id
        self.button = button
    def to_dict(self):
        return {"user_id": self.user_id, "button": self.button}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(832742238, signed=False)
        writer.write(bytes(self.user_id))
        writer.write(bytes(self.button))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        user_id = reader.tgread_object()
        button = reader.tgread_object()
        return cls(user_id, button)

@register
class BotsGetRequestedWebViewButton(TLObject):
    CONSTRUCTOR_ID = 3206920179
    __slots__ = ('bot', 'webapp_req_id')
    def __init__(self, bot: 'InputUser', webapp_req_id: str):
        self.bot = bot
        self.webapp_req_id = webapp_req_id
    def to_dict(self):
        return {"bot": self.bot, "webapp_req_id": self.webapp_req_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3206920179, signed=False)
        writer.write(bytes(self.bot))
        writer.write_string(self.webapp_req_id)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        bot = reader.tgread_object()
        webapp_req_id = reader.read_string()
        return cls(bot, webapp_req_id)

@register
class BotsGetAccessSettings(TLObject):
    CONSTRUCTOR_ID = 557339555
    __slots__ = ('bot')
    def __init__(self, bot: 'InputUser'):
        self.bot = bot
    def to_dict(self):
        return {"bot": self.bot}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(557339555, signed=False)
        writer.write(bytes(self.bot))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        bot = reader.tgread_object()
        return cls(bot)

@register
class BotsEditAccessSettings(TLObject):
    CONSTRUCTOR_ID = 830553304
    __slots__ = ('restricted', 'bot', 'add_users')
    def __init__(self, bot: 'InputUser', restricted: bool = None, add_users: 'Vector' = None):
        self.restricted = restricted
        self.bot = bot
        self.add_users = add_users
    def to_dict(self):
        return {"restricted": self.restricted, "bot": self.bot, "add_users": self.add_users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(830553304, signed=False)
        flags = 0
        if self.restricted: flags |= 1 << 0
        if self.add_users is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.bot))
        if flags & (1 << 1):
            writer.write(bytes(self.add_users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        restricted = bool(flags & (1 << 0))
        bot = reader.tgread_object()
        if flags & (1 << 1):
            add_users = reader.tgread_object()
        else:
            add_users = None
        return cls(restricted, bot, add_users)

