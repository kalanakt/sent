"""Auto-generated TL functions. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

@register
class AccountRegisterDevice(TLObject):
    CONSTRUCTOR_ID = 3968205178
    __slots__ = ('no_muted', 'token_type', 'token', 'app_sandbox', 'secret', 'other_uids')
    def __init__(self, token_type: int, token: str, app_sandbox: bool, secret: bytes, other_uids: 'Vector', no_muted: bool = None):
        self.no_muted = no_muted
        self.token_type = token_type
        self.token = token
        self.app_sandbox = app_sandbox
        self.secret = secret
        self.other_uids = other_uids
    def to_dict(self):
        return {"no_muted": self.no_muted, "token_type": self.token_type, "token": self.token, "app_sandbox": self.app_sandbox, "secret": self.secret, "other_uids": self.other_uids}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3968205178, signed=False)
        flags = 0
        if self.no_muted: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write_int(self.token_type, signed=True)
        writer.write_string(self.token)
        writer.write(serialize_bool(self.app_sandbox))
        writer.write_bytes(self.secret)
        writer.write(bytes(self.other_uids))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        no_muted = bool(flags & (1 << 0))
        token_type = reader.read_int()
        token = reader.read_string()
        app_sandbox = reader.tgread_bool()
        secret = reader.read_bytes()
        other_uids = reader.tgread_object()
        return cls(no_muted, token_type, token, app_sandbox, secret, other_uids)

@register
class AccountUnregisterDevice(TLObject):
    CONSTRUCTOR_ID = 1779249670
    __slots__ = ('token_type', 'token', 'other_uids')
    def __init__(self, token_type: int, token: str, other_uids: 'Vector'):
        self.token_type = token_type
        self.token = token
        self.other_uids = other_uids
    def to_dict(self):
        return {"token_type": self.token_type, "token": self.token, "other_uids": self.other_uids}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1779249670, signed=False)
        writer.write_int(self.token_type, signed=True)
        writer.write_string(self.token)
        writer.write(bytes(self.other_uids))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        token_type = reader.read_int()
        token = reader.read_string()
        other_uids = reader.tgread_object()
        return cls(token_type, token, other_uids)

@register
class AccountUpdateNotifySettings(TLObject):
    CONSTRUCTOR_ID = 2227067795
    __slots__ = ('peer', 'settings')
    def __init__(self, peer: 'InputNotifyPeer', settings: 'InputPeerNotifySettings'):
        self.peer = peer
        self.settings = settings
    def to_dict(self):
        return {"peer": self.peer, "settings": self.settings}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2227067795, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.settings))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        settings = reader.tgread_object()
        return cls(peer, settings)

@register
class AccountGetNotifySettings(TLObject):
    CONSTRUCTOR_ID = 313765169
    __slots__ = ('peer')
    def __init__(self, peer: 'InputNotifyPeer'):
        self.peer = peer
    def to_dict(self):
        return {"peer": self.peer}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(313765169, signed=False)
        writer.write(bytes(self.peer))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        return cls(peer)

@register
class AccountResetNotifySettings(TLObject):
    CONSTRUCTOR_ID = 3682473799
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3682473799, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class AccountUpdateProfile(TLObject):
    CONSTRUCTOR_ID = 2018596725
    __slots__ = ('first_name', 'last_name', 'about')
    def __init__(self, first_name: str = None, last_name: str = None, about: str = None):
        self.first_name = first_name
        self.last_name = last_name
        self.about = about
    def to_dict(self):
        return {"first_name": self.first_name, "last_name": self.last_name, "about": self.about}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2018596725, signed=False)
        flags = 0
        if self.first_name is not None: flags |= 1 << 0
        if self.last_name is not None: flags |= 1 << 1
        if self.about is not None: flags |= 1 << 2
        writer.write_int(flags, signed=False)
        if flags & (1 << 0):
            writer.write_string(self.first_name)
        if flags & (1 << 1):
            writer.write_string(self.last_name)
        if flags & (1 << 2):
            writer.write_string(self.about)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        if flags & (1 << 0):
            first_name = reader.read_string()
        else:
            first_name = None
        if flags & (1 << 1):
            last_name = reader.read_string()
        else:
            last_name = None
        if flags & (1 << 2):
            about = reader.read_string()
        else:
            about = None
        return cls(first_name, last_name, about)

@register
class AccountUpdateStatus(TLObject):
    CONSTRUCTOR_ID = 1713919532
    __slots__ = ('offline')
    def __init__(self, offline: bool):
        self.offline = offline
    def to_dict(self):
        return {"offline": self.offline}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1713919532, signed=False)
        writer.write(serialize_bool(self.offline))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        offline = reader.tgread_bool()
        return cls(offline)

@register
class AccountGetWallPapers(TLObject):
    CONSTRUCTOR_ID = 127302966
    __slots__ = ('hash')
    def __init__(self, hash: int):
        self.hash = hash
    def to_dict(self):
        return {"hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(127302966, signed=False)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_long()
        return cls(hash)

@register
class AccountReportPeer(TLObject):
    CONSTRUCTOR_ID = 3317316998
    __slots__ = ('peer', 'reason', 'message')
    def __init__(self, peer: 'InputPeer', reason: 'ReportReason', message: str):
        self.peer = peer
        self.reason = reason
        self.message = message
    def to_dict(self):
        return {"peer": self.peer, "reason": self.reason, "message": self.message}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3317316998, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.reason))
        writer.write_string(self.message)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        reason = reader.tgread_object()
        message = reader.read_string()
        return cls(peer, reason, message)

@register
class AccountCheckUsername(TLObject):
    CONSTRUCTOR_ID = 655677548
    __slots__ = ('username')
    def __init__(self, username: str):
        self.username = username
    def to_dict(self):
        return {"username": self.username}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(655677548, signed=False)
        writer.write_string(self.username)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        username = reader.read_string()
        return cls(username)

@register
class AccountUpdateUsername(TLObject):
    CONSTRUCTOR_ID = 1040964988
    __slots__ = ('username')
    def __init__(self, username: str):
        self.username = username
    def to_dict(self):
        return {"username": self.username}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1040964988, signed=False)
        writer.write_string(self.username)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        username = reader.read_string()
        return cls(username)

@register
class AccountGetPrivacy(TLObject):
    CONSTRUCTOR_ID = 3671837008
    __slots__ = ('key')
    def __init__(self, key: 'InputPrivacyKey'):
        self.key = key
    def to_dict(self):
        return {"key": self.key}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3671837008, signed=False)
        writer.write(bytes(self.key))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        key = reader.tgread_object()
        return cls(key)

@register
class AccountSetPrivacy(TLObject):
    CONSTRUCTOR_ID = 3388480744
    __slots__ = ('key', 'rules')
    def __init__(self, key: 'InputPrivacyKey', rules: 'Vector'):
        self.key = key
        self.rules = rules
    def to_dict(self):
        return {"key": self.key, "rules": self.rules}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3388480744, signed=False)
        writer.write(bytes(self.key))
        writer.write(bytes(self.rules))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        key = reader.tgread_object()
        rules = reader.tgread_object()
        return cls(key, rules)

@register
class AccountDeleteAccount(TLObject):
    CONSTRUCTOR_ID = 2730545012
    __slots__ = ('reason', 'password')
    def __init__(self, reason: str, password: 'InputCheckPasswordSRP' = None):
        self.reason = reason
        self.password = password
    def to_dict(self):
        return {"reason": self.reason, "password": self.password}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2730545012, signed=False)
        flags = 0
        if self.password is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write_string(self.reason)
        if flags & (1 << 0):
            writer.write(bytes(self.password))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        reason = reader.read_string()
        if flags & (1 << 0):
            password = reader.tgread_object()
        else:
            password = None
        return cls(reason, password)

@register
class AccountGetAccountTTL(TLObject):
    CONSTRUCTOR_ID = 150761757
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(150761757, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class AccountSetAccountTTL(TLObject):
    CONSTRUCTOR_ID = 608323678
    __slots__ = ('ttl')
    def __init__(self, ttl: 'AccountDaysTTL'):
        self.ttl = ttl
    def to_dict(self):
        return {"ttl": self.ttl}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(608323678, signed=False)
        writer.write(bytes(self.ttl))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        ttl = reader.tgread_object()
        return cls(ttl)

@register
class AccountSendChangePhoneCode(TLObject):
    CONSTRUCTOR_ID = 2186758885
    __slots__ = ('phone_number', 'settings')
    def __init__(self, phone_number: str, settings: 'CodeSettings'):
        self.phone_number = phone_number
        self.settings = settings
    def to_dict(self):
        return {"phone_number": self.phone_number, "settings": self.settings}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2186758885, signed=False)
        writer.write_string(self.phone_number)
        writer.write(bytes(self.settings))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        phone_number = reader.read_string()
        settings = reader.tgread_object()
        return cls(phone_number, settings)

@register
class AccountChangePhone(TLObject):
    CONSTRUCTOR_ID = 1891839707
    __slots__ = ('phone_number', 'phone_code_hash', 'phone_code')
    def __init__(self, phone_number: str, phone_code_hash: str, phone_code: str):
        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash
        self.phone_code = phone_code
    def to_dict(self):
        return {"phone_number": self.phone_number, "phone_code_hash": self.phone_code_hash, "phone_code": self.phone_code}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1891839707, signed=False)
        writer.write_string(self.phone_number)
        writer.write_string(self.phone_code_hash)
        writer.write_string(self.phone_code)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        phone_number = reader.read_string()
        phone_code_hash = reader.read_string()
        phone_code = reader.read_string()
        return cls(phone_number, phone_code_hash, phone_code)

@register
class AccountUpdateDeviceLocked(TLObject):
    CONSTRUCTOR_ID = 954152242
    __slots__ = ('period')
    def __init__(self, period: int):
        self.period = period
    def to_dict(self):
        return {"period": self.period}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(954152242, signed=False)
        writer.write_int(self.period, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        period = reader.read_int()
        return cls(period)

@register
class AccountGetAuthorizations(TLObject):
    CONSTRUCTOR_ID = 3810574680
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3810574680, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class AccountResetAuthorization(TLObject):
    CONSTRUCTOR_ID = 3749180348
    __slots__ = ('hash')
    def __init__(self, hash: int):
        self.hash = hash
    def to_dict(self):
        return {"hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3749180348, signed=False)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_long()
        return cls(hash)

@register
class AccountGetPassword(TLObject):
    CONSTRUCTOR_ID = 1418342645
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1418342645, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class AccountGetPasswordSettings(TLObject):
    CONSTRUCTOR_ID = 2631199481
    __slots__ = ('password')
    def __init__(self, password: 'InputCheckPasswordSRP'):
        self.password = password
    def to_dict(self):
        return {"password": self.password}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2631199481, signed=False)
        writer.write(bytes(self.password))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        password = reader.tgread_object()
        return cls(password)

@register
class AccountUpdatePasswordSettings(TLObject):
    CONSTRUCTOR_ID = 2778402863
    __slots__ = ('password', 'new_settings')
    def __init__(self, password: 'InputCheckPasswordSRP', new_settings: 'AccountPasswordInputSettings'):
        self.password = password
        self.new_settings = new_settings
    def to_dict(self):
        return {"password": self.password, "new_settings": self.new_settings}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2778402863, signed=False)
        writer.write(bytes(self.password))
        writer.write(bytes(self.new_settings))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        password = reader.tgread_object()
        new_settings = reader.tgread_object()
        return cls(password, new_settings)

@register
class AccountSendConfirmPhoneCode(TLObject):
    CONSTRUCTOR_ID = 457157256
    __slots__ = ('hash', 'settings')
    def __init__(self, hash: str, settings: 'CodeSettings'):
        self.hash = hash
        self.settings = settings
    def to_dict(self):
        return {"hash": self.hash, "settings": self.settings}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(457157256, signed=False)
        writer.write_string(self.hash)
        writer.write(bytes(self.settings))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_string()
        settings = reader.tgread_object()
        return cls(hash, settings)

@register
class AccountConfirmPhone(TLObject):
    CONSTRUCTOR_ID = 1596029123
    __slots__ = ('phone_code_hash', 'phone_code')
    def __init__(self, phone_code_hash: str, phone_code: str):
        self.phone_code_hash = phone_code_hash
        self.phone_code = phone_code
    def to_dict(self):
        return {"phone_code_hash": self.phone_code_hash, "phone_code": self.phone_code}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1596029123, signed=False)
        writer.write_string(self.phone_code_hash)
        writer.write_string(self.phone_code)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        phone_code_hash = reader.read_string()
        phone_code = reader.read_string()
        return cls(phone_code_hash, phone_code)

@register
class AccountGetTmpPassword(TLObject):
    CONSTRUCTOR_ID = 1151208273
    __slots__ = ('password', 'period')
    def __init__(self, password: 'InputCheckPasswordSRP', period: int):
        self.password = password
        self.period = period
    def to_dict(self):
        return {"password": self.password, "period": self.period}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1151208273, signed=False)
        writer.write(bytes(self.password))
        writer.write_int(self.period, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        password = reader.tgread_object()
        period = reader.read_int()
        return cls(password, period)

@register
class AccountGetWebAuthorizations(TLObject):
    CONSTRUCTOR_ID = 405695855
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(405695855, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class AccountResetWebAuthorization(TLObject):
    CONSTRUCTOR_ID = 755087855
    __slots__ = ('hash')
    def __init__(self, hash: int):
        self.hash = hash
    def to_dict(self):
        return {"hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(755087855, signed=False)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_long()
        return cls(hash)

@register
class AccountResetWebAuthorizations(TLObject):
    CONSTRUCTOR_ID = 1747789204
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1747789204, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class AccountGetAllSecureValues(TLObject):
    CONSTRUCTOR_ID = 2995305597
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2995305597, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class AccountGetSecureValue(TLObject):
    CONSTRUCTOR_ID = 1936088002
    __slots__ = ('types')
    def __init__(self, types: 'Vector'):
        self.types = types
    def to_dict(self):
        return {"types": self.types}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1936088002, signed=False)
        writer.write(bytes(self.types))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        types = reader.tgread_object()
        return cls(types)

@register
class AccountSaveSecureValue(TLObject):
    CONSTRUCTOR_ID = 2308956957
    __slots__ = ('value', 'secure_secret_id')
    def __init__(self, value: 'InputSecureValue', secure_secret_id: int):
        self.value = value
        self.secure_secret_id = secure_secret_id
    def to_dict(self):
        return {"value": self.value, "secure_secret_id": self.secure_secret_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2308956957, signed=False)
        writer.write(bytes(self.value))
        writer.write_long(self.secure_secret_id, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        value = reader.tgread_object()
        secure_secret_id = reader.read_long()
        return cls(value, secure_secret_id)

@register
class AccountDeleteSecureValue(TLObject):
    CONSTRUCTOR_ID = 3095444555
    __slots__ = ('types')
    def __init__(self, types: 'Vector'):
        self.types = types
    def to_dict(self):
        return {"types": self.types}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3095444555, signed=False)
        writer.write(bytes(self.types))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        types = reader.tgread_object()
        return cls(types)

@register
class AccountGetAuthorizationForm(TLObject):
    CONSTRUCTOR_ID = 2838059386
    __slots__ = ('bot_id', 'scope', 'public_key')
    def __init__(self, bot_id: int, scope: str, public_key: str):
        self.bot_id = bot_id
        self.scope = scope
        self.public_key = public_key
    def to_dict(self):
        return {"bot_id": self.bot_id, "scope": self.scope, "public_key": self.public_key}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2838059386, signed=False)
        writer.write_long(self.bot_id, signed=False)
        writer.write_string(self.scope)
        writer.write_string(self.public_key)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        bot_id = reader.read_long()
        scope = reader.read_string()
        public_key = reader.read_string()
        return cls(bot_id, scope, public_key)

@register
class AccountAcceptAuthorization(TLObject):
    CONSTRUCTOR_ID = 4092415091
    __slots__ = ('bot_id', 'scope', 'public_key', 'value_hashes', 'credentials')
    def __init__(self, bot_id: int, scope: str, public_key: str, value_hashes: 'Vector', credentials: 'SecureCredentialsEncrypted'):
        self.bot_id = bot_id
        self.scope = scope
        self.public_key = public_key
        self.value_hashes = value_hashes
        self.credentials = credentials
    def to_dict(self):
        return {"bot_id": self.bot_id, "scope": self.scope, "public_key": self.public_key, "value_hashes": self.value_hashes, "credentials": self.credentials}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4092415091, signed=False)
        writer.write_long(self.bot_id, signed=False)
        writer.write_string(self.scope)
        writer.write_string(self.public_key)
        writer.write(bytes(self.value_hashes))
        writer.write(bytes(self.credentials))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        bot_id = reader.read_long()
        scope = reader.read_string()
        public_key = reader.read_string()
        value_hashes = reader.tgread_object()
        credentials = reader.tgread_object()
        return cls(bot_id, scope, public_key, value_hashes, credentials)

@register
class AccountSendVerifyPhoneCode(TLObject):
    CONSTRUCTOR_ID = 2778945273
    __slots__ = ('phone_number', 'settings')
    def __init__(self, phone_number: str, settings: 'CodeSettings'):
        self.phone_number = phone_number
        self.settings = settings
    def to_dict(self):
        return {"phone_number": self.phone_number, "settings": self.settings}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2778945273, signed=False)
        writer.write_string(self.phone_number)
        writer.write(bytes(self.settings))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        phone_number = reader.read_string()
        settings = reader.tgread_object()
        return cls(phone_number, settings)

@register
class AccountVerifyPhone(TLObject):
    CONSTRUCTOR_ID = 1305716726
    __slots__ = ('phone_number', 'phone_code_hash', 'phone_code')
    def __init__(self, phone_number: str, phone_code_hash: str, phone_code: str):
        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash
        self.phone_code = phone_code
    def to_dict(self):
        return {"phone_number": self.phone_number, "phone_code_hash": self.phone_code_hash, "phone_code": self.phone_code}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1305716726, signed=False)
        writer.write_string(self.phone_number)
        writer.write_string(self.phone_code_hash)
        writer.write_string(self.phone_code)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        phone_number = reader.read_string()
        phone_code_hash = reader.read_string()
        phone_code = reader.read_string()
        return cls(phone_number, phone_code_hash, phone_code)

@register
class AccountSendVerifyEmailCode(TLObject):
    CONSTRUCTOR_ID = 2564831163
    __slots__ = ('purpose', 'email')
    def __init__(self, purpose: 'EmailVerifyPurpose', email: str):
        self.purpose = purpose
        self.email = email
    def to_dict(self):
        return {"purpose": self.purpose, "email": self.email}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2564831163, signed=False)
        writer.write(bytes(self.purpose))
        writer.write_string(self.email)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        purpose = reader.tgread_object()
        email = reader.read_string()
        return cls(purpose, email)

@register
class AccountVerifyEmail(TLObject):
    CONSTRUCTOR_ID = 53322959
    __slots__ = ('purpose', 'verification')
    def __init__(self, purpose: 'EmailVerifyPurpose', verification: 'EmailVerification'):
        self.purpose = purpose
        self.verification = verification
    def to_dict(self):
        return {"purpose": self.purpose, "verification": self.verification}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(53322959, signed=False)
        writer.write(bytes(self.purpose))
        writer.write(bytes(self.verification))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        purpose = reader.tgread_object()
        verification = reader.tgread_object()
        return cls(purpose, verification)

@register
class AccountInitTakeoutSession(TLObject):
    CONSTRUCTOR_ID = 2398350000
    __slots__ = ('contacts', 'message_users', 'message_chats', 'message_megagroups', 'message_channels', 'files', 'file_max_size')
    def __init__(self, contacts: bool = None, message_users: bool = None, message_chats: bool = None, message_megagroups: bool = None, message_channels: bool = None, files: bool = None, file_max_size: int = None):
        self.contacts = contacts
        self.message_users = message_users
        self.message_chats = message_chats
        self.message_megagroups = message_megagroups
        self.message_channels = message_channels
        self.files = files
        self.file_max_size = file_max_size
    def to_dict(self):
        return {"contacts": self.contacts, "message_users": self.message_users, "message_chats": self.message_chats, "message_megagroups": self.message_megagroups, "message_channels": self.message_channels, "files": self.files, "file_max_size": self.file_max_size}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2398350000, signed=False)
        flags = 0
        if self.contacts: flags |= 1 << 0
        if self.message_users: flags |= 1 << 1
        if self.message_chats: flags |= 1 << 2
        if self.message_megagroups: flags |= 1 << 3
        if self.message_channels: flags |= 1 << 4
        if self.files: flags |= 1 << 5
        if self.file_max_size is not None: flags |= 1 << 5
        writer.write_int(flags, signed=False)
        if flags & (1 << 5):
            writer.write_long(self.file_max_size, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        contacts = bool(flags & (1 << 0))
        message_users = bool(flags & (1 << 1))
        message_chats = bool(flags & (1 << 2))
        message_megagroups = bool(flags & (1 << 3))
        message_channels = bool(flags & (1 << 4))
        files = bool(flags & (1 << 5))
        if flags & (1 << 5):
            file_max_size = reader.read_long()
        else:
            file_max_size = None
        return cls(contacts, message_users, message_chats, message_megagroups, message_channels, files, file_max_size)

@register
class AccountFinishTakeoutSession(TLObject):
    CONSTRUCTOR_ID = 489050862
    __slots__ = ('success')
    def __init__(self, success: bool = None):
        self.success = success
    def to_dict(self):
        return {"success": self.success}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(489050862, signed=False)
        flags = 0
        if self.success: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        success = bool(flags & (1 << 0))
        return cls(success)

@register
class AccountConfirmPasswordEmail(TLObject):
    CONSTRUCTOR_ID = 2413762848
    __slots__ = ('code')
    def __init__(self, code: str):
        self.code = code
    def to_dict(self):
        return {"code": self.code}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2413762848, signed=False)
        writer.write_string(self.code)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        code = reader.read_string()
        return cls(code)

@register
class AccountResendPasswordEmail(TLObject):
    CONSTRUCTOR_ID = 2055154197
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2055154197, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class AccountCancelPasswordEmail(TLObject):
    CONSTRUCTOR_ID = 3251361206
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3251361206, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class AccountGetContactSignUpNotification(TLObject):
    CONSTRUCTOR_ID = 2668087080
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2668087080, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class AccountSetContactSignUpNotification(TLObject):
    CONSTRUCTOR_ID = 3488890721
    __slots__ = ('silent')
    def __init__(self, silent: bool):
        self.silent = silent
    def to_dict(self):
        return {"silent": self.silent}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3488890721, signed=False)
        writer.write(serialize_bool(self.silent))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        silent = reader.tgread_bool()
        return cls(silent)

@register
class AccountGetNotifyExceptions(TLObject):
    CONSTRUCTOR_ID = 1398240377
    __slots__ = ('compare_sound', 'compare_stories', 'peer')
    def __init__(self, compare_sound: bool = None, compare_stories: bool = None, peer: 'InputNotifyPeer' = None):
        self.compare_sound = compare_sound
        self.compare_stories = compare_stories
        self.peer = peer
    def to_dict(self):
        return {"compare_sound": self.compare_sound, "compare_stories": self.compare_stories, "peer": self.peer}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1398240377, signed=False)
        flags = 0
        if self.compare_sound: flags |= 1 << 1
        if self.compare_stories: flags |= 1 << 2
        if self.peer is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        if flags & (1 << 0):
            writer.write(bytes(self.peer))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        compare_sound = bool(flags & (1 << 1))
        compare_stories = bool(flags & (1 << 2))
        if flags & (1 << 0):
            peer = reader.tgread_object()
        else:
            peer = None
        return cls(compare_sound, compare_stories, peer)

@register
class AccountGetWallPaper(TLObject):
    CONSTRUCTOR_ID = 4237155306
    __slots__ = ('wallpaper')
    def __init__(self, wallpaper: 'InputWallPaper'):
        self.wallpaper = wallpaper
    def to_dict(self):
        return {"wallpaper": self.wallpaper}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4237155306, signed=False)
        writer.write(bytes(self.wallpaper))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        wallpaper = reader.tgread_object()
        return cls(wallpaper)

@register
class AccountUploadWallPaper(TLObject):
    CONSTRUCTOR_ID = 3818557187
    __slots__ = ('for_chat', 'file', 'mime_type', 'settings')
    def __init__(self, file: 'InputFile', mime_type: str, settings: 'WallPaperSettings', for_chat: bool = None):
        self.for_chat = for_chat
        self.file = file
        self.mime_type = mime_type
        self.settings = settings
    def to_dict(self):
        return {"for_chat": self.for_chat, "file": self.file, "mime_type": self.mime_type, "settings": self.settings}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3818557187, signed=False)
        flags = 0
        if self.for_chat: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.file))
        writer.write_string(self.mime_type)
        writer.write(bytes(self.settings))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        for_chat = bool(flags & (1 << 0))
        file = reader.tgread_object()
        mime_type = reader.read_string()
        settings = reader.tgread_object()
        return cls(for_chat, file, mime_type, settings)

@register
class AccountSaveWallPaper(TLObject):
    CONSTRUCTOR_ID = 1817860919
    __slots__ = ('wallpaper', 'unsave', 'settings')
    def __init__(self, wallpaper: 'InputWallPaper', unsave: bool, settings: 'WallPaperSettings'):
        self.wallpaper = wallpaper
        self.unsave = unsave
        self.settings = settings
    def to_dict(self):
        return {"wallpaper": self.wallpaper, "unsave": self.unsave, "settings": self.settings}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1817860919, signed=False)
        writer.write(bytes(self.wallpaper))
        writer.write(serialize_bool(self.unsave))
        writer.write(bytes(self.settings))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        wallpaper = reader.tgread_object()
        unsave = reader.tgread_bool()
        settings = reader.tgread_object()
        return cls(wallpaper, unsave, settings)

@register
class AccountInstallWallPaper(TLObject):
    CONSTRUCTOR_ID = 4276967273
    __slots__ = ('wallpaper', 'settings')
    def __init__(self, wallpaper: 'InputWallPaper', settings: 'WallPaperSettings'):
        self.wallpaper = wallpaper
        self.settings = settings
    def to_dict(self):
        return {"wallpaper": self.wallpaper, "settings": self.settings}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4276967273, signed=False)
        writer.write(bytes(self.wallpaper))
        writer.write(bytes(self.settings))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        wallpaper = reader.tgread_object()
        settings = reader.tgread_object()
        return cls(wallpaper, settings)

@register
class AccountResetWallPapers(TLObject):
    CONSTRUCTOR_ID = 3141244932
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3141244932, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class AccountGetAutoDownloadSettings(TLObject):
    CONSTRUCTOR_ID = 1457130303
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1457130303, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class AccountSaveAutoDownloadSettings(TLObject):
    CONSTRUCTOR_ID = 1995661875
    __slots__ = ('low', 'high', 'settings')
    def __init__(self, settings: 'AutoDownloadSettings', low: bool = None, high: bool = None):
        self.low = low
        self.high = high
        self.settings = settings
    def to_dict(self):
        return {"low": self.low, "high": self.high, "settings": self.settings}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1995661875, signed=False)
        flags = 0
        if self.low: flags |= 1 << 0
        if self.high: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.settings))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        low = bool(flags & (1 << 0))
        high = bool(flags & (1 << 1))
        settings = reader.tgread_object()
        return cls(low, high, settings)

@register
class AccountUploadTheme(TLObject):
    CONSTRUCTOR_ID = 473805619
    __slots__ = ('file', 'thumb', 'file_name', 'mime_type')
    def __init__(self, file: 'InputFile', file_name: str, mime_type: str, thumb: 'InputFile' = None):
        self.file = file
        self.thumb = thumb
        self.file_name = file_name
        self.mime_type = mime_type
    def to_dict(self):
        return {"file": self.file, "thumb": self.thumb, "file_name": self.file_name, "mime_type": self.mime_type}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(473805619, signed=False)
        flags = 0
        if self.thumb is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.file))
        if flags & (1 << 0):
            writer.write(bytes(self.thumb))
        writer.write_string(self.file_name)
        writer.write_string(self.mime_type)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        file = reader.tgread_object()
        if flags & (1 << 0):
            thumb = reader.tgread_object()
        else:
            thumb = None
        file_name = reader.read_string()
        mime_type = reader.read_string()
        return cls(file, thumb, file_name, mime_type)

@register
class AccountCreateTheme(TLObject):
    CONSTRUCTOR_ID = 1697530880
    __slots__ = ('slug', 'title', 'document', 'settings')
    def __init__(self, slug: str, title: str, document: 'InputDocument' = None, settings: 'Vector' = None):
        self.slug = slug
        self.title = title
        self.document = document
        self.settings = settings
    def to_dict(self):
        return {"slug": self.slug, "title": self.title, "document": self.document, "settings": self.settings}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1697530880, signed=False)
        flags = 0
        if self.document is not None: flags |= 1 << 2
        if self.settings is not None: flags |= 1 << 3
        writer.write_int(flags, signed=False)
        writer.write_string(self.slug)
        writer.write_string(self.title)
        if flags & (1 << 2):
            writer.write(bytes(self.document))
        if flags & (1 << 3):
            writer.write(bytes(self.settings))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        slug = reader.read_string()
        title = reader.read_string()
        if flags & (1 << 2):
            document = reader.tgread_object()
        else:
            document = None
        if flags & (1 << 3):
            settings = reader.tgread_object()
        else:
            settings = None
        return cls(slug, title, document, settings)

@register
class AccountUpdateTheme(TLObject):
    CONSTRUCTOR_ID = 737414348
    __slots__ = ('format', 'theme', 'slug', 'title', 'document', 'settings')
    def __init__(self, format: str, theme: 'InputTheme', slug: str = None, title: str = None, document: 'InputDocument' = None, settings: 'Vector' = None):
        self.format = format
        self.theme = theme
        self.slug = slug
        self.title = title
        self.document = document
        self.settings = settings
    def to_dict(self):
        return {"format": self.format, "theme": self.theme, "slug": self.slug, "title": self.title, "document": self.document, "settings": self.settings}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(737414348, signed=False)
        flags = 0
        if self.slug is not None: flags |= 1 << 0
        if self.title is not None: flags |= 1 << 1
        if self.document is not None: flags |= 1 << 2
        if self.settings is not None: flags |= 1 << 3
        writer.write_int(flags, signed=False)
        writer.write_string(self.format)
        writer.write(bytes(self.theme))
        if flags & (1 << 0):
            writer.write_string(self.slug)
        if flags & (1 << 1):
            writer.write_string(self.title)
        if flags & (1 << 2):
            writer.write(bytes(self.document))
        if flags & (1 << 3):
            writer.write(bytes(self.settings))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        format = reader.read_string()
        theme = reader.tgread_object()
        if flags & (1 << 0):
            slug = reader.read_string()
        else:
            slug = None
        if flags & (1 << 1):
            title = reader.read_string()
        else:
            title = None
        if flags & (1 << 2):
            document = reader.tgread_object()
        else:
            document = None
        if flags & (1 << 3):
            settings = reader.tgread_object()
        else:
            settings = None
        return cls(format, theme, slug, title, document, settings)

@register
class AccountSaveTheme(TLObject):
    CONSTRUCTOR_ID = 4065792108
    __slots__ = ('theme', 'unsave')
    def __init__(self, theme: 'InputTheme', unsave: bool):
        self.theme = theme
        self.unsave = unsave
    def to_dict(self):
        return {"theme": self.theme, "unsave": self.unsave}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4065792108, signed=False)
        writer.write(bytes(self.theme))
        writer.write(serialize_bool(self.unsave))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        theme = reader.tgread_object()
        unsave = reader.tgread_bool()
        return cls(theme, unsave)

@register
class AccountInstallTheme(TLObject):
    CONSTRUCTOR_ID = 3341269819
    __slots__ = ('dark', 'theme', 'format', 'base_theme')
    def __init__(self, dark: bool = None, theme: 'InputTheme' = None, format: str = None, base_theme: 'BaseTheme' = None):
        self.dark = dark
        self.theme = theme
        self.format = format
        self.base_theme = base_theme
    def to_dict(self):
        return {"dark": self.dark, "theme": self.theme, "format": self.format, "base_theme": self.base_theme}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3341269819, signed=False)
        flags = 0
        if self.dark: flags |= 1 << 0
        if self.theme is not None: flags |= 1 << 1
        if self.format is not None: flags |= 1 << 2
        if self.base_theme is not None: flags |= 1 << 3
        writer.write_int(flags, signed=False)
        if flags & (1 << 1):
            writer.write(bytes(self.theme))
        if flags & (1 << 2):
            writer.write_string(self.format)
        if flags & (1 << 3):
            writer.write(bytes(self.base_theme))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        dark = bool(flags & (1 << 0))
        if flags & (1 << 1):
            theme = reader.tgread_object()
        else:
            theme = None
        if flags & (1 << 2):
            format = reader.read_string()
        else:
            format = None
        if flags & (1 << 3):
            base_theme = reader.tgread_object()
        else:
            base_theme = None
        return cls(dark, theme, format, base_theme)

@register
class AccountGetTheme(TLObject):
    CONSTRUCTOR_ID = 978872812
    __slots__ = ('format', 'theme')
    def __init__(self, format: str, theme: 'InputTheme'):
        self.format = format
        self.theme = theme
    def to_dict(self):
        return {"format": self.format, "theme": self.theme}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(978872812, signed=False)
        writer.write_string(self.format)
        writer.write(bytes(self.theme))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        format = reader.read_string()
        theme = reader.tgread_object()
        return cls(format, theme)

@register
class AccountGetThemes(TLObject):
    CONSTRUCTOR_ID = 1913054296
    __slots__ = ('format', 'hash')
    def __init__(self, format: str, hash: int):
        self.format = format
        self.hash = hash
    def to_dict(self):
        return {"format": self.format, "hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1913054296, signed=False)
        writer.write_string(self.format)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        format = reader.read_string()
        hash = reader.read_long()
        return cls(format, hash)

@register
class AccountSetContentSettings(TLObject):
    CONSTRUCTOR_ID = 3044323691
    __slots__ = ('sensitive_enabled')
    def __init__(self, sensitive_enabled: bool = None):
        self.sensitive_enabled = sensitive_enabled
    def to_dict(self):
        return {"sensitive_enabled": self.sensitive_enabled}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3044323691, signed=False)
        flags = 0
        if self.sensitive_enabled: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        sensitive_enabled = bool(flags & (1 << 0))
        return cls(sensitive_enabled)

@register
class AccountGetContentSettings(TLObject):
    CONSTRUCTOR_ID = 2342210990
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2342210990, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class AccountGetMultiWallPapers(TLObject):
    CONSTRUCTOR_ID = 1705865692
    __slots__ = ('wallpapers')
    def __init__(self, wallpapers: 'Vector'):
        self.wallpapers = wallpapers
    def to_dict(self):
        return {"wallpapers": self.wallpapers}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1705865692, signed=False)
        writer.write(bytes(self.wallpapers))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        wallpapers = reader.tgread_object()
        return cls(wallpapers)

@register
class AccountGetGlobalPrivacySettings(TLObject):
    CONSTRUCTOR_ID = 3945483510
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3945483510, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class AccountSetGlobalPrivacySettings(TLObject):
    CONSTRUCTOR_ID = 517647042
    __slots__ = ('settings')
    def __init__(self, settings: 'GlobalPrivacySettings'):
        self.settings = settings
    def to_dict(self):
        return {"settings": self.settings}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(517647042, signed=False)
        writer.write(bytes(self.settings))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        settings = reader.tgread_object()
        return cls(settings)

@register
class AccountReportProfilePhoto(TLObject):
    CONSTRUCTOR_ID = 4203529973
    __slots__ = ('peer', 'photo_id', 'reason', 'message')
    def __init__(self, peer: 'InputPeer', photo_id: 'InputPhoto', reason: 'ReportReason', message: str):
        self.peer = peer
        self.photo_id = photo_id
        self.reason = reason
        self.message = message
    def to_dict(self):
        return {"peer": self.peer, "photo_id": self.photo_id, "reason": self.reason, "message": self.message}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4203529973, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.photo_id))
        writer.write(bytes(self.reason))
        writer.write_string(self.message)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        photo_id = reader.tgread_object()
        reason = reader.tgread_object()
        message = reader.read_string()
        return cls(peer, photo_id, reason, message)

@register
class AccountResetPassword(TLObject):
    CONSTRUCTOR_ID = 2466827803
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2466827803, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class AccountDeclinePasswordReset(TLObject):
    CONSTRUCTOR_ID = 1284770294
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1284770294, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class AccountGetChatThemes(TLObject):
    CONSTRUCTOR_ID = 3594051209
    __slots__ = ('hash')
    def __init__(self, hash: int):
        self.hash = hash
    def to_dict(self):
        return {"hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3594051209, signed=False)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_long()
        return cls(hash)

@register
class AccountSetAuthorizationTTL(TLObject):
    CONSTRUCTOR_ID = 3213466272
    __slots__ = ('authorization_ttl_days')
    def __init__(self, authorization_ttl_days: int):
        self.authorization_ttl_days = authorization_ttl_days
    def to_dict(self):
        return {"authorization_ttl_days": self.authorization_ttl_days}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3213466272, signed=False)
        writer.write_int(self.authorization_ttl_days, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        authorization_ttl_days = reader.read_int()
        return cls(authorization_ttl_days)

@register
class AccountChangeAuthorizationSettings(TLObject):
    CONSTRUCTOR_ID = 1089766498
    __slots__ = ('confirmed', 'hash', 'encrypted_requests_disabled', 'call_requests_disabled')
    def __init__(self, hash: int, confirmed: bool = None, encrypted_requests_disabled: bool = None, call_requests_disabled: bool = None):
        self.confirmed = confirmed
        self.hash = hash
        self.encrypted_requests_disabled = encrypted_requests_disabled
        self.call_requests_disabled = call_requests_disabled
    def to_dict(self):
        return {"confirmed": self.confirmed, "hash": self.hash, "encrypted_requests_disabled": self.encrypted_requests_disabled, "call_requests_disabled": self.call_requests_disabled}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1089766498, signed=False)
        flags = 0
        if self.confirmed: flags |= 1 << 3
        if self.encrypted_requests_disabled is not None: flags |= 1 << 0
        if self.call_requests_disabled is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write_long(self.hash, signed=False)
        if flags & (1 << 0):
            writer.write(serialize_bool(self.encrypted_requests_disabled))
        if flags & (1 << 1):
            writer.write(serialize_bool(self.call_requests_disabled))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        confirmed = bool(flags & (1 << 3))
        hash = reader.read_long()
        if flags & (1 << 0):
            encrypted_requests_disabled = reader.tgread_bool()
        else:
            encrypted_requests_disabled = None
        if flags & (1 << 1):
            call_requests_disabled = reader.tgread_bool()
        else:
            call_requests_disabled = None
        return cls(confirmed, hash, encrypted_requests_disabled, call_requests_disabled)

@register
class AccountGetSavedRingtones(TLObject):
    CONSTRUCTOR_ID = 3784319624
    __slots__ = ('hash')
    def __init__(self, hash: int):
        self.hash = hash
    def to_dict(self):
        return {"hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3784319624, signed=False)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_long()
        return cls(hash)

@register
class AccountSaveRingtone(TLObject):
    CONSTRUCTOR_ID = 1038768899
    __slots__ = ('id', 'unsave')
    def __init__(self, id: 'InputDocument', unsave: bool):
        self.id = id
        self.unsave = unsave
    def to_dict(self):
        return {"id": self.id, "unsave": self.unsave}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1038768899, signed=False)
        writer.write(bytes(self.id))
        writer.write(serialize_bool(self.unsave))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        id = reader.tgread_object()
        unsave = reader.tgread_bool()
        return cls(id, unsave)

@register
class AccountUploadRingtone(TLObject):
    CONSTRUCTOR_ID = 2199552930
    __slots__ = ('file', 'file_name', 'mime_type')
    def __init__(self, file: 'InputFile', file_name: str, mime_type: str):
        self.file = file
        self.file_name = file_name
        self.mime_type = mime_type
    def to_dict(self):
        return {"file": self.file, "file_name": self.file_name, "mime_type": self.mime_type}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2199552930, signed=False)
        writer.write(bytes(self.file))
        writer.write_string(self.file_name)
        writer.write_string(self.mime_type)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        file = reader.tgread_object()
        file_name = reader.read_string()
        mime_type = reader.read_string()
        return cls(file, file_name, mime_type)

@register
class AccountUpdateEmojiStatus(TLObject):
    CONSTRUCTOR_ID = 4224966251
    __slots__ = ('emoji_status')
    def __init__(self, emoji_status: 'EmojiStatus'):
        self.emoji_status = emoji_status
    def to_dict(self):
        return {"emoji_status": self.emoji_status}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4224966251, signed=False)
        writer.write(bytes(self.emoji_status))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        emoji_status = reader.tgread_object()
        return cls(emoji_status)

@register
class AccountGetDefaultEmojiStatuses(TLObject):
    CONSTRUCTOR_ID = 3598005126
    __slots__ = ('hash')
    def __init__(self, hash: int):
        self.hash = hash
    def to_dict(self):
        return {"hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3598005126, signed=False)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_long()
        return cls(hash)

@register
class AccountGetRecentEmojiStatuses(TLObject):
    CONSTRUCTOR_ID = 257392901
    __slots__ = ('hash')
    def __init__(self, hash: int):
        self.hash = hash
    def to_dict(self):
        return {"hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(257392901, signed=False)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_long()
        return cls(hash)

@register
class AccountClearRecentEmojiStatuses(TLObject):
    CONSTRUCTOR_ID = 404757166
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(404757166, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class AccountReorderUsernames(TLObject):
    CONSTRUCTOR_ID = 4015001259
    __slots__ = ('order')
    def __init__(self, order: 'Vector'):
        self.order = order
    def to_dict(self):
        return {"order": self.order}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4015001259, signed=False)
        writer.write(bytes(self.order))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        order = reader.tgread_object()
        return cls(order)

@register
class AccountToggleUsername(TLObject):
    CONSTRUCTOR_ID = 1490465654
    __slots__ = ('username', 'active')
    def __init__(self, username: str, active: bool):
        self.username = username
        self.active = active
    def to_dict(self):
        return {"username": self.username, "active": self.active}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1490465654, signed=False)
        writer.write_string(self.username)
        writer.write(serialize_bool(self.active))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        username = reader.read_string()
        active = reader.tgread_bool()
        return cls(username, active)

@register
class AccountGetDefaultProfilePhotoEmojis(TLObject):
    CONSTRUCTOR_ID = 3799319336
    __slots__ = ('hash')
    def __init__(self, hash: int):
        self.hash = hash
    def to_dict(self):
        return {"hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3799319336, signed=False)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_long()
        return cls(hash)

@register
class AccountGetDefaultGroupPhotoEmojis(TLObject):
    CONSTRUCTOR_ID = 2438488238
    __slots__ = ('hash')
    def __init__(self, hash: int):
        self.hash = hash
    def to_dict(self):
        return {"hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2438488238, signed=False)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_long()
        return cls(hash)

@register
class AccountGetAutoSaveSettings(TLObject):
    CONSTRUCTOR_ID = 2915810522
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2915810522, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class AccountSaveAutoSaveSettings(TLObject):
    CONSTRUCTOR_ID = 3600515937
    __slots__ = ('users', 'chats', 'broadcasts', 'peer', 'settings')
    def __init__(self, settings: 'AutoSaveSettings', users: bool = None, chats: bool = None, broadcasts: bool = None, peer: 'InputPeer' = None):
        self.users = users
        self.chats = chats
        self.broadcasts = broadcasts
        self.peer = peer
        self.settings = settings
    def to_dict(self):
        return {"users": self.users, "chats": self.chats, "broadcasts": self.broadcasts, "peer": self.peer, "settings": self.settings}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3600515937, signed=False)
        flags = 0
        if self.users: flags |= 1 << 0
        if self.chats: flags |= 1 << 1
        if self.broadcasts: flags |= 1 << 2
        if self.peer is not None: flags |= 1 << 3
        writer.write_int(flags, signed=False)
        if flags & (1 << 3):
            writer.write(bytes(self.peer))
        writer.write(bytes(self.settings))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        users = bool(flags & (1 << 0))
        chats = bool(flags & (1 << 1))
        broadcasts = bool(flags & (1 << 2))
        if flags & (1 << 3):
            peer = reader.tgread_object()
        else:
            peer = None
        settings = reader.tgread_object()
        return cls(users, chats, broadcasts, peer, settings)

@register
class AccountDeleteAutoSaveExceptions(TLObject):
    CONSTRUCTOR_ID = 1404829728
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1404829728, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class AccountInvalidateSignInCodes(TLObject):
    CONSTRUCTOR_ID = 3398101178
    __slots__ = ('codes')
    def __init__(self, codes: 'Vector'):
        self.codes = codes
    def to_dict(self):
        return {"codes": self.codes}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3398101178, signed=False)
        writer.write(bytes(self.codes))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        codes = reader.tgread_object()
        return cls(codes)

@register
class AccountUpdateColor(TLObject):
    CONSTRUCTOR_ID = 1749885262
    __slots__ = ('for_profile', 'color')
    def __init__(self, for_profile: bool = None, color: 'PeerColor' = None):
        self.for_profile = for_profile
        self.color = color
    def to_dict(self):
        return {"for_profile": self.for_profile, "color": self.color}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1749885262, signed=False)
        flags = 0
        if self.for_profile: flags |= 1 << 1
        if self.color is not None: flags |= 1 << 2
        writer.write_int(flags, signed=False)
        if flags & (1 << 2):
            writer.write(bytes(self.color))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        for_profile = bool(flags & (1 << 1))
        if flags & (1 << 2):
            color = reader.tgread_object()
        else:
            color = None
        return cls(for_profile, color)

@register
class AccountGetDefaultBackgroundEmojis(TLObject):
    CONSTRUCTOR_ID = 2785720782
    __slots__ = ('hash')
    def __init__(self, hash: int):
        self.hash = hash
    def to_dict(self):
        return {"hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2785720782, signed=False)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_long()
        return cls(hash)

@register
class AccountGetChannelDefaultEmojiStatuses(TLObject):
    CONSTRUCTOR_ID = 1999087573
    __slots__ = ('hash')
    def __init__(self, hash: int):
        self.hash = hash
    def to_dict(self):
        return {"hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1999087573, signed=False)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_long()
        return cls(hash)

@register
class AccountGetChannelRestrictedStatusEmojis(TLObject):
    CONSTRUCTOR_ID = 900325589
    __slots__ = ('hash')
    def __init__(self, hash: int):
        self.hash = hash
    def to_dict(self):
        return {"hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(900325589, signed=False)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_long()
        return cls(hash)

@register
class AccountUpdateBusinessWorkHours(TLObject):
    CONSTRUCTOR_ID = 1258348646
    __slots__ = ('business_work_hours')
    def __init__(self, business_work_hours: 'BusinessWorkHours' = None):
        self.business_work_hours = business_work_hours
    def to_dict(self):
        return {"business_work_hours": self.business_work_hours}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1258348646, signed=False)
        flags = 0
        if self.business_work_hours is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        if flags & (1 << 0):
            writer.write(bytes(self.business_work_hours))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        if flags & (1 << 0):
            business_work_hours = reader.tgread_object()
        else:
            business_work_hours = None
        return cls(business_work_hours)

@register
class AccountUpdateBusinessLocation(TLObject):
    CONSTRUCTOR_ID = 2657817370
    __slots__ = ('geo_point', 'address')
    def __init__(self, geo_point: 'InputGeoPoint' = None, address: str = None):
        self.geo_point = geo_point
        self.address = address
    def to_dict(self):
        return {"geo_point": self.geo_point, "address": self.address}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2657817370, signed=False)
        flags = 0
        if self.geo_point is not None: flags |= 1 << 1
        if self.address is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        if flags & (1 << 1):
            writer.write(bytes(self.geo_point))
        if flags & (1 << 0):
            writer.write_string(self.address)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        if flags & (1 << 1):
            geo_point = reader.tgread_object()
        else:
            geo_point = None
        if flags & (1 << 0):
            address = reader.read_string()
        else:
            address = None
        return cls(geo_point, address)

@register
class AccountUpdateBusinessGreetingMessage(TLObject):
    CONSTRUCTOR_ID = 1724755908
    __slots__ = ('message')
    def __init__(self, message: 'InputBusinessGreetingMessage' = None):
        self.message = message
    def to_dict(self):
        return {"message": self.message}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1724755908, signed=False)
        flags = 0
        if self.message is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        if flags & (1 << 0):
            writer.write(bytes(self.message))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        if flags & (1 << 0):
            message = reader.tgread_object()
        else:
            message = None
        return cls(message)

@register
class AccountUpdateBusinessAwayMessage(TLObject):
    CONSTRUCTOR_ID = 2724888485
    __slots__ = ('message')
    def __init__(self, message: 'InputBusinessAwayMessage' = None):
        self.message = message
    def to_dict(self):
        return {"message": self.message}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2724888485, signed=False)
        flags = 0
        if self.message is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        if flags & (1 << 0):
            writer.write(bytes(self.message))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        if flags & (1 << 0):
            message = reader.tgread_object()
        else:
            message = None
        return cls(message)

@register
class AccountUpdateConnectedBot(TLObject):
    CONSTRUCTOR_ID = 1721797758
    __slots__ = ('deleted', 'rights', 'bot', 'recipients')
    def __init__(self, bot: 'InputUser', recipients: 'InputBusinessBotRecipients', deleted: bool = None, rights: 'BusinessBotRights' = None):
        self.deleted = deleted
        self.rights = rights
        self.bot = bot
        self.recipients = recipients
    def to_dict(self):
        return {"deleted": self.deleted, "rights": self.rights, "bot": self.bot, "recipients": self.recipients}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1721797758, signed=False)
        flags = 0
        if self.deleted: flags |= 1 << 1
        if self.rights is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        if flags & (1 << 0):
            writer.write(bytes(self.rights))
        writer.write(bytes(self.bot))
        writer.write(bytes(self.recipients))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        deleted = bool(flags & (1 << 1))
        if flags & (1 << 0):
            rights = reader.tgread_object()
        else:
            rights = None
        bot = reader.tgread_object()
        recipients = reader.tgread_object()
        return cls(deleted, rights, bot, recipients)

@register
class AccountGetConnectedBots(TLObject):
    CONSTRUCTOR_ID = 1319421967
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1319421967, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class AccountGetBotBusinessConnection(TLObject):
    CONSTRUCTOR_ID = 1990746736
    __slots__ = ('connection_id')
    def __init__(self, connection_id: str):
        self.connection_id = connection_id
    def to_dict(self):
        return {"connection_id": self.connection_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1990746736, signed=False)
        writer.write_string(self.connection_id)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        connection_id = reader.read_string()
        return cls(connection_id)

@register
class AccountUpdateBusinessIntro(TLObject):
    CONSTRUCTOR_ID = 2786381876
    __slots__ = ('intro')
    def __init__(self, intro: 'InputBusinessIntro' = None):
        self.intro = intro
    def to_dict(self):
        return {"intro": self.intro}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2786381876, signed=False)
        flags = 0
        if self.intro is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        if flags & (1 << 0):
            writer.write(bytes(self.intro))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        if flags & (1 << 0):
            intro = reader.tgread_object()
        else:
            intro = None
        return cls(intro)

@register
class AccountToggleConnectedBotPaused(TLObject):
    CONSTRUCTOR_ID = 1684934807
    __slots__ = ('peer', 'paused')
    def __init__(self, peer: 'InputPeer', paused: bool):
        self.peer = peer
        self.paused = paused
    def to_dict(self):
        return {"peer": self.peer, "paused": self.paused}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1684934807, signed=False)
        writer.write(bytes(self.peer))
        writer.write(serialize_bool(self.paused))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        paused = reader.tgread_bool()
        return cls(peer, paused)

@register
class AccountDisablePeerConnectedBot(TLObject):
    CONSTRUCTOR_ID = 1581481689
    __slots__ = ('peer')
    def __init__(self, peer: 'InputPeer'):
        self.peer = peer
    def to_dict(self):
        return {"peer": self.peer}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1581481689, signed=False)
        writer.write(bytes(self.peer))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        return cls(peer)

@register
class AccountUpdateBirthday(TLObject):
    CONSTRUCTOR_ID = 3429764113
    __slots__ = ('birthday')
    def __init__(self, birthday: 'Birthday' = None):
        self.birthday = birthday
    def to_dict(self):
        return {"birthday": self.birthday}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3429764113, signed=False)
        flags = 0
        if self.birthday is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        if flags & (1 << 0):
            writer.write(bytes(self.birthday))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        if flags & (1 << 0):
            birthday = reader.tgread_object()
        else:
            birthday = None
        return cls(birthday)

@register
class AccountCreateBusinessChatLink(TLObject):
    CONSTRUCTOR_ID = 2287068814
    __slots__ = ('link')
    def __init__(self, link: 'InputBusinessChatLink'):
        self.link = link
    def to_dict(self):
        return {"link": self.link}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2287068814, signed=False)
        writer.write(bytes(self.link))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        link = reader.tgread_object()
        return cls(link)

@register
class AccountEditBusinessChatLink(TLObject):
    CONSTRUCTOR_ID = 2352222383
    __slots__ = ('slug', 'link')
    def __init__(self, slug: str, link: 'InputBusinessChatLink'):
        self.slug = slug
        self.link = link
    def to_dict(self):
        return {"slug": self.slug, "link": self.link}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2352222383, signed=False)
        writer.write_string(self.slug)
        writer.write(bytes(self.link))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        slug = reader.read_string()
        link = reader.tgread_object()
        return cls(slug, link)

@register
class AccountDeleteBusinessChatLink(TLObject):
    CONSTRUCTOR_ID = 1611085428
    __slots__ = ('slug')
    def __init__(self, slug: str):
        self.slug = slug
    def to_dict(self):
        return {"slug": self.slug}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1611085428, signed=False)
        writer.write_string(self.slug)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        slug = reader.read_string()
        return cls(slug)

@register
class AccountGetBusinessChatLinks(TLObject):
    CONSTRUCTOR_ID = 1869667809
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1869667809, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class AccountResolveBusinessChatLink(TLObject):
    CONSTRUCTOR_ID = 1418913262
    __slots__ = ('slug')
    def __init__(self, slug: str):
        self.slug = slug
    def to_dict(self):
        return {"slug": self.slug}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1418913262, signed=False)
        writer.write_string(self.slug)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        slug = reader.read_string()
        return cls(slug)

@register
class AccountUpdatePersonalChannel(TLObject):
    CONSTRUCTOR_ID = 3645048288
    __slots__ = ('channel')
    def __init__(self, channel: 'InputChannel'):
        self.channel = channel
    def to_dict(self):
        return {"channel": self.channel}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3645048288, signed=False)
        writer.write(bytes(self.channel))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        channel = reader.tgread_object()
        return cls(channel)

@register
class AccountToggleSponsoredMessages(TLObject):
    CONSTRUCTOR_ID = 3118048141
    __slots__ = ('enabled')
    def __init__(self, enabled: bool):
        self.enabled = enabled
    def to_dict(self):
        return {"enabled": self.enabled}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3118048141, signed=False)
        writer.write(serialize_bool(self.enabled))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        enabled = reader.tgread_bool()
        return cls(enabled)

@register
class AccountGetReactionsNotifySettings(TLObject):
    CONSTRUCTOR_ID = 115172684
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(115172684, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class AccountSetReactionsNotifySettings(TLObject):
    CONSTRUCTOR_ID = 829220168
    __slots__ = ('settings')
    def __init__(self, settings: 'ReactionsNotifySettings'):
        self.settings = settings
    def to_dict(self):
        return {"settings": self.settings}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(829220168, signed=False)
        writer.write(bytes(self.settings))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        settings = reader.tgread_object()
        return cls(settings)

@register
class AccountGetCollectibleEmojiStatuses(TLObject):
    CONSTRUCTOR_ID = 779830595
    __slots__ = ('hash')
    def __init__(self, hash: int):
        self.hash = hash
    def to_dict(self):
        return {"hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(779830595, signed=False)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_long()
        return cls(hash)

@register
class AccountGetPaidMessagesRevenue(TLObject):
    CONSTRUCTOR_ID = 431639143
    __slots__ = ('parent_peer', 'user_id')
    def __init__(self, user_id: 'InputUser', parent_peer: 'InputPeer' = None):
        self.parent_peer = parent_peer
        self.user_id = user_id
    def to_dict(self):
        return {"parent_peer": self.parent_peer, "user_id": self.user_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(431639143, signed=False)
        flags = 0
        if self.parent_peer is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        if flags & (1 << 0):
            writer.write(bytes(self.parent_peer))
        writer.write(bytes(self.user_id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        if flags & (1 << 0):
            parent_peer = reader.tgread_object()
        else:
            parent_peer = None
        user_id = reader.tgread_object()
        return cls(parent_peer, user_id)

@register
class AccountToggleNoPaidMessagesException(TLObject):
    CONSTRUCTOR_ID = 4264483446
    __slots__ = ('refund_charged', 'require_payment', 'parent_peer', 'user_id')
    def __init__(self, user_id: 'InputUser', refund_charged: bool = None, require_payment: bool = None, parent_peer: 'InputPeer' = None):
        self.refund_charged = refund_charged
        self.require_payment = require_payment
        self.parent_peer = parent_peer
        self.user_id = user_id
    def to_dict(self):
        return {"refund_charged": self.refund_charged, "require_payment": self.require_payment, "parent_peer": self.parent_peer, "user_id": self.user_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4264483446, signed=False)
        flags = 0
        if self.refund_charged: flags |= 1 << 0
        if self.require_payment: flags |= 1 << 2
        if self.parent_peer is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        if flags & (1 << 1):
            writer.write(bytes(self.parent_peer))
        writer.write(bytes(self.user_id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        refund_charged = bool(flags & (1 << 0))
        require_payment = bool(flags & (1 << 2))
        if flags & (1 << 1):
            parent_peer = reader.tgread_object()
        else:
            parent_peer = None
        user_id = reader.tgread_object()
        return cls(refund_charged, require_payment, parent_peer, user_id)

@register
class AccountSetMainProfileTab(TLObject):
    CONSTRUCTOR_ID = 1575909552
    __slots__ = ('tab')
    def __init__(self, tab: 'ProfileTab'):
        self.tab = tab
    def to_dict(self):
        return {"tab": self.tab}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1575909552, signed=False)
        writer.write(bytes(self.tab))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        tab = reader.tgread_object()
        return cls(tab)

@register
class AccountSaveMusic(TLObject):
    CONSTRUCTOR_ID = 2993107625
    __slots__ = ('unsave', 'id', 'after_id')
    def __init__(self, id: 'InputDocument', unsave: bool = None, after_id: 'InputDocument' = None):
        self.unsave = unsave
        self.id = id
        self.after_id = after_id
    def to_dict(self):
        return {"unsave": self.unsave, "id": self.id, "after_id": self.after_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2993107625, signed=False)
        flags = 0
        if self.unsave: flags |= 1 << 0
        if self.after_id is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.id))
        if flags & (1 << 1):
            writer.write(bytes(self.after_id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        unsave = bool(flags & (1 << 0))
        id = reader.tgread_object()
        if flags & (1 << 1):
            after_id = reader.tgread_object()
        else:
            after_id = None
        return cls(unsave, id, after_id)

@register
class AccountGetSavedMusicIds(TLObject):
    CONSTRUCTOR_ID = 3768410031
    __slots__ = ('hash')
    def __init__(self, hash: int):
        self.hash = hash
    def to_dict(self):
        return {"hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3768410031, signed=False)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_long()
        return cls(hash)

@register
class AccountGetUniqueGiftChatThemes(TLObject):
    CONSTRUCTOR_ID = 3828148681
    __slots__ = ('offset', 'limit', 'hash')
    def __init__(self, offset: str, limit: int, hash: int):
        self.offset = offset
        self.limit = limit
        self.hash = hash
    def to_dict(self):
        return {"offset": self.offset, "limit": self.limit, "hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3828148681, signed=False)
        writer.write_string(self.offset)
        writer.write_int(self.limit, signed=True)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        offset = reader.read_string()
        limit = reader.read_int()
        hash = reader.read_long()
        return cls(offset, limit, hash)

@register
class AccountInitPasskeyRegistration(TLObject):
    CONSTRUCTOR_ID = 1117079528
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1117079528, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class AccountRegisterPasskey(TLObject):
    CONSTRUCTOR_ID = 1437867990
    __slots__ = ('credential')
    def __init__(self, credential: 'InputPasskeyCredential'):
        self.credential = credential
    def to_dict(self):
        return {"credential": self.credential}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1437867990, signed=False)
        writer.write(bytes(self.credential))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        credential = reader.tgread_object()
        return cls(credential)

@register
class AccountGetPasskeys(TLObject):
    CONSTRUCTOR_ID = 3927903314
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3927903314, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class AccountDeletePasskey(TLObject):
    CONSTRUCTOR_ID = 4122302015
    __slots__ = ('id')
    def __init__(self, id: str):
        self.id = id
    def to_dict(self):
        return {"id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4122302015, signed=False)
        writer.write_string(self.id)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        id = reader.read_string()
        return cls(id)

