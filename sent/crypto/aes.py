"""AES encryption for MTProto (IGE and CTR modes)."""

from __future__ import annotations

from enum import Enum

try:
    import cryptg

    _HAS_CRYPTG = True
except ImportError:
    _HAS_CRYPTG = False

try:
    from Crypto.Cipher import AES as _AES
    from Crypto.Util import Counter as _Counter

    _HAS_PYCRYPTODOME = True
except ImportError:
    _HAS_PYCRYPTODOME = False
    _AES = None
    _Counter = None

try:
    import pyaes
except ImportError:
    pyaes = None


class AESMode(Enum):
    IGE = "ige"
    CTR = "ctr"


def _xor_blocks(a: bytes, b: bytes) -> bytes:
    """XOR two 16-byte blocks using integer ops (faster than per-byte zip)."""
    return (int.from_bytes(a, "big") ^ int.from_bytes(b, "big")).to_bytes(16, "big")


def _ige_crypt_ecb(key: bytes, iv: bytes, data: bytes, encrypt: bool, ecb_encrypt, ecb_decrypt) -> bytes:
    iv1, iv2 = iv[:16], iv[16:32]
    result = bytearray()

    for i in range(0, len(data), 16):
        block = data[i : i + 16]
        if len(block) < 16:
            block = block.ljust(16, b"\x00")
        if encrypt:
            xored = _xor_blocks(block, iv2)
            encrypted = ecb_encrypt(xored)
            out = _xor_blocks(encrypted, iv1)
            result.extend(out)
            iv1, iv2 = block, out
        else:
            xored = _xor_blocks(block, iv1)
            decrypted = ecb_decrypt(xored)
            out = _xor_blocks(decrypted, iv2)
            result.extend(out)
            iv1, iv2 = out, block
    return bytes(result)


def _ige_crypt_pycryptodome(key: bytes, iv: bytes, data: bytes, encrypt: bool) -> bytes:
    cipher = _AES.new(key, _AES.MODE_ECB)
    return _ige_crypt_ecb(
        key,
        iv,
        data,
        encrypt,
        cipher.encrypt,
        cipher.decrypt,
    )


def _ige_crypt_pure(key: bytes, iv: bytes, data: bytes, encrypt: bool) -> bytes:
    """Pure-Python AES-IGE using pyaes ECB as block primitive."""
    if pyaes is None:
        raise RuntimeError("Install cryptg, pycryptodome, or pyaes for AES-IGE support")

    aes = pyaes.AESModeOfOperationECB(key)
    return _ige_crypt_ecb(key, iv, data, encrypt, aes.encrypt, aes.decrypt)


def encrypt_ige(key: bytes, iv: bytes, data: bytes) -> bytes:
    if _HAS_CRYPTG:
        return cryptg.encrypt_ige(data, key, iv)
    if _HAS_PYCRYPTODOME:
        return _ige_crypt_pycryptodome(key, iv, data, encrypt=True)
    return _ige_crypt_pure(key, iv, data, encrypt=True)


def decrypt_ige(key: bytes, iv: bytes, data: bytes) -> bytes:
    if _HAS_CRYPTG:
        return cryptg.decrypt_ige(data, key, iv)
    if _HAS_PYCRYPTODOME:
        return _ige_crypt_pycryptodome(key, iv, data, encrypt=False)
    return _ige_crypt_pure(key, iv, data, encrypt=False)


def ctr_encrypt(key: bytes, iv: bytes, data: bytes) -> bytes:
    if _HAS_CRYPTG:
        return cryptg.encrypt_ctr(data, key, bytearray(iv[:16]))
    if _HAS_PYCRYPTODOME:
        ctr = _Counter.new(128, initial_value=int.from_bytes(iv[:16], "big"))
        cipher = _AES.new(key, _AES.MODE_CTR, counter=ctr)
        return cipher.encrypt(data)
    if pyaes is None:
        raise RuntimeError("Install cryptg, pycryptodome, or pyaes for AES-CTR support")
    ctr = pyaes.util.Counter(int.from_bytes(iv[:16], "big"))
    aes = pyaes.AESModeOfOperationCTR(key, counter=ctr)
    return aes.encrypt(data)
