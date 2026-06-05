"""Unit tests for sent MTProto framework."""

import pytest

from sent.tl.core import BoolFalse, BoolTrue, GzipPacked
from sent.tl.serialization import BinaryReader, BinaryWriter
from sent.tl.tlobject import serialize_bytes, serialize_int, serialize_long
from sent.crypto.mtproto2 import sha256, calc_msg_key, derive_keys_iv
from sent.crypto.auth_key import AuthKey, calc_key_id
from sent.crypto.factorization import factorize


class TestTLSerialization:
    def test_bool_roundtrip(self):
        assert bytes(BoolTrue()) == b"\xb5u\x72\x99"
        assert bytes(BoolFalse()) == b"\x37\x97y\xbc"

    def test_int_serialization(self):
        assert serialize_int(12345) == b"90\x00\x00"

    def test_bytes_serialization(self):
        data = b"hello"
        encoded = serialize_bytes(data)
        reader = BinaryReader(encoded)

    def test_vector_serialization(self):
        from sent.tl.types.all import InputPeerEmpty

        items = [InputPeerEmpty(), InputPeerEmpty()]
        data = BinaryWriter.serialize_vector(items)
        reader = BinaryReader(data)
        result = reader.tgread_vector()
        assert len(result) == 2

    def test_bare_vector_long(self):
        items = [1234567890123456789, 987654321098765432]
        data = BinaryWriter.serialize_vector(items, item_type="long")
        reader = BinaryReader(data)
        result = reader.tgread_vector_long()
        assert result == items


class TestTLTypes:
    def test_input_peer_empty_roundtrip(self):
        from sent.tl.types.all import InputPeerEmpty

        obj = InputPeerEmpty()
        restored = InputPeerEmpty.from_reader(BinaryReader(bytes(obj)[4:]))
        assert isinstance(restored, InputPeerEmpty)

    def test_res_pq_roundtrip(self):
        from sent.tl.types.all import ResPQ

        obj = ResPQ(
            nonce=b"\x00" * 16,
            server_nonce=b"\x01" * 16,
            pq="15",
            server_public_key_fingerprints=[1234567890123456789],
        )
        raw = bytes(obj)
        assert len(raw) > 4
        restored = ResPQ.from_reader(BinaryReader(raw[4:]))
        assert restored.pq == "15"
        assert restored.server_public_key_fingerprints == [1234567890123456789]

    def test_rpc_result_roundtrip(self):
        from sent.tl.mtproto_types import RpcResult
        from sent.tl.types.all import Pong

        inner = Pong(msg_id=1, ping_id=42)
        obj = RpcResult(req_msg_id=999, result=inner)
        restored = RpcResult.from_reader(BinaryReader(bytes(obj)[4:]))
        assert restored.req_msg_id == 999
        assert restored.result.ping_id == 42

    def test_msg_container_roundtrip(self):
        from sent.tl.mtproto_types import ContainerMessage, MsgContainer
        from sent.tl.types.all import Pong

        msg = ContainerMessage(msg_id=1, seqno=1, body=Pong(msg_id=1, ping_id=7))
        obj = MsgContainer(messages=[msg])
        restored = MsgContainer.from_reader(BinaryReader(bytes(obj)[4:]))
        assert len(restored.messages) == 1
        assert restored.messages[0].body.ping_id == 7


class TestCrypto:
    def test_ige_roundtrip(self):
        from sent.crypto.aes import decrypt_ige, encrypt_ige
        from sent.crypto.mtproto2 import calc_msg_key, derive_keys_iv

        key = b"\xcd" * 256
        data = b"mtproto padding test!!" + b"\x00" * 10
        msg_key = calc_msg_key(key, data, outgoing=True)
        aes_key, aes_iv = derive_keys_iv(key, msg_key, outgoing=True)
        encrypted = encrypt_ige(aes_key, aes_iv, data)
        decrypted = decrypt_ige(aes_key, aes_iv, encrypted)
        assert decrypted == data

    def test_sha256(self):
        result = sha256(b"test")
        assert len(result) == 32

    def test_auth_key_id(self):
        key = b"\x00" * 256
        auth = AuthKey(key)
        assert auth.key_id == calc_key_id(key)

    def test_factorize(self):
        p, q = factorize(15)
        assert p * q == 15

    def test_msg_key_derivation(self):
        key = b"\xab" * 256
        data = b"test message data"
        msg_key = calc_msg_key(key, data, outgoing=True)
        aes_key, aes_iv = derive_keys_iv(key, msg_key, outgoing=True)
        assert len(aes_key) == 32
        assert len(aes_iv) == 32


