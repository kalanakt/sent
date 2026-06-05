"""Auto-generated TL functions. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

@register
class LangpackGetLangPack(TLObject):
    CONSTRUCTOR_ID = 4075959050
    __slots__ = ('lang_pack', 'lang_code')
    def __init__(self, lang_pack: str, lang_code: str):
        self.lang_pack = lang_pack
        self.lang_code = lang_code
    def to_dict(self):
        return {"lang_pack": self.lang_pack, "lang_code": self.lang_code}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4075959050, signed=False)
        writer.write_string(self.lang_pack)
        writer.write_string(self.lang_code)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        lang_pack = reader.read_string()
        lang_code = reader.read_string()
        return cls(lang_pack, lang_code)

@register
class LangpackGetStrings(TLObject):
    CONSTRUCTOR_ID = 4025104387
    __slots__ = ('lang_pack', 'lang_code', 'keys')
    def __init__(self, lang_pack: str, lang_code: str, keys: 'Vector'):
        self.lang_pack = lang_pack
        self.lang_code = lang_code
        self.keys = keys
    def to_dict(self):
        return {"lang_pack": self.lang_pack, "lang_code": self.lang_code, "keys": self.keys}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4025104387, signed=False)
        writer.write_string(self.lang_pack)
        writer.write_string(self.lang_code)
        writer.write(bytes(self.keys))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        lang_pack = reader.read_string()
        lang_code = reader.read_string()
        keys = reader.tgread_object()
        return cls(lang_pack, lang_code, keys)

@register
class LangpackGetDifference(TLObject):
    CONSTRUCTOR_ID = 3449309861
    __slots__ = ('lang_pack', 'lang_code', 'from_version')
    def __init__(self, lang_pack: str, lang_code: str, from_version: int):
        self.lang_pack = lang_pack
        self.lang_code = lang_code
        self.from_version = from_version
    def to_dict(self):
        return {"lang_pack": self.lang_pack, "lang_code": self.lang_code, "from_version": self.from_version}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(3449309861, signed=False)
        writer.write_string(self.lang_pack)
        writer.write_string(self.lang_code)
        writer.write_int(self.from_version, signed=True)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        lang_pack = reader.read_string()
        lang_code = reader.read_string()
        from_version = reader.read_int()
        return cls(lang_pack, lang_code, from_version)

@register
class LangpackGetLanguages(TLObject):
    CONSTRUCTOR_ID = 1120311183
    __slots__ = ('lang_pack')
    def __init__(self, lang_pack: str):
        self.lang_pack = lang_pack
    def to_dict(self):
        return {"lang_pack": self.lang_pack}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1120311183, signed=False)
        writer.write_string(self.lang_pack)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        lang_pack = reader.read_string()
        return cls(lang_pack)

@register
class LangpackGetLanguage(TLObject):
    CONSTRUCTOR_ID = 1784243458
    __slots__ = ('lang_pack', 'lang_code')
    def __init__(self, lang_pack: str, lang_code: str):
        self.lang_pack = lang_pack
        self.lang_code = lang_code
    def to_dict(self):
        return {"lang_pack": self.lang_pack, "lang_code": self.lang_code}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1784243458, signed=False)
        writer.write_string(self.lang_pack)
        writer.write_string(self.lang_code)
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        lang_pack = reader.read_string()
        lang_code = reader.read_string()
        return cls(lang_pack, lang_code)

