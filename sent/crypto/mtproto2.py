"""Hashing utilities for MTProto 2.0."""

from __future__ import annotations

import hashlib


def sha1(data: bytes) -> bytes:
    return hashlib.sha1(data).digest()


def sha256(data: bytes) -> bytes:
    return hashlib.sha256(data).digest()


def calc_msg_key(auth_key: bytes, data: bytes, outgoing: bool) -> bytes:
    """Calculate message key for MTProto 2.0."""
    x = 0 if outgoing else 8
    return sha256(auth_key[88 + x : 88 + x + 32] + data)[8:24]


def derive_keys_iv(auth_key: bytes, msg_key: bytes, outgoing: bool) -> tuple:
    """Derive AES key and IV from auth key and message key."""
    x = 0 if outgoing else 8
    sha256_a = sha256(msg_key + auth_key[x : x + 36])
    sha256_b = sha256(auth_key[x + 40 : x + 76] + msg_key)
    aes_key = sha256_a[:8] + sha256_b[8:24] + sha256_a[24:32]
    aes_iv = sha256_b[:8] + sha256_a[8:24] + sha256_b[24:32]
    return aes_key, aes_iv


def KDF(auth_key: bytes, msg_key: bytes, outgoing: bool) -> tuple:
    """Key derivation function alias."""
    return derive_keys_iv(auth_key, msg_key, outgoing)
