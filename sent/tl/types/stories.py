"""Auto-generated TL types. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional, TYPE_CHECKING
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

@register
class StoriesAllStoriesNotModified(TLObject):
    CONSTRUCTOR_ID = 291044926
    __slots__ = ('state', 'stealth_mode')
    def __init__(self, state: str, stealth_mode: 'StoriesStealthMode'):
        self.state = state
        self.stealth_mode = stealth_mode
    def to_dict(self):
        return {"state": self.state, "stealth_mode": self.stealth_mode}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(291044926, signed=False)
        flags = 0
        writer.write_int(flags, signed=False)
        writer.write_string(self.state)
        writer.write(bytes(self.stealth_mode))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        state = reader.read_string()
        stealth_mode = reader.tgread_object()
        return cls(state, stealth_mode)

@register
class StoriesAllStories(TLObject):
    CONSTRUCTOR_ID = 1862033025
    __slots__ = ('has_more', 'count', 'state', 'peer_stories', 'chats', 'users', 'stealth_mode')
    def __init__(self, count: int, state: str, peer_stories: 'Vector', chats: 'Vector', users: 'Vector', stealth_mode: 'StoriesStealthMode', has_more: bool = None):
        self.has_more = has_more
        self.count = count
        self.state = state
        self.peer_stories = peer_stories
        self.chats = chats
        self.users = users
        self.stealth_mode = stealth_mode
    def to_dict(self):
        return {"has_more": self.has_more, "count": self.count, "state": self.state, "peer_stories": self.peer_stories, "chats": self.chats, "users": self.users, "stealth_mode": self.stealth_mode}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1862033025, signed=False)
        flags = 0
        if self.has_more: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write_int(self.count, signed=True)
        writer.write_string(self.state)
        writer.write(bytes(self.peer_stories))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        writer.write(bytes(self.stealth_mode))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        has_more = bool(flags & (1 << 0))
        count = reader.read_int()
        state = reader.read_string()
        peer_stories = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        stealth_mode = reader.tgread_object()
        return cls(has_more, count, state, peer_stories, chats, users, stealth_mode)

@register
class StoriesStories(TLObject):
    CONSTRUCTOR_ID = 1673780490
    __slots__ = ('count', 'stories', 'pinned_to_top', 'chats', 'users')
    def __init__(self, count: int, stories: 'Vector', chats: 'Vector', users: 'Vector', pinned_to_top: 'Vector' = None):
        self.count = count
        self.stories = stories
        self.pinned_to_top = pinned_to_top
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"count": self.count, "stories": self.stories, "pinned_to_top": self.pinned_to_top, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1673780490, signed=False)
        flags = 0
        if self.pinned_to_top is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write_int(self.count, signed=True)
        writer.write(bytes(self.stories))
        if flags & (1 << 0):
            writer.write(bytes(self.pinned_to_top))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        count = reader.read_int()
        stories = reader.tgread_object()
        if flags & (1 << 0):
            pinned_to_top = reader.tgread_object()
        else:
            pinned_to_top = None
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(count, stories, pinned_to_top, chats, users)

@register
class StoriesStoryViewsList(TLObject):
    CONSTRUCTOR_ID = 1507299269
    __slots__ = ('count', 'views_count', 'forwards_count', 'reactions_count', 'views', 'chats', 'users', 'next_offset')
    def __init__(self, count: int, views_count: int, forwards_count: int, reactions_count: int, views: 'Vector', chats: 'Vector', users: 'Vector', next_offset: str = None):
        self.count = count
        self.views_count = views_count
        self.forwards_count = forwards_count
        self.reactions_count = reactions_count
        self.views = views
        self.chats = chats
        self.users = users
        self.next_offset = next_offset
    def to_dict(self):
        return {"count": self.count, "views_count": self.views_count, "forwards_count": self.forwards_count, "reactions_count": self.reactions_count, "views": self.views, "chats": self.chats, "users": self.users, "next_offset": self.next_offset}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1507299269, signed=False)
        flags = 0
        if self.next_offset is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write_int(self.count, signed=True)
        writer.write_int(self.views_count, signed=True)
        writer.write_int(self.forwards_count, signed=True)
        writer.write_int(self.reactions_count, signed=True)
        writer.write(bytes(self.views))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        if flags & (1 << 0):
            writer.write_string(self.next_offset)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        count = reader.read_int()
        views_count = reader.read_int()
        forwards_count = reader.read_int()
        reactions_count = reader.read_int()
        views = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        if flags & (1 << 0):
            next_offset = reader.read_string()
        else:
            next_offset = None
        return cls(count, views_count, forwards_count, reactions_count, views, chats, users, next_offset)

@register
class StoriesStoryViews(TLObject):
    CONSTRUCTOR_ID = 3734957341
    __slots__ = ('views', 'users')
    def __init__(self, views: 'Vector', users: 'Vector'):
        self.views = views
        self.users = users
    def to_dict(self):
        return {"views": self.views, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3734957341, signed=False)
        writer.write(bytes(self.views))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        views = reader.tgread_object()
        users = reader.tgread_object()
        return cls(views, users)

@register
class StoriesPeerStories(TLObject):
    CONSTRUCTOR_ID = 3404105576
    __slots__ = ('stories', 'chats', 'users')
    def __init__(self, stories: 'PeerStories', chats: 'Vector', users: 'Vector'):
        self.stories = stories
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"stories": self.stories, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3404105576, signed=False)
        writer.write(bytes(self.stories))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        stories = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(stories, chats, users)

@register
class StoriesStoryReactionsList(TLObject):
    CONSTRUCTOR_ID = 2858383516
    __slots__ = ('count', 'reactions', 'chats', 'users', 'next_offset')
    def __init__(self, count: int, reactions: 'Vector', chats: 'Vector', users: 'Vector', next_offset: str = None):
        self.count = count
        self.reactions = reactions
        self.chats = chats
        self.users = users
        self.next_offset = next_offset
    def to_dict(self):
        return {"count": self.count, "reactions": self.reactions, "chats": self.chats, "users": self.users, "next_offset": self.next_offset}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2858383516, signed=False)
        flags = 0
        if self.next_offset is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write_int(self.count, signed=True)
        writer.write(bytes(self.reactions))
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        if flags & (1 << 0):
            writer.write_string(self.next_offset)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        count = reader.read_int()
        reactions = reader.tgread_object()
        chats = reader.tgread_object()
        users = reader.tgread_object()
        if flags & (1 << 0):
            next_offset = reader.read_string()
        else:
            next_offset = None
        return cls(count, reactions, chats, users, next_offset)

@register
class StoriesFoundStories(TLObject):
    CONSTRUCTOR_ID = 3806230327
    __slots__ = ('count', 'stories', 'next_offset', 'chats', 'users')
    def __init__(self, count: int, stories: 'Vector', chats: 'Vector', users: 'Vector', next_offset: str = None):
        self.count = count
        self.stories = stories
        self.next_offset = next_offset
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"count": self.count, "stories": self.stories, "next_offset": self.next_offset, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3806230327, signed=False)
        flags = 0
        if self.next_offset is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write_int(self.count, signed=True)
        writer.write(bytes(self.stories))
        if flags & (1 << 0):
            writer.write_string(self.next_offset)
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        count = reader.read_int()
        stories = reader.tgread_object()
        if flags & (1 << 0):
            next_offset = reader.read_string()
        else:
            next_offset = None
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(count, stories, next_offset, chats, users)

@register
class StoriesCanSendStoryCount(TLObject):
    CONSTRUCTOR_ID = 3280453710
    __slots__ = ('count_remains')
    def __init__(self, count_remains: int):
        self.count_remains = count_remains
    def to_dict(self):
        return {"count_remains": self.count_remains}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3280453710, signed=False)
        writer.write_int(self.count_remains, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        count_remains = reader.read_int()
        return cls(count_remains)

@register
class StoriesAlbumsNotModified(TLObject):
    CONSTRUCTOR_ID = 1448008427
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1448008427, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class StoriesAlbums(TLObject):
    CONSTRUCTOR_ID = 3281549882
    __slots__ = ('hash', 'albums')
    def __init__(self, hash: int, albums: 'Vector'):
        self.hash = hash
        self.albums = albums
    def to_dict(self):
        return {"hash": self.hash, "albums": self.albums}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3281549882, signed=False)
        writer.write_long(self.hash, signed=False)
        writer.write(bytes(self.albums))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_long()
        albums = reader.tgread_object()
        return cls(hash, albums)

