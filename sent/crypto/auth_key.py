"""Auth key management."""

from __future__ import annotations

import struct

from sent.crypto.mtproto2 import sha1


def calc_key_id(key: bytes) -> int:
    """Calculate auth key ID from the key bytes."""
    return struct.unpack("<q", sha1(key)[-8:])[0]


class AuthKey:
    """Represents an MTProto authorization key."""

    __slots__ = ("key", "aux_hash", "key_id", "_key")

    def __init__(self, key: bytes):
        if len(key) != 256:
            raise ValueError("Auth key must be 256 bytes")
        self._key = key
        self.key = key
        self.aux_hash = sha1(key)[:8]
        self.key_id = calc_key_id(key)

    def __bool__(self) -> bool:
        return bool(self._key)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, AuthKey) and self._key == other._key

    def __hash__(self) -> int:
        return hash(self._key)

    @property
    def id(self) -> int:
        return self.key_id
