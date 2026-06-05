"""Auto-generated TL types. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional, TYPE_CHECKING
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

@register
class PaymentsPaymentForm(TLObject):
    CONSTRUCTOR_ID = 2684716881
    __slots__ = ('can_save_credentials', 'password_missing', 'form_id', 'bot_id', 'title', 'description', 'photo', 'invoice', 'provider_id', 'url', 'native_provider', 'native_params', 'additional_methods', 'saved_info', 'saved_credentials', 'users')
    def __init__(self, form_id: int, bot_id: int, title: str, description: str, invoice: 'Invoice', provider_id: int, url: str, users: 'Vector', can_save_credentials: bool = None, password_missing: bool = None, photo: 'WebDocument' = None, native_provider: str = None, native_params: 'DataJSON' = None, additional_methods: 'Vector' = None, saved_info: 'PaymentRequestedInfo' = None, saved_credentials: 'Vector' = None):
        self.can_save_credentials = can_save_credentials
        self.password_missing = password_missing
        self.form_id = form_id
        self.bot_id = bot_id
        self.title = title
        self.description = description
        self.photo = photo
        self.invoice = invoice
        self.provider_id = provider_id
        self.url = url
        self.native_provider = native_provider
        self.native_params = native_params
        self.additional_methods = additional_methods
        self.saved_info = saved_info
        self.saved_credentials = saved_credentials
        self.users = users
    def to_dict(self):
        return {"can_save_credentials": self.can_save_credentials, "password_missing": self.password_missing, "form_id": self.form_id, "bot_id": self.bot_id, "title": self.title, "description": self.description, "photo": self.photo, "invoice": self.invoice, "provider_id": self.provider_id, "url": self.url, "native_provider": self.native_provider, "native_params": self.native_params, "additional_methods": self.additional_methods, "saved_info": self.saved_info, "saved_credentials": self.saved_credentials, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2684716881, signed=False)
        flags = 0
        if self.can_save_credentials: flags |= 1 << 2
        if self.password_missing: flags |= 1 << 3
        if self.photo is not None: flags |= 1 << 5
        if self.native_provider is not None: flags |= 1 << 4
        if self.native_params is not None: flags |= 1 << 4
        if self.additional_methods is not None: flags |= 1 << 6
        if self.saved_info is not None: flags |= 1 << 0
        if self.saved_credentials is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write_long(self.form_id, signed=False)
        writer.write_long(self.bot_id, signed=False)
        writer.write_string(self.title)
        writer.write_string(self.description)
        if flags & (1 << 5):
            writer.write(bytes(self.photo))
        writer.write(bytes(self.invoice))
        writer.write_long(self.provider_id, signed=False)
        writer.write_string(self.url)
        if flags & (1 << 4):
            writer.write_string(self.native_provider)
        if flags & (1 << 4):
            writer.write(bytes(self.native_params))
        if flags & (1 << 6):
            writer.write(bytes(self.additional_methods))
        if flags & (1 << 0):
            writer.write(bytes(self.saved_info))
        if flags & (1 << 1):
            writer.write(bytes(self.saved_credentials))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        can_save_credentials = bool(flags & (1 << 2))
        password_missing = bool(flags & (1 << 3))
        form_id = reader.read_long()
        bot_id = reader.read_long()
        title = reader.read_string()
        description = reader.read_string()
        if flags & (1 << 5):
            photo = reader.tgread_object()
        else:
            photo = None
        invoice = reader.tgread_object()
        provider_id = reader.read_long()
        url = reader.read_string()
        if flags & (1 << 4):
            native_provider = reader.read_string()
        else:
            native_provider = None
        if flags & (1 << 4):
            native_params = reader.tgread_object()
        else:
            native_params = None
        if flags & (1 << 6):
            additional_methods = reader.tgread_object()
        else:
            additional_methods = None
        if flags & (1 << 0):
            saved_info = reader.tgread_object()
        else:
            saved_info = None
        if flags & (1 << 1):
            saved_credentials = reader.tgread_object()
        else:
            saved_credentials = None
        users = reader.tgread_object()
        return cls(can_save_credentials, password_missing, form_id, bot_id, title, description, photo, invoice, provider_id, url, native_provider, native_params, additional_methods, saved_info, saved_credentials, users)

@register
class PaymentsPaymentFormStars(TLObject):
    CONSTRUCTOR_ID = 2079764828
    __slots__ = ('form_id', 'bot_id', 'title', 'description', 'photo', 'invoice', 'users')
    def __init__(self, form_id: int, bot_id: int, title: str, description: str, invoice: 'Invoice', users: 'Vector', photo: 'WebDocument' = None):
        self.form_id = form_id
        self.bot_id = bot_id
        self.title = title
        self.description = description
        self.photo = photo
        self.invoice = invoice
        self.users = users
    def to_dict(self):
        return {"form_id": self.form_id, "bot_id": self.bot_id, "title": self.title, "description": self.description, "photo": self.photo, "invoice": self.invoice, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2079764828, signed=False)
        flags = 0
        if self.photo is not None: flags |= 1 << 5
        writer.write_int(flags, signed=False)
        writer.write_long(self.form_id, signed=False)
        writer.write_long(self.bot_id, signed=False)
        writer.write_string(self.title)
        writer.write_string(self.description)
        if flags & (1 << 5):
            writer.write(bytes(self.photo))
        writer.write(bytes(self.invoice))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        form_id = reader.read_long()
        bot_id = reader.read_long()
        title = reader.read_string()
        description = reader.read_string()
        if flags & (1 << 5):
            photo = reader.tgread_object()
        else:
            photo = None
        invoice = reader.tgread_object()
        users = reader.tgread_object()
        return cls(form_id, bot_id, title, description, photo, invoice, users)

@register
class PaymentsPaymentFormStarGift(TLObject):
    CONSTRUCTOR_ID = 3022376929
    __slots__ = ('form_id', 'invoice')
    def __init__(self, form_id: int, invoice: 'Invoice'):
        self.form_id = form_id
        self.invoice = invoice
    def to_dict(self):
        return {"form_id": self.form_id, "invoice": self.invoice}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3022376929, signed=False)
        writer.write_long(self.form_id, signed=False)
        writer.write(bytes(self.invoice))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        form_id = reader.read_long()
        invoice = reader.tgread_object()
        return cls(form_id, invoice)

@register
class PaymentsValidatedRequestedInfo(TLObject):
    CONSTRUCTOR_ID = 3510966403
    __slots__ = ('id', 'shipping_options')
    def __init__(self, id: str = None, shipping_options: 'Vector' = None):
        self.id = id
        self.shipping_options = shipping_options
    def to_dict(self):
        return {"id": self.id, "shipping_options": self.shipping_options}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3510966403, signed=False)
        flags = 0
        if self.id is not None: flags |= 1 << 0
        if self.shipping_options is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        if flags & (1 << 0):
            writer.write_string(self.id)
        if flags & (1 << 1):
            writer.write(bytes(self.shipping_options))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        if flags & (1 << 0):
            id = reader.read_string()
        else:
            id = None
        if flags & (1 << 1):
            shipping_options = reader.tgread_object()
        else:
            shipping_options = None
        return cls(id, shipping_options)

@register
class PaymentsPaymentResult(TLObject):
    CONSTRUCTOR_ID = 1314881805
    __slots__ = ('updates')
    def __init__(self, updates: 'Updates'):
        self.updates = updates
    def to_dict(self):
        return {"updates": self.updates}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1314881805, signed=False)
        writer.write(bytes(self.updates))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        updates = reader.tgread_object()
        return cls(updates)

@register
class PaymentsPaymentVerificationNeeded(TLObject):
    CONSTRUCTOR_ID = 3628142905
    __slots__ = ('url')
    def __init__(self, url: str):
        self.url = url
    def to_dict(self):
        return {"url": self.url}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3628142905, signed=False)
        writer.write_string(self.url)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        url = reader.read_string()
        return cls(url)

@register
class PaymentsPaymentReceipt(TLObject):
    CONSTRUCTOR_ID = 1891958275
    __slots__ = ('date', 'bot_id', 'provider_id', 'title', 'description', 'photo', 'invoice', 'info', 'shipping', 'tip_amount', 'currency', 'total_amount', 'credentials_title', 'users')
    def __init__(self, date: int, bot_id: int, provider_id: int, title: str, description: str, invoice: 'Invoice', currency: str, total_amount: int, credentials_title: str, users: 'Vector', photo: 'WebDocument' = None, info: 'PaymentRequestedInfo' = None, shipping: 'ShippingOption' = None, tip_amount: int = None):
        self.date = date
        self.bot_id = bot_id
        self.provider_id = provider_id
        self.title = title
        self.description = description
        self.photo = photo
        self.invoice = invoice
        self.info = info
        self.shipping = shipping
        self.tip_amount = tip_amount
        self.currency = currency
        self.total_amount = total_amount
        self.credentials_title = credentials_title
        self.users = users
    def to_dict(self):
        return {"date": self.date, "bot_id": self.bot_id, "provider_id": self.provider_id, "title": self.title, "description": self.description, "photo": self.photo, "invoice": self.invoice, "info": self.info, "shipping": self.shipping, "tip_amount": self.tip_amount, "currency": self.currency, "total_amount": self.total_amount, "credentials_title": self.credentials_title, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1891958275, signed=False)
        flags = 0
        if self.photo is not None: flags |= 1 << 2
        if self.info is not None: flags |= 1 << 0
        if self.shipping is not None: flags |= 1 << 1
        if self.tip_amount is not None: flags |= 1 << 3
        writer.write_int(flags, signed=False)
        writer.write_int(self.date, signed=True)
        writer.write_long(self.bot_id, signed=False)
        writer.write_long(self.provider_id, signed=False)
        writer.write_string(self.title)
        writer.write_string(self.description)
        if flags & (1 << 2):
            writer.write(bytes(self.photo))
        writer.write(bytes(self.invoice))
        if flags & (1 << 0):
            writer.write(bytes(self.info))
        if flags & (1 << 1):
            writer.write(bytes(self.shipping))
        if flags & (1 << 3):
            writer.write_long(self.tip_amount, signed=False)
        writer.write_string(self.currency)
        writer.write_long(self.total_amount, signed=False)
        writer.write_string(self.credentials_title)
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        date = reader.read_int()
        bot_id = reader.read_long()
        provider_id = reader.read_long()
        title = reader.read_string()
        description = reader.read_string()
        if flags & (1 << 2):
            photo = reader.tgread_object()
        else:
            photo = None
        invoice = reader.tgread_object()
        if flags & (1 << 0):
            info = reader.tgread_object()
        else:
            info = None
        if flags & (1 << 1):
            shipping = reader.tgread_object()
        else:
            shipping = None
        if flags & (1 << 3):
            tip_amount = reader.read_long()
        else:
            tip_amount = None
        currency = reader.read_string()
        total_amount = reader.read_long()
        credentials_title = reader.read_string()
        users = reader.tgread_object()
        return cls(date, bot_id, provider_id, title, description, photo, invoice, info, shipping, tip_amount, currency, total_amount, credentials_title, users)

@register
class PaymentsPaymentReceiptStars(TLObject):
    CONSTRUCTOR_ID = 3669751866
    __slots__ = ('date', 'bot_id', 'title', 'description', 'photo', 'invoice', 'currency', 'total_amount', 'transaction_id', 'users')
    def __init__(self, date: int, bot_id: int, title: str, description: str, invoice: 'Invoice', currency: str, total_amount: int, transaction_id: str, users: 'Vector', photo: 'WebDocument' = None):
        self.date = date
        self.bot_id = bot_id
        self.title = title
        self.description = description
        self.photo = photo
        self.invoice = invoice
        self.currency = currency
        self.total_amount = total_amount
        self.transaction_id = transaction_id
        self.users = users
    def to_dict(self):
        return {"date": self.date, "bot_id": self.bot_id, "title": self.title, "description": self.description, "photo": self.photo, "invoice": self.invoice, "currency": self.currency, "total_amount": self.total_amount, "transaction_id": self.transaction_id, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3669751866, signed=False)
        flags = 0
        if self.photo is not None: flags |= 1 << 2
        writer.write_int(flags, signed=False)
        writer.write_int(self.date, signed=True)
        writer.write_long(self.bot_id, signed=False)
        writer.write_string(self.title)
        writer.write_string(self.description)
        if flags & (1 << 2):
            writer.write(bytes(self.photo))
        writer.write(bytes(self.invoice))
        writer.write_string(self.currency)
        writer.write_long(self.total_amount, signed=False)
        writer.write_string(self.transaction_id)
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        date = reader.read_int()
        bot_id = reader.read_long()
        title = reader.read_string()
        description = reader.read_string()
        if flags & (1 << 2):
            photo = reader.tgread_object()
        else:
            photo = None
        invoice = reader.tgread_object()
        currency = reader.read_string()
        total_amount = reader.read_long()
        transaction_id = reader.read_string()
        users = reader.tgread_object()
        return cls(date, bot_id, title, description, photo, invoice, currency, total_amount, transaction_id, users)

@register
class PaymentsSavedInfo(TLObject):
    CONSTRUCTOR_ID = 4220511292
    __slots__ = ('has_saved_credentials', 'saved_info')
    def __init__(self, has_saved_credentials: bool = None, saved_info: 'PaymentRequestedInfo' = None):
        self.has_saved_credentials = has_saved_credentials
        self.saved_info = saved_info
    def to_dict(self):
        return {"has_saved_credentials": self.has_saved_credentials, "saved_info": self.saved_info}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4220511292, signed=False)
        flags = 0
        if self.has_saved_credentials: flags |= 1 << 1
        if self.saved_info is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        if flags & (1 << 0):
            writer.write(bytes(self.saved_info))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        has_saved_credentials = bool(flags & (1 << 1))
        if flags & (1 << 0):
            saved_info = reader.tgread_object()
        else:
            saved_info = None
        return cls(has_saved_credentials, saved_info)

@register
class PaymentsBankCardData(TLObject):
    CONSTRUCTOR_ID = 1042605427
    __slots__ = ('title', 'open_urls')
    def __init__(self, title: str, open_urls: 'Vector'):
        self.title = title
        self.open_urls = open_urls
    def to_dict(self):
        return {"title": self.title, "open_urls": self.open_urls}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1042605427, signed=False)
        writer.write_string(self.title)
        writer.write(bytes(self.open_urls))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        title = reader.read_string()
        open_urls = reader.tgread_object()
        return cls(title, open_urls)

@register
class PaymentsExportedInvoice(TLObject):
    CONSTRUCTOR_ID = 2932919257
    __slots__ = ('url')
    def __init__(self, url: str):
        self.url = url
    def to_dict(self):
        return {"url": self.url}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2932919257, signed=False)
        writer.write_string(self.url)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        url = reader.read_string()
        return cls(url)

@register
class PaymentsCheckedGiftCode(TLObject):
    CONSTRUCTOR_ID = 3952623503
    __slots__ = ('via_giveaway', 'from_id', 'giveaway_msg_id', 'to_id', 'date', 'days', 'used_date', 'chats', 'users')
    def __init__(self, date: int, days: int, chats: 'Vector', users: 'Vector', via_giveaway: bool = None, from_id: 'Peer' = None, giveaway_msg_id: int = None, to_id: int = None, used_date: int = None):
        self.via_giveaway = via_giveaway
        self.from_id = from_id
        self.giveaway_msg_id = giveaway_msg_id
        self.to_id = to_id
        self.date = date
        self.days = days
        self.used_date = used_date
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"via_giveaway": self.via_giveaway, "from_id": self.from_id, "giveaway_msg_id": self.giveaway_msg_id, "to_id": self.to_id, "date": self.date, "days": self.days, "used_date": self.used_date, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3952623503, signed=False)
        flags = 0
        if self.via_giveaway: flags |= 1 << 2
        if self.from_id is not None: flags |= 1 << 4
        if self.giveaway_msg_id is not None: flags |= 1 << 3
        if self.to_id is not None: flags |= 1 << 0
        if self.used_date is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        if flags & (1 << 4):
            writer.write(bytes(self.from_id))
        if flags & (1 << 3):
            writer.write_int(self.giveaway_msg_id, signed=True)
        if flags & (1 << 0):
            writer.write_long(self.to_id, signed=False)
        writer.write_int(self.date, signed=True)
        writer.write_int(self.days, signed=True)
        if flags & (1 << 1):
            writer.write_int(self.used_date, signed=True)
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        via_giveaway = bool(flags & (1 << 2))
        if flags & (1 << 4):
            from_id = reader.tgread_object()
        else:
            from_id = None
        if flags & (1 << 3):
            giveaway_msg_id = reader.read_int()
        else:
            giveaway_msg_id = None
        if flags & (1 << 0):
            to_id = reader.read_long()
        else:
            to_id = None
        date = reader.read_int()
        days = reader.read_int()
        if flags & (1 << 1):
            used_date = reader.read_int()
        else:
            used_date = None
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(via_giveaway, from_id, giveaway_msg_id, to_id, date, days, used_date, chats, users)

@register
class PaymentsGiveawayInfo(TLObject):
    CONSTRUCTOR_ID = 1130879648
    __slots__ = ('participating', 'preparing_results', 'start_date', 'joined_too_early_date', 'admin_disallowed_chat_id', 'disallowed_country')
    def __init__(self, start_date: int, participating: bool = None, preparing_results: bool = None, joined_too_early_date: int = None, admin_disallowed_chat_id: int = None, disallowed_country: str = None):
        self.participating = participating
        self.preparing_results = preparing_results
        self.start_date = start_date
        self.joined_too_early_date = joined_too_early_date
        self.admin_disallowed_chat_id = admin_disallowed_chat_id
        self.disallowed_country = disallowed_country
    def to_dict(self):
        return {"participating": self.participating, "preparing_results": self.preparing_results, "start_date": self.start_date, "joined_too_early_date": self.joined_too_early_date, "admin_disallowed_chat_id": self.admin_disallowed_chat_id, "disallowed_country": self.disallowed_country}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1130879648, signed=False)
        flags = 0
        if self.participating: flags |= 1 << 0
        if self.preparing_results: flags |= 1 << 3
        if self.joined_too_early_date is not None: flags |= 1 << 1
        if self.admin_disallowed_chat_id is not None: flags |= 1 << 2
        if self.disallowed_country is not None: flags |= 1 << 4
        writer.write_int(flags, signed=False)
        writer.write_int(self.start_date, signed=True)
        if flags & (1 << 1):
            writer.write_int(self.joined_too_early_date, signed=True)
        if flags & (1 << 2):
            writer.write_long(self.admin_disallowed_chat_id, signed=False)
        if flags & (1 << 4):
            writer.write_string(self.disallowed_country)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        participating = bool(flags & (1 << 0))
        preparing_results = bool(flags & (1 << 3))
        start_date = reader.read_int()
        if flags & (1 << 1):
            joined_too_early_date = reader.read_int()
        else:
            joined_too_early_date = None
        if flags & (1 << 2):
            admin_disallowed_chat_id = reader.read_long()
        else:
            admin_disallowed_chat_id = None
        if flags & (1 << 4):
            disallowed_country = reader.read_string()
        else:
            disallowed_country = None
        return cls(participating, preparing_results, start_date, joined_too_early_date, admin_disallowed_chat_id, disallowed_country)

@register
class PaymentsGiveawayInfoResults(TLObject):
    CONSTRUCTOR_ID = 3782600303
    __slots__ = ('winner', 'refunded', 'start_date', 'gift_code_slug', 'stars_prize', 'finish_date', 'winners_count', 'activated_count')
    def __init__(self, start_date: int, finish_date: int, winners_count: int, winner: bool = None, refunded: bool = None, gift_code_slug: str = None, stars_prize: int = None, activated_count: int = None):
        self.winner = winner
        self.refunded = refunded
        self.start_date = start_date
        self.gift_code_slug = gift_code_slug
        self.stars_prize = stars_prize
        self.finish_date = finish_date
        self.winners_count = winners_count
        self.activated_count = activated_count
    def to_dict(self):
        return {"winner": self.winner, "refunded": self.refunded, "start_date": self.start_date, "gift_code_slug": self.gift_code_slug, "stars_prize": self.stars_prize, "finish_date": self.finish_date, "winners_count": self.winners_count, "activated_count": self.activated_count}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3782600303, signed=False)
        flags = 0
        if self.winner: flags |= 1 << 0
        if self.refunded: flags |= 1 << 1
        if self.gift_code_slug is not None: flags |= 1 << 3
        if self.stars_prize is not None: flags |= 1 << 4
        if self.activated_count is not None: flags |= 1 << 2
        writer.write_int(flags, signed=False)
        writer.write_int(self.start_date, signed=True)
        if flags & (1 << 3):
            writer.write_string(self.gift_code_slug)
        if flags & (1 << 4):
            writer.write_long(self.stars_prize, signed=False)
        writer.write_int(self.finish_date, signed=True)
        writer.write_int(self.winners_count, signed=True)
        if flags & (1 << 2):
            writer.write_int(self.activated_count, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        winner = bool(flags & (1 << 0))
        refunded = bool(flags & (1 << 1))
        start_date = reader.read_int()
        if flags & (1 << 3):
            gift_code_slug = reader.read_string()
        else:
            gift_code_slug = None
        if flags & (1 << 4):
            stars_prize = reader.read_long()
        else:
            stars_prize = None
        finish_date = reader.read_int()
        winners_count = reader.read_int()
        if flags & (1 << 2):
            activated_count = reader.read_int()
        else:
            activated_count = None
        return cls(winner, refunded, start_date, gift_code_slug, stars_prize, finish_date, winners_count, activated_count)

@register
class PaymentsStarsStatus(TLObject):
    CONSTRUCTOR_ID = 1822222573
    __slots__ = ('balance', 'subscriptions', 'subscriptions_next_offset', 'subscriptions_missing_balance', 'history', 'next_offset', 'chats', 'users')
    def __init__(self, balance: 'StarsAmount', chats: 'Vector', users: 'Vector', subscriptions: 'Vector' = None, subscriptions_next_offset: str = None, subscriptions_missing_balance: int = None, history: 'Vector' = None, next_offset: str = None):
        self.balance = balance
        self.subscriptions = subscriptions
        self.subscriptions_next_offset = subscriptions_next_offset
        self.subscriptions_missing_balance = subscriptions_missing_balance
        self.history = history
        self.next_offset = next_offset
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"balance": self.balance, "subscriptions": self.subscriptions, "subscriptions_next_offset": self.subscriptions_next_offset, "subscriptions_missing_balance": self.subscriptions_missing_balance, "history": self.history, "next_offset": self.next_offset, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1822222573, signed=False)
        flags = 0
        if self.subscriptions is not None: flags |= 1 << 1
        if self.subscriptions_next_offset is not None: flags |= 1 << 2
        if self.subscriptions_missing_balance is not None: flags |= 1 << 4
        if self.history is not None: flags |= 1 << 3
        if self.next_offset is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.balance))
        if flags & (1 << 1):
            writer.write(bytes(self.subscriptions))
        if flags & (1 << 2):
            writer.write_string(self.subscriptions_next_offset)
        if flags & (1 << 4):
            writer.write_long(self.subscriptions_missing_balance, signed=False)
        if flags & (1 << 3):
            writer.write(bytes(self.history))
        if flags & (1 << 0):
            writer.write_string(self.next_offset)
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        balance = reader.tgread_object()
        if flags & (1 << 1):
            subscriptions = reader.tgread_object()
        else:
            subscriptions = None
        if flags & (1 << 2):
            subscriptions_next_offset = reader.read_string()
        else:
            subscriptions_next_offset = None
        if flags & (1 << 4):
            subscriptions_missing_balance = reader.read_long()
        else:
            subscriptions_missing_balance = None
        if flags & (1 << 3):
            history = reader.tgread_object()
        else:
            history = None
        if flags & (1 << 0):
            next_offset = reader.read_string()
        else:
            next_offset = None
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(balance, subscriptions, subscriptions_next_offset, subscriptions_missing_balance, history, next_offset, chats, users)

@register
class PaymentsStarsRevenueStats(TLObject):
    CONSTRUCTOR_ID = 1814066038
    __slots__ = ('top_hours_graph', 'revenue_graph', 'status', 'usd_rate')
    def __init__(self, revenue_graph: 'StatsGraph', status: 'StarsRevenueStatus', usd_rate: float, top_hours_graph: 'StatsGraph' = None):
        self.top_hours_graph = top_hours_graph
        self.revenue_graph = revenue_graph
        self.status = status
        self.usd_rate = usd_rate
    def to_dict(self):
        return {"top_hours_graph": self.top_hours_graph, "revenue_graph": self.revenue_graph, "status": self.status, "usd_rate": self.usd_rate}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1814066038, signed=False)
        flags = 0
        if self.top_hours_graph is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        if flags & (1 << 0):
            writer.write(bytes(self.top_hours_graph))
        writer.write(bytes(self.revenue_graph))
        writer.write(bytes(self.status))
        writer.write_double(self.usd_rate)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        if flags & (1 << 0):
            top_hours_graph = reader.tgread_object()
        else:
            top_hours_graph = None
        revenue_graph = reader.tgread_object()
        status = reader.tgread_object()
        usd_rate = reader.read_double()
        return cls(top_hours_graph, revenue_graph, status, usd_rate)

@register
class PaymentsStarsRevenueWithdrawalUrl(TLObject):
    CONSTRUCTOR_ID = 497778871
    __slots__ = ('url')
    def __init__(self, url: str):
        self.url = url
    def to_dict(self):
        return {"url": self.url}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(497778871, signed=False)
        writer.write_string(self.url)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        url = reader.read_string()
        return cls(url)

@register
class PaymentsStarsRevenueAdsAccountUrl(TLObject):
    CONSTRUCTOR_ID = 961445665
    __slots__ = ('url')
    def __init__(self, url: str):
        self.url = url
    def to_dict(self):
        return {"url": self.url}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(961445665, signed=False)
        writer.write_string(self.url)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        url = reader.read_string()
        return cls(url)

@register
class PaymentsStarGiftsNotModified(TLObject):
    CONSTRUCTOR_ID = 2743640936
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2743640936, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class PaymentsStarGifts(TLObject):
    CONSTRUCTOR_ID = 785918357
    __slots__ = ('hash', 'gifts', 'chats', 'users')
    def __init__(self, hash: int, gifts: 'Vector', chats: 'Vector', users: 'Vector'):
        self.hash = hash
        self.gifts = gifts
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"hash": self.hash, "gifts": self.gifts, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(785918357, signed=False)
        writer.write_int(self.hash, signed=True)
        writer.write(bytes(self.gifts))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_int()
        gifts = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(hash, gifts, chats, users)

@register
class PaymentsConnectedStarRefBots(TLObject):
    CONSTRUCTOR_ID = 2564155933
    __slots__ = ('count', 'connected_bots', 'users')
    def __init__(self, count: int, connected_bots: 'Vector', users: 'Vector'):
        self.count = count
        self.connected_bots = connected_bots
        self.users = users
    def to_dict(self):
        return {"count": self.count, "connected_bots": self.connected_bots, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2564155933, signed=False)
        writer.write_int(self.count, signed=True)
        writer.write(bytes(self.connected_bots))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        count = reader.read_int()
        connected_bots = reader.tgread_object()
        users = reader.tgread_object()
        return cls(count, connected_bots, users)

@register
class PaymentsSuggestedStarRefBots(TLObject):
    CONSTRUCTOR_ID = 3033913433
    __slots__ = ('count', 'suggested_bots', 'users', 'next_offset')
    def __init__(self, count: int, suggested_bots: 'Vector', users: 'Vector', next_offset: str = None):
        self.count = count
        self.suggested_bots = suggested_bots
        self.users = users
        self.next_offset = next_offset
    def to_dict(self):
        return {"count": self.count, "suggested_bots": self.suggested_bots, "users": self.users, "next_offset": self.next_offset}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3033913433, signed=False)
        flags = 0
        if self.next_offset is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write_int(self.count, signed=True)
        writer.write(bytes(self.suggested_bots))
        writer.write(bytes(self.users))
        if flags & (1 << 0):
            writer.write_string(self.next_offset)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        count = reader.read_int()
        suggested_bots = reader.tgread_object()
        users = reader.tgread_object()
        if flags & (1 << 0):
            next_offset = reader.read_string()
        else:
            next_offset = None
        return cls(count, suggested_bots, users, next_offset)

@register
class PaymentsStarGiftUpgradePreview(TLObject):
    CONSTRUCTOR_ID = 1038213101
    __slots__ = ('sample_attributes', 'prices', 'next_prices')
    def __init__(self, sample_attributes: 'Vector', prices: 'Vector', next_prices: 'Vector'):
        self.sample_attributes = sample_attributes
        self.prices = prices
        self.next_prices = next_prices
    def to_dict(self):
        return {"sample_attributes": self.sample_attributes, "prices": self.prices, "next_prices": self.next_prices}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1038213101, signed=False)
        writer.write(bytes(self.sample_attributes))
        writer.write(bytes(self.prices))
        writer.write(bytes(self.next_prices))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        sample_attributes = reader.tgread_object()
        prices = reader.tgread_object()
        next_prices = reader.tgread_object()
        return cls(sample_attributes, prices, next_prices)

@register
class PaymentsUniqueStarGift(TLObject):
    CONSTRUCTOR_ID = 1097619176
    __slots__ = ('gift', 'chats', 'users')
    def __init__(self, gift: 'StarGift', chats: 'Vector', users: 'Vector'):
        self.gift = gift
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"gift": self.gift, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1097619176, signed=False)
        writer.write(bytes(self.gift))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        gift = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(gift, chats, users)

@register
class PaymentsSavedStarGifts(TLObject):
    CONSTRUCTOR_ID = 2515765681
    __slots__ = ('count', 'chat_notifications_enabled', 'gifts', 'next_offset', 'chats', 'users')
    def __init__(self, count: int, gifts: 'Vector', chats: 'Vector', users: 'Vector', chat_notifications_enabled: bool = None, next_offset: str = None):
        self.count = count
        self.chat_notifications_enabled = chat_notifications_enabled
        self.gifts = gifts
        self.next_offset = next_offset
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"count": self.count, "chat_notifications_enabled": self.chat_notifications_enabled, "gifts": self.gifts, "next_offset": self.next_offset, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2515765681, signed=False)
        flags = 0
        if self.chat_notifications_enabled is not None: flags |= 1 << 1
        if self.next_offset is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write_int(self.count, signed=True)
        if flags & (1 << 1):
            writer.write(serialize_bool(self.chat_notifications_enabled))
        writer.write(bytes(self.gifts))
        if flags & (1 << 0):
            writer.write_string(self.next_offset)
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        count = reader.read_int()
        if flags & (1 << 1):
            chat_notifications_enabled = reader.tgread_bool()
        else:
            chat_notifications_enabled = None
        gifts = reader.tgread_object()
        if flags & (1 << 0):
            next_offset = reader.read_string()
        else:
            next_offset = None
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(count, chat_notifications_enabled, gifts, next_offset, chats, users)

@register
class PaymentsStarGiftWithdrawalUrl(TLObject):
    CONSTRUCTOR_ID = 2225748636
    __slots__ = ('url')
    def __init__(self, url: str):
        self.url = url
    def to_dict(self):
        return {"url": self.url}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2225748636, signed=False)
        writer.write_string(self.url)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        url = reader.read_string()
        return cls(url)

@register
class PaymentsResaleStarGifts(TLObject):
    CONSTRUCTOR_ID = 2491028191
    __slots__ = ('count', 'gifts', 'next_offset', 'attributes', 'attributes_hash', 'chats', 'counters', 'users')
    def __init__(self, count: int, gifts: 'Vector', chats: 'Vector', users: 'Vector', next_offset: str = None, attributes: 'Vector' = None, attributes_hash: int = None, counters: 'Vector' = None):
        self.count = count
        self.gifts = gifts
        self.next_offset = next_offset
        self.attributes = attributes
        self.attributes_hash = attributes_hash
        self.chats = chats
        self.counters = counters
        self.users = users
    def to_dict(self):
        return {"count": self.count, "gifts": self.gifts, "next_offset": self.next_offset, "attributes": self.attributes, "attributes_hash": self.attributes_hash, "chats": self.chats, "counters": self.counters, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2491028191, signed=False)
        flags = 0
        if self.next_offset is not None: flags |= 1 << 0
        if self.attributes is not None: flags |= 1 << 1
        if self.attributes_hash is not None: flags |= 1 << 1
        if self.counters is not None: flags |= 1 << 2
        writer.write_int(flags, signed=False)
        writer.write_int(self.count, signed=True)
        writer.write(bytes(self.gifts))
        if flags & (1 << 0):
            writer.write_string(self.next_offset)
        if flags & (1 << 1):
            writer.write(bytes(self.attributes))
        if flags & (1 << 1):
            writer.write_long(self.attributes_hash, signed=False)
        writer.write(bytes(self.chats))
        if flags & (1 << 2):
            writer.write(bytes(self.counters))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        count = reader.read_int()
        gifts = reader.tgread_object()
        if flags & (1 << 0):
            next_offset = reader.read_string()
        else:
            next_offset = None
        if flags & (1 << 1):
            attributes = reader.tgread_object()
        else:
            attributes = None
        if flags & (1 << 1):
            attributes_hash = reader.read_long()
        else:
            attributes_hash = None
        chats = reader.tgread_object()
        if flags & (1 << 2):
            counters = reader.tgread_object()
        else:
            counters = None
        users = reader.tgread_object()
        return cls(count, gifts, next_offset, attributes, attributes_hash, chats, counters, users)

@register
class PaymentsStarGiftCollectionsNotModified(TLObject):
    CONSTRUCTOR_ID = 2696564503
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2696564503, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class PaymentsStarGiftCollections(TLObject):
    CONSTRUCTOR_ID = 2317955827
    __slots__ = ('collections')
    def __init__(self, collections: 'Vector'):
        self.collections = collections
    def to_dict(self):
        return {"collections": self.collections}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2317955827, signed=False)
        writer.write(bytes(self.collections))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        collections = reader.tgread_object()
        return cls(collections)

@register
class PaymentsUniqueStarGiftValueInfo(TLObject):
    CONSTRUCTOR_ID = 1362093126
    __slots__ = ('last_sale_on_fragment', 'value_is_average', 'currency', 'value', 'initial_sale_date', 'initial_sale_stars', 'initial_sale_price', 'last_sale_date', 'last_sale_price', 'floor_price', 'average_price', 'listed_count', 'fragment_listed_count', 'fragment_listed_url')
    def __init__(self, currency: str, value: int, initial_sale_date: int, initial_sale_stars: int, initial_sale_price: int, last_sale_on_fragment: bool = None, value_is_average: bool = None, last_sale_date: int = None, last_sale_price: int = None, floor_price: int = None, average_price: int = None, listed_count: int = None, fragment_listed_count: int = None, fragment_listed_url: str = None):
        self.last_sale_on_fragment = last_sale_on_fragment
        self.value_is_average = value_is_average
        self.currency = currency
        self.value = value
        self.initial_sale_date = initial_sale_date
        self.initial_sale_stars = initial_sale_stars
        self.initial_sale_price = initial_sale_price
        self.last_sale_date = last_sale_date
        self.last_sale_price = last_sale_price
        self.floor_price = floor_price
        self.average_price = average_price
        self.listed_count = listed_count
        self.fragment_listed_count = fragment_listed_count
        self.fragment_listed_url = fragment_listed_url
    def to_dict(self):
        return {"last_sale_on_fragment": self.last_sale_on_fragment, "value_is_average": self.value_is_average, "currency": self.currency, "value": self.value, "initial_sale_date": self.initial_sale_date, "initial_sale_stars": self.initial_sale_stars, "initial_sale_price": self.initial_sale_price, "last_sale_date": self.last_sale_date, "last_sale_price": self.last_sale_price, "floor_price": self.floor_price, "average_price": self.average_price, "listed_count": self.listed_count, "fragment_listed_count": self.fragment_listed_count, "fragment_listed_url": self.fragment_listed_url}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1362093126, signed=False)
        flags = 0
        if self.last_sale_on_fragment: flags |= 1 << 1
        if self.value_is_average: flags |= 1 << 6
        if self.last_sale_date is not None: flags |= 1 << 0
        if self.last_sale_price is not None: flags |= 1 << 0
        if self.floor_price is not None: flags |= 1 << 2
        if self.average_price is not None: flags |= 1 << 3
        if self.listed_count is not None: flags |= 1 << 4
        if self.fragment_listed_count is not None: flags |= 1 << 5
        if self.fragment_listed_url is not None: flags |= 1 << 5
        writer.write_int(flags, signed=False)
        writer.write_string(self.currency)
        writer.write_long(self.value, signed=False)
        writer.write_int(self.initial_sale_date, signed=True)
        writer.write_long(self.initial_sale_stars, signed=False)
        writer.write_long(self.initial_sale_price, signed=False)
        if flags & (1 << 0):
            writer.write_int(self.last_sale_date, signed=True)
        if flags & (1 << 0):
            writer.write_long(self.last_sale_price, signed=False)
        if flags & (1 << 2):
            writer.write_long(self.floor_price, signed=False)
        if flags & (1 << 3):
            writer.write_long(self.average_price, signed=False)
        if flags & (1 << 4):
            writer.write_int(self.listed_count, signed=True)
        if flags & (1 << 5):
            writer.write_int(self.fragment_listed_count, signed=True)
        if flags & (1 << 5):
            writer.write_string(self.fragment_listed_url)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        last_sale_on_fragment = bool(flags & (1 << 1))
        value_is_average = bool(flags & (1 << 6))
        currency = reader.read_string()
        value = reader.read_long()
        initial_sale_date = reader.read_int()
        initial_sale_stars = reader.read_long()
        initial_sale_price = reader.read_long()
        if flags & (1 << 0):
            last_sale_date = reader.read_int()
        else:
            last_sale_date = None
        if flags & (1 << 0):
            last_sale_price = reader.read_long()
        else:
            last_sale_price = None
        if flags & (1 << 2):
            floor_price = reader.read_long()
        else:
            floor_price = None
        if flags & (1 << 3):
            average_price = reader.read_long()
        else:
            average_price = None
        if flags & (1 << 4):
            listed_count = reader.read_int()
        else:
            listed_count = None
        if flags & (1 << 5):
            fragment_listed_count = reader.read_int()
        else:
            fragment_listed_count = None
        if flags & (1 << 5):
            fragment_listed_url = reader.read_string()
        else:
            fragment_listed_url = None
        return cls(last_sale_on_fragment, value_is_average, currency, value, initial_sale_date, initial_sale_stars, initial_sale_price, last_sale_date, last_sale_price, floor_price, average_price, listed_count, fragment_listed_count, fragment_listed_url)

@register
class PaymentsCheckCanSendGiftResultOk(TLObject):
    CONSTRUCTOR_ID = 927967149
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(927967149, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class PaymentsCheckCanSendGiftResultFail(TLObject):
    CONSTRUCTOR_ID = 3588588148
    __slots__ = ('reason')
    def __init__(self, reason: 'TextWithEntities'):
        self.reason = reason
    def to_dict(self):
        return {"reason": self.reason}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3588588148, signed=False)
        writer.write(bytes(self.reason))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        reason = reader.tgread_object()
        return cls(reason)

@register
class PaymentsStarGiftAuctionState(TLObject):
    CONSTRUCTOR_ID = 1798960364
    __slots__ = ('gift', 'state', 'user_state', 'timeout', 'users', 'chats')
    def __init__(self, gift: 'StarGift', state: 'StarGiftAuctionState', user_state: 'StarGiftAuctionUserState', timeout: int, users: 'Vector', chats: 'Vector'):
        self.gift = gift
        self.state = state
        self.user_state = user_state
        self.timeout = timeout
        self.users = users
        self.chats = chats
    def to_dict(self):
        return {"gift": self.gift, "state": self.state, "user_state": self.user_state, "timeout": self.timeout, "users": self.users, "chats": self.chats}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1798960364, signed=False)
        writer.write(bytes(self.gift))
        writer.write(bytes(self.state))
        writer.write(bytes(self.user_state))
        writer.write_int(self.timeout, signed=True)
        writer.write(bytes(self.users))
        writer.write(bytes(self.chats))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        gift = reader.tgread_object()
        state = reader.tgread_object()
        user_state = reader.tgread_object()
        timeout = reader.read_int()
        users = reader.tgread_object()
        chats = reader.tgread_object()
        return cls(gift, state, user_state, timeout, users, chats)

@register
class PaymentsStarGiftAuctionAcquiredGifts(TLObject):
    CONSTRUCTOR_ID = 2103169520
    __slots__ = ('gifts', 'users', 'chats')
    def __init__(self, gifts: 'Vector', users: 'Vector', chats: 'Vector'):
        self.gifts = gifts
        self.users = users
        self.chats = chats
    def to_dict(self):
        return {"gifts": self.gifts, "users": self.users, "chats": self.chats}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2103169520, signed=False)
        writer.write(bytes(self.gifts))
        writer.write(bytes(self.users))
        writer.write(bytes(self.chats))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        gifts = reader.tgread_object()
        users = reader.tgread_object()
        chats = reader.tgread_object()
        return cls(gifts, users, chats)

@register
class PaymentsStarGiftActiveAuctionsNotModified(TLObject):
    CONSTRUCTOR_ID = 3677608656
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3677608656, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class PaymentsStarGiftActiveAuctions(TLObject):
    CONSTRUCTOR_ID = 2935401404
    __slots__ = ('auctions', 'users', 'chats')
    def __init__(self, auctions: 'Vector', users: 'Vector', chats: 'Vector'):
        self.auctions = auctions
        self.users = users
        self.chats = chats
    def to_dict(self):
        return {"auctions": self.auctions, "users": self.users, "chats": self.chats}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2935401404, signed=False)
        writer.write(bytes(self.auctions))
        writer.write(bytes(self.users))
        writer.write(bytes(self.chats))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        auctions = reader.tgread_object()
        users = reader.tgread_object()
        chats = reader.tgread_object()
        return cls(auctions, users, chats)

@register
class PaymentsStarGiftUpgradeAttributes(TLObject):
    CONSTRUCTOR_ID = 1187439471
    __slots__ = ('attributes')
    def __init__(self, attributes: 'Vector'):
        self.attributes = attributes
    def to_dict(self):
        return {"attributes": self.attributes}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1187439471, signed=False)
        writer.write(bytes(self.attributes))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        attributes = reader.tgread_object()
        return cls(attributes)

