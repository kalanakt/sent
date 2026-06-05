"""Auto-generated TL functions. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

@register
class AicomposeCreateTone(TLObject):
    CONSTRUCTOR_ID = 1252538643
    __slots__ = ('display_author', 'emoji_id', 'title', 'prompt')
    def __init__(self, emoji_id: int, title: str, prompt: str, display_author: bool = None):
        self.display_author = display_author
        self.emoji_id = emoji_id
        self.title = title
        self.prompt = prompt
    def to_dict(self):
        return {"display_author": self.display_author, "emoji_id": self.emoji_id, "title": self.title, "prompt": self.prompt}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1252538643, signed=False)
        flags = 0
        if self.display_author: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write_long(self.emoji_id, signed=False)
        writer.write_string(self.title)
        writer.write_string(self.prompt)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        display_author = bool(flags & (1 << 0))
        emoji_id = reader.read_long()
        title = reader.read_string()
        prompt = reader.read_string()
        return cls(display_author, emoji_id, title, prompt)

@register
class AicomposeUpdateTone(TLObject):
    CONSTRUCTOR_ID = 2419838809
    __slots__ = ('tone', 'display_author', 'emoji_id', 'title', 'prompt')
    def __init__(self, tone: 'InputAiComposeTone', display_author: bool = None, emoji_id: int = None, title: str = None, prompt: str = None):
        self.tone = tone
        self.display_author = display_author
        self.emoji_id = emoji_id
        self.title = title
        self.prompt = prompt
    def to_dict(self):
        return {"tone": self.tone, "display_author": self.display_author, "emoji_id": self.emoji_id, "title": self.title, "prompt": self.prompt}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2419838809, signed=False)
        flags = 0
        if self.display_author is not None: flags |= 1 << 0
        if self.emoji_id is not None: flags |= 1 << 1
        if self.title is not None: flags |= 1 << 2
        if self.prompt is not None: flags |= 1 << 3
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.tone))
        if flags & (1 << 0):
            writer.write(serialize_bool(self.display_author))
        if flags & (1 << 1):
            writer.write_long(self.emoji_id, signed=False)
        if flags & (1 << 2):
            writer.write_string(self.title)
        if flags & (1 << 3):
            writer.write_string(self.prompt)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        tone = reader.tgread_object()
        if flags & (1 << 0):
            display_author = reader.tgread_bool()
        else:
            display_author = None
        if flags & (1 << 1):
            emoji_id = reader.read_long()
        else:
            emoji_id = None
        if flags & (1 << 2):
            title = reader.read_string()
        else:
            title = None
        if flags & (1 << 3):
            prompt = reader.read_string()
        else:
            prompt = None
        return cls(tone, display_author, emoji_id, title, prompt)

@register
class AicomposeSaveTone(TLObject):
    CONSTRUCTOR_ID = 394447793
    __slots__ = ('tone', 'unsave')
    def __init__(self, tone: 'InputAiComposeTone', unsave: bool):
        self.tone = tone
        self.unsave = unsave
    def to_dict(self):
        return {"tone": self.tone, "unsave": self.unsave}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(394447793, signed=False)
        writer.write(bytes(self.tone))
        writer.write(serialize_bool(self.unsave))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        tone = reader.tgread_object()
        unsave = reader.tgread_bool()
        return cls(tone, unsave)

@register
class AicomposeDeleteTone(TLObject):
    CONSTRUCTOR_ID = 3711512938
    __slots__ = ('tone')
    def __init__(self, tone: 'InputAiComposeTone'):
        self.tone = tone
    def to_dict(self):
        return {"tone": self.tone}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3711512938, signed=False)
        writer.write(bytes(self.tone))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        tone = reader.tgread_object()
        return cls(tone)

@register
class AicomposeGetTone(TLObject):
    CONSTRUCTOR_ID = 3001596419
    __slots__ = ('tone')
    def __init__(self, tone: 'InputAiComposeTone'):
        self.tone = tone
    def to_dict(self):
        return {"tone": self.tone}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3001596419, signed=False)
        writer.write(bytes(self.tone))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        tone = reader.tgread_object()
        return cls(tone)

@register
class AicomposeGetTones(TLObject):
    CONSTRUCTOR_ID = 2882900481
    __slots__ = ('hash')
    def __init__(self, hash: int):
        self.hash = hash
    def to_dict(self):
        return {"hash": self.hash}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2882900481, signed=False)
        writer.write_long(self.hash, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        hash = reader.read_long()
        return cls(hash)

@register
class AicomposeGetToneExample(TLObject):
    CONSTRUCTOR_ID = 3518278420
    __slots__ = ('tone', 'num')
    def __init__(self, tone: 'InputAiComposeTone', num: int):
        self.tone = tone
        self.num = num
    def to_dict(self):
        return {"tone": self.tone, "num": self.num}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3518278420, signed=False)
        writer.write(bytes(self.tone))
        writer.write_int(self.num, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        tone = reader.tgread_object()
        num = reader.read_int()
        return cls(tone, num)

