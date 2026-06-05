"""Hand-written MTProto transport layer types."""

from __future__ import annotations

from typing import List

from sent.tl.serialization import BinaryReader, BinaryWriter
from sent.tl.tlobject import TLObject, read_object, register


@register
class RpcResult(TLObject):
    CONSTRUCTOR_ID = 0xF35C6D01
    __slots__ = ("req_msg_id", "result")

    def __init__(self, req_msg_id: int, result: TLObject):
        self.req_msg_id = req_msg_id
        self.result = result

    def to_dict(self):
        return {
            "req_msg_id": self.req_msg_id,
            "result": self.result.to_dict() if self.result else None,
        }

    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(self.CONSTRUCTOR_ID, signed=False)
        writer.write_long(self.req_msg_id, signed=False)
        writer.write(bytes(self.result))
        return writer.get_bytes()

    @classmethod
    def from_reader(cls, reader: BinaryReader):
        req_msg_id = reader.read_long(signed=False)
        result = read_object(reader)
        return cls(req_msg_id, result)


@register
class ContainerMessage(TLObject):
    """A message inside a msg_container (no constructor id)."""

    CONSTRUCTOR_ID = 0
    __slots__ = ("msg_id", "seqno", "body")

    def __init__(self, msg_id: int, seqno: int, body: TLObject):
        self.msg_id = msg_id
        self.seqno = seqno
        self.body = body

    def to_dict(self):
        return {
            "msg_id": self.msg_id,
            "seqno": self.seqno,
            "body": self.body.to_dict() if self.body else None,
        }

    def _bytes(self):
        body_bytes = bytes(self.body)
        writer = BinaryWriter()
        writer.write_long(self.msg_id, signed=False)
        writer.write_int(self.seqno)
        writer.write_int(len(body_bytes))
        writer.write(body_bytes)
        return writer.get_bytes()

    @classmethod
    def from_reader(cls, reader: BinaryReader):
        msg_id = reader.read_long(signed=False)
        seqno = reader.read_int()
        length = reader.read_int()
        body = read_object(BinaryReader(reader.read(length)))
        return cls(msg_id, seqno, body)

    @classmethod
    def read_container_message(cls, reader: BinaryReader) -> "ContainerMessage":
        return cls.from_reader(reader)


@register
class MsgContainer(TLObject):
    CONSTRUCTOR_ID = 0x73F1F8DC
    __slots__ = ("messages",)

    def __init__(self, messages: List[ContainerMessage]):
        self.messages = messages

    def to_dict(self):
        return {"messages": [m.to_dict() for m in self.messages]}

    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(self.CONSTRUCTOR_ID, signed=False)
        writer.write_int(len(self.messages), signed=False)
        for message in self.messages:
            writer.write(message._bytes())
        return writer.get_bytes()

    @classmethod
    def from_reader(cls, reader: BinaryReader):
        count = reader.read_int(signed=False)
        messages = [ContainerMessage.from_reader(reader) for _ in range(count)]
        return cls(messages)


def decompress_gzip_if_needed(obj: TLObject) -> TLObject:
    """Unwrap GzipPacked and return the inner object."""
    from sent.tl.core import GzipPacked

    if isinstance(obj, GzipPacked):
        return obj.data
    if getattr(obj, "__class__", None).__name__ == "GzipPacked":
        return obj.data
    return obj


def unwrap_object(obj: TLObject) -> TLObject:
    """Recursively unwrap RpcResult, MsgContainer, and GzipPacked."""
    obj = decompress_gzip_if_needed(obj)
    cls_name = obj.__class__.__name__
    if cls_name == "RpcResult":
        return unwrap_object(obj.result)
    if cls_name == "MsgContainer":
        results = []
        for message in obj.messages:
            results.append(unwrap_object(message.body))
        return results[0] if len(results) == 1 else obj
    return obj
