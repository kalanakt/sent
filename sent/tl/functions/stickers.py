"""Auto-generated TL functions. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

@register
class StickersCreateStickerSet(TLObject):
    CONSTRUCTOR_ID = 2418125671
    __slots__ = ('masks', 'emojis', 'text_color', 'user_id', 'title', 'short_name', 'thumb', 'stickers', 'software')
    def __init__(self, user_id: 'InputUser', title: str, short_name: str, stickers: 'Vector', masks: bool = None, emojis: bool = None, text_color: bool = None, thumb: 'InputDocument' = None, software: str = None):
        self.masks = masks
        self.emojis = emojis
        self.text_color = text_color
        self.user_id = user_id
        self.title = title
        self.short_name = short_name
        self.thumb = thumb
        self.stickers = stickers
        self.software = software
    def to_dict(self):
        return {"masks": self.masks, "emojis": self.emojis, "text_color": self.text_color, "user_id": self.user_id, "title": self.title, "short_name": self.short_name, "thumb": self.thumb, "stickers": self.stickers, "software": self.software}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2418125671, signed=False)
        flags = 0
        if self.masks: flags |= 1 << 0
        if self.emojis: flags |= 1 << 5
        if self.text_color: flags |= 1 << 6
        if self.thumb is not None: flags |= 1 << 2
        if self.software is not None: flags |= 1 << 3
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.user_id))
        writer.write_string(self.title)
        writer.write_string(self.short_name)
        if flags & (1 << 2):
            writer.write(bytes(self.thumb))
        writer.write(bytes(self.stickers))
        if flags & (1 << 3):
            writer.write_string(self.software)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        masks = bool(flags & (1 << 0))
        emojis = bool(flags & (1 << 5))
        text_color = bool(flags & (1 << 6))
        user_id = reader.tgread_object()
        title = reader.read_string()
        short_name = reader.read_string()
        if flags & (1 << 2):
            thumb = reader.tgread_object()
        else:
            thumb = None
        stickers = reader.tgread_object()
        if flags & (1 << 3):
            software = reader.read_string()
        else:
            software = None
        return cls(masks, emojis, text_color, user_id, title, short_name, thumb, stickers, software)

@register
class StickersRemoveStickerFromSet(TLObject):
    CONSTRUCTOR_ID = 4151709521
    __slots__ = ('sticker')
    def __init__(self, sticker: 'InputDocument'):
        self.sticker = sticker
    def to_dict(self):
        return {"sticker": self.sticker}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4151709521, signed=False)
        writer.write(bytes(self.sticker))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        sticker = reader.tgread_object()
        return cls(sticker)

@register
class StickersChangeStickerPosition(TLObject):
    CONSTRUCTOR_ID = 4290172106
    __slots__ = ('sticker', 'position')
    def __init__(self, sticker: 'InputDocument', position: int):
        self.sticker = sticker
        self.position = position
    def to_dict(self):
        return {"sticker": self.sticker, "position": self.position}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4290172106, signed=False)
        writer.write(bytes(self.sticker))
        writer.write_int(self.position, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        sticker = reader.tgread_object()
        position = reader.read_int()
        return cls(sticker, position)

@register
class StickersAddStickerToSet(TLObject):
    CONSTRUCTOR_ID = 2253651646
    __slots__ = ('stickerset', 'sticker')
    def __init__(self, stickerset: 'InputStickerSet', sticker: 'InputStickerSetItem'):
        self.stickerset = stickerset
        self.sticker = sticker
    def to_dict(self):
        return {"stickerset": self.stickerset, "sticker": self.sticker}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2253651646, signed=False)
        writer.write(bytes(self.stickerset))
        writer.write(bytes(self.sticker))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        stickerset = reader.tgread_object()
        sticker = reader.tgread_object()
        return cls(stickerset, sticker)

@register
class StickersSetStickerSetThumb(TLObject):
    CONSTRUCTOR_ID = 2808763282
    __slots__ = ('stickerset', 'thumb', 'thumb_document_id')
    def __init__(self, stickerset: 'InputStickerSet', thumb: 'InputDocument' = None, thumb_document_id: int = None):
        self.stickerset = stickerset
        self.thumb = thumb
        self.thumb_document_id = thumb_document_id
    def to_dict(self):
        return {"stickerset": self.stickerset, "thumb": self.thumb, "thumb_document_id": self.thumb_document_id}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2808763282, signed=False)
        flags = 0
        if self.thumb is not None: flags |= 1 << 0
        if self.thumb_document_id is not None: flags |= 1 << 1
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.stickerset))
        if flags & (1 << 0):
            writer.write(bytes(self.thumb))
        if flags & (1 << 1):
            writer.write_long(self.thumb_document_id, signed=False)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        stickerset = reader.tgread_object()
        if flags & (1 << 0):
            thumb = reader.tgread_object()
        else:
            thumb = None
        if flags & (1 << 1):
            thumb_document_id = reader.read_long()
        else:
            thumb_document_id = None
        return cls(stickerset, thumb, thumb_document_id)

@register
class StickersCheckShortName(TLObject):
    CONSTRUCTOR_ID = 676017721
    __slots__ = ('short_name')
    def __init__(self, short_name: str):
        self.short_name = short_name
    def to_dict(self):
        return {"short_name": self.short_name}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(676017721, signed=False)
        writer.write_string(self.short_name)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        short_name = reader.read_string()
        return cls(short_name)

@register
class StickersSuggestShortName(TLObject):
    CONSTRUCTOR_ID = 1303364867
    __slots__ = ('title')
    def __init__(self, title: str):
        self.title = title
    def to_dict(self):
        return {"title": self.title}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1303364867, signed=False)
        writer.write_string(self.title)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        title = reader.read_string()
        return cls(title)

@register
class StickersChangeSticker(TLObject):
    CONSTRUCTOR_ID = 4115889852
    __slots__ = ('sticker', 'emoji', 'mask_coords', 'keywords')
    def __init__(self, sticker: 'InputDocument', emoji: str = None, mask_coords: 'MaskCoords' = None, keywords: str = None):
        self.sticker = sticker
        self.emoji = emoji
        self.mask_coords = mask_coords
        self.keywords = keywords
    def to_dict(self):
        return {"sticker": self.sticker, "emoji": self.emoji, "mask_coords": self.mask_coords, "keywords": self.keywords}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4115889852, signed=False)
        flags = 0
        if self.emoji is not None: flags |= 1 << 0
        if self.mask_coords is not None: flags |= 1 << 1
        if self.keywords is not None: flags |= 1 << 2
        writer.write_int(flags, signed=False)
        writer.write(bytes(self.sticker))
        if flags & (1 << 0):
            writer.write_string(self.emoji)
        if flags & (1 << 1):
            writer.write(bytes(self.mask_coords))
        if flags & (1 << 2):
            writer.write_string(self.keywords)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        sticker = reader.tgread_object()
        if flags & (1 << 0):
            emoji = reader.read_string()
        else:
            emoji = None
        if flags & (1 << 1):
            mask_coords = reader.tgread_object()
        else:
            mask_coords = None
        if flags & (1 << 2):
            keywords = reader.read_string()
        else:
            keywords = None
        return cls(sticker, emoji, mask_coords, keywords)

@register
class StickersRenameStickerSet(TLObject):
    CONSTRUCTOR_ID = 306912256
    __slots__ = ('stickerset', 'title')
    def __init__(self, stickerset: 'InputStickerSet', title: str):
        self.stickerset = stickerset
        self.title = title
    def to_dict(self):
        return {"stickerset": self.stickerset, "title": self.title}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(306912256, signed=False)
        writer.write(bytes(self.stickerset))
        writer.write_string(self.title)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        stickerset = reader.tgread_object()
        title = reader.read_string()
        return cls(stickerset, title)

@register
class StickersDeleteStickerSet(TLObject):
    CONSTRUCTOR_ID = 2272281492
    __slots__ = ('stickerset')
    def __init__(self, stickerset: 'InputStickerSet'):
        self.stickerset = stickerset
    def to_dict(self):
        return {"stickerset": self.stickerset}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2272281492, signed=False)
        writer.write(bytes(self.stickerset))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        stickerset = reader.tgread_object()
        return cls(stickerset)

@register
class StickersReplaceSticker(TLObject):
    CONSTRUCTOR_ID = 1184253338
    __slots__ = ('sticker', 'new_sticker')
    def __init__(self, sticker: 'InputDocument', new_sticker: 'InputStickerSetItem'):
        self.sticker = sticker
        self.new_sticker = new_sticker
    def to_dict(self):
        return {"sticker": self.sticker, "new_sticker": self.new_sticker}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1184253338, signed=False)
        writer.write(bytes(self.sticker))
        writer.write(bytes(self.new_sticker))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        sticker = reader.tgread_object()
        new_sticker = reader.tgread_object()
        return cls(sticker, new_sticker)

