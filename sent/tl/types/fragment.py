"""Auto-generated TL types. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional, TYPE_CHECKING
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

@register
class FragmentCollectibleInfo(TLObject):
    CONSTRUCTOR_ID = 1857945489
    __slots__ = ('purchase_date', 'currency', 'amount', 'crypto_currency', 'crypto_amount', 'url')
    def __init__(self, purchase_date: int, currency: str, amount: int, crypto_currency: str, crypto_amount: int, url: str):
        self.purchase_date = purchase_date
        self.currency = currency
        self.amount = amount
        self.crypto_currency = crypto_currency
        self.crypto_amount = crypto_amount
        self.url = url
    def to_dict(self):
        return {"purchase_date": self.purchase_date, "currency": self.currency, "amount": self.amount, "crypto_currency": self.crypto_currency, "crypto_amount": self.crypto_amount, "url": self.url}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1857945489, signed=False)
        writer.write_int(self.purchase_date, signed=True)
        writer.write_string(self.currency)
        writer.write_long(self.amount, signed=False)
        writer.write_string(self.crypto_currency)
        writer.write_long(self.crypto_amount, signed=False)
        writer.write_string(self.url)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        purchase_date = reader.read_int()
        currency = reader.read_string()
        amount = reader.read_long()
        crypto_currency = reader.read_string()
        crypto_amount = reader.read_long()
        url = reader.read_string()
        return cls(purchase_date, currency, amount, crypto_currency, crypto_amount, url)

