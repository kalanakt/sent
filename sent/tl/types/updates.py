"""Auto-generated TL types. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional, TYPE_CHECKING
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

@register
class UpdatesState(TLObject):
    CONSTRUCTOR_ID = 2775329342
    __slots__ = ('pts', 'qts', 'date', 'seq', 'unread_count')
    def __init__(self, pts: int, qts: int, date: int, seq: int, unread_count: int):
        self.pts = pts
        self.qts = qts
        self.date = date
        self.seq = seq
        self.unread_count = unread_count
    def to_dict(self):
        return {"pts": self.pts, "qts": self.qts, "date": self.date, "seq": self.seq, "unread_count": self.unread_count}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2775329342, signed=False)
        writer.write_int(self.pts, signed=True)
        writer.write_int(self.qts, signed=True)
        writer.write_int(self.date, signed=True)
        writer.write_int(self.seq, signed=True)
        writer.write_int(self.unread_count, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        pts = reader.read_int()
        qts = reader.read_int()
        date = reader.read_int()
        seq = reader.read_int()
        unread_count = reader.read_int()
        return cls(pts, qts, date, seq, unread_count)

@register
class UpdatesDifferenceEmpty(TLObject):
    CONSTRUCTOR_ID = 1567990072
    __slots__ = ('date', 'seq')
    def __init__(self, date: int, seq: int):
        self.date = date
        self.seq = seq
    def to_dict(self):
        return {"date": self.date, "seq": self.seq}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1567990072, signed=False)
        writer.write_int(self.date, signed=True)
        writer.write_int(self.seq, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        date = reader.read_int()
        seq = reader.read_int()
        return cls(date, seq)

@register
class UpdatesDifference(TLObject):
    CONSTRUCTOR_ID = 16030880
    __slots__ = ('new_messages', 'new_encrypted_messages', 'other_updates', 'chats', 'users', 'state')
    def __init__(self, new_messages: 'Vector', new_encrypted_messages: 'Vector', other_updates: 'Vector', chats: 'Vector', users: 'Vector', state: 'UpdatesState'):
        self.new_messages = new_messages
        self.new_encrypted_messages = new_encrypted_messages
        self.other_updates = other_updates
        self.chats = chats
        self.users = users
        self.state = state
    def to_dict(self):
        return {"new_messages": self.new_messages, "new_encrypted_messages": self.new_encrypted_messages, "other_updates": self.other_updates, "chats": self.chats, "users": self.users, "state": self.state}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(16030880, signed=False)
        writer.write(bytes(self.new_messages))
        writer.write(bytes(self.new_encrypted_messages))
        writer.write(bytes(self.other_updates))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        writer.write(bytes(self.state))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        new_messages = reader.tgread_object()
        new_encrypted_messages = reader.tgread_object()
        other_updates = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        state = reader.tgread_object()
        return cls(new_messages, new_encrypted_messages, other_updates, chats, users, state)

@register
class UpdatesDifferenceSlice(TLObject):
    CONSTRUCTOR_ID = 2835028353
    __slots__ = ('new_messages', 'new_encrypted_messages', 'other_updates', 'chats', 'users', 'intermediate_state')
    def __init__(self, new_messages: 'Vector', new_encrypted_messages: 'Vector', other_updates: 'Vector', chats: 'Vector', users: 'Vector', intermediate_state: 'UpdatesState'):
        self.new_messages = new_messages
        self.new_encrypted_messages = new_encrypted_messages
        self.other_updates = other_updates
        self.chats = chats
        self.users = users
        self.intermediate_state = intermediate_state
    def to_dict(self):
        return {"new_messages": self.new_messages, "new_encrypted_messages": self.new_encrypted_messages, "other_updates": self.other_updates, "chats": self.chats, "users": self.users, "intermediate_state": self.intermediate_state}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2835028353, signed=False)
        writer.write(bytes(self.new_messages))
        writer.write(bytes(self.new_encrypted_messages))
        writer.write(bytes(self.other_updates))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        writer.write(bytes(self.intermediate_state))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        new_messages = reader.tgread_object()
        new_encrypted_messages = reader.tgread_object()
        other_updates = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        intermediate_state = reader.tgread_object()
        return cls(new_messages, new_encrypted_messages, other_updates, chats, users, intermediate_state)

@register
class UpdatesDifferenceTooLong(TLObject):
    CONSTRUCTOR_ID = 1258196845
    __slots__ = ('pts')
    def __init__(self, pts: int):
        self.pts = pts
    def to_dict(self):
        return {"pts": self.pts}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1258196845, signed=False)
        writer.write_int(self.pts, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        pts = reader.read_int()
        return cls(pts)

@register
class UpdatesChannelDifferenceEmpty(TLObject):
    CONSTRUCTOR_ID = 1041346555
    __slots__ = ('final', 'pts', 'timeout')
    def __init__(self, pts: int, final: bool = None, timeout: int = None):
        self.final = final
        self.pts = pts
        self.timeout = timeout
    def to_dict(self):
        return {"final": self.final, "pts": self.pts, "timeout": self.timeout}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1041346555, signed=False)
        flags = 0
        if self.final: flags |= 1 << 0
        if self.timeout is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write_int(self.pts, signed=True)
        if flags & (1 << 1):
            writer.write_int(self.timeout, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        final = bool(flags & (1 << 0))
        pts = reader.read_int()
        if flags & (1 << 1):
            timeout = reader.read_int()
        else:
            timeout = None
        return cls(final, pts, timeout)

@register
class UpdatesChannelDifferenceTooLong(TLObject):
    CONSTRUCTOR_ID = 2763835134
    __slots__ = ('final', 'timeout', 'dialog', 'messages', 'chats', 'users')
    def __init__(self, dialog: 'Dialog', messages: 'Vector', chats: 'Vector', users: 'Vector', final: bool = None, timeout: int = None):
        self.final = final
        self.timeout = timeout
        self.dialog = dialog
        self.messages = messages
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"final": self.final, "timeout": self.timeout, "dialog": self.dialog, "messages": self.messages, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2763835134, signed=False)
        flags = 0
        if self.final: flags |= 1 << 0
        if self.timeout is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        if flags & (1 << 1):
            writer.write_int(self.timeout, signed=True)
        writer.write(bytes(self.dialog))
        writer.write(bytes(self.messages))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        final = bool(flags & (1 << 0))
        if flags & (1 << 1):
            timeout = reader.read_int()
        else:
            timeout = None
        dialog = reader.tgread_object()
        messages = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(final, timeout, dialog, messages, chats, users)

@register
class UpdatesChannelDifference(TLObject):
    CONSTRUCTOR_ID = 543450958
    __slots__ = ('final', 'pts', 'timeout', 'new_messages', 'other_updates', 'chats', 'users')
    def __init__(self, pts: int, new_messages: 'Vector', other_updates: 'Vector', chats: 'Vector', users: 'Vector', final: bool = None, timeout: int = None):
        self.final = final
        self.pts = pts
        self.timeout = timeout
        self.new_messages = new_messages
        self.other_updates = other_updates
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"final": self.final, "pts": self.pts, "timeout": self.timeout, "new_messages": self.new_messages, "other_updates": self.other_updates, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(543450958, signed=False)
        flags = 0
        if self.final: flags |= 1 << 0
        if self.timeout is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write_int(self.pts, signed=True)
        if flags & (1 << 1):
            writer.write_int(self.timeout, signed=True)
        writer.write(bytes(self.new_messages))
        writer.write(bytes(self.other_updates))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        final = bool(flags & (1 << 0))
        pts = reader.read_int()
        if flags & (1 << 1):
            timeout = reader.read_int()
        else:
            timeout = None
        new_messages = reader.tgread_object()
        other_updates = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(final, pts, timeout, new_messages, other_updates, chats, users)

