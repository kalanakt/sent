"""Auto-generated TL functions. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

@register
class FoldersEditPeerFolders(TLObject):
    CONSTRUCTOR_ID = 1749536939
    __slots__ = ('folder_peers')
    def __init__(self, folder_peers: 'Vector'):
        self.folder_peers = folder_peers
    def to_dict(self):
        return {"folder_peers": self.folder_peers}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1749536939, signed=False)
        writer.write(bytes(self.folder_peers))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        folder_peers = reader.tgread_object()
        return cls(folder_peers)

