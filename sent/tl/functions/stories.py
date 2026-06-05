"""Auto-generated TL functions. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

@register
class StoriesCanSendStory(TLObject):
    CONSTRUCTOR_ID = 820732912
    __slots__ = ('peer')
    def __init__(self, peer: 'InputPeer'):
        self.peer = peer
    def to_dict(self):
        return {"peer": self.peer}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(820732912, signed=False)
        writer.write(bytes(self.peer))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        return cls(peer)

@register
class StoriesSendStory(TLObject):
    CONSTRUCTOR_ID = 2409523352
    __slots__ = ('pinned', 'noforwards', 'fwd_modified', 'peer', 'media', 'media_areas', 'caption', 'entities', 'privacy_rules', 'random_id', 'period', 'fwd_from_id', 'fwd_from_story', 'albums', 'music')
    def __init__(self, peer: 'InputPeer', media: 'InputMedia', privacy_rules: 'Vector', random_id: int, pinned: bool = None, noforwards: bool = None, fwd_modified: bool = None, media_areas: 'Vector' = None, caption: str = None, entities: 'Vector' = None, period: int = None, fwd_from_id: 'InputPeer' = None, fwd_from_story: int = None, albums: 'Vector' = None, music: 'InputDocument' = None):
        self.pinned = pinned
        self.noforwards = noforwards
        self.fwd_modified = fwd_modified
        self.peer = peer
        self.media = media
        self.media_areas = media_areas
        self.caption = caption
        self.entities = entities
        self.privacy_rules = privacy_rules
        self.random_id = random_id
        self.period = period
        self.fwd_from_id = fwd_from_id
        self.fwd_from_story = fwd_from_story
        self.albums = albums
        self.music = music
    def to_dict(self):
        return {"pinned": self.pinned, "noforwards": self.noforwards, "fwd_modified": self.fwd_modified, "peer": self.peer, "media": self.media, "media_areas": self.media_areas, "caption": self.caption, "entities": self.entities, "privacy_rules": self.privacy_rules, "random_id": self.random_id, "period": self.period, "fwd_from_id": self.fwd_from_id, "fwd_from_story": self.fwd_from_story, "albums": self.albums, "music": self.music}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2409523352, signed=False)
        flags = 0
        if self.pinned: flags |= 1 << 2
        if self.noforwards: flags |= 1 << 4
        if self.fwd_modified: flags |= 1 << 7
        if self.media_areas is not None: flags |= 1 << 5
        if self.caption is not None: flags |= 1 << 0
        if self.entities is not None: flags |= 1 << 1
        if self.period is not None: flags |= 1 << 3
        if self.fwd_from_id is not None: flags |= 1 << 6
        if self.fwd_from_story is not None: flags |= 1 << 6
        if self.albums is not None: flags |= 1 << 8
        if self.music is not None: flags |= 1 << 9
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.media))
        if flags & (1 << 5):
            writer.write(bytes(self.media_areas))
        if flags & (1 << 0):
            writer.write_string(self.caption)
        if flags & (1 << 1):
            writer.write(bytes(self.entities))
        writer.write(bytes(self.privacy_rules))
        writer.write_long(self.random_id, signed=False)
        if flags & (1 << 3):
            writer.write_int(self.period, signed=True)
        if flags & (1 << 6):
            writer.write(bytes(self.fwd_from_id))
        if flags & (1 << 6):
            writer.write_int(self.fwd_from_story, signed=True)
        if flags & (1 << 8):
            writer.write(bytes(self.albums))
        if flags & (1 << 9):
            writer.write(bytes(self.music))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        pinned = bool(flags & (1 << 2))
        noforwards = bool(flags & (1 << 4))
        fwd_modified = bool(flags & (1 << 7))
        peer = reader.tgread_object()
        media = reader.tgread_object()
        if flags & (1 << 5):
            media_areas = reader.tgread_object()
        else:
            media_areas = None
        if flags & (1 << 0):
            caption = reader.read_string()
        else:
            caption = None
        if flags & (1 << 1):
            entities = reader.tgread_object()
        else:
            entities = None
        privacy_rules = reader.tgread_object()
        random_id = reader.read_long()
        if flags & (1 << 3):
            period = reader.read_int()
        else:
            period = None
        if flags & (1 << 6):
            fwd_from_id = reader.tgread_object()
        else:
            fwd_from_id = None
        if flags & (1 << 6):
            fwd_from_story = reader.read_int()
        else:
            fwd_from_story = None
        if flags & (1 << 8):
            albums = reader.tgread_object()
        else:
            albums = None
        if flags & (1 << 9):
            music = reader.tgread_object()
        else:
            music = None
        return cls(pinned, noforwards, fwd_modified, peer, media, media_areas, caption, entities, privacy_rules, random_id, period, fwd_from_id, fwd_from_story, albums, music)

@register
class StoriesEditStory(TLObject):
    CONSTRUCTOR_ID = 744728363
    __slots__ = ('peer', 'id', 'media', 'media_areas', 'caption', 'entities', 'privacy_rules', 'music')
    def __init__(self, peer: 'InputPeer', id: int, media: 'InputMedia' = None, media_areas: 'Vector' = None, caption: str = None, entities: 'Vector' = None, privacy_rules: 'Vector' = None, music: 'InputDocument' = None):
        self.peer = peer
        self.id = id
        self.media = media
        self.media_areas = media_areas
        self.caption = caption
        self.entities = entities
        self.privacy_rules = privacy_rules
        self.music = music
    def to_dict(self):
        return {"peer": self.peer, "id": self.id, "media": self.media, "media_areas": self.media_areas, "caption": self.caption, "entities": self.entities, "privacy_rules": self.privacy_rules, "music": self.music}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(744728363, signed=False)
        flags = 0
        if self.media is not None: flags |= 1 << 0
        if self.media_areas is not None: flags |= 1 << 3
        if self.caption is not None: flags |= 1 << 1
        if self.entities is not None: flags |= 1 << 1
        if self.privacy_rules is not None: flags |= 1 << 2
        if self.music is not None: flags |= 1 << 4
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.id, signed=True)
        if flags & (1 << 0):
            writer.write(bytes(self.media))
        if flags & (1 << 3):
            writer.write(bytes(self.media_areas))
        if flags & (1 << 1):
            writer.write_string(self.caption)
        if flags & (1 << 1):
            writer.write(bytes(self.entities))
        if flags & (1 << 2):
            writer.write(bytes(self.privacy_rules))
        if flags & (1 << 4):
            writer.write(bytes(self.music))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        peer = reader.tgread_object()
        id = reader.read_int()
        if flags & (1 << 0):
            media = reader.tgread_object()
        else:
            media = None
        if flags & (1 << 3):
            media_areas = reader.tgread_object()
        else:
            media_areas = None
        if flags & (1 << 1):
            caption = reader.read_string()
        else:
            caption = None
        if flags & (1 << 1):
            entities = reader.tgread_object()
        else:
            entities = None
        if flags & (1 << 2):
            privacy_rules = reader.tgread_object()
        else:
            privacy_rules = None
        if flags & (1 << 4):
            music = reader.tgread_object()
        else:
            music = None
        return cls(peer, id, media, media_areas, caption, entities, privacy_rules, music)

@register
class StoriesDeleteStories(TLObject):
    CONSTRUCTOR_ID = 2925124447
    __slots__ = ('peer', 'id')
    def __init__(self, peer: 'InputPeer', id: 'Vector'):
        self.peer = peer
        self.id = id
    def to_dict(self):
        return {"peer": self.peer, "id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2925124447, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        id = reader.tgread_object()
        return cls(peer, id)

@register
class StoriesTogglePinned(TLObject):
    CONSTRUCTOR_ID = 2591400431
    __slots__ = ('peer', 'id', 'pinned')
    def __init__(self, peer: 'InputPeer', id: 'Vector', pinned: bool):
        self.peer = peer
        self.id = id
        self.pinned = pinned
    def to_dict(self):
        return {"peer": self.peer, "id": self.id, "pinned": self.pinned}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2591400431, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.id))
        writer.write(serialize_bool(self.pinned))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        id = reader.tgread_object()
        pinned = reader.tgread_bool()
        return cls(peer, id, pinned)

@register
class StoriesGetAllStories(TLObject):
    CONSTRUCTOR_ID = 4004566565
    __slots__ = ('next', 'hidden', 'state')
    def __init__(self, next: bool = None, hidden: bool = None, state: str = None):
        self.next = next
        self.hidden = hidden
        self.state = state
    def to_dict(self):
        return {"next": self.next, "hidden": self.hidden, "state": self.state}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4004566565, signed=False)
        flags = 0
        if self.next: flags |= 1 << 1
        if self.hidden: flags |= 1 << 2
        if self.state is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        if flags & (1 << 0):
            writer.write_string(self.state)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        next = bool(flags & (1 << 1))
        hidden = bool(flags & (1 << 2))
        if flags & (1 << 0):
            state = reader.read_string()
        else:
            state = None
        return cls(next, hidden, state)

@register
class StoriesGetPinnedStories(TLObject):
    CONSTRUCTOR_ID = 1478600156
    __slots__ = ('peer', 'offset_id', 'limit')
    def __init__(self, peer: 'InputPeer', offset_id: int, limit: int):
        self.peer = peer
        self.offset_id = offset_id
        self.limit = limit
    def to_dict(self):
        return {"peer": self.peer, "offset_id": self.offset_id, "limit": self.limit}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1478600156, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.offset_id, signed=True)
        writer.write_int(self.limit, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        offset_id = reader.read_int()
        limit = reader.read_int()
        return cls(peer, offset_id, limit)

@register
class StoriesGetStoriesArchive(TLObject):
    CONSTRUCTOR_ID = 3023380502
    __slots__ = ('peer', 'offset_id', 'limit')
    def __init__(self, peer: 'InputPeer', offset_id: int, limit: int):
        self.peer = peer
        self.offset_id = offset_id
        self.limit = limit
    def to_dict(self):
        return {"peer": self.peer, "offset_id": self.offset_id, "limit": self.limit}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3023380502, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.offset_id, signed=True)
        writer.write_int(self.limit, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        offset_id = reader.read_int()
        limit = reader.read_int()
        return cls(peer, offset_id, limit)

@register
class StoriesGetStoriesByID(TLObject):
    CONSTRUCTOR_ID = 1467271796
    __slots__ = ('peer', 'id')
    def __init__(self, peer: 'InputPeer', id: 'Vector'):
        self.peer = peer
        self.id = id
    def to_dict(self):
        return {"peer": self.peer, "id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1467271796, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        id = reader.tgread_object()
        return cls(peer, id)

@register
class StoriesToggleAllStoriesHidden(TLObject):
    CONSTRUCTOR_ID = 2082822084
    __slots__ = ('hidden')
    def __init__(self, hidden: bool):
        self.hidden = hidden
    def to_dict(self):
        return {"hidden": self.hidden}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2082822084, signed=False)
        writer.write(serialize_bool(self.hidden))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hidden = reader.tgread_bool()
        return cls(hidden)

@register
class StoriesReadStories(TLObject):
    CONSTRUCTOR_ID = 2773932744
    __slots__ = ('peer', 'max_id')
    def __init__(self, peer: 'InputPeer', max_id: int):
        self.peer = peer
        self.max_id = max_id
    def to_dict(self):
        return {"peer": self.peer, "max_id": self.max_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2773932744, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.max_id, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        max_id = reader.read_int()
        return cls(peer, max_id)

@register
class StoriesIncrementStoryViews(TLObject):
    CONSTRUCTOR_ID = 2986511099
    __slots__ = ('peer', 'id')
    def __init__(self, peer: 'InputPeer', id: 'Vector'):
        self.peer = peer
        self.id = id
    def to_dict(self):
        return {"peer": self.peer, "id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2986511099, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        id = reader.tgread_object()
        return cls(peer, id)

@register
class StoriesGetStoryViewsList(TLObject):
    CONSTRUCTOR_ID = 2127707223
    __slots__ = ('just_contacts', 'reactions_first', 'forwards_first', 'peer', 'q', 'id', 'offset', 'limit')
    def __init__(self, peer: 'InputPeer', id: int, offset: str, limit: int, just_contacts: bool = None, reactions_first: bool = None, forwards_first: bool = None, q: str = None):
        self.just_contacts = just_contacts
        self.reactions_first = reactions_first
        self.forwards_first = forwards_first
        self.peer = peer
        self.q = q
        self.id = id
        self.offset = offset
        self.limit = limit
    def to_dict(self):
        return {"just_contacts": self.just_contacts, "reactions_first": self.reactions_first, "forwards_first": self.forwards_first, "peer": self.peer, "q": self.q, "id": self.id, "offset": self.offset, "limit": self.limit}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2127707223, signed=False)
        flags = 0
        if self.just_contacts: flags |= 1 << 0
        if self.reactions_first: flags |= 1 << 2
        if self.forwards_first: flags |= 1 << 3
        if self.q is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        if flags & (1 << 1):
            writer.write_string(self.q)
        writer.write_int(self.id, signed=True)
        writer.write_string(self.offset)
        writer.write_int(self.limit, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        just_contacts = bool(flags & (1 << 0))
        reactions_first = bool(flags & (1 << 2))
        forwards_first = bool(flags & (1 << 3))
        peer = reader.tgread_object()
        if flags & (1 << 1):
            q = reader.read_string()
        else:
            q = None
        id = reader.read_int()
        offset = reader.read_string()
        limit = reader.read_int()
        return cls(just_contacts, reactions_first, forwards_first, peer, q, id, offset, limit)

@register
class StoriesGetStoriesViews(TLObject):
    CONSTRUCTOR_ID = 685862088
    __slots__ = ('peer', 'id')
    def __init__(self, peer: 'InputPeer', id: 'Vector'):
        self.peer = peer
        self.id = id
    def to_dict(self):
        return {"peer": self.peer, "id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(685862088, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        id = reader.tgread_object()
        return cls(peer, id)

@register
class StoriesExportStoryLink(TLObject):
    CONSTRUCTOR_ID = 2072899360
    __slots__ = ('peer', 'id')
    def __init__(self, peer: 'InputPeer', id: int):
        self.peer = peer
        self.id = id
    def to_dict(self):
        return {"peer": self.peer, "id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2072899360, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.id, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        id = reader.read_int()
        return cls(peer, id)

@register
class StoriesReport(TLObject):
    CONSTRUCTOR_ID = 433646405
    __slots__ = ('peer', 'id', 'option', 'message')
    def __init__(self, peer: 'InputPeer', id: 'Vector', option: bytes, message: str):
        self.peer = peer
        self.id = id
        self.option = option
        self.message = message
    def to_dict(self):
        return {"peer": self.peer, "id": self.id, "option": self.option, "message": self.message}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(433646405, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.id))
        writer.write_bytes(self.option)
        writer.write_string(self.message)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        id = reader.tgread_object()
        option = reader.read_bytes()
        message = reader.read_string()
        return cls(peer, id, option, message)

@register
class StoriesActivateStealthMode(TLObject):
    CONSTRUCTOR_ID = 1471926630
    __slots__ = ('past', 'future')
    def __init__(self, past: bool = None, future: bool = None):
        self.past = past
        self.future = future
    def to_dict(self):
        return {"past": self.past, "future": self.future}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1471926630, signed=False)
        flags = 0
        if self.past: flags |= 1 << 0
        if self.future: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        past = bool(flags & (1 << 0))
        future = bool(flags & (1 << 1))
        return cls(past, future)

@register
class StoriesSendReaction(TLObject):
    CONSTRUCTOR_ID = 2144810674
    __slots__ = ('add_to_recent', 'peer', 'story_id', 'reaction')
    def __init__(self, peer: 'InputPeer', story_id: int, reaction: 'Reaction', add_to_recent: bool = None):
        self.add_to_recent = add_to_recent
        self.peer = peer
        self.story_id = story_id
        self.reaction = reaction
    def to_dict(self):
        return {"add_to_recent": self.add_to_recent, "peer": self.peer, "story_id": self.story_id, "reaction": self.reaction}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2144810674, signed=False)
        flags = 0
        if self.add_to_recent: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.story_id, signed=True)
        writer.write(bytes(self.reaction))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        add_to_recent = bool(flags & (1 << 0))
        peer = reader.tgread_object()
        story_id = reader.read_int()
        reaction = reader.tgread_object()
        return cls(add_to_recent, peer, story_id, reaction)

@register
class StoriesGetPeerStories(TLObject):
    CONSTRUCTOR_ID = 743103056
    __slots__ = ('peer')
    def __init__(self, peer: 'InputPeer'):
        self.peer = peer
    def to_dict(self):
        return {"peer": self.peer}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(743103056, signed=False)
        writer.write(bytes(self.peer))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        return cls(peer)

@register
class StoriesGetAllReadPeerStories(TLObject):
    CONSTRUCTOR_ID = 2606426105
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2606426105, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class StoriesGetPeerMaxIDs(TLObject):
    CONSTRUCTOR_ID = 2018087280
    __slots__ = ('id')
    def __init__(self, id: 'Vector'):
        self.id = id
    def to_dict(self):
        return {"id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2018087280, signed=False)
        writer.write(bytes(self.id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        id = reader.tgread_object()
        return cls(id)

@register
class StoriesGetChatsToSend(TLObject):
    CONSTRUCTOR_ID = 2775223136
    __slots__ = ()
    def __init__(self):
        pass
    def to_dict(self):
        return {}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2775223136, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        return cls()

@register
class StoriesTogglePeerStoriesHidden(TLObject):
    CONSTRUCTOR_ID = 3171161540
    __slots__ = ('peer', 'hidden')
    def __init__(self, peer: 'InputPeer', hidden: bool):
        self.peer = peer
        self.hidden = hidden
    def to_dict(self):
        return {"peer": self.peer, "hidden": self.hidden}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3171161540, signed=False)
        writer.write(bytes(self.peer))
        writer.write(serialize_bool(self.hidden))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        hidden = reader.tgread_bool()
        return cls(peer, hidden)

@register
class StoriesGetStoryReactionsList(TLObject):
    CONSTRUCTOR_ID = 3115485215
    __slots__ = ('forwards_first', 'peer', 'id', 'reaction', 'offset', 'limit')
    def __init__(self, peer: 'InputPeer', id: int, limit: int, forwards_first: bool = None, reaction: 'Reaction' = None, offset: str = None):
        self.forwards_first = forwards_first
        self.peer = peer
        self.id = id
        self.reaction = reaction
        self.offset = offset
        self.limit = limit
    def to_dict(self):
        return {"forwards_first": self.forwards_first, "peer": self.peer, "id": self.id, "reaction": self.reaction, "offset": self.offset, "limit": self.limit}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3115485215, signed=False)
        flags = 0
        if self.forwards_first: flags |= 1 << 2
        if self.reaction is not None: flags |= 1 << 0
        if self.offset is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.id, signed=True)
        if flags & (1 << 0):
            writer.write(bytes(self.reaction))
        if flags & (1 << 1):
            writer.write_string(self.offset)
        writer.write_int(self.limit, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        forwards_first = bool(flags & (1 << 2))
        peer = reader.tgread_object()
        id = reader.read_int()
        if flags & (1 << 0):
            reaction = reader.tgread_object()
        else:
            reaction = None
        if flags & (1 << 1):
            offset = reader.read_string()
        else:
            offset = None
        limit = reader.read_int()
        return cls(forwards_first, peer, id, reaction, offset, limit)

@register
class StoriesTogglePinnedToTop(TLObject):
    CONSTRUCTOR_ID = 187268763
    __slots__ = ('peer', 'id')
    def __init__(self, peer: 'InputPeer', id: 'Vector'):
        self.peer = peer
        self.id = id
    def to_dict(self):
        return {"peer": self.peer, "id": self.id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(187268763, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.id))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        id = reader.tgread_object()
        return cls(peer, id)

@register
class StoriesSearchPosts(TLObject):
    CONSTRUCTOR_ID = 3514894599
    __slots__ = ('hashtag', 'area', 'peer', 'offset', 'limit')
    def __init__(self, offset: str, limit: int, hashtag: str = None, area: 'MediaArea' = None, peer: 'InputPeer' = None):
        self.hashtag = hashtag
        self.area = area
        self.peer = peer
        self.offset = offset
        self.limit = limit
    def to_dict(self):
        return {"hashtag": self.hashtag, "area": self.area, "peer": self.peer, "offset": self.offset, "limit": self.limit}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3514894599, signed=False)
        flags = 0
        if self.hashtag is not None: flags |= 1 << 0
        if self.area is not None: flags |= 1 << 1
        if self.peer is not None: flags |= 1 << 2
        writer.write_int(flags, signed=False)
        if flags & (1 << 0):
            writer.write_string(self.hashtag)
        if flags & (1 << 1):
            writer.write(bytes(self.area))
        if flags & (1 << 2):
            writer.write(bytes(self.peer))
        writer.write_string(self.offset)
        writer.write_int(self.limit, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        if flags & (1 << 0):
            hashtag = reader.read_string()
        else:
            hashtag = None
        if flags & (1 << 1):
            area = reader.tgread_object()
        else:
            area = None
        if flags & (1 << 2):
            peer = reader.tgread_object()
        else:
            peer = None
        offset = reader.read_string()
        limit = reader.read_int()
        return cls(hashtag, area, peer, offset, limit)

@register
class StoriesCreateAlbum(TLObject):
    CONSTRUCTOR_ID = 2741212901
    __slots__ = ('peer', 'title', 'stories')
    def __init__(self, peer: 'InputPeer', title: str, stories: 'Vector'):
        self.peer = peer
        self.title = title
        self.stories = stories
    def to_dict(self):
        return {"peer": self.peer, "title": self.title, "stories": self.stories}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2741212901, signed=False)
        writer.write(bytes(self.peer))
        writer.write_string(self.title)
        writer.write(bytes(self.stories))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        title = reader.read_string()
        stories = reader.tgread_object()
        return cls(peer, title, stories)

@register
class StoriesUpdateAlbum(TLObject):
    CONSTRUCTOR_ID = 1582455222
    __slots__ = ('peer', 'album_id', 'title', 'delete_stories', 'add_stories', 'order')
    def __init__(self, peer: 'InputPeer', album_id: int, title: str = None, delete_stories: 'Vector' = None, add_stories: 'Vector' = None, order: 'Vector' = None):
        self.peer = peer
        self.album_id = album_id
        self.title = title
        self.delete_stories = delete_stories
        self.add_stories = add_stories
        self.order = order
    def to_dict(self):
        return {"peer": self.peer, "album_id": self.album_id, "title": self.title, "delete_stories": self.delete_stories, "add_stories": self.add_stories, "order": self.order}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1582455222, signed=False)
        flags = 0
        if self.title is not None: flags |= 1 << 0
        if self.delete_stories is not None: flags |= 1 << 1
        if self.add_stories is not None: flags |= 1 << 2
        if self.order is not None: flags |= 1 << 3
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.album_id, signed=True)
        if flags & (1 << 0):
            writer.write_string(self.title)
        if flags & (1 << 1):
            writer.write(bytes(self.delete_stories))
        if flags & (1 << 2):
            writer.write(bytes(self.add_stories))
        if flags & (1 << 3):
            writer.write(bytes(self.order))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        peer = reader.tgread_object()
        album_id = reader.read_int()
        if flags & (1 << 0):
            title = reader.read_string()
        else:
            title = None
        if flags & (1 << 1):
            delete_stories = reader.tgread_object()
        else:
            delete_stories = None
        if flags & (1 << 2):
            add_stories = reader.tgread_object()
        else:
            add_stories = None
        if flags & (1 << 3):
            order = reader.tgread_object()
        else:
            order = None
        return cls(peer, album_id, title, delete_stories, add_stories, order)

@register
class StoriesReorderAlbums(TLObject):
    CONSTRUCTOR_ID = 2234907609
    __slots__ = ('peer', 'order')
    def __init__(self, peer: 'InputPeer', order: 'Vector'):
        self.peer = peer
        self.order = order
    def to_dict(self):
        return {"peer": self.peer, "order": self.order}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2234907609, signed=False)
        writer.write(bytes(self.peer))
        writer.write(bytes(self.order))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        order = reader.tgread_object()
        return cls(peer, order)

@register
class StoriesDeleteAlbum(TLObject):
    CONSTRUCTOR_ID = 2369017552
    __slots__ = ('peer', 'album_id')
    def __init__(self, peer: 'InputPeer', album_id: int):
        self.peer = peer
        self.album_id = album_id
    def to_dict(self):
        return {"peer": self.peer, "album_id": self.album_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2369017552, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.album_id, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        album_id = reader.read_int()
        return cls(peer, album_id)

@register
class StoriesGetAlbums(TLObject):
    CONSTRUCTOR_ID = 632548039
    __slots__ = ('peer', 'hash')
    def __init__(self, peer: 'InputPeer', hash: int):
        self.peer = peer
        self.hash = hash
    def to_dict(self):
        return {"peer": self.peer, "hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(632548039, signed=False)
        writer.write(bytes(self.peer))
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        hash = reader.read_long()
        return cls(peer, hash)

@register
class StoriesGetAlbumStories(TLObject):
    CONSTRUCTOR_ID = 2894097761
    __slots__ = ('peer', 'album_id', 'offset', 'limit')
    def __init__(self, peer: 'InputPeer', album_id: int, offset: int, limit: int):
        self.peer = peer
        self.album_id = album_id
        self.offset = offset
        self.limit = limit
    def to_dict(self):
        return {"peer": self.peer, "album_id": self.album_id, "offset": self.offset, "limit": self.limit}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2894097761, signed=False)
        writer.write(bytes(self.peer))
        writer.write_int(self.album_id, signed=True)
        writer.write_int(self.offset, signed=True)
        writer.write_int(self.limit, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        peer = reader.tgread_object()
        album_id = reader.read_int()
        offset = reader.read_int()
        limit = reader.read_int()
        return cls(peer, album_id, offset, limit)

@register
class StoriesStartLive(TLObject):
    CONSTRUCTOR_ID = 3496594654
    __slots__ = ('pinned', 'noforwards', 'rtmp_stream', 'peer', 'caption', 'entities', 'privacy_rules', 'random_id', 'messages_enabled', 'send_paid_messages_stars')
    def __init__(self, peer: 'InputPeer', privacy_rules: 'Vector', random_id: int, pinned: bool = None, noforwards: bool = None, rtmp_stream: bool = None, caption: str = None, entities: 'Vector' = None, messages_enabled: bool = None, send_paid_messages_stars: int = None):
        self.pinned = pinned
        self.noforwards = noforwards
        self.rtmp_stream = rtmp_stream
        self.peer = peer
        self.caption = caption
        self.entities = entities
        self.privacy_rules = privacy_rules
        self.random_id = random_id
        self.messages_enabled = messages_enabled
        self.send_paid_messages_stars = send_paid_messages_stars
    def to_dict(self):
        return {"pinned": self.pinned, "noforwards": self.noforwards, "rtmp_stream": self.rtmp_stream, "peer": self.peer, "caption": self.caption, "entities": self.entities, "privacy_rules": self.privacy_rules, "random_id": self.random_id, "messages_enabled": self.messages_enabled, "send_paid_messages_stars": self.send_paid_messages_stars}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3496594654, signed=False)
        flags = 0
        if self.pinned: flags |= 1 << 2
        if self.noforwards: flags |= 1 << 4
        if self.rtmp_stream: flags |= 1 << 5
        if self.caption is not None: flags |= 1 << 0
        if self.entities is not None: flags |= 1 << 1
        if self.messages_enabled is not None: flags |= 1 << 6
        if self.send_paid_messages_stars is not None: flags |= 1 << 7
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.peer))
        if flags & (1 << 0):
            writer.write_string(self.caption)
        if flags & (1 << 1):
            writer.write(bytes(self.entities))
        writer.write(bytes(self.privacy_rules))
        writer.write_long(self.random_id, signed=False)
        if flags & (1 << 6):
            writer.write(serialize_bool(self.messages_enabled))
        if flags & (1 << 7):
            writer.write_long(self.send_paid_messages_stars, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        pinned = bool(flags & (1 << 2))
        noforwards = bool(flags & (1 << 4))
        rtmp_stream = bool(flags & (1 << 5))
        peer = reader.tgread_object()
        if flags & (1 << 0):
            caption = reader.read_string()
        else:
            caption = None
        if flags & (1 << 1):
            entities = reader.tgread_object()
        else:
            entities = None
        privacy_rules = reader.tgread_object()
        random_id = reader.read_long()
        if flags & (1 << 6):
            messages_enabled = reader.tgread_bool()
        else:
            messages_enabled = None
        if flags & (1 << 7):
            send_paid_messages_stars = reader.read_long()
        else:
            send_paid_messages_stars = None
        return cls(pinned, noforwards, rtmp_stream, peer, caption, entities, privacy_rules, random_id, messages_enabled, send_paid_messages_stars)

