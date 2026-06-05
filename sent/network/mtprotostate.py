"""MTProto state: encryption, message IDs, salts."""

from __future__ import annotations

import os
import struct
import time
from typing import Optional

from sent.crypto.aes import decrypt_ige, encrypt_ige
from sent.crypto.auth_key import AuthKey
from sent.crypto.mtproto2 import calc_msg_key, derive_keys_iv

_MSG_HEADER = struct.Struct("<qqqii")
_KEY_ID = struct.Struct("<q")


class MTProtoState:
    """Manages MTProto 2.0 message encryption and state."""

    def __init__(self, auth_key: AuthKey, session_id: Optional[int] = None, salt: int = 0):
        self.auth_key = auth_key
        self.session_id = session_id or int.from_bytes(os.urandom(8), "little", signed=True)
        self.salt = salt
        self.time_offset = 0
        self._last_msg_id = 0
        self._seq_no = 0

    def _generate_msg_id(self) -> int:
        now = int(time.time()) + self.time_offset
        msg_id = (now << 32) | (os.urandom(4)[0] << 24)
        if msg_id <= self._last_msg_id:
            msg_id = self._last_msg_id + 4
        self._last_msg_id = msg_id
        return msg_id

    def _generate_seq_no(self, content_related: bool) -> int:
        if content_related:
            result = self._seq_no * 2 + 1
            self._seq_no += 1
            return result
        return self._seq_no * 2

    def build_message_data(
        self,
        body: bytes,
        *,
        content_related: bool = True,
        msg_id: Optional[int] = None,
        seq_no: Optional[int] = None,
    ) -> tuple[int, int, bytes]:
        """Build plaintext MTProto message data. Returns (msg_id, seq_no, data)."""
        if msg_id is None:
            msg_id = self._generate_msg_id()
        if seq_no is None:
            seq_no = self._generate_seq_no(content_related)
        data = _MSG_HEADER.pack(self.salt, self.session_id, msg_id, len(body), seq_no) + body
        return msg_id, seq_no, data

    def parse_message_data(self, data: bytes) -> tuple[int, int, int, int, bytes]:
        """Parse plaintext MTProto message data. Returns (salt, session_id, msg_id, seq_no, body)."""
        salt, session_id, msg_id, length, seq_no = _MSG_HEADER.unpack(data[:32])
        body = data[32 : 32 + length]
        return salt, session_id, msg_id, seq_no, body

    def encrypt_message_data(self, data: bytes) -> bytes:
        """Encrypt a message body for sending."""
        padding = (-len(data)) % 16
        if padding == 0:
            padding = 16
        data = data + os.urandom(padding)
        msg_key = calc_msg_key(self.auth_key.key, data, outgoing=True)
        aes_key, aes_iv = derive_keys_iv(self.auth_key.key, msg_key, outgoing=True)
        encrypted = encrypt_ige(aes_key, aes_iv, data)
        return _KEY_ID.pack(self.auth_key.key_id) + msg_key + encrypted

    def decrypt_message_data(self, body: bytes) -> bytes:
        """Decrypt received message body."""
        key_id = _KEY_ID.unpack(body[:8])[0]
        if key_id != self.auth_key.key_id:
            raise ValueError(f"Key ID mismatch: {key_id} != {self.auth_key.key_id}")
        msg_key = body[8:24]
        encrypted = body[24:]
        aes_key, aes_iv = derive_keys_iv(self.auth_key.key, msg_key, outgoing=False)
        return decrypt_ige(aes_key, aes_iv, encrypted)

    def pack_message(
        self,
        body: bytes,
        content_related: bool = True,
        encrypted: bool = True,
    ) -> bytes:
        """Pack a message with auth key wrapper."""
        _, _, data = self.build_message_data(body, content_related=content_related)
        if encrypted and self.auth_key:
            return self.encrypt_message_data(data)
        return data

    def unpack_message(self, data: bytes) -> tuple:
        """Unpack and decrypt a received message. Returns (msg_id, seq_no, body)."""
        if self.auth_key:
            data = self.decrypt_message_data(data)
        _, _, msg_id, seq_no, body = self.parse_message_data(data)
        return msg_id, seq_no, body

    def write_data_as_message(self, writer, data: bytes, content_related: bool = True) -> int:
        """Write data as an encrypted MTProto message, return msg_id."""
        msg_id, _, _ = self.build_message_data(data, content_related=content_related)
        return msg_id
