"""Auto-generated TL functions. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

@register
class AuthSendCode(TLObject):
    CONSTRUCTOR_ID = 2792825935
    __slots__ = ('phone_number', 'api_id', 'api_hash', 'settings')
    def __init__(self, phone_number: str, api_id: int, api_hash: str, settings: 'CodeSettings'):
        self.phone_number = phone_number
        self.api_id = api_id
        self.api_hash = api_hash
        self.settings = settings
    def to_dict(self):
        return {"phone_number": self.phone_number, "api_id": self.api_id, "api_hash": self.api_hash, "settings": self.settings}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2792825935, signed=False)
        writer.write_string(self.phone_number)
        writer.write_int(self.api_id, signed=True)
        writer.write_string(self.api_hash)
        writer.write(bytes(self.settings))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        phone_number = reader.read_string()
        api_id = reader.read_int()
        api_hash = reader.read_string()
        settings = reader.tgread_object()
        return cls(phone_number, api_id, api_hash, settings)

@register
class AuthSignUp(TLObject):
    CONSTRUCTOR_ID = 2865215255
    __slots__ = ('no_joined_notifications', 'phone_number', 'phone_code_hash', 'first_name', 'last_name')
    def __init__(self, phone_number: str, phone_code_hash: str, first_name: str, last_name: str, no_joined_notifications: bool = None):
        self.no_joined_notifications = no_joined_notifications
        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash
        self.first_name = first_name
        self.last_name = last_name
    def to_dict(self):
        return {"no_joined_notifications": self.no_joined_notifications, "phone_number": self.phone_number, "phone_code_hash": self.phone_code_hash, "first_name": self.first_name, "last_name": self.last_name}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2865215255, signed=False)
        flags = 0
        if self.no_joined_notifications: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write_string(self.phone_number)
        writer.write_string(self.phone_code_hash)
        writer.write_string(self.first_name)
        writer.write_string(self.last_name)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        no_joined_notifications = bool(flags & (1 << 0))
        phone_number = reader.read_string()
        phone_code_hash = reader.read_string()
        first_name = reader.read_string()
        last_name = reader.read_string()
        return cls(no_joined_notifications, phone_number, phone_code_hash, first_name, last_name)

@register
class AuthSignIn(TLObject):
    CONSTRUCTOR_ID = 2371004753
    __slots__ = ('phone_number', 'phone_code_hash', 'phone_code', 'email_verification')
    def __init__(self, phone_number: str, phone_code_hash: str, phone_code: str = None, email_verification: 'EmailVerification' = None):
        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash
        self.phone_code = phone_code
        self.email_verification = email_verification
    def to_dict(self):
        return {"phone_number": self.phone_number, "phone_code_hash": self.phone_code_hash, "phone_code": self.phone_code, "email_verification": self.email_verification}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2371004753, signed=False)
        flags = 0
        if self.phone_code is not None: flags |= 1 << 0
        if self.email_verification is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write_string(self.phone_number)
        writer.write_string(self.phone_code_hash)
        if flags & (1 << 0):
            writer.write_string(self.phone_code)
        if flags & (1 << 1):
            writer.write(bytes(self.email_verification))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        phone_number = reader.read_string()
        phone_code_hash = reader.read_string()
        if flags & (1 << 0):
            phone_code = reader.read_string()
        else:
            phone_code = None
        if flags & (1 << 1):
            email_verification = reader.tgread_object()
        else:
            email_verification = None
        return cls(phone_number, phone_code_hash, phone_code, email_verification)

@register
class AuthLogOut(TLObject):
    CONSTRUCTOR_ID = 1047706137
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1047706137, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class AuthResetAuthorizations(TLObject):
    CONSTRUCTOR_ID = 2678787354
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2678787354, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class AuthExportAuthorization(TLObject):
    CONSTRUCTOR_ID = 3854565325
    __slots__ = ('dc_id')
    def __init__(self, dc_id: int):
        self.dc_id = dc_id
    def to_dict(self):
        return {"dc_id": self.dc_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3854565325, signed=False)
        writer.write_int(self.dc_id, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        dc_id = reader.read_int()
        return cls(dc_id)

@register
class AuthImportAuthorization(TLObject):
    CONSTRUCTOR_ID = 2776268205
    __slots__ = ('id', 'bytes')
    def __init__(self, id: int, bytes: bytes):
        self.id = id
        self.bytes = bytes
    def to_dict(self):
        return {"id": self.id, "bytes": self.bytes}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2776268205, signed=False)
        writer.write_long(self.id, signed=False)
        writer.write_bytes(self.bytes)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        id = reader.read_long()
        bytes = reader.read_bytes()
        return cls(id, bytes)

@register
class AuthBindTempAuthKey(TLObject):
    CONSTRUCTOR_ID = 3453233669
    __slots__ = ('perm_auth_key_id', 'nonce', 'expires_at', 'encrypted_message')
    def __init__(self, perm_auth_key_id: int, nonce: int, expires_at: int, encrypted_message: bytes):
        self.perm_auth_key_id = perm_auth_key_id
        self.nonce = nonce
        self.expires_at = expires_at
        self.encrypted_message = encrypted_message
    def to_dict(self):
        return {"perm_auth_key_id": self.perm_auth_key_id, "nonce": self.nonce, "expires_at": self.expires_at, "encrypted_message": self.encrypted_message}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3453233669, signed=False)
        writer.write_long(self.perm_auth_key_id, signed=False)
        writer.write_long(self.nonce, signed=False)
        writer.write_int(self.expires_at, signed=True)
        writer.write_bytes(self.encrypted_message)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        perm_auth_key_id = reader.read_long()
        nonce = reader.read_long()
        expires_at = reader.read_int()
        encrypted_message = reader.read_bytes()
        return cls(perm_auth_key_id, nonce, expires_at, encrypted_message)

@register
class AuthImportBotAuthorization(TLObject):
    CONSTRUCTOR_ID = 1738800940
    __slots__ = ('flags', 'api_id', 'api_hash', 'bot_auth_token')
    def __init__(self, flags: int, api_id: int, api_hash: str, bot_auth_token: str):
        self.flags = flags
        self.api_id = api_id
        self.api_hash = api_hash
        self.bot_auth_token = bot_auth_token
    def to_dict(self):
        return {"flags": self.flags, "api_id": self.api_id, "api_hash": self.api_hash, "bot_auth_token": self.bot_auth_token}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1738800940, signed=False)
        writer.write_int(self.flags, signed=True)
        writer.write_int(self.api_id, signed=True)
        writer.write_string(self.api_hash)
        writer.write_string(self.bot_auth_token)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()
        api_id = reader.read_int()
        api_hash = reader.read_string()
        bot_auth_token = reader.read_string()
        return cls(flags, api_id, api_hash, bot_auth_token)

@register
class AuthCheckPassword(TLObject):
    CONSTRUCTOR_ID = 3515567382
    __slots__ = ('password')
    def __init__(self, password: 'InputCheckPasswordSRP'):
        self.password = password
    def to_dict(self):
        return {"password": self.password}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3515567382, signed=False)
        writer.write(bytes(self.password))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        password = reader.tgread_object()
        return cls(password)

@register
class AuthRequestPasswordRecovery(TLObject):
    CONSTRUCTOR_ID = 3633822822
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3633822822, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class AuthRecoverPassword(TLObject):
    CONSTRUCTOR_ID = 923364464
    __slots__ = ('code', 'new_settings')
    def __init__(self, code: str, new_settings: 'AccountPasswordInputSettings' = None):
        self.code = code
        self.new_settings = new_settings
    def to_dict(self):
        return {"code": self.code, "new_settings": self.new_settings}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(923364464, signed=False)
        flags = 0
        if self.new_settings is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write_string(self.code)
        if flags & (1 << 0):
            writer.write(bytes(self.new_settings))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        code = reader.read_string()
        if flags & (1 << 0):
            new_settings = reader.tgread_object()
        else:
            new_settings = None
        return cls(code, new_settings)

@register
class AuthResendCode(TLObject):
    CONSTRUCTOR_ID = 3403969827
    __slots__ = ('phone_number', 'phone_code_hash', 'reason')
    def __init__(self, phone_number: str, phone_code_hash: str, reason: str = None):
        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash
        self.reason = reason
    def to_dict(self):
        return {"phone_number": self.phone_number, "phone_code_hash": self.phone_code_hash, "reason": self.reason}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3403969827, signed=False)
        flags = 0
        if self.reason is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write_string(self.phone_number)
        writer.write_string(self.phone_code_hash)
        if flags & (1 << 0):
            writer.write_string(self.reason)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        phone_number = reader.read_string()
        phone_code_hash = reader.read_string()
        if flags & (1 << 0):
            reason = reader.read_string()
        else:
            reason = None
        return cls(phone_number, phone_code_hash, reason)

@register
class AuthCancelCode(TLObject):
    CONSTRUCTOR_ID = 520357240
    __slots__ = ('phone_number', 'phone_code_hash')
    def __init__(self, phone_number: str, phone_code_hash: str):
        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash
    def to_dict(self):
        return {"phone_number": self.phone_number, "phone_code_hash": self.phone_code_hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(520357240, signed=False)
        writer.write_string(self.phone_number)
        writer.write_string(self.phone_code_hash)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        phone_number = reader.read_string()
        phone_code_hash = reader.read_string()
        return cls(phone_number, phone_code_hash)

@register
class AuthDropTempAuthKeys(TLObject):
    CONSTRUCTOR_ID = 2387124616
    __slots__ = ('except_auth_keys')
    def __init__(self, except_auth_keys: 'Vector'):
        self.except_auth_keys = except_auth_keys
    def to_dict(self):
        return {"except_auth_keys": self.except_auth_keys}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2387124616, signed=False)
        writer.write(bytes(self.except_auth_keys))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        except_auth_keys = reader.tgread_object()
        return cls(except_auth_keys)

@register
class AuthExportLoginToken(TLObject):
    CONSTRUCTOR_ID = 3084944894
    __slots__ = ('api_id', 'api_hash', 'except_ids')
    def __init__(self, api_id: int, api_hash: str, except_ids: 'Vector'):
        self.api_id = api_id
        self.api_hash = api_hash
        self.except_ids = except_ids
    def to_dict(self):
        return {"api_id": self.api_id, "api_hash": self.api_hash, "except_ids": self.except_ids}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3084944894, signed=False)
        writer.write_int(self.api_id, signed=True)
        writer.write_string(self.api_hash)
        writer.write(bytes(self.except_ids))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        api_id = reader.read_int()
        api_hash = reader.read_string()
        except_ids = reader.tgread_object()
        return cls(api_id, api_hash, except_ids)

@register
class AuthImportLoginToken(TLObject):
    CONSTRUCTOR_ID = 2511101156
    __slots__ = ('token')
    def __init__(self, token: bytes):
        self.token = token
    def to_dict(self):
        return {"token": self.token}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2511101156, signed=False)
        writer.write_bytes(self.token)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        token = reader.read_bytes()
        return cls(token)

@register
class AuthAcceptLoginToken(TLObject):
    CONSTRUCTOR_ID = 3902057805
    __slots__ = ('token')
    def __init__(self, token: bytes):
        self.token = token
    def to_dict(self):
        return {"token": self.token}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3902057805, signed=False)
        writer.write_bytes(self.token)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        token = reader.read_bytes()
        return cls(token)

@register
class AuthCheckRecoveryPassword(TLObject):
    CONSTRUCTOR_ID = 221691769
    __slots__ = ('code')
    def __init__(self, code: str):
        self.code = code
    def to_dict(self):
        return {"code": self.code}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(221691769, signed=False)
        writer.write_string(self.code)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        code = reader.read_string()
        return cls(code)

@register
class AuthImportWebTokenAuthorization(TLObject):
    CONSTRUCTOR_ID = 767062953
    __slots__ = ('api_id', 'api_hash', 'web_auth_token')
    def __init__(self, api_id: int, api_hash: str, web_auth_token: str):
        self.api_id = api_id
        self.api_hash = api_hash
        self.web_auth_token = web_auth_token
    def to_dict(self):
        return {"api_id": self.api_id, "api_hash": self.api_hash, "web_auth_token": self.web_auth_token}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(767062953, signed=False)
        writer.write_int(self.api_id, signed=True)
        writer.write_string(self.api_hash)
        writer.write_string(self.web_auth_token)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        api_id = reader.read_int()
        api_hash = reader.read_string()
        web_auth_token = reader.read_string()
        return cls(api_id, api_hash, web_auth_token)

@register
class AuthRequestFirebaseSms(TLObject):
    CONSTRUCTOR_ID = 2386109982
    __slots__ = ('phone_number', 'phone_code_hash', 'safety_net_token', 'play_integrity_token', 'ios_push_secret')
    def __init__(self, phone_number: str, phone_code_hash: str, safety_net_token: str = None, play_integrity_token: str = None, ios_push_secret: str = None):
        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash
        self.safety_net_token = safety_net_token
        self.play_integrity_token = play_integrity_token
        self.ios_push_secret = ios_push_secret
    def to_dict(self):
        return {"phone_number": self.phone_number, "phone_code_hash": self.phone_code_hash, "safety_net_token": self.safety_net_token, "play_integrity_token": self.play_integrity_token, "ios_push_secret": self.ios_push_secret}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2386109982, signed=False)
        flags = 0
        if self.safety_net_token is not None: flags |= 1 << 0
        if self.play_integrity_token is not None: flags |= 1 << 2
        if self.ios_push_secret is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write_string(self.phone_number)
        writer.write_string(self.phone_code_hash)
        if flags & (1 << 0):
            writer.write_string(self.safety_net_token)
        if flags & (1 << 2):
            writer.write_string(self.play_integrity_token)
        if flags & (1 << 1):
            writer.write_string(self.ios_push_secret)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        phone_number = reader.read_string()
        phone_code_hash = reader.read_string()
        if flags & (1 << 0):
            safety_net_token = reader.read_string()
        else:
            safety_net_token = None
        if flags & (1 << 2):
            play_integrity_token = reader.read_string()
        else:
            play_integrity_token = None
        if flags & (1 << 1):
            ios_push_secret = reader.read_string()
        else:
            ios_push_secret = None
        return cls(phone_number, phone_code_hash, safety_net_token, play_integrity_token, ios_push_secret)

@register
class AuthResetLoginEmail(TLObject):
    CONSTRUCTOR_ID = 2123760019
    __slots__ = ('phone_number', 'phone_code_hash')
    def __init__(self, phone_number: str, phone_code_hash: str):
        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash
    def to_dict(self):
        return {"phone_number": self.phone_number, "phone_code_hash": self.phone_code_hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2123760019, signed=False)
        writer.write_string(self.phone_number)
        writer.write_string(self.phone_code_hash)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        phone_number = reader.read_string()
        phone_code_hash = reader.read_string()
        return cls(phone_number, phone_code_hash)

@register
class AuthReportMissingCode(TLObject):
    CONSTRUCTOR_ID = 3416125430
    __slots__ = ('phone_number', 'phone_code_hash', 'mnc')
    def __init__(self, phone_number: str, phone_code_hash: str, mnc: str):
        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash
        self.mnc = mnc
    def to_dict(self):
        return {"phone_number": self.phone_number, "phone_code_hash": self.phone_code_hash, "mnc": self.mnc}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3416125430, signed=False)
        writer.write_string(self.phone_number)
        writer.write_string(self.phone_code_hash)
        writer.write_string(self.mnc)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        phone_number = reader.read_string()
        phone_code_hash = reader.read_string()
        mnc = reader.read_string()
        return cls(phone_number, phone_code_hash, mnc)

@register
class AuthCheckPaidAuth(TLObject):
    CONSTRUCTOR_ID = 1457889180
    __slots__ = ('phone_number', 'phone_code_hash', 'form_id')
    def __init__(self, phone_number: str, phone_code_hash: str, form_id: int):
        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash
        self.form_id = form_id
    def to_dict(self):
        return {"phone_number": self.phone_number, "phone_code_hash": self.phone_code_hash, "form_id": self.form_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1457889180, signed=False)
        writer.write_string(self.phone_number)
        writer.write_string(self.phone_code_hash)
        writer.write_long(self.form_id, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        phone_number = reader.read_string()
        phone_code_hash = reader.read_string()
        form_id = reader.read_long()
        return cls(phone_number, phone_code_hash, form_id)

@register
class AuthInitPasskeyLogin(TLObject):
    CONSTRUCTOR_ID = 1368051895
    __slots__ = ('api_id', 'api_hash')
    def __init__(self, api_id: int, api_hash: str):
        self.api_id = api_id
        self.api_hash = api_hash
    def to_dict(self):
        return {"api_id": self.api_id, "api_hash": self.api_hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1368051895, signed=False)
        writer.write_int(self.api_id, signed=True)
        writer.write_string(self.api_hash)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        api_id = reader.read_int()
        api_hash = reader.read_string()
        return cls(api_id, api_hash)

@register
class AuthFinishPasskeyLogin(TLObject):
    CONSTRUCTOR_ID = 2555882759
    __slots__ = ('credential', 'from_dc_id', 'from_auth_key_id')
    def __init__(self, credential: 'InputPasskeyCredential', from_dc_id: int = None, from_auth_key_id: int = None):
        self.credential = credential
        self.from_dc_id = from_dc_id
        self.from_auth_key_id = from_auth_key_id
    def to_dict(self):
        return {"credential": self.credential, "from_dc_id": self.from_dc_id, "from_auth_key_id": self.from_auth_key_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2555882759, signed=False)
        flags = 0
        if self.from_dc_id is not None: flags |= 1 << 0
        if self.from_auth_key_id is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.credential))
        if flags & (1 << 0):
            writer.write_int(self.from_dc_id, signed=True)
        if flags & (1 << 0):
            writer.write_long(self.from_auth_key_id, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        credential = reader.tgread_object()
        if flags & (1 << 0):
            from_dc_id = reader.read_int()
        else:
            from_dc_id = None
        if flags & (1 << 0):
            from_auth_key_id = reader.read_long()
        else:
            from_auth_key_id = None
        return cls(credential, from_dc_id, from_auth_key_id)

