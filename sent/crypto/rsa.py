"""RSA encryption for MTProto auth key creation."""

from __future__ import annotations

import struct
from typing import Dict, List, Tuple

# Telegram production RSA public keys (fingerprints -> (modulus, exponent))
# These are the well-known Telegram server public keys
_RSA_KEYS: Dict[int, Tuple[int, int]] = {
    0xC3B42B026CE86B21: (
        int(
            "C150023EB2E70FE7982CED726FB1345750A4333A487266F2FC5269A"
            "589A8975622F141E6E360A629FDB976B769E7FD684898476E4175E"
            "8F2E84827B0C529EF168965DF2631980584BBEB8FAE663DF1EE1046"
            "A0EAC47D8A9373AB4ACCAE6FA67E9CF1A575A537B1D5E0F289158"
            "223BA276AAED2A7D9A1F8EE840598FC8BE836AC4A667AAEB2D654"
            "71B997A25675A3D294226161600E6E7203259434B449AF2AFD79"
            "DF8851BED2ED847FD3E1E7785C1FA2",
            16,
        ),
        65537,
    ),
    0x9A996A682489108511: (
        int(
            "CA499FC774272437FDB327C3C4FD2A0D5915C467F0EA2A5A030"
            "2FA24B0670EDF1C6D975814D8496A8E5E5A316272170F5D244"
            "C7E434E93B585EA966D282753539D9D6632923A280F031B498"
            "D0ECAA6AE139EE882F567159FA3CEAC947AE5771774A57A4D"
            "43ADBC6376D1AB266F6A6B598D691698BB5768ADA2EA715DA"
            "2569856077CF1C702E716EA5184E3E726E1965739651DB98"
            "3D374484562464F1A",
            16,
        ),
        65537,
    ),
    0xB05B814474334B43: (
        int(
            "E8BB3965C9FCFB5A3A6E8787FCFD6E5D7FE157639DB965F239"
            "4691453F8F877B245D4877F0B8C0A6A9181733FAEE171579"
            "829F8DF111F475D558FD045CC14881DDDBAE784AD6C6D486"
            "8655740FBF8FA7831D79AC763F6DAB656552D5A0A5FCF598"
            "DD99D796F1547F130FA00A7D947E62B3B054DE3366D6E0F"
            "62954846B9775D7146184C3EC5948FF1B7638E1A1E054D5"
            "C424B088567E5836",
            16,
        ),
        65537,
    ),
}


def get_public_key_fingerprints() -> List[int]:
    return list(_RSA_KEYS.keys())


def _rsa_pad(data: bytes, modulus: int) -> int:
    """RSA pad data for encryption."""
    data_with_hash = data
    # Add random padding to fill to modulus size
    from sent.crypto.mtproto2 import sha1
    import os

    data_hash = sha1(data)
    random_bytes = os.urandom(235 - len(data) - len(data_hash))
    padded = b"\x00" + data_hash + data + random_bytes
    return int.from_bytes(padded, "big")


def encrypt(data: bytes, fingerprint: int) -> bytes:
    """Encrypt data with RSA using the key matching fingerprint."""
    if fingerprint not in _RSA_KEYS:
        raise ValueError(f"Unknown RSA fingerprint {fingerprint:#x}")
    modulus, exponent = _RSA_KEYS[fingerprint]
    padded = _rsa_pad(data, modulus)
    encrypted = pow(padded, exponent, modulus)
    byte_length = (modulus.bit_length() + 7) // 8
    return encrypted.to_bytes(byte_length, "big")
