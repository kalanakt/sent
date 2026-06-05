"""Auto-generated TL types. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional, TYPE_CHECKING
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

@register
class AuthSentCode(TLObject):
    CONSTRUCTOR_ID = 1577067778
    __slots__ = ('type_', 'phone_code_hash', 'next_type', 'timeout')
    def __init__(self, type_: 'AuthSentCodeType', phone_code_hash: str, next_type: 'AuthCodeType' = None, timeout: int = None):
        self.type_ = type_
        self.phone_code_hash = phone_code_hash
        self.next_type = next_type
        self.timeout = timeout
    def to_dict(self):
        return {"type": self.type_, "phone_code_hash": self.phone_code_hash, "next_type": self.next_type, "timeout": self.timeout}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1577067778, signed=False)
        flags = 0
        if self.next_type is not None: flags |= 1 << 1
        if self.timeout is not None: flags |= 1 << 2
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.type_))
        writer.write_string(self.phone_code_hash)
        if flags & (1 << 1):
            writer.write(bytes(self.next_type))
        if flags & (1 << 2):
            writer.write_int(self.timeout, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        type_ = reader.tgread_object()
        phone_code_hash = reader.read_string()
        if flags & (1 << 1):
            next_type = reader.tgread_object()
        else:
            next_type = None
        if flags & (1 << 2):
            timeout = reader.read_int()
        else:
            timeout = None
        return cls(type_, phone_code_hash, next_type, timeout)

@register
class AuthSentCodeSuccess(TLObject):
    CONSTRUCTOR_ID = 596704836
    __slots__ = ('authorization')
    def __init__(self, authorization: 'AuthAuthorization'):
        self.authorization = authorization
    def to_dict(self):
        return {"authorization": self.authorization}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(596704836, signed=False)
        writer.write(bytes(self.authorization))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        authorization = reader.tgread_object()
        return cls(authorization)

@register
class AuthSentCodePaymentRequired(TLObject):
    CONSTRUCTOR_ID = 4169301695
    __slots__ = ('store_product', 'phone_code_hash', 'support_email_address', 'support_email_subject', 'premium_days', 'currency', 'amount')
    def __init__(self, store_product: str, phone_code_hash: str, support_email_address: str, support_email_subject: str, premium_days: int, currency: str, amount: int):
        self.store_product = store_product
        self.phone_code_hash = phone_code_hash
        self.support_email_address = support_email_address
        self.support_email_subject = support_email_subject
        self.premium_days = premium_days
        self.currency = currency
        self.amount = amount
    def to_dict(self):
        return {"store_product": self.store_product, "phone_code_hash": self.phone_code_hash, "support_email_address": self.support_email_address, "support_email_subject": self.support_email_subject, "premium_days": self.premium_days, "currency": self.currency, "amount": self.amount}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4169301695, signed=False)
        writer.write_string(self.store_product)
        writer.write_string(self.phone_code_hash)
        writer.write_string(self.support_email_address)
        writer.write_string(self.support_email_subject)
        writer.write_int(self.premium_days, signed=True)
        writer.write_string(self.currency)
        writer.write_long(self.amount, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        store_product = reader.read_string()
        phone_code_hash = reader.read_string()
        support_email_address = reader.read_string()
        support_email_subject = reader.read_string()
        premium_days = reader.read_int()
        currency = reader.read_string()
        amount = reader.read_long()
        return cls(store_product, phone_code_hash, support_email_address, support_email_subject, premium_days, currency, amount)

@register
class AuthAuthorization(TLObject):
    CONSTRUCTOR_ID = 782418132
    __slots__ = ('setup_password_required', 'otherwise_relogin_days', 'tmp_sessions', 'future_auth_token', 'user')
    def __init__(self, user: 'User', setup_password_required: bool = None, otherwise_relogin_days: int = None, tmp_sessions: int = None, future_auth_token: bytes = None):
        self.setup_password_required = setup_password_required
        self.otherwise_relogin_days = otherwise_relogin_days
        self.tmp_sessions = tmp_sessions
        self.future_auth_token = future_auth_token
        self.user = user
    def to_dict(self):
        return {"setup_password_required": self.setup_password_required, "otherwise_relogin_days": self.otherwise_relogin_days, "tmp_sessions": self.tmp_sessions, "future_auth_token": self.future_auth_token, "user": self.user}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(782418132, signed=False)
        flags = 0
        if self.setup_password_required: flags |= 1 << 1
        if self.otherwise_relogin_days is not None: flags |= 1 << 1
        if self.tmp_sessions is not None: flags |= 1 << 0
        if self.future_auth_token is not None: flags |= 1 << 2
        writer.write_int(flags, signed=False)
        if flags & (1 << 1):
            writer.write_int(self.otherwise_relogin_days, signed=True)
        if flags & (1 << 0):
            writer.write_int(self.tmp_sessions, signed=True)
        if flags & (1 << 2):
            writer.write_bytes(self.future_auth_token)
        writer.write(bytes(self.user))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        setup_password_required = bool(flags & (1 << 1))
        if flags & (1 << 1):
            otherwise_relogin_days = reader.read_int()
        else:
            otherwise_relogin_days = None
        if flags & (1 << 0):
            tmp_sessions = reader.read_int()
        else:
            tmp_sessions = None
        if flags & (1 << 2):
            future_auth_token = reader.read_bytes()
        else:
            future_auth_token = None
        user = reader.tgread_object()
        return cls(setup_password_required, otherwise_relogin_days, tmp_sessions, future_auth_token, user)

@register
class AuthAuthorizationSignUpRequired(TLObject):
    CONSTRUCTOR_ID = 1148485274
    __slots__ = ('terms_of_service')
    def __init__(self, terms_of_service: 'HelpTermsOfService' = None):
        self.terms_of_service = terms_of_service
    def to_dict(self):
        return {"terms_of_service": self.terms_of_service}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1148485274, signed=False)
        flags = 0
        if self.terms_of_service is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        if flags & (1 << 0):
            writer.write(bytes(self.terms_of_service))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        if flags & (1 << 0):
            terms_of_service = reader.tgread_object()
        else:
            terms_of_service = None
        return cls(terms_of_service)

@register
class AuthExportedAuthorization(TLObject):
    CONSTRUCTOR_ID = 3023364792
    __slots__ = ('id', 'bytes')
    def __init__(self, id: int, bytes: bytes):
        self.id = id
        self.bytes = bytes
    def to_dict(self):
        return {"id": self.id, "bytes": self.bytes}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3023364792, signed=False)
        writer.write_long(self.id, signed=False)
        writer.write_bytes(self.bytes)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        id = reader.read_long()
        bytes = reader.read_bytes()
        return cls(id, bytes)

@register
class AuthPasswordRecovery(TLObject):
    CONSTRUCTOR_ID = 326715557
    __slots__ = ('email_pattern')
    def __init__(self, email_pattern: str):
        self.email_pattern = email_pattern
    def to_dict(self):
        return {"email_pattern": self.email_pattern}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(326715557, signed=False)
        writer.write_string(self.email_pattern)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        email_pattern = reader.read_string()
        return cls(email_pattern)

@register
class AuthCodeTypeSms(TLObject):
    CONSTRUCTOR_ID = 1923290508
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1923290508, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class AuthCodeTypeCall(TLObject):
    CONSTRUCTOR_ID = 1948046307
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1948046307, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class AuthCodeTypeFlashCall(TLObject):
    CONSTRUCTOR_ID = 577556219
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(577556219, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class AuthCodeTypeMissedCall(TLObject):
    CONSTRUCTOR_ID = 3592083182
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3592083182, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class AuthCodeTypeFragmentSms(TLObject):
    CONSTRUCTOR_ID = 116234636
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(116234636, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class AuthSentCodeTypeApp(TLObject):
    CONSTRUCTOR_ID = 1035688326
    __slots__ = ('length')
    def __init__(self, length: int):
        self.length = length
    def to_dict(self):
        return {"length": self.length}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1035688326, signed=False)
        writer.write_int(self.length, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        length = reader.read_int()
        return cls(length)

@register
class AuthSentCodeTypeSms(TLObject):
    CONSTRUCTOR_ID = 3221273506
    __slots__ = ('length')
    def __init__(self, length: int):
        self.length = length
    def to_dict(self):
        return {"length": self.length}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3221273506, signed=False)
        writer.write_int(self.length, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        length = reader.read_int()
        return cls(length)

@register
class AuthSentCodeTypeCall(TLObject):
    CONSTRUCTOR_ID = 1398007207
    __slots__ = ('length')
    def __init__(self, length: int):
        self.length = length
    def to_dict(self):
        return {"length": self.length}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1398007207, signed=False)
        writer.write_int(self.length, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        length = reader.read_int()
        return cls(length)

@register
class AuthSentCodeTypeFlashCall(TLObject):
    CONSTRUCTOR_ID = 2869151449
    __slots__ = ('pattern')
    def __init__(self, pattern: str):
        self.pattern = pattern
    def to_dict(self):
        return {"pattern": self.pattern}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2869151449, signed=False)
        writer.write_string(self.pattern)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        pattern = reader.read_string()
        return cls(pattern)

@register
class AuthSentCodeTypeMissedCall(TLObject):
    CONSTRUCTOR_ID = 2181063812
    __slots__ = ('prefix', 'length')
    def __init__(self, prefix: str, length: int):
        self.prefix = prefix
        self.length = length
    def to_dict(self):
        return {"prefix": self.prefix, "length": self.length}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2181063812, signed=False)
        writer.write_string(self.prefix)
        writer.write_int(self.length, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        prefix = reader.read_string()
        length = reader.read_int()
        return cls(prefix, length)

@register
class AuthSentCodeTypeEmailCode(TLObject):
    CONSTRUCTOR_ID = 4098946459
    __slots__ = ('apple_signin_allowed', 'google_signin_allowed', 'email_pattern', 'length', 'reset_available_period', 'reset_pending_date')
    def __init__(self, email_pattern: str, length: int, apple_signin_allowed: bool = None, google_signin_allowed: bool = None, reset_available_period: int = None, reset_pending_date: int = None):
        self.apple_signin_allowed = apple_signin_allowed
        self.google_signin_allowed = google_signin_allowed
        self.email_pattern = email_pattern
        self.length = length
        self.reset_available_period = reset_available_period
        self.reset_pending_date = reset_pending_date
    def to_dict(self):
        return {"apple_signin_allowed": self.apple_signin_allowed, "google_signin_allowed": self.google_signin_allowed, "email_pattern": self.email_pattern, "length": self.length, "reset_available_period": self.reset_available_period, "reset_pending_date": self.reset_pending_date}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4098946459, signed=False)
        flags = 0
        if self.apple_signin_allowed: flags |= 1 << 0
        if self.google_signin_allowed: flags |= 1 << 1
        if self.reset_available_period is not None: flags |= 1 << 3
        if self.reset_pending_date is not None: flags |= 1 << 4
        writer.write_int(flags, signed=False)
        writer.write_string(self.email_pattern)
        writer.write_int(self.length, signed=True)
        if flags & (1 << 3):
            writer.write_int(self.reset_available_period, signed=True)
        if flags & (1 << 4):
            writer.write_int(self.reset_pending_date, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        apple_signin_allowed = bool(flags & (1 << 0))
        google_signin_allowed = bool(flags & (1 << 1))
        email_pattern = reader.read_string()
        length = reader.read_int()
        if flags & (1 << 3):
            reset_available_period = reader.read_int()
        else:
            reset_available_period = None
        if flags & (1 << 4):
            reset_pending_date = reader.read_int()
        else:
            reset_pending_date = None
        return cls(apple_signin_allowed, google_signin_allowed, email_pattern, length, reset_available_period, reset_pending_date)

@register
class AuthSentCodeTypeSetUpEmailRequired(TLObject):
    CONSTRUCTOR_ID = 2773032426
    __slots__ = ('apple_signin_allowed', 'google_signin_allowed')
    def __init__(self, apple_signin_allowed: bool = None, google_signin_allowed: bool = None):
        self.apple_signin_allowed = apple_signin_allowed
        self.google_signin_allowed = google_signin_allowed
    def to_dict(self):
        return {"apple_signin_allowed": self.apple_signin_allowed, "google_signin_allowed": self.google_signin_allowed}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2773032426, signed=False)
        flags = 0
        if self.apple_signin_allowed: flags |= 1 << 0
        if self.google_signin_allowed: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        apple_signin_allowed = bool(flags & (1 << 0))
        google_signin_allowed = bool(flags & (1 << 1))
        return cls(apple_signin_allowed, google_signin_allowed)

@register
class AuthSentCodeTypeFragmentSms(TLObject):
    CONSTRUCTOR_ID = 3646315577
    __slots__ = ('url', 'length')
    def __init__(self, url: str, length: int):
        self.url = url
        self.length = length
    def to_dict(self):
        return {"url": self.url, "length": self.length}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3646315577, signed=False)
        writer.write_string(self.url)
        writer.write_int(self.length, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        url = reader.read_string()
        length = reader.read_int()
        return cls(url, length)

@register
class AuthSentCodeTypeFirebaseSms(TLObject):
    CONSTRUCTOR_ID = 10475318
    __slots__ = ('nonce', 'play_integrity_project_id', 'play_integrity_nonce', 'receipt', 'push_timeout', 'length')
    def __init__(self, length: int, nonce: bytes = None, play_integrity_project_id: int = None, play_integrity_nonce: bytes = None, receipt: str = None, push_timeout: int = None):
        self.nonce = nonce
        self.play_integrity_project_id = play_integrity_project_id
        self.play_integrity_nonce = play_integrity_nonce
        self.receipt = receipt
        self.push_timeout = push_timeout
        self.length = length
    def to_dict(self):
        return {"nonce": self.nonce, "play_integrity_project_id": self.play_integrity_project_id, "play_integrity_nonce": self.play_integrity_nonce, "receipt": self.receipt, "push_timeout": self.push_timeout, "length": self.length}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(10475318, signed=False)
        flags = 0
        if self.nonce is not None: flags |= 1 << 0
        if self.play_integrity_project_id is not None: flags |= 1 << 2
        if self.play_integrity_nonce is not None: flags |= 1 << 2
        if self.receipt is not None: flags |= 1 << 1
        if self.push_timeout is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        if flags & (1 << 0):
            writer.write_bytes(self.nonce)
        if flags & (1 << 2):
            writer.write_long(self.play_integrity_project_id, signed=False)
        if flags & (1 << 2):
            writer.write_bytes(self.play_integrity_nonce)
        if flags & (1 << 1):
            writer.write_string(self.receipt)
        if flags & (1 << 1):
            writer.write_int(self.push_timeout, signed=True)
        writer.write_int(self.length, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        if flags & (1 << 0):
            nonce = reader.read_bytes()
        else:
            nonce = None
        if flags & (1 << 2):
            play_integrity_project_id = reader.read_long()
        else:
            play_integrity_project_id = None
        if flags & (1 << 2):
            play_integrity_nonce = reader.read_bytes()
        else:
            play_integrity_nonce = None
        if flags & (1 << 1):
            receipt = reader.read_string()
        else:
            receipt = None
        if flags & (1 << 1):
            push_timeout = reader.read_int()
        else:
            push_timeout = None
        length = reader.read_int()
        return cls(nonce, play_integrity_project_id, play_integrity_nonce, receipt, push_timeout, length)

@register
class AuthSentCodeTypeSmsWord(TLObject):
    CONSTRUCTOR_ID = 2752949377
    __slots__ = ('beginning')
    def __init__(self, beginning: str = None):
        self.beginning = beginning
    def to_dict(self):
        return {"beginning": self.beginning}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2752949377, signed=False)
        flags = 0
        if self.beginning is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        if flags & (1 << 0):
            writer.write_string(self.beginning)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        if flags & (1 << 0):
            beginning = reader.read_string()
        else:
            beginning = None
        return cls(beginning)

@register
class AuthSentCodeTypeSmsPhrase(TLObject):
    CONSTRUCTOR_ID = 3010958511
    __slots__ = ('beginning')
    def __init__(self, beginning: str = None):
        self.beginning = beginning
    def to_dict(self):
        return {"beginning": self.beginning}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3010958511, signed=False)
        flags = 0
        if self.beginning is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        if flags & (1 << 0):
            writer.write_string(self.beginning)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        if flags & (1 << 0):
            beginning = reader.read_string()
        else:
            beginning = None
        return cls(beginning)

@register
class AuthLoginToken(TLObject):
    CONSTRUCTOR_ID = 1654593920
    __slots__ = ('expires', 'token')
    def __init__(self, expires: int, token: bytes):
        self.expires = expires
        self.token = token
    def to_dict(self):
        return {"expires": self.expires, "token": self.token}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1654593920, signed=False)
        writer.write_int(self.expires, signed=True)
        writer.write_bytes(self.token)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        expires = reader.read_int()
        token = reader.read_bytes()
        return cls(expires, token)

@register
class AuthLoginTokenMigrateTo(TLObject):
    CONSTRUCTOR_ID = 110008598
    __slots__ = ('dc_id', 'token')
    def __init__(self, dc_id: int, token: bytes):
        self.dc_id = dc_id
        self.token = token
    def to_dict(self):
        return {"dc_id": self.dc_id, "token": self.token}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(110008598, signed=False)
        writer.write_int(self.dc_id, signed=True)
        writer.write_bytes(self.token)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        dc_id = reader.read_int()
        token = reader.read_bytes()
        return cls(dc_id, token)

@register
class AuthLoginTokenSuccess(TLObject):
    CONSTRUCTOR_ID = 957176926
    __slots__ = ('authorization')
    def __init__(self, authorization: 'AuthAuthorization'):
        self.authorization = authorization
    def to_dict(self):
        return {"authorization": self.authorization}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(957176926, signed=False)
        writer.write(bytes(self.authorization))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        authorization = reader.tgread_object()
        return cls(authorization)

@register
class AuthLoggedOut(TLObject):
    CONSTRUCTOR_ID = 3282207583
    __slots__ = ('future_auth_token')
    def __init__(self, future_auth_token: bytes = None):
        self.future_auth_token = future_auth_token
    def to_dict(self):
        return {"future_auth_token": self.future_auth_token}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3282207583, signed=False)
        flags = 0
        if self.future_auth_token is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        if flags & (1 << 0):
            writer.write_bytes(self.future_auth_token)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        if flags & (1 << 0):
            future_auth_token = reader.read_bytes()
        else:
            future_auth_token = None
        return cls(future_auth_token)

@register
class AuthPasskeyLoginOptions(TLObject):
    CONSTRUCTOR_ID = 3791878025
    __slots__ = ('options')
    def __init__(self, options: 'DataJSON'):
        self.options = options
    def to_dict(self):
        return {"options": self.options}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3791878025, signed=False)
        writer.write(bytes(self.options))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        options = reader.tgread_object()
        return cls(options)

