"""SRP implementation for Telegram 2FA."""

from __future__ import annotations

import hashlib
import os
from typing import Tuple


def _sha256(data: bytes) -> bytes:
    return hashlib.sha256(data).digest()


def compute_password_hash(algo, password: str) -> bytes:
    """Compute x from password using Telegram's KDF algo."""
    hash1 = _sha256(algo.salt1 + password.encode("utf-8") + algo.salt1)
    hash2 = _sha256(hash1 + algo.salt2)
    return hashlib.pbkdf2_hmac("sha512", hash2, algo.salt1, 100000)


def compute_check(
    *,
    password: str,
    srp_id: int,
    srp_B: bytes,
    secure_random: bytes,
    algo,
) -> Tuple[int, bytes, bytes]:
    """Compute InputCheckPasswordSRP fields (srp_id, A, M1)."""
    g = algo.g
    p = algo.p
    p_int = int.from_bytes(p, "big")
    g_b = int.from_bytes(srp_B, "big")

    x = int.from_bytes(compute_password_hash(algo, password), "big")
    a = int.from_bytes(secure_random[:256], "big")
    g_a = pow(g, a, p_int)
    A = g_a.to_bytes(256, "big")

    k = int.from_bytes(_sha256(p + str(g).encode()), "big")
    u = int.from_bytes(_sha256(A + srp_B), "big")

    g_x = pow(g, x, p_int)
    k_g_x = (k * g_x) % p_int
    t = (g_b - k_g_x) % p_int
    s_a = pow(t, a + u * x, p_int)
    K = _sha256(s_a.to_bytes(256, "big"))

    M1 = _sha256(_sha256(p) + _sha256(str(g).encode()) + algo.salt1 + A + srp_B + K)
    return srp_id, A, M1
