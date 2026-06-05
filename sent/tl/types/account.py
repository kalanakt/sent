"""Auto-generated TL types. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional, TYPE_CHECKING
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

@register
class AccountPrivacyRules(TLObject):
    CONSTRUCTOR_ID = 1352683077
    __slots__ = ('rules', 'chats', 'users')
    def __init__(self, rules: 'Vector', chats: 'Vector', users: 'Vector'):
        self.rules = rules
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"rules": self.rules, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1352683077, signed=False)
        writer.write(bytes(self.rules))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        rules = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(rules, chats, users)

@register
class AccountAuthorizations(TLObject):
    CONSTRUCTOR_ID = 1275039392
    __slots__ = ('authorization_ttl_days', 'authorizations')
    def __init__(self, authorization_ttl_days: int, authorizations: 'Vector'):
        self.authorization_ttl_days = authorization_ttl_days
        self.authorizations = authorizations
    def to_dict(self):
        return {"authorization_ttl_days": self.authorization_ttl_days, "authorizations": self.authorizations}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1275039392, signed=False)
        writer.write_int(self.authorization_ttl_days, signed=True)
        writer.write(bytes(self.authorizations))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        authorization_ttl_days = reader.read_int()
        authorizations = reader.tgread_object()
        return cls(authorization_ttl_days, authorizations)

@register
class AccountPassword(TLObject):
    CONSTRUCTOR_ID = 2507886843
    __slots__ = ('has_recovery', 'has_secure_values', 'has_password', 'current_algo', 'srp_B', 'srp_id', 'hint', 'email_unconfirmed_pattern', 'new_algo', 'new_secure_algo', 'secure_random', 'pending_reset_date', 'login_email_pattern')
    def __init__(self, new_algo: 'PasswordKdfAlgo', new_secure_algo: 'SecurePasswordKdfAlgo', secure_random: bytes, has_recovery: bool = None, has_secure_values: bool = None, has_password: bool = None, current_algo: 'PasswordKdfAlgo' = None, srp_B: bytes = None, srp_id: int = None, hint: str = None, email_unconfirmed_pattern: str = None, pending_reset_date: int = None, login_email_pattern: str = None):
        self.has_recovery = has_recovery
        self.has_secure_values = has_secure_values
        self.has_password = has_password
        self.current_algo = current_algo
        self.srp_B = srp_B
        self.srp_id = srp_id
        self.hint = hint
        self.email_unconfirmed_pattern = email_unconfirmed_pattern
        self.new_algo = new_algo
        self.new_secure_algo = new_secure_algo
        self.secure_random = secure_random
        self.pending_reset_date = pending_reset_date
        self.login_email_pattern = login_email_pattern
    def to_dict(self):
        return {"has_recovery": self.has_recovery, "has_secure_values": self.has_secure_values, "has_password": self.has_password, "current_algo": self.current_algo, "srp_B": self.srp_B, "srp_id": self.srp_id, "hint": self.hint, "email_unconfirmed_pattern": self.email_unconfirmed_pattern, "new_algo": self.new_algo, "new_secure_algo": self.new_secure_algo, "secure_random": self.secure_random, "pending_reset_date": self.pending_reset_date, "login_email_pattern": self.login_email_pattern}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2507886843, signed=False)
        flags = 0
        if self.has_recovery: flags |= 1 << 0
        if self.has_secure_values: flags |= 1 << 1
        if self.has_password: flags |= 1 << 2
        if self.current_algo is not None: flags |= 1 << 2
        if self.srp_B is not None: flags |= 1 << 2
        if self.srp_id is not None: flags |= 1 << 2
        if self.hint is not None: flags |= 1 << 3
        if self.email_unconfirmed_pattern is not None: flags |= 1 << 4
        if self.pending_reset_date is not None: flags |= 1 << 5
        if self.login_email_pattern is not None: flags |= 1 << 6
        writer.write_int(flags, signed=False)
        if flags & (1 << 2):
            writer.write(bytes(self.current_algo))
        if flags & (1 << 2):
            writer.write_bytes(self.srp_B)
        if flags & (1 << 2):
            writer.write_long(self.srp_id, signed=False)
        if flags & (1 << 3):
            writer.write_string(self.hint)
        if flags & (1 << 4):
            writer.write_string(self.email_unconfirmed_pattern)
        writer.write(bytes(self.new_algo))
        writer.write(bytes(self.new_secure_algo))
        writer.write_bytes(self.secure_random)
        if flags & (1 << 5):
            writer.write_int(self.pending_reset_date, signed=True)
        if flags & (1 << 6):
            writer.write_string(self.login_email_pattern)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        has_recovery = bool(flags & (1 << 0))
        has_secure_values = bool(flags & (1 << 1))
        has_password = bool(flags & (1 << 2))
        if flags & (1 << 2):
            current_algo = reader.tgread_object()
        else:
            current_algo = None
        if flags & (1 << 2):
            srp_B = reader.read_bytes()
        else:
            srp_B = None
        if flags & (1 << 2):
            srp_id = reader.read_long()
        else:
            srp_id = None
        if flags & (1 << 3):
            hint = reader.read_string()
        else:
            hint = None
        if flags & (1 << 4):
            email_unconfirmed_pattern = reader.read_string()
        else:
            email_unconfirmed_pattern = None
        new_algo = reader.tgread_object()
        new_secure_algo = reader.tgread_object()
        secure_random = reader.read_bytes()
        if flags & (1 << 5):
            pending_reset_date = reader.read_int()
        else:
            pending_reset_date = None
        if flags & (1 << 6):
            login_email_pattern = reader.read_string()
        else:
            login_email_pattern = None
        return cls(has_recovery, has_secure_values, has_password, current_algo, srp_B, srp_id, hint, email_unconfirmed_pattern, new_algo, new_secure_algo, secure_random, pending_reset_date, login_email_pattern)

@register
class AccountPasswordSettings(TLObject):
    CONSTRUCTOR_ID = 2589733861
    __slots__ = ('email', 'secure_settings')
    def __init__(self, email: str = None, secure_settings: 'SecureSecretSettings' = None):
        self.email = email
        self.secure_settings = secure_settings
    def to_dict(self):
        return {"email": self.email, "secure_settings": self.secure_settings}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2589733861, signed=False)
        flags = 0
        if self.email is not None: flags |= 1 << 0
        if self.secure_settings is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        if flags & (1 << 0):
            writer.write_string(self.email)
        if flags & (1 << 1):
            writer.write(bytes(self.secure_settings))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        if flags & (1 << 0):
            email = reader.read_string()
        else:
            email = None
        if flags & (1 << 1):
            secure_settings = reader.tgread_object()
        else:
            secure_settings = None
        return cls(email, secure_settings)

@register
class AccountPasswordInputSettings(TLObject):
    CONSTRUCTOR_ID = 3258394569
    __slots__ = ('new_algo', 'new_password_hash', 'hint', 'email', 'new_secure_settings')
    def __init__(self, new_algo: 'PasswordKdfAlgo' = None, new_password_hash: bytes = None, hint: str = None, email: str = None, new_secure_settings: 'SecureSecretSettings' = None):
        self.new_algo = new_algo
        self.new_password_hash = new_password_hash
        self.hint = hint
        self.email = email
        self.new_secure_settings = new_secure_settings
    def to_dict(self):
        return {"new_algo": self.new_algo, "new_password_hash": self.new_password_hash, "hint": self.hint, "email": self.email, "new_secure_settings": self.new_secure_settings}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3258394569, signed=False)
        flags = 0
        if self.new_algo is not None: flags |= 1 << 0
        if self.new_password_hash is not None: flags |= 1 << 0
        if self.hint is not None: flags |= 1 << 0
        if self.email is not None: flags |= 1 << 1
        if self.new_secure_settings is not None: flags |= 1 << 2
        writer.write_int(flags, signed=False)
        if flags & (1 << 0):
            writer.write(bytes(self.new_algo))
        if flags & (1 << 0):
            writer.write_bytes(self.new_password_hash)
        if flags & (1 << 0):
            writer.write_string(self.hint)
        if flags & (1 << 1):
            writer.write_string(self.email)
        if flags & (1 << 2):
            writer.write(bytes(self.new_secure_settings))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        if flags & (1 << 0):
            new_algo = reader.tgread_object()
        else:
            new_algo = None
        if flags & (1 << 0):
            new_password_hash = reader.read_bytes()
        else:
            new_password_hash = None
        if flags & (1 << 0):
            hint = reader.read_string()
        else:
            hint = None
        if flags & (1 << 1):
            email = reader.read_string()
        else:
            email = None
        if flags & (1 << 2):
            new_secure_settings = reader.tgread_object()
        else:
            new_secure_settings = None
        return cls(new_algo, new_password_hash, hint, email, new_secure_settings)

@register
class AccountTmpPassword(TLObject):
    CONSTRUCTOR_ID = 3680828724
    __slots__ = ('tmp_password', 'valid_until')
    def __init__(self, tmp_password: bytes, valid_until: int):
        self.tmp_password = tmp_password
        self.valid_until = valid_until
    def to_dict(self):
        return {"tmp_password": self.tmp_password, "valid_until": self.valid_until}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3680828724, signed=False)
        writer.write_bytes(self.tmp_password)
        writer.write_int(self.valid_until, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        tmp_password = reader.read_bytes()
        valid_until = reader.read_int()
        return cls(tmp_password, valid_until)

@register
class AccountWebAuthorizations(TLObject):
    CONSTRUCTOR_ID = 3981887996
    __slots__ = ('authorizations', 'users')
    def __init__(self, authorizations: 'Vector', users: 'Vector'):
        self.authorizations = authorizations
        self.users = users
    def to_dict(self):
        return {"authorizations": self.authorizations, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3981887996, signed=False)
        writer.write(bytes(self.authorizations))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        authorizations = reader.tgread_object()
        users = reader.tgread_object()
        return cls(authorizations, users)

@register
class AccountAuthorizationForm(TLObject):
    CONSTRUCTOR_ID = 2905480408
    __slots__ = ('required_types', 'values', 'errors', 'users', 'privacy_policy_url')
    def __init__(self, required_types: 'Vector', values: 'Vector', errors: 'Vector', users: 'Vector', privacy_policy_url: str = None):
        self.required_types = required_types
        self.values = values
        self.errors = errors
        self.users = users
        self.privacy_policy_url = privacy_policy_url
    def to_dict(self):
        return {"required_types": self.required_types, "values": self.values, "errors": self.errors, "users": self.users, "privacy_policy_url": self.privacy_policy_url}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2905480408, signed=False)
        flags = 0
        if self.privacy_policy_url is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.required_types))
        writer.write(bytes(self.values))
        writer.write(bytes(self.errors))
        writer.write(bytes(self.users))
        if flags & (1 << 0):
            writer.write_string(self.privacy_policy_url)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        required_types = reader.tgread_object()
        values = reader.tgread_object()
        errors = reader.tgread_object()
        users = reader.tgread_object()
        if flags & (1 << 0):
            privacy_policy_url = reader.read_string()
        else:
            privacy_policy_url = None
        return cls(required_types, values, errors, users, privacy_policy_url)

@register
class AccountSentEmailCode(TLObject):
    CONSTRUCTOR_ID = 2166326607
    __slots__ = ('email_pattern', 'length')
    def __init__(self, email_pattern: str, length: int):
        self.email_pattern = email_pattern
        self.length = length
    def to_dict(self):
        return {"email_pattern": self.email_pattern, "length": self.length}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2166326607, signed=False)
        writer.write_string(self.email_pattern)
        writer.write_int(self.length, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        email_pattern = reader.read_string()
        length = reader.read_int()
        return cls(email_pattern, length)

@register
class AccountTakeout(TLObject):
    CONSTRUCTOR_ID = 1304052993
    __slots__ = ('id')
    def __init__(self, id: int):
        self.id = id
    def to_dict(self):
        return {"id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1304052993, signed=False)
        writer.write_long(self.id, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        id = reader.read_long()
        return cls(id)

@register
class AccountWallPapersNotModified(TLObject):
    CONSTRUCTOR_ID = 471437699
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(471437699, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class AccountWallPapers(TLObject):
    CONSTRUCTOR_ID = 3452142988
    __slots__ = ('hash', 'wallpapers')
    def __init__(self, hash: int, wallpapers: 'Vector'):
        self.hash = hash
        self.wallpapers = wallpapers
    def to_dict(self):
        return {"hash": self.hash, "wallpapers": self.wallpapers}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3452142988, signed=False)
        writer.write_long(self.hash, signed=False)
        writer.write(bytes(self.wallpapers))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_long()
        wallpapers = reader.tgread_object()
        return cls(hash, wallpapers)

@register
class AccountAutoDownloadSettings(TLObject):
    CONSTRUCTOR_ID = 1674235686
    __slots__ = ('low', 'medium', 'high')
    def __init__(self, low: 'AutoDownloadSettings', medium: 'AutoDownloadSettings', high: 'AutoDownloadSettings'):
        self.low = low
        self.medium = medium
        self.high = high
    def to_dict(self):
        return {"low": self.low, "medium": self.medium, "high": self.high}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1674235686, signed=False)
        writer.write(bytes(self.low))
        writer.write(bytes(self.medium))
        writer.write(bytes(self.high))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        low = reader.tgread_object()
        medium = reader.tgread_object()
        high = reader.tgread_object()
        return cls(low, medium, high)

@register
class AccountThemesNotModified(TLObject):
    CONSTRUCTOR_ID = 4095653410
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4095653410, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class AccountThemes(TLObject):
    CONSTRUCTOR_ID = 2587724909
    __slots__ = ('hash', 'themes')
    def __init__(self, hash: int, themes: 'Vector'):
        self.hash = hash
        self.themes = themes
    def to_dict(self):
        return {"hash": self.hash, "themes": self.themes}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2587724909, signed=False)
        writer.write_long(self.hash, signed=False)
        writer.write(bytes(self.themes))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_long()
        themes = reader.tgread_object()
        return cls(hash, themes)

@register
class AccountContentSettings(TLObject):
    CONSTRUCTOR_ID = 1474462241
    __slots__ = ('sensitive_enabled', 'sensitive_can_change')
    def __init__(self, sensitive_enabled: bool = None, sensitive_can_change: bool = None):
        self.sensitive_enabled = sensitive_enabled
        self.sensitive_can_change = sensitive_can_change
    def to_dict(self):
        return {"sensitive_enabled": self.sensitive_enabled, "sensitive_can_change": self.sensitive_can_change}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1474462241, signed=False)
        flags = 0
        if self.sensitive_enabled: flags |= 1 << 0
        if self.sensitive_can_change: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        sensitive_enabled = bool(flags & (1 << 0))
        sensitive_can_change = bool(flags & (1 << 1))
        return cls(sensitive_enabled, sensitive_can_change)

@register
class AccountResetPasswordFailedWait(TLObject):
    CONSTRUCTOR_ID = 3816265825
    __slots__ = ('retry_date')
    def __init__(self, retry_date: int):
        self.retry_date = retry_date
    def to_dict(self):
        return {"retry_date": self.retry_date}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3816265825, signed=False)
        writer.write_int(self.retry_date, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        retry_date = reader.read_int()
        return cls(retry_date)

@register
class AccountResetPasswordRequestedWait(TLObject):
    CONSTRUCTOR_ID = 3924819069
    __slots__ = ('until_date')
    def __init__(self, until_date: int):
        self.until_date = until_date
    def to_dict(self):
        return {"until_date": self.until_date}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3924819069, signed=False)
        writer.write_int(self.until_date, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        until_date = reader.read_int()
        return cls(until_date)

@register
class AccountResetPasswordOk(TLObject):
    CONSTRUCTOR_ID = 3911636542
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3911636542, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class AccountChatThemesNotModified(TLObject):
    CONSTRUCTOR_ID = 3759268292
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3759268292, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class AccountChatThemes(TLObject):
    CONSTRUCTOR_ID = 3188294003
    __slots__ = ('hash', 'themes', 'chats', 'users', 'next_offset')
    def __init__(self, hash: int, themes: 'Vector', chats: 'Vector', users: 'Vector', next_offset: str = None):
        self.hash = hash
        self.themes = themes
        self.chats = chats
        self.users = users
        self.next_offset = next_offset
    def to_dict(self):
        return {"hash": self.hash, "themes": self.themes, "chats": self.chats, "users": self.users, "next_offset": self.next_offset}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3188294003, signed=False)
        flags = 0
        if self.next_offset is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write_long(self.hash, signed=False)
        writer.write(bytes(self.themes))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        if flags & (1 << 0):
            writer.write_string(self.next_offset)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        hash = reader.read_long()
        themes = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        if flags & (1 << 0):
            next_offset = reader.read_string()
        else:
            next_offset = None
        return cls(hash, themes, chats, users, next_offset)

@register
class AccountSavedRingtonesNotModified(TLObject):
    CONSTRUCTOR_ID = 4227262641
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4227262641, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class AccountSavedRingtones(TLObject):
    CONSTRUCTOR_ID = 3253284037
    __slots__ = ('hash', 'ringtones')
    def __init__(self, hash: int, ringtones: 'Vector'):
        self.hash = hash
        self.ringtones = ringtones
    def to_dict(self):
        return {"hash": self.hash, "ringtones": self.ringtones}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3253284037, signed=False)
        writer.write_long(self.hash, signed=False)
        writer.write(bytes(self.ringtones))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_long()
        ringtones = reader.tgread_object()
        return cls(hash, ringtones)

@register
class AccountSavedRingtone(TLObject):
    CONSTRUCTOR_ID = 3072737133
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3072737133, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class AccountSavedRingtoneConverted(TLObject):
    CONSTRUCTOR_ID = 523271863
    __slots__ = ('document')
    def __init__(self, document: 'Document'):
        self.document = document
    def to_dict(self):
        return {"document": self.document}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(523271863, signed=False)
        writer.write(bytes(self.document))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        document = reader.tgread_object()
        return cls(document)

@register
class AccountEmojiStatusesNotModified(TLObject):
    CONSTRUCTOR_ID = 3498894917
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3498894917, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class AccountEmojiStatuses(TLObject):
    CONSTRUCTOR_ID = 2428790737
    __slots__ = ('hash', 'statuses')
    def __init__(self, hash: int, statuses: 'Vector'):
        self.hash = hash
        self.statuses = statuses
    def to_dict(self):
        return {"hash": self.hash, "statuses": self.statuses}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2428790737, signed=False)
        writer.write_long(self.hash, signed=False)
        writer.write(bytes(self.statuses))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_long()
        statuses = reader.tgread_object()
        return cls(hash, statuses)

@register
class AccountEmailVerified(TLObject):
    CONSTRUCTOR_ID = 731303195
    __slots__ = ('email')
    def __init__(self, email: str):
        self.email = email
    def to_dict(self):
        return {"email": self.email}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(731303195, signed=False)
        writer.write_string(self.email)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        email = reader.read_string()
        return cls(email)

@register
class AccountEmailVerifiedLogin(TLObject):
    CONSTRUCTOR_ID = 3787132257
    __slots__ = ('email', 'sent_code')
    def __init__(self, email: str, sent_code: 'AuthSentCode'):
        self.email = email
        self.sent_code = sent_code
    def to_dict(self):
        return {"email": self.email, "sent_code": self.sent_code}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3787132257, signed=False)
        writer.write_string(self.email)
        writer.write(bytes(self.sent_code))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        email = reader.read_string()
        sent_code = reader.tgread_object()
        return cls(email, sent_code)

@register
class AccountAutoSaveSettings(TLObject):
    CONSTRUCTOR_ID = 1279133341
    __slots__ = ('users_settings', 'chats_settings', 'broadcasts_settings', 'exceptions', 'chats', 'users')
    def __init__(self, users_settings: 'AutoSaveSettings', chats_settings: 'AutoSaveSettings', broadcasts_settings: 'AutoSaveSettings', exceptions: 'Vector', chats: 'Vector', users: 'Vector'):
        self.users_settings = users_settings
        self.chats_settings = chats_settings
        self.broadcasts_settings = broadcasts_settings
        self.exceptions = exceptions
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"users_settings": self.users_settings, "chats_settings": self.chats_settings, "broadcasts_settings": self.broadcasts_settings, "exceptions": self.exceptions, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1279133341, signed=False)
        writer.write(bytes(self.users_settings))
        writer.write(bytes(self.chats_settings))
        writer.write(bytes(self.broadcasts_settings))
        writer.write(bytes(self.exceptions))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        users_settings = reader.tgread_object()
        chats_settings = reader.tgread_object()
        broadcasts_settings = reader.tgread_object()
        exceptions = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(users_settings, chats_settings, broadcasts_settings, exceptions, chats, users)

@register
class AccountConnectedBots(TLObject):
    CONSTRUCTOR_ID = 400029819
    __slots__ = ('connected_bots', 'users')
    def __init__(self, connected_bots: 'Vector', users: 'Vector'):
        self.connected_bots = connected_bots
        self.users = users
    def to_dict(self):
        return {"connected_bots": self.connected_bots, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(400029819, signed=False)
        writer.write(bytes(self.connected_bots))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        connected_bots = reader.tgread_object()
        users = reader.tgread_object()
        return cls(connected_bots, users)

@register
class AccountBusinessChatLinks(TLObject):
    CONSTRUCTOR_ID = 3963855569
    __slots__ = ('links', 'chats', 'users')
    def __init__(self, links: 'Vector', chats: 'Vector', users: 'Vector'):
        self.links = links
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"links": self.links, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3963855569, signed=False)
        writer.write(bytes(self.links))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        links = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(links, chats, users)

@register
class AccountResolvedBusinessChatLinks(TLObject):
    CONSTRUCTOR_ID = 2586029857
    __slots__ = ('peer', 'message', 'entities', 'chats', 'users')
    def __init__(self, peer: 'Peer', message: str, chats: 'Vector', users: 'Vector', entities: 'Vector' = None):
        self.peer = peer
        self.message = message
        self.entities = entities
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"peer": self.peer, "message": self.message, "entities": self.entities, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2586029857, signed=False)
        flags = 0
        if self.entities is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write_string(self.message)
        if flags & (1 << 0):
            writer.write(bytes(self.entities))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        peer = reader.tgread_object()
        message = reader.read_string()
        if flags & (1 << 0):
            entities = reader.tgread_object()
        else:
            entities = None
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(peer, message, entities, chats, users)

@register
class AccountPaidMessagesRevenue(TLObject):
    CONSTRUCTOR_ID = 504403720
    __slots__ = ('stars_amount')
    def __init__(self, stars_amount: int):
        self.stars_amount = stars_amount
    def to_dict(self):
        return {"stars_amount": self.stars_amount}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(504403720, signed=False)
        writer.write_long(self.stars_amount, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        stars_amount = reader.read_long()
        return cls(stars_amount)

@register
class AccountSavedMusicIdsNotModified(TLObject):
    CONSTRUCTOR_ID = 1338514798
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1338514798, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class AccountSavedMusicIds(TLObject):
    CONSTRUCTOR_ID = 2576180790
    __slots__ = ('ids')
    def __init__(self, ids: 'Vector'):
        self.ids = ids
    def to_dict(self):
        return {"ids": self.ids}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2576180790, signed=False)
        writer.write(bytes(self.ids))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        ids = reader.tgread_object()
        return cls(ids)

@register
class AccountPasskeys(TLObject):
    CONSTRUCTOR_ID = 4175473180
    __slots__ = ('passkeys')
    def __init__(self, passkeys: 'Vector'):
        self.passkeys = passkeys
    def to_dict(self):
        return {"passkeys": self.passkeys}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4175473180, signed=False)
        writer.write(bytes(self.passkeys))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        passkeys = reader.tgread_object()
        return cls(passkeys)

@register
class AccountPasskeyRegistrationOptions(TLObject):
    CONSTRUCTOR_ID = 3781909729
    __slots__ = ('options')
    def __init__(self, options: 'DataJSON'):
        self.options = options
    def to_dict(self):
        return {"options": self.options}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3781909729, signed=False)
        writer.write(bytes(self.options))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        options = reader.tgread_object()
        return cls(options)

