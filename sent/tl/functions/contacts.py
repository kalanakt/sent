"""Auto-generated TL functions. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

@register
class ContactsGetContactIDs(TLObject):
    CONSTRUCTOR_ID = 2061264541
    __slots__ = ('hash')
    def __init__(self, hash: int):
        self.hash = hash
    def to_dict(self):
        return {"hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2061264541, signed=False)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_long()
        return cls(hash)

@register
class ContactsGetStatuses(TLObject):
    CONSTRUCTOR_ID = 3299038190
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3299038190, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class ContactsGetContacts(TLObject):
    CONSTRUCTOR_ID = 1574346258
    __slots__ = ('hash')
    def __init__(self, hash: int):
        self.hash = hash
    def to_dict(self):
        return {"hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1574346258, signed=False)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_long()
        return cls(hash)

@register
class ContactsImportContacts(TLObject):
    CONSTRUCTOR_ID = 746589157
    __slots__ = ('contacts')
    def __init__(self, contacts: 'Vector'):
        self.contacts = contacts
    def to_dict(self):
        return {"contacts": self.contacts}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(746589157, signed=False)
        writer.write(bytes(self.contacts))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        contacts = reader.tgread_object()
        return cls(contacts)

@register
class ContactsDeleteContacts(TLObject):
    CONSTRUCTOR_ID = 157945344
    __slots__ = ('id')
    def __init__(self, id: 'Vector'):
        self.id = id
    def to_dict(self):
        return {"id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(157945344, signed=False)
        writer.write(bytes(self.id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        id = reader.tgread_object()
        return cls(id)

@register
class ContactsDeleteByPhones(TLObject):
    CONSTRUCTOR_ID = 269745566
    __slots__ = ('phones')
    def __init__(self, phones: 'Vector'):
        self.phones = phones
    def to_dict(self):
        return {"phones": self.phones}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(269745566, signed=False)
        writer.write(bytes(self.phones))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        phones = reader.tgread_object()
        return cls(phones)

@register
class ContactsBlock(TLObject):
    CONSTRUCTOR_ID = 774801204
    __slots__ = ('my_stories_from', 'id')
    def __init__(self, id: 'InputPeer', my_stories_from: bool = None):
        self.my_stories_from = my_stories_from
        self.id = id
    def to_dict(self):
        return {"my_stories_from": self.my_stories_from, "id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(774801204, signed=False)
        flags = 0
        if self.my_stories_from: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        my_stories_from = bool(flags & (1 << 0))
        id = reader.tgread_object()
        return cls(my_stories_from, id)

@register
class ContactsUnblock(TLObject):
    CONSTRUCTOR_ID = 3041973032
    __slots__ = ('my_stories_from', 'id')
    def __init__(self, id: 'InputPeer', my_stories_from: bool = None):
        self.my_stories_from = my_stories_from
        self.id = id
    def to_dict(self):
        return {"my_stories_from": self.my_stories_from, "id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3041973032, signed=False)
        flags = 0
        if self.my_stories_from: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        my_stories_from = bool(flags & (1 << 0))
        id = reader.tgread_object()
        return cls(my_stories_from, id)

@register
class ContactsGetBlocked(TLObject):
    CONSTRUCTOR_ID = 2592509824
    __slots__ = ('my_stories_from', 'offset', 'limit')
    def __init__(self, offset: int, limit: int, my_stories_from: bool = None):
        self.my_stories_from = my_stories_from
        self.offset = offset
        self.limit = limit
    def to_dict(self):
        return {"my_stories_from": self.my_stories_from, "offset": self.offset, "limit": self.limit}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2592509824, signed=False)
        flags = 0
        if self.my_stories_from: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write_int(self.offset, signed=True)
        writer.write_int(self.limit, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        my_stories_from = bool(flags & (1 << 0))
        offset = reader.read_int()
        limit = reader.read_int()
        return cls(my_stories_from, offset, limit)

@register
class ContactsSearch(TLObject):
    CONSTRUCTOR_ID = 301470424
    __slots__ = ('q', 'limit')
    def __init__(self, q: str, limit: int):
        self.q = q
        self.limit = limit
    def to_dict(self):
        return {"q": self.q, "limit": self.limit}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(301470424, signed=False)
        writer.write_string(self.q)
        writer.write_int(self.limit, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        q = reader.read_string()
        limit = reader.read_int()
        return cls(q, limit)

@register
class ContactsResolveUsername(TLObject):
    CONSTRUCTOR_ID = 1918565308
    __slots__ = ('username', 'referer')
    def __init__(self, username: str, referer: str = None):
        self.username = username
        self.referer = referer
    def to_dict(self):
        return {"username": self.username, "referer": self.referer}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1918565308, signed=False)
        flags = 0
        if self.referer is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write_string(self.username)
        if flags & (1 << 0):
            writer.write_string(self.referer)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        username = reader.read_string()
        if flags & (1 << 0):
            referer = reader.read_string()
        else:
            referer = None
        return cls(username, referer)

@register
class ContactsGetTopPeers(TLObject):
    CONSTRUCTOR_ID = 2536798390
    __slots__ = ('correspondents', 'bots_pm', 'bots_inline', 'phone_calls', 'forward_users', 'forward_chats', 'groups', 'channels', 'bots_app', 'bots_guestchat', 'offset', 'limit', 'hash')
    def __init__(self, offset: int, limit: int, hash: int, correspondents: bool = None, bots_pm: bool = None, bots_inline: bool = None, phone_calls: bool = None, forward_users: bool = None, forward_chats: bool = None, groups: bool = None, channels: bool = None, bots_app: bool = None, bots_guestchat: bool = None):
        self.correspondents = correspondents
        self.bots_pm = bots_pm
        self.bots_inline = bots_inline
        self.phone_calls = phone_calls
        self.forward_users = forward_users
        self.forward_chats = forward_chats
        self.groups = groups
        self.channels = channels
        self.bots_app = bots_app
        self.bots_guestchat = bots_guestchat
        self.offset = offset
        self.limit = limit
        self.hash = hash
    def to_dict(self):
        return {"correspondents": self.correspondents, "bots_pm": self.bots_pm, "bots_inline": self.bots_inline, "phone_calls": self.phone_calls, "forward_users": self.forward_users, "forward_chats": self.forward_chats, "groups": self.groups, "channels": self.channels, "bots_app": self.bots_app, "bots_guestchat": self.bots_guestchat, "offset": self.offset, "limit": self.limit, "hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2536798390, signed=False)
        flags = 0
        if self.correspondents: flags |= 1 << 0
        if self.bots_pm: flags |= 1 << 1
        if self.bots_inline: flags |= 1 << 2
        if self.phone_calls: flags |= 1 << 3
        if self.forward_users: flags |= 1 << 4
        if self.forward_chats: flags |= 1 << 5
        if self.groups: flags |= 1 << 10
        if self.channels: flags |= 1 << 15
        if self.bots_app: flags |= 1 << 16
        if self.bots_guestchat: flags |= 1 << 17
        writer.write_int(flags, signed=False)
        writer.write_int(self.offset, signed=True)
        writer.write_int(self.limit, signed=True)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        correspondents = bool(flags & (1 << 0))
        bots_pm = bool(flags & (1 << 1))
        bots_inline = bool(flags & (1 << 2))
        phone_calls = bool(flags & (1 << 3))
        forward_users = bool(flags & (1 << 4))
        forward_chats = bool(flags & (1 << 5))
        groups = bool(flags & (1 << 10))
        channels = bool(flags & (1 << 15))
        bots_app = bool(flags & (1 << 16))
        bots_guestchat = bool(flags & (1 << 17))
        offset = reader.read_int()
        limit = reader.read_int()
        hash = reader.read_long()
        return cls(correspondents, bots_pm, bots_inline, phone_calls, forward_users, forward_chats, groups, channels, bots_app, bots_guestchat, offset, limit, hash)

@register
class ContactsResetTopPeerRating(TLObject):
    CONSTRUCTOR_ID = 451113900
    __slots__ = ('category', 'peer')
    def __init__(self, category: 'TopPeerCategory', peer: 'InputPeer'):
        self.category = category
        self.peer = peer
    def to_dict(self):
        return {"category": self.category, "peer": self.peer}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(451113900, signed=False)
        writer.write(bytes(self.category))
        writer.write(bytes(self.peer))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        category = reader.tgread_object()
        peer = reader.tgread_object()
        return cls(category, peer)

@register
class ContactsResetSaved(TLObject):
    CONSTRUCTOR_ID = 2274703345
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2274703345, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class ContactsGetSaved(TLObject):
    CONSTRUCTOR_ID = 2196890527
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2196890527, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class ContactsToggleTopPeers(TLObject):
    CONSTRUCTOR_ID = 2232729050
    __slots__ = ('enabled')
    def __init__(self, enabled: bool):
        self.enabled = enabled
    def to_dict(self):
        return {"enabled": self.enabled}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2232729050, signed=False)
        writer.write(serialize_bool(self.enabled))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        enabled = reader.tgread_bool()
        return cls(enabled)

@register
class ContactsAddContact(TLObject):
    CONSTRUCTOR_ID = 3652857428
    __slots__ = ('add_phone_privacy_exception', 'id', 'first_name', 'last_name', 'phone', 'note')
    def __init__(self, id: 'InputUser', first_name: str, last_name: str, phone: str, add_phone_privacy_exception: bool = None, note: 'TextWithEntities' = None):
        self.add_phone_privacy_exception = add_phone_privacy_exception
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.note = note
    def to_dict(self):
        return {"add_phone_privacy_exception": self.add_phone_privacy_exception, "id": self.id, "first_name": self.first_name, "last_name": self.last_name, "phone": self.phone, "note": self.note}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3652857428, signed=False)
        flags = 0
        if self.add_phone_privacy_exception: flags |= 1 << 0
        if self.note is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.id))
        writer.write_string(self.first_name)
        writer.write_string(self.last_name)
        writer.write_string(self.phone)
        if flags & (1 << 1):
            writer.write(bytes(self.note))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        add_phone_privacy_exception = bool(flags & (1 << 0))
        id = reader.tgread_object()
        first_name = reader.read_string()
        last_name = reader.read_string()
        phone = reader.read_string()
        if flags & (1 << 1):
            note = reader.tgread_object()
        else:
            note = None
        return cls(add_phone_privacy_exception, id, first_name, last_name, phone, note)

@register
class ContactsAcceptContact(TLObject):
    CONSTRUCTOR_ID = 4164002319
    __slots__ = ('id')
    def __init__(self, id: 'InputUser'):
        self.id = id
    def to_dict(self):
        return {"id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4164002319, signed=False)
        writer.write(bytes(self.id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        id = reader.tgread_object()
        return cls(id)

@register
class ContactsGetLocated(TLObject):
    CONSTRUCTOR_ID = 3544759364
    __slots__ = ('background', 'geo_point', 'self_expires')
    def __init__(self, geo_point: 'InputGeoPoint', background: bool = None, self_expires: int = None):
        self.background = background
        self.geo_point = geo_point
        self.self_expires = self_expires
    def to_dict(self):
        return {"background": self.background, "geo_point": self.geo_point, "self_expires": self.self_expires}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3544759364, signed=False)
        flags = 0
        if self.background: flags |= 1 << 1
        if self.self_expires is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.geo_point))
        if flags & (1 << 0):
            writer.write_int(self.self_expires, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        background = bool(flags & (1 << 1))
        geo_point = reader.tgread_object()
        if flags & (1 << 0):
            self_expires = reader.read_int()
        else:
            self_expires = None
        return cls(background, geo_point, self_expires)

@register
class ContactsBlockFromReplies(TLObject):
    CONSTRUCTOR_ID = 698914348
    __slots__ = ('delete_message', 'delete_history', 'report_spam', 'msg_id')
    def __init__(self, msg_id: int, delete_message: bool = None, delete_history: bool = None, report_spam: bool = None):
        self.delete_message = delete_message
        self.delete_history = delete_history
        self.report_spam = report_spam
        self.msg_id = msg_id
    def to_dict(self):
        return {"delete_message": self.delete_message, "delete_history": self.delete_history, "report_spam": self.report_spam, "msg_id": self.msg_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(698914348, signed=False)
        flags = 0
        if self.delete_message: flags |= 1 << 0
        if self.delete_history: flags |= 1 << 1
        if self.report_spam: flags |= 1 << 2
        writer.write_int(flags, signed=False)
        writer.write_int(self.msg_id, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        delete_message = bool(flags & (1 << 0))
        delete_history = bool(flags & (1 << 1))
        report_spam = bool(flags & (1 << 2))
        msg_id = reader.read_int()
        return cls(delete_message, delete_history, report_spam, msg_id)

@register
class ContactsResolvePhone(TLObject):
    CONSTRUCTOR_ID = 2331591492
    __slots__ = ('phone')
    def __init__(self, phone: str):
        self.phone = phone
    def to_dict(self):
        return {"phone": self.phone}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2331591492, signed=False)
        writer.write_string(self.phone)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        phone = reader.read_string()
        return cls(phone)

@register
class ContactsExportContactToken(TLObject):
    CONSTRUCTOR_ID = 4167385127
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4167385127, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class ContactsImportContactToken(TLObject):
    CONSTRUCTOR_ID = 318789512
    __slots__ = ('token')
    def __init__(self, token: str):
        self.token = token
    def to_dict(self):
        return {"token": self.token}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(318789512, signed=False)
        writer.write_string(self.token)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        token = reader.read_string()
        return cls(token)

@register
class ContactsEditCloseFriends(TLObject):
    CONSTRUCTOR_ID = 3127313904
    __slots__ = ('id')
    def __init__(self, id: 'Vector'):
        self.id = id
    def to_dict(self):
        return {"id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3127313904, signed=False)
        writer.write(bytes(self.id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        id = reader.tgread_object()
        return cls(id)

@register
class ContactsSetBlocked(TLObject):
    CONSTRUCTOR_ID = 2496027766
    __slots__ = ('my_stories_from', 'id', 'limit')
    def __init__(self, id: 'Vector', limit: int, my_stories_from: bool = None):
        self.my_stories_from = my_stories_from
        self.id = id
        self.limit = limit
    def to_dict(self):
        return {"my_stories_from": self.my_stories_from, "id": self.id, "limit": self.limit}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2496027766, signed=False)
        flags = 0
        if self.my_stories_from: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.id))
        writer.write_int(self.limit, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        my_stories_from = bool(flags & (1 << 0))
        id = reader.tgread_object()
        limit = reader.read_int()
        return cls(my_stories_from, id, limit)

@register
class ContactsGetBirthdays(TLObject):
    CONSTRUCTOR_ID = 3673008228
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3673008228, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class ContactsGetSponsoredPeers(TLObject):
    CONSTRUCTOR_ID = 3066610579
    __slots__ = ('q')
    def __init__(self, q: str):
        self.q = q
    def to_dict(self):
        return {"q": self.q}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3066610579, signed=False)
        writer.write_string(self.q)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        q = reader.read_string()
        return cls(q)

@register
class ContactsUpdateContactNote(TLObject):
    CONSTRUCTOR_ID = 329212923
    __slots__ = ('id', 'note')
    def __init__(self, id: 'InputUser', note: 'TextWithEntities'):
        self.id = id
        self.note = note
    def to_dict(self):
        return {"id": self.id, "note": self.note}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(329212923, signed=False)
        writer.write(bytes(self.id))
        writer.write(bytes(self.note))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        id = reader.tgread_object()
        note = reader.tgread_object()
        return cls(id, note)

