"""TL layer package."""

import sent.tl.mtproto_types  # noqa: F401 — register RpcResult, MsgContainer
from sent.tl.core import BoolFalse, BoolTrue, GzipPacked, Null
from sent.tl.serialization import BinaryReader, BinaryWriter
from sent.tl.tlobject import CONSTRUCTORS, TLObject, read_object, register

__all__ = [
    "TLObject",
    "CONSTRUCTORS",
    "read_object",
    "register",
    "BinaryReader",
    "BinaryWriter",
    "BoolFalse",
    "BoolTrue",
    "GzipPacked",
    "Null",
]