class TestSessions:
    def test_memory_session(self):
        from sent.sessions import MemorySession

        s = MemorySession()
        s.set_auth_key(b"\x00" * 256)
        s.set_salt(12345)
        s.set_session_id(999)
        assert s.auth_key() == b"\x00" * 256
        assert s.get_salt() == 12345
        assert s.get_session_id() == 999

    def test_string_session(self):
        from sent.sessions import StringSession

        s = StringSession()
        s.set_auth_key(b"\x01" * 256)
        encoded = s.save()
        restored = StringSession(encoded)
        assert restored.auth_key() == b"\x01" * 256


class TestEvents:
    def test_new_message_pattern(self):
        from sent.events import NewMessage

        builder = NewMessage(pattern="(?i)hello")
        assert builder.pattern is not None

    def test_event_builder_decorator(self):
        from sent.events import NewMessage

        @NewMessage(pattern="test")
        def handler(event):
            pass

        assert hasattr(handler, "_event_builder")

    def test_message_deleted_event(self):
        from sent.events import MessageDeleted
        from sent.tl.types.all import UpdateDeleteMessages

        builder = MessageDeleted()
        event = builder.build(
            UpdateDeleteMessages(messages=[1, 2, 3], pts=1, pts_count=1),
            client=None,
        )
        assert event is not None
        assert event.deleted_ids == [1, 2, 3]

    def test_update_normalization(self):
        from sent.client.updates import UpdateMethods
        from sent.tl.types.all import UpdateDeleteMessages, Updates

        mixin = UpdateMethods()
        update = Updates(
            updates=[UpdateDeleteMessages(messages=[5], pts=1, pts_count=1)],
            users=[],
            chats=[],
            date=0,
            seq=0,
        )
        normalized = list(mixin._normalize_updates(update))
        assert len(normalized) == 1
        assert normalized[0].__class__.__name__ == "UpdateDeleteMessages"


class TestErrors:
    def test_rpc_error(self):
        from sent.errors import RPCError, FloodWaitError, rpc_message_to_error

        err = rpc_message_to_error("FLOOD_WAIT_30", 420)
        assert isinstance(err, FloodWaitError)
        assert err.seconds == 30

    def test_phone_code_invalid(self):
        from sent.errors import PhoneCodeInvalidError

        err = PhoneCodeInvalidError()
        assert err.code == 400

    def test_peer_id_invalid(self):
        from sent.errors import rpc_message_to_error
        from sent.errors.rpcerrorlist import PeerIdInvalidError

        err = rpc_message_to_error("PEER_ID_INVALID", 400)
        assert isinstance(err, PeerIdInvalidError)


class TestImports:
    def test_main_imports(self):
        from sent import TelegramClient, events, types, functions, errors

        assert TelegramClient is not None
        assert events.NewMessage is not None
        assert events.MessageDeleted is not None

    def test_tl_layer(self):
        from sent.version import LAYER

        assert LAYER >= 195

    def test_constructor_registry(self):
        from sent.tl.tlobject import CONSTRUCTORS
        import sent.tl.types  # noqa

        assert len(CONSTRUCTORS) > 1000

    def test_mtproto_types_registered(self):
        from sent.tl.mtproto_types import MsgContainer, RpcResult

        assert RpcResult.CONSTRUCTOR_ID in __import__(
            "sent.tl.tlobject", fromlist=["CONSTRUCTORS"]
        ).CONSTRUCTORS
