"""Auto-generated TL functions. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

@register
class PaymentsGetPaymentForm(TLObject):
    CONSTRUCTOR_ID = 924093883
    __slots__ = ('invoice', 'theme_params')
    def __init__(self, invoice: 'InputInvoice', theme_params: 'DataJSON' = None):
        self.invoice = invoice
        self.theme_params = theme_params
    def to_dict(self):
        return {"invoice": self.invoice, "theme_params": self.theme_params}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(924093883, signed=False)
        flags = 0
        if self.theme_params is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.invoice))
        if flags & (1 << 0):
            writer.write(bytes(self.theme_params))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        invoice = reader.tgread_object()
        if flags & (1 << 0):
            theme_params = reader.tgread_object()
        else:
            theme_params = None
        return cls(invoice, theme_params)

@register
class PaymentsGetPaymentReceipt(TLObject):
    CONSTRUCTOR_ID = 611897804
    __slots__ = ('peer', 'msg_id')
    def __init__(self, peer: 'InputPeer', msg_id: int):
        self.peer = peer
        self.msg_id = msg_id
    def to_dict(self):
        return {"peer": self.peer, "msg_id": self.msg_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(611897804, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.msg_id, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        msg_id = reader.read_int()
        return cls(peer, msg_id)

@register
class PaymentsValidateRequestedInfo(TLObject):
    CONSTRUCTOR_ID = 3066622251
    __slots__ = ('save', 'invoice', 'info')
    def __init__(self, invoice: 'InputInvoice', info: 'PaymentRequestedInfo', save: bool = None):
        self.save = save
        self.invoice = invoice
        self.info = info
    def to_dict(self):
        return {"save": self.save, "invoice": self.invoice, "info": self.info}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3066622251, signed=False)
        flags = 0
        if self.save: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.invoice))
        writer.write(bytes(self.info))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        save = bool(flags & (1 << 0))
        invoice = reader.tgread_object()
        info = reader.tgread_object()
        return cls(save, invoice, info)

@register
class PaymentsSendPaymentForm(TLObject):
    CONSTRUCTOR_ID = 755192367
    __slots__ = ('form_id', 'invoice', 'requested_info_id', 'shipping_option_id', 'credentials', 'tip_amount')
    def __init__(self, form_id: int, invoice: 'InputInvoice', credentials: 'InputPaymentCredentials', requested_info_id: str = None, shipping_option_id: str = None, tip_amount: int = None):
        self.form_id = form_id
        self.invoice = invoice
        self.requested_info_id = requested_info_id
        self.shipping_option_id = shipping_option_id
        self.credentials = credentials
        self.tip_amount = tip_amount
    def to_dict(self):
        return {"form_id": self.form_id, "invoice": self.invoice, "requested_info_id": self.requested_info_id, "shipping_option_id": self.shipping_option_id, "credentials": self.credentials, "tip_amount": self.tip_amount}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(755192367, signed=False)
        flags = 0
        if self.requested_info_id is not None: flags |= 1 << 0
        if self.shipping_option_id is not None: flags |= 1 << 1
        if self.tip_amount is not None: flags |= 1 << 2
        writer.write_int(flags, signed=False)
        writer.write_long(self.form_id, signed=False)
        writer.write(bytes(self.invoice))
        if flags & (1 << 0):
            writer.write_string(self.requested_info_id)
        if flags & (1 << 1):
            writer.write_string(self.shipping_option_id)
        writer.write(bytes(self.credentials))
        if flags & (1 << 2):
            writer.write_long(self.tip_amount, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        form_id = reader.read_long()
        invoice = reader.tgread_object()
        if flags & (1 << 0):
            requested_info_id = reader.read_string()
        else:
            requested_info_id = None
        if flags & (1 << 1):
            shipping_option_id = reader.read_string()
        else:
            shipping_option_id = None
        credentials = reader.tgread_object()
        if flags & (1 << 2):
            tip_amount = reader.read_long()
        else:
            tip_amount = None
        return cls(form_id, invoice, requested_info_id, shipping_option_id, credentials, tip_amount)

@register
class PaymentsGetSavedInfo(TLObject):
    CONSTRUCTOR_ID = 578650699
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(578650699, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class PaymentsClearSavedInfo(TLObject):
    CONSTRUCTOR_ID = 3627905217
    __slots__ = ('credentials', 'info')
    def __init__(self, credentials: bool = None, info: bool = None):
        self.credentials = credentials
        self.info = info
    def to_dict(self):
        return {"credentials": self.credentials, "info": self.info}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3627905217, signed=False)
        flags = 0
        if self.credentials: flags |= 1 << 0
        if self.info: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        credentials = bool(flags & (1 << 0))
        info = bool(flags & (1 << 1))
        return cls(credentials, info)

@register
class PaymentsGetBankCardData(TLObject):
    CONSTRUCTOR_ID = 779736953
    __slots__ = ('number')
    def __init__(self, number: str):
        self.number = number
    def to_dict(self):
        return {"number": self.number}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(779736953, signed=False)
        writer.write_string(self.number)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        number = reader.read_string()
        return cls(number)

@register
class PaymentsExportInvoice(TLObject):
    CONSTRUCTOR_ID = 261206117
    __slots__ = ('invoice_media')
    def __init__(self, invoice_media: 'InputMedia'):
        self.invoice_media = invoice_media
    def to_dict(self):
        return {"invoice_media": self.invoice_media}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(261206117, signed=False)
        writer.write(bytes(self.invoice_media))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        invoice_media = reader.tgread_object()
        return cls(invoice_media)

@register
class PaymentsAssignAppStoreTransaction(TLObject):
    CONSTRUCTOR_ID = 2163045501
    __slots__ = ('receipt', 'purpose')
    def __init__(self, receipt: bytes, purpose: 'InputStorePaymentPurpose'):
        self.receipt = receipt
        self.purpose = purpose
    def to_dict(self):
        return {"receipt": self.receipt, "purpose": self.purpose}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2163045501, signed=False)
        writer.write_bytes(self.receipt)
        writer.write(bytes(self.purpose))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        receipt = reader.read_bytes()
        purpose = reader.tgread_object()
        return cls(receipt, purpose)

@register
class PaymentsAssignPlayMarketTransaction(TLObject):
    CONSTRUCTOR_ID = 3757920467
    __slots__ = ('receipt', 'purpose')
    def __init__(self, receipt: 'DataJSON', purpose: 'InputStorePaymentPurpose'):
        self.receipt = receipt
        self.purpose = purpose
    def to_dict(self):
        return {"receipt": self.receipt, "purpose": self.purpose}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3757920467, signed=False)
        writer.write(bytes(self.receipt))
        writer.write(bytes(self.purpose))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        receipt = reader.tgread_object()
        purpose = reader.tgread_object()
        return cls(receipt, purpose)

@register
class PaymentsGetPremiumGiftCodeOptions(TLObject):
    CONSTRUCTOR_ID = 660060756
    __slots__ = ('boost_peer')
    def __init__(self, boost_peer: 'InputPeer' = None):
        self.boost_peer = boost_peer
    def to_dict(self):
        return {"boost_peer": self.boost_peer}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(660060756, signed=False)
        flags = 0
        if self.boost_peer is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        if flags & (1 << 0):
            writer.write(bytes(self.boost_peer))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        if flags & (1 << 0):
            boost_peer = reader.tgread_object()
        else:
            boost_peer = None
        return cls(boost_peer)

@register
class PaymentsCheckGiftCode(TLObject):
    CONSTRUCTOR_ID = 2387719361
    __slots__ = ('slug')
    def __init__(self, slug: str):
        self.slug = slug
    def to_dict(self):
        return {"slug": self.slug}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2387719361, signed=False)
        writer.write_string(self.slug)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        slug = reader.read_string()
        return cls(slug)

@register
class PaymentsApplyGiftCode(TLObject):
    CONSTRUCTOR_ID = 4142032980
    __slots__ = ('slug')
    def __init__(self, slug: str):
        self.slug = slug
    def to_dict(self):
        return {"slug": self.slug}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4142032980, signed=False)
        writer.write_string(self.slug)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        slug = reader.read_string()
        return cls(slug)

@register
class PaymentsGetGiveawayInfo(TLObject):
    CONSTRUCTOR_ID = 4095972389
    __slots__ = ('peer', 'msg_id')
    def __init__(self, peer: 'InputPeer', msg_id: int):
        self.peer = peer
        self.msg_id = msg_id
    def to_dict(self):
        return {"peer": self.peer, "msg_id": self.msg_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4095972389, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.msg_id, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        msg_id = reader.read_int()
        return cls(peer, msg_id)

@register
class PaymentsLaunchPrepaidGiveaway(TLObject):
    CONSTRUCTOR_ID = 1609928480
    __slots__ = ('peer', 'giveaway_id', 'purpose')
    def __init__(self, peer: 'InputPeer', giveaway_id: int, purpose: 'InputStorePaymentPurpose'):
        self.peer = peer
        self.giveaway_id = giveaway_id
        self.purpose = purpose
    def to_dict(self):
        return {"peer": self.peer, "giveaway_id": self.giveaway_id, "purpose": self.purpose}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1609928480, signed=False)
        writer.write(bytes(self.peer))
        writer.write_long(self.giveaway_id, signed=False)
        writer.write(bytes(self.purpose))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        giveaway_id = reader.read_long()
        purpose = reader.tgread_object()
        return cls(peer, giveaway_id, purpose)

@register
class PaymentsGetStarsTopupOptions(TLObject):
    CONSTRUCTOR_ID = 3222194131
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3222194131, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class PaymentsGetStarsStatus(TLObject):
    CONSTRUCTOR_ID = 1319744447
    __slots__ = ('ton', 'peer')
    def __init__(self, peer: 'InputPeer', ton: bool = None):
        self.ton = ton
        self.peer = peer
    def to_dict(self):
        return {"ton": self.ton, "peer": self.peer}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1319744447, signed=False)
        flags = 0
        if self.ton: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        ton = bool(flags & (1 << 0))
        peer = reader.tgread_object()
        return cls(ton, peer)

@register
class PaymentsGetStarsTransactions(TLObject):
    CONSTRUCTOR_ID = 1775912279
    __slots__ = ('inbound', 'outbound', 'ascending', 'ton', 'subscription_id', 'peer', 'offset', 'limit')
    def __init__(self, peer: 'InputPeer', offset: str, limit: int, inbound: bool = None, outbound: bool = None, ascending: bool = None, ton: bool = None, subscription_id: str = None):
        self.inbound = inbound
        self.outbound = outbound
        self.ascending = ascending
        self.ton = ton
        self.subscription_id = subscription_id
        self.peer = peer
        self.offset = offset
        self.limit = limit
    def to_dict(self):
        return {"inbound": self.inbound, "outbound": self.outbound, "ascending": self.ascending, "ton": self.ton, "subscription_id": self.subscription_id, "peer": self.peer, "offset": self.offset, "limit": self.limit}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1775912279, signed=False)
        flags = 0
        if self.inbound: flags |= 1 << 0
        if self.outbound: flags |= 1 << 1
        if self.ascending: flags |= 1 << 2
        if self.ton: flags |= 1 << 4
        if self.subscription_id is not None: flags |= 1 << 3
        writer.write_int(flags, signed=False)
        if flags & (1 << 3):
            writer.write_string(self.subscription_id)
        writer.write(bytes(self.peer))
        writer.write_string(self.offset)
        writer.write_int(self.limit, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        inbound = bool(flags & (1 << 0))
        outbound = bool(flags & (1 << 1))
        ascending = bool(flags & (1 << 2))
        ton = bool(flags & (1 << 4))
        if flags & (1 << 3):
            subscription_id = reader.read_string()
        else:
            subscription_id = None
        peer = reader.tgread_object()
        offset = reader.read_string()
        limit = reader.read_int()
        return cls(inbound, outbound, ascending, ton, subscription_id, peer, offset, limit)

@register
class PaymentsSendStarsForm(TLObject):
    CONSTRUCTOR_ID = 2040056084
    __slots__ = ('form_id', 'invoice')
    def __init__(self, form_id: int, invoice: 'InputInvoice'):
        self.form_id = form_id
        self.invoice = invoice
    def to_dict(self):
        return {"form_id": self.form_id, "invoice": self.invoice}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2040056084, signed=False)
        writer.write_long(self.form_id, signed=False)
        writer.write(bytes(self.invoice))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        form_id = reader.read_long()
        invoice = reader.tgread_object()
        return cls(form_id, invoice)

@register
class PaymentsRefundStarsCharge(TLObject):
    CONSTRUCTOR_ID = 632196938
    __slots__ = ('user_id', 'charge_id')
    def __init__(self, user_id: 'InputUser', charge_id: str):
        self.user_id = user_id
        self.charge_id = charge_id
    def to_dict(self):
        return {"user_id": self.user_id, "charge_id": self.charge_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(632196938, signed=False)
        writer.write(bytes(self.user_id))
        writer.write_string(self.charge_id)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        user_id = reader.tgread_object()
        charge_id = reader.read_string()
        return cls(user_id, charge_id)

@register
class PaymentsGetStarsRevenueStats(TLObject):
    CONSTRUCTOR_ID = 3642751702
    __slots__ = ('dark', 'ton', 'peer')
    def __init__(self, peer: 'InputPeer', dark: bool = None, ton: bool = None):
        self.dark = dark
        self.ton = ton
        self.peer = peer
    def to_dict(self):
        return {"dark": self.dark, "ton": self.ton, "peer": self.peer}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3642751702, signed=False)
        flags = 0
        if self.dark: flags |= 1 << 0
        if self.ton: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        dark = bool(flags & (1 << 0))
        ton = bool(flags & (1 << 1))
        peer = reader.tgread_object()
        return cls(dark, ton, peer)

@register
class PaymentsGetStarsRevenueWithdrawalUrl(TLObject):
    CONSTRUCTOR_ID = 607378578
    __slots__ = ('ton', 'peer', 'amount', 'password')
    def __init__(self, peer: 'InputPeer', password: 'InputCheckPasswordSRP', ton: bool = None, amount: int = None):
        self.ton = ton
        self.peer = peer
        self.amount = amount
        self.password = password
    def to_dict(self):
        return {"ton": self.ton, "peer": self.peer, "amount": self.amount, "password": self.password}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(607378578, signed=False)
        flags = 0
        if self.ton: flags |= 1 << 0
        if self.amount is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        if flags & (1 << 1):
            writer.write_long(self.amount, signed=False)
        writer.write(bytes(self.password))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        ton = bool(flags & (1 << 0))
        peer = reader.tgread_object()
        if flags & (1 << 1):
            amount = reader.read_long()
        else:
            amount = None
        password = reader.tgread_object()
        return cls(ton, peer, amount, password)

@register
class PaymentsGetStarsRevenueAdsAccountUrl(TLObject):
    CONSTRUCTOR_ID = 3520589765
    __slots__ = ('peer')
    def __init__(self, peer: 'InputPeer'):
        self.peer = peer
    def to_dict(self):
        return {"peer": self.peer}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3520589765, signed=False)
        writer.write(bytes(self.peer))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        return cls(peer)

@register
class PaymentsGetStarsTransactionsByID(TLObject):
    CONSTRUCTOR_ID = 768218808
    __slots__ = ('ton', 'peer', 'id')
    def __init__(self, peer: 'InputPeer', id: 'Vector', ton: bool = None):
        self.ton = ton
        self.peer = peer
        self.id = id
    def to_dict(self):
        return {"ton": self.ton, "peer": self.peer, "id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(768218808, signed=False)
        flags = 0
        if self.ton: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        ton = bool(flags & (1 << 0))
        peer = reader.tgread_object()
        id = reader.tgread_object()
        return cls(ton, peer, id)

@register
class PaymentsGetStarsGiftOptions(TLObject):
    CONSTRUCTOR_ID = 3553192904
    __slots__ = ('user_id')
    def __init__(self, user_id: 'InputUser' = None):
        self.user_id = user_id
    def to_dict(self):
        return {"user_id": self.user_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3553192904, signed=False)
        flags = 0
        if self.user_id is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        if flags & (1 << 0):
            writer.write(bytes(self.user_id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        if flags & (1 << 0):
            user_id = reader.tgread_object()
        else:
            user_id = None
        return cls(user_id)

@register
class PaymentsGetStarsSubscriptions(TLObject):
    CONSTRUCTOR_ID = 52761285
    __slots__ = ('missing_balance', 'peer', 'offset')
    def __init__(self, peer: 'InputPeer', offset: str, missing_balance: bool = None):
        self.missing_balance = missing_balance
        self.peer = peer
        self.offset = offset
    def to_dict(self):
        return {"missing_balance": self.missing_balance, "peer": self.peer, "offset": self.offset}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(52761285, signed=False)
        flags = 0
        if self.missing_balance: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write_string(self.offset)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        missing_balance = bool(flags & (1 << 0))
        peer = reader.tgread_object()
        offset = reader.read_string()
        return cls(missing_balance, peer, offset)

@register
class PaymentsChangeStarsSubscription(TLObject):
    CONSTRUCTOR_ID = 3346466936
    __slots__ = ('peer', 'subscription_id', 'canceled')
    def __init__(self, peer: 'InputPeer', subscription_id: str, canceled: bool = None):
        self.peer = peer
        self.subscription_id = subscription_id
        self.canceled = canceled
    def to_dict(self):
        return {"peer": self.peer, "subscription_id": self.subscription_id, "canceled": self.canceled}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3346466936, signed=False)
        flags = 0
        if self.canceled is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write_string(self.subscription_id)
        if flags & (1 << 0):
            writer.write(serialize_bool(self.canceled))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        peer = reader.tgread_object()
        subscription_id = reader.read_string()
        if flags & (1 << 0):
            canceled = reader.tgread_bool()
        else:
            canceled = None
        return cls(peer, subscription_id, canceled)

@register
class PaymentsFulfillStarsSubscription(TLObject):
    CONSTRUCTOR_ID = 3428576179
    __slots__ = ('peer', 'subscription_id')
    def __init__(self, peer: 'InputPeer', subscription_id: str):
        self.peer = peer
        self.subscription_id = subscription_id
    def to_dict(self):
        return {"peer": self.peer, "subscription_id": self.subscription_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3428576179, signed=False)
        writer.write(bytes(self.peer))
        writer.write_string(self.subscription_id)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        subscription_id = reader.read_string()
        return cls(peer, subscription_id)

@register
class PaymentsGetStarsGiveawayOptions(TLObject):
    CONSTRUCTOR_ID = 3172924734
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3172924734, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class PaymentsGetStarGifts(TLObject):
    CONSTRUCTOR_ID = 3293984144
    __slots__ = ('hash')
    def __init__(self, hash: int):
        self.hash = hash
    def to_dict(self):
        return {"hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3293984144, signed=False)
        writer.write_int(self.hash, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_int()
        return cls(hash)

@register
class PaymentsSaveStarGift(TLObject):
    CONSTRUCTOR_ID = 707422588
    __slots__ = ('unsave', 'stargift')
    def __init__(self, stargift: 'InputSavedStarGift', unsave: bool = None):
        self.unsave = unsave
        self.stargift = stargift
    def to_dict(self):
        return {"unsave": self.unsave, "stargift": self.stargift}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(707422588, signed=False)
        flags = 0
        if self.unsave: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.stargift))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        unsave = bool(flags & (1 << 0))
        stargift = reader.tgread_object()
        return cls(unsave, stargift)

@register
class PaymentsConvertStarGift(TLObject):
    CONSTRUCTOR_ID = 1958676331
    __slots__ = ('stargift')
    def __init__(self, stargift: 'InputSavedStarGift'):
        self.stargift = stargift
    def to_dict(self):
        return {"stargift": self.stargift}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1958676331, signed=False)
        writer.write(bytes(self.stargift))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        stargift = reader.tgread_object()
        return cls(stargift)

@register
class PaymentsBotCancelStarsSubscription(TLObject):
    CONSTRUCTOR_ID = 1845102114
    __slots__ = ('restore', 'user_id', 'charge_id')
    def __init__(self, user_id: 'InputUser', charge_id: str, restore: bool = None):
        self.restore = restore
        self.user_id = user_id
        self.charge_id = charge_id
    def to_dict(self):
        return {"restore": self.restore, "user_id": self.user_id, "charge_id": self.charge_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1845102114, signed=False)
        flags = 0
        if self.restore: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.user_id))
        writer.write_string(self.charge_id)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        restore = bool(flags & (1 << 0))
        user_id = reader.tgread_object()
        charge_id = reader.read_string()
        return cls(restore, user_id, charge_id)

@register
class PaymentsGetConnectedStarRefBots(TLObject):
    CONSTRUCTOR_ID = 1483318611
    __slots__ = ('peer', 'offset_date', 'offset_link', 'limit')
    def __init__(self, peer: 'InputPeer', limit: int, offset_date: int = None, offset_link: str = None):
        self.peer = peer
        self.offset_date = offset_date
        self.offset_link = offset_link
        self.limit = limit
    def to_dict(self):
        return {"peer": self.peer, "offset_date": self.offset_date, "offset_link": self.offset_link, "limit": self.limit}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1483318611, signed=False)
        flags = 0
        if self.offset_date is not None: flags |= 1 << 2
        if self.offset_link is not None: flags |= 1 << 2
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        if flags & (1 << 2):
            writer.write_int(self.offset_date, signed=True)
        if flags & (1 << 2):
            writer.write_string(self.offset_link)
        writer.write_int(self.limit, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        peer = reader.tgread_object()
        if flags & (1 << 2):
            offset_date = reader.read_int()
        else:
            offset_date = None
        if flags & (1 << 2):
            offset_link = reader.read_string()
        else:
            offset_link = None
        limit = reader.read_int()
        return cls(peer, offset_date, offset_link, limit)

@register
class PaymentsGetConnectedStarRefBot(TLObject):
    CONSTRUCTOR_ID = 3084490992
    __slots__ = ('peer', 'bot')
    def __init__(self, peer: 'InputPeer', bot: 'InputUser'):
        self.peer = peer
        self.bot = bot
    def to_dict(self):
        return {"peer": self.peer, "bot": self.bot}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3084490992, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.bot))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        bot = reader.tgread_object()
        return cls(peer, bot)

@register
class PaymentsGetSuggestedStarRefBots(TLObject):
    CONSTRUCTOR_ID = 225134839
    __slots__ = ('order_by_revenue', 'order_by_date', 'peer', 'offset', 'limit')
    def __init__(self, peer: 'InputPeer', offset: str, limit: int, order_by_revenue: bool = None, order_by_date: bool = None):
        self.order_by_revenue = order_by_revenue
        self.order_by_date = order_by_date
        self.peer = peer
        self.offset = offset
        self.limit = limit
    def to_dict(self):
        return {"order_by_revenue": self.order_by_revenue, "order_by_date": self.order_by_date, "peer": self.peer, "offset": self.offset, "limit": self.limit}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(225134839, signed=False)
        flags = 0
        if self.order_by_revenue: flags |= 1 << 0
        if self.order_by_date: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write_string(self.offset)
        writer.write_int(self.limit, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        order_by_revenue = bool(flags & (1 << 0))
        order_by_date = bool(flags & (1 << 1))
        peer = reader.tgread_object()
        offset = reader.read_string()
        limit = reader.read_int()
        return cls(order_by_revenue, order_by_date, peer, offset, limit)

@register
class PaymentsConnectStarRefBot(TLObject):
    CONSTRUCTOR_ID = 2127901834
    __slots__ = ('peer', 'bot')
    def __init__(self, peer: 'InputPeer', bot: 'InputUser'):
        self.peer = peer
        self.bot = bot
    def to_dict(self):
        return {"peer": self.peer, "bot": self.bot}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2127901834, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.bot))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        bot = reader.tgread_object()
        return cls(peer, bot)

@register
class PaymentsEditConnectedStarRefBot(TLObject):
    CONSTRUCTOR_ID = 3841762467
    __slots__ = ('revoked', 'peer', 'link')
    def __init__(self, peer: 'InputPeer', link: str, revoked: bool = None):
        self.revoked = revoked
        self.peer = peer
        self.link = link
    def to_dict(self):
        return {"revoked": self.revoked, "peer": self.peer, "link": self.link}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3841762467, signed=False)
        flags = 0
        if self.revoked: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write_string(self.link)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        revoked = bool(flags & (1 << 0))
        peer = reader.tgread_object()
        link = reader.read_string()
        return cls(revoked, peer, link)

@register
class PaymentsGetStarGiftUpgradePreview(TLObject):
    CONSTRUCTOR_ID = 2627386545
    __slots__ = ('gift_id')
    def __init__(self, gift_id: int):
        self.gift_id = gift_id
    def to_dict(self):
        return {"gift_id": self.gift_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2627386545, signed=False)
        writer.write_long(self.gift_id, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        gift_id = reader.read_long()
        return cls(gift_id)

@register
class PaymentsUpgradeStarGift(TLObject):
    CONSTRUCTOR_ID = 2933318901
    __slots__ = ('keep_original_details', 'stargift')
    def __init__(self, stargift: 'InputSavedStarGift', keep_original_details: bool = None):
        self.keep_original_details = keep_original_details
        self.stargift = stargift
    def to_dict(self):
        return {"keep_original_details": self.keep_original_details, "stargift": self.stargift}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2933318901, signed=False)
        flags = 0
        if self.keep_original_details: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.stargift))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        keep_original_details = bool(flags & (1 << 0))
        stargift = reader.tgread_object()
        return cls(keep_original_details, stargift)

@register
class PaymentsTransferStarGift(TLObject):
    CONSTRUCTOR_ID = 2132285290
    __slots__ = ('stargift', 'to_id')
    def __init__(self, stargift: 'InputSavedStarGift', to_id: 'InputPeer'):
        self.stargift = stargift
        self.to_id = to_id
    def to_dict(self):
        return {"stargift": self.stargift, "to_id": self.to_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2132285290, signed=False)
        writer.write(bytes(self.stargift))
        writer.write(bytes(self.to_id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        stargift = reader.tgread_object()
        to_id = reader.tgread_object()
        return cls(stargift, to_id)

@register
class PaymentsGetUniqueStarGift(TLObject):
    CONSTRUCTOR_ID = 2711047538
    __slots__ = ('slug')
    def __init__(self, slug: str):
        self.slug = slug
    def to_dict(self):
        return {"slug": self.slug}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2711047538, signed=False)
        writer.write_string(self.slug)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        slug = reader.read_string()
        return cls(slug)

@register
class PaymentsGetSavedStarGifts(TLObject):
    CONSTRUCTOR_ID = 2736383337
    __slots__ = ('exclude_unsaved', 'exclude_saved', 'exclude_unlimited', 'exclude_unique', 'sort_by_value', 'exclude_upgradable', 'exclude_unupgradable', 'peer_color_available', 'exclude_hosted', 'peer', 'collection_id', 'offset', 'limit')
    def __init__(self, peer: 'InputPeer', offset: str, limit: int, exclude_unsaved: bool = None, exclude_saved: bool = None, exclude_unlimited: bool = None, exclude_unique: bool = None, sort_by_value: bool = None, exclude_upgradable: bool = None, exclude_unupgradable: bool = None, peer_color_available: bool = None, exclude_hosted: bool = None, collection_id: int = None):
        self.exclude_unsaved = exclude_unsaved
        self.exclude_saved = exclude_saved
        self.exclude_unlimited = exclude_unlimited
        self.exclude_unique = exclude_unique
        self.sort_by_value = sort_by_value
        self.exclude_upgradable = exclude_upgradable
        self.exclude_unupgradable = exclude_unupgradable
        self.peer_color_available = peer_color_available
        self.exclude_hosted = exclude_hosted
        self.peer = peer
        self.collection_id = collection_id
        self.offset = offset
        self.limit = limit
    def to_dict(self):
        return {"exclude_unsaved": self.exclude_unsaved, "exclude_saved": self.exclude_saved, "exclude_unlimited": self.exclude_unlimited, "exclude_unique": self.exclude_unique, "sort_by_value": self.sort_by_value, "exclude_upgradable": self.exclude_upgradable, "exclude_unupgradable": self.exclude_unupgradable, "peer_color_available": self.peer_color_available, "exclude_hosted": self.exclude_hosted, "peer": self.peer, "collection_id": self.collection_id, "offset": self.offset, "limit": self.limit}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2736383337, signed=False)
        flags = 0
        if self.exclude_unsaved: flags |= 1 << 0
        if self.exclude_saved: flags |= 1 << 1
        if self.exclude_unlimited: flags |= 1 << 2
        if self.exclude_unique: flags |= 1 << 4
        if self.sort_by_value: flags |= 1 << 5
        if self.exclude_upgradable: flags |= 1 << 7
        if self.exclude_unupgradable: flags |= 1 << 8
        if self.peer_color_available: flags |= 1 << 9
        if self.exclude_hosted: flags |= 1 << 10
        if self.collection_id is not None: flags |= 1 << 6
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        if flags & (1 << 6):
            writer.write_int(self.collection_id, signed=True)
        writer.write_string(self.offset)
        writer.write_int(self.limit, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        exclude_unsaved = bool(flags & (1 << 0))
        exclude_saved = bool(flags & (1 << 1))
        exclude_unlimited = bool(flags & (1 << 2))
        exclude_unique = bool(flags & (1 << 4))
        sort_by_value = bool(flags & (1 << 5))
        exclude_upgradable = bool(flags & (1 << 7))
        exclude_unupgradable = bool(flags & (1 << 8))
        peer_color_available = bool(flags & (1 << 9))
        exclude_hosted = bool(flags & (1 << 10))
        peer = reader.tgread_object()
        if flags & (1 << 6):
            collection_id = reader.read_int()
        else:
            collection_id = None
        offset = reader.read_string()
        limit = reader.read_int()
        return cls(exclude_unsaved, exclude_saved, exclude_unlimited, exclude_unique, sort_by_value, exclude_upgradable, exclude_unupgradable, peer_color_available, exclude_hosted, peer, collection_id, offset, limit)

@register
class PaymentsGetSavedStarGift(TLObject):
    CONSTRUCTOR_ID = 3025510662
    __slots__ = ('stargift')
    def __init__(self, stargift: 'Vector'):
        self.stargift = stargift
    def to_dict(self):
        return {"stargift": self.stargift}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3025510662, signed=False)
        writer.write(bytes(self.stargift))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        stargift = reader.tgread_object()
        return cls(stargift)

@register
class PaymentsGetStarGiftWithdrawalUrl(TLObject):
    CONSTRUCTOR_ID = 3496907688
    __slots__ = ('stargift', 'password')
    def __init__(self, stargift: 'InputSavedStarGift', password: 'InputCheckPasswordSRP'):
        self.stargift = stargift
        self.password = password
    def to_dict(self):
        return {"stargift": self.stargift, "password": self.password}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3496907688, signed=False)
        writer.write(bytes(self.stargift))
        writer.write(bytes(self.password))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        stargift = reader.tgread_object()
        password = reader.tgread_object()
        return cls(stargift, password)

@register
class PaymentsToggleChatStarGiftNotifications(TLObject):
    CONSTRUCTOR_ID = 1626009505
    __slots__ = ('enabled', 'peer')
    def __init__(self, peer: 'InputPeer', enabled: bool = None):
        self.enabled = enabled
        self.peer = peer
    def to_dict(self):
        return {"enabled": self.enabled, "peer": self.peer}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1626009505, signed=False)
        flags = 0
        if self.enabled: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        enabled = bool(flags & (1 << 0))
        peer = reader.tgread_object()
        return cls(enabled, peer)

@register
class PaymentsToggleStarGiftsPinnedToTop(TLObject):
    CONSTRUCTOR_ID = 353626032
    __slots__ = ('peer', 'stargift')
    def __init__(self, peer: 'InputPeer', stargift: 'Vector'):
        self.peer = peer
        self.stargift = stargift
    def to_dict(self):
        return {"peer": self.peer, "stargift": self.stargift}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(353626032, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.stargift))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        stargift = reader.tgread_object()
        return cls(peer, stargift)

@register
class PaymentsCanPurchaseStore(TLObject):
    CONSTRUCTOR_ID = 1339842215
    __slots__ = ('purpose')
    def __init__(self, purpose: 'InputStorePaymentPurpose'):
        self.purpose = purpose
    def to_dict(self):
        return {"purpose": self.purpose}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1339842215, signed=False)
        writer.write(bytes(self.purpose))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        purpose = reader.tgread_object()
        return cls(purpose)

@register
class PaymentsGetResaleStarGifts(TLObject):
    CONSTRUCTOR_ID = 2053087798
    __slots__ = ('sort_by_price', 'sort_by_num', 'for_craft', 'stars_only', 'attributes_hash', 'gift_id', 'attributes', 'offset', 'limit')
    def __init__(self, gift_id: int, offset: str, limit: int, sort_by_price: bool = None, sort_by_num: bool = None, for_craft: bool = None, stars_only: bool = None, attributes_hash: int = None, attributes: 'Vector' = None):
        self.sort_by_price = sort_by_price
        self.sort_by_num = sort_by_num
        self.for_craft = for_craft
        self.stars_only = stars_only
        self.attributes_hash = attributes_hash
        self.gift_id = gift_id
        self.attributes = attributes
        self.offset = offset
        self.limit = limit
    def to_dict(self):
        return {"sort_by_price": self.sort_by_price, "sort_by_num": self.sort_by_num, "for_craft": self.for_craft, "stars_only": self.stars_only, "attributes_hash": self.attributes_hash, "gift_id": self.gift_id, "attributes": self.attributes, "offset": self.offset, "limit": self.limit}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2053087798, signed=False)
        flags = 0
        if self.sort_by_price: flags |= 1 << 1
        if self.sort_by_num: flags |= 1 << 2
        if self.for_craft: flags |= 1 << 4
        if self.stars_only: flags |= 1 << 5
        if self.attributes_hash is not None: flags |= 1 << 0
        if self.attributes is not None: flags |= 1 << 3
        writer.write_int(flags, signed=False)
        if flags & (1 << 0):
            writer.write_long(self.attributes_hash, signed=False)
        writer.write_long(self.gift_id, signed=False)
        if flags & (1 << 3):
            writer.write(bytes(self.attributes))
        writer.write_string(self.offset)
        writer.write_int(self.limit, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        sort_by_price = bool(flags & (1 << 1))
        sort_by_num = bool(flags & (1 << 2))
        for_craft = bool(flags & (1 << 4))
        stars_only = bool(flags & (1 << 5))
        if flags & (1 << 0):
            attributes_hash = reader.read_long()
        else:
            attributes_hash = None
        gift_id = reader.read_long()
        if flags & (1 << 3):
            attributes = reader.tgread_object()
        else:
            attributes = None
        offset = reader.read_string()
        limit = reader.read_int()
        return cls(sort_by_price, sort_by_num, for_craft, stars_only, attributes_hash, gift_id, attributes, offset, limit)

@register
class PaymentsUpdateStarGiftPrice(TLObject):
    CONSTRUCTOR_ID = 3988679883
    __slots__ = ('stargift', 'resell_amount')
    def __init__(self, stargift: 'InputSavedStarGift', resell_amount: 'StarsAmount'):
        self.stargift = stargift
        self.resell_amount = resell_amount
    def to_dict(self):
        return {"stargift": self.stargift, "resell_amount": self.resell_amount}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3988679883, signed=False)
        writer.write(bytes(self.stargift))
        writer.write(bytes(self.resell_amount))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        stargift = reader.tgread_object()
        resell_amount = reader.tgread_object()
        return cls(stargift, resell_amount)

@register
class PaymentsCreateStarGiftCollection(TLObject):
    CONSTRUCTOR_ID = 524947079
    __slots__ = ('peer', 'title', 'stargift')
    def __init__(self, peer: 'InputPeer', title: str, stargift: 'Vector'):
        self.peer = peer
        self.title = title
        self.stargift = stargift
    def to_dict(self):
        return {"peer": self.peer, "title": self.title, "stargift": self.stargift}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(524947079, signed=False)
        writer.write(bytes(self.peer))
        writer.write_string(self.title)
        writer.write(bytes(self.stargift))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        title = reader.read_string()
        stargift = reader.tgread_object()
        return cls(peer, title, stargift)

@register
class PaymentsUpdateStarGiftCollection(TLObject):
    CONSTRUCTOR_ID = 1339932391
    __slots__ = ('peer', 'collection_id', 'title', 'delete_stargift', 'add_stargift', 'order')
    def __init__(self, peer: 'InputPeer', collection_id: int, title: str = None, delete_stargift: 'Vector' = None, add_stargift: 'Vector' = None, order: 'Vector' = None):
        self.peer = peer
        self.collection_id = collection_id
        self.title = title
        self.delete_stargift = delete_stargift
        self.add_stargift = add_stargift
        self.order = order
    def to_dict(self):
        return {"peer": self.peer, "collection_id": self.collection_id, "title": self.title, "delete_stargift": self.delete_stargift, "add_stargift": self.add_stargift, "order": self.order}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1339932391, signed=False)
        flags = 0
        if self.title is not None: flags |= 1 << 0
        if self.delete_stargift is not None: flags |= 1 << 1
        if self.add_stargift is not None: flags |= 1 << 2
        if self.order is not None: flags |= 1 << 3
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.collection_id, signed=True)
        if flags & (1 << 0):
            writer.write_string(self.title)
        if flags & (1 << 1):
            writer.write(bytes(self.delete_stargift))
        if flags & (1 << 2):
            writer.write(bytes(self.add_stargift))
        if flags & (1 << 3):
            writer.write(bytes(self.order))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        peer = reader.tgread_object()
        collection_id = reader.read_int()
        if flags & (1 << 0):
            title = reader.read_string()
        else:
            title = None
        if flags & (1 << 1):
            delete_stargift = reader.tgread_object()
        else:
            delete_stargift = None
        if flags & (1 << 2):
            add_stargift = reader.tgread_object()
        else:
            add_stargift = None
        if flags & (1 << 3):
            order = reader.tgread_object()
        else:
            order = None
        return cls(peer, collection_id, title, delete_stargift, add_stargift, order)

@register
class PaymentsReorderStarGiftCollections(TLObject):
    CONSTRUCTOR_ID = 3274372300
    __slots__ = ('peer', 'order')
    def __init__(self, peer: 'InputPeer', order: 'Vector'):
        self.peer = peer
        self.order = order
    def to_dict(self):
        return {"peer": self.peer, "order": self.order}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3274372300, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.order))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        order = reader.tgread_object()
        return cls(peer, order)

@register
class PaymentsDeleteStarGiftCollection(TLObject):
    CONSTRUCTOR_ID = 2908113128
    __slots__ = ('peer', 'collection_id')
    def __init__(self, peer: 'InputPeer', collection_id: int):
        self.peer = peer
        self.collection_id = collection_id
    def to_dict(self):
        return {"peer": self.peer, "collection_id": self.collection_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2908113128, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.collection_id, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        collection_id = reader.read_int()
        return cls(peer, collection_id)

@register
class PaymentsGetStarGiftCollections(TLObject):
    CONSTRUCTOR_ID = 2551943645
    __slots__ = ('peer', 'hash')
    def __init__(self, peer: 'InputPeer', hash: int):
        self.peer = peer
        self.hash = hash
    def to_dict(self):
        return {"peer": self.peer, "hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2551943645, signed=False)
        writer.write(bytes(self.peer))
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        hash = reader.read_long()
        return cls(peer, hash)

@register
class PaymentsGetUniqueStarGiftValueInfo(TLObject):
    CONSTRUCTOR_ID = 1130737515
    __slots__ = ('slug')
    def __init__(self, slug: str):
        self.slug = slug
    def to_dict(self):
        return {"slug": self.slug}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1130737515, signed=False)
        writer.write_string(self.slug)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        slug = reader.read_string()
        return cls(slug)

@register
class PaymentsCheckCanSendGift(TLObject):
    CONSTRUCTOR_ID = 3234131401
    __slots__ = ('gift_id')
    def __init__(self, gift_id: int):
        self.gift_id = gift_id
    def to_dict(self):
        return {"gift_id": self.gift_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3234131401, signed=False)
        writer.write_long(self.gift_id, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        gift_id = reader.read_long()
        return cls(gift_id)

@register
class PaymentsGetStarGiftAuctionState(TLObject):
    CONSTRUCTOR_ID = 1553986774
    __slots__ = ('auction', 'version')
    def __init__(self, auction: 'InputStarGiftAuction', version: int):
        self.auction = auction
        self.version = version
    def to_dict(self):
        return {"auction": self.auction, "version": self.version}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1553986774, signed=False)
        writer.write(bytes(self.auction))
        writer.write_int(self.version, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        auction = reader.tgread_object()
        version = reader.read_int()
        return cls(auction, version)

@register
class PaymentsGetStarGiftAuctionAcquiredGifts(TLObject):
    CONSTRUCTOR_ID = 1805831148
    __slots__ = ('gift_id')
    def __init__(self, gift_id: int):
        self.gift_id = gift_id
    def to_dict(self):
        return {"gift_id": self.gift_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1805831148, signed=False)
        writer.write_long(self.gift_id, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        gift_id = reader.read_long()
        return cls(gift_id)

@register
class PaymentsGetStarGiftActiveAuctions(TLObject):
    CONSTRUCTOR_ID = 2781892941
    __slots__ = ('hash')
    def __init__(self, hash: int):
        self.hash = hash
    def to_dict(self):
        return {"hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2781892941, signed=False)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_long()
        return cls(hash)

@register
class PaymentsResolveStarGiftOffer(TLObject):
    CONSTRUCTOR_ID = 3922622492
    __slots__ = ('decline', 'offer_msg_id')
    def __init__(self, offer_msg_id: int, decline: bool = None):
        self.decline = decline
        self.offer_msg_id = offer_msg_id
    def to_dict(self):
        return {"decline": self.decline, "offer_msg_id": self.offer_msg_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3922622492, signed=False)
        flags = 0
        if self.decline: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write_int(self.offer_msg_id, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        decline = bool(flags & (1 << 0))
        offer_msg_id = reader.read_int()
        return cls(decline, offer_msg_id)

@register
class PaymentsSendStarGiftOffer(TLObject):
    CONSTRUCTOR_ID = 2411227969
    __slots__ = ('peer', 'slug', 'price', 'duration', 'random_id', 'allow_paid_stars')
    def __init__(self, peer: 'InputPeer', slug: str, price: 'StarsAmount', duration: int, random_id: int, allow_paid_stars: int = None):
        self.peer = peer
        self.slug = slug
        self.price = price
        self.duration = duration
        self.random_id = random_id
        self.allow_paid_stars = allow_paid_stars
    def to_dict(self):
        return {"peer": self.peer, "slug": self.slug, "price": self.price, "duration": self.duration, "random_id": self.random_id, "allow_paid_stars": self.allow_paid_stars}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2411227969, signed=False)
        flags = 0
        if self.allow_paid_stars is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write_string(self.slug)
        writer.write(bytes(self.price))
        writer.write_int(self.duration, signed=True)
        writer.write_long(self.random_id, signed=False)
        if flags & (1 << 0):
            writer.write_long(self.allow_paid_stars, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        peer = reader.tgread_object()
        slug = reader.read_string()
        price = reader.tgread_object()
        duration = reader.read_int()
        random_id = reader.read_long()
        if flags & (1 << 0):
            allow_paid_stars = reader.read_long()
        else:
            allow_paid_stars = None
        return cls(peer, slug, price, duration, random_id, allow_paid_stars)

@register
class PaymentsGetStarGiftUpgradeAttributes(TLObject):
    CONSTRUCTOR_ID = 1828948824
    __slots__ = ('gift_id')
    def __init__(self, gift_id: int):
        self.gift_id = gift_id
    def to_dict(self):
        return {"gift_id": self.gift_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1828948824, signed=False)
        writer.write_long(self.gift_id, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        gift_id = reader.read_long()
        return cls(gift_id)

@register
class PaymentsGetCraftStarGifts(TLObject):
    CONSTRUCTOR_ID = 4245019904
    __slots__ = ('gift_id', 'offset', 'limit')
    def __init__(self, gift_id: int, offset: str, limit: int):
        self.gift_id = gift_id
        self.offset = offset
        self.limit = limit
    def to_dict(self):
        return {"gift_id": self.gift_id, "offset": self.offset, "limit": self.limit}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4245019904, signed=False)
        writer.write_long(self.gift_id, signed=False)
        writer.write_string(self.offset)
        writer.write_int(self.limit, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        gift_id = reader.read_long()
        offset = reader.read_string()
        limit = reader.read_int()
        return cls(gift_id, offset, limit)

@register
class PaymentsCraftStarGift(TLObject):
    CONSTRUCTOR_ID = 2969135183
    __slots__ = ('stargift')
    def __init__(self, stargift: 'Vector'):
        self.stargift = stargift
    def to_dict(self):
        return {"stargift": self.stargift}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2969135183, signed=False)
        writer.write(bytes(self.stargift))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        stargift = reader.tgread_object()
        return cls(stargift)

