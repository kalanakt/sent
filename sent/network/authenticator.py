"""MTProto auth key creation (Diffie-Hellman handshake)."""

from __future__ import annotations

import os
import struct
import time

from sent.crypto.auth_key import AuthKey
from sent.crypto.factorization import factorize
from sent.crypto.mtproto2 import sha1, sha256
from sent.crypto.rsa import encrypt as rsa_encrypt
from sent.network.connection import Connection
from sent.tl.functions.all import ReqDHParams, ReqPqMulti, SetClientDHParams
from sent.tl.serialization import BinaryReader
from sent.tl.tlobject import read_object
from sent.tl.types.all import ClientDHInnerData, PQInnerData, ServerDHInnerData

_G = 3


def _pq_string(n: int) -> str:
    return n.to_bytes((n.bit_length() + 7) // 8, "big").decode("latin1")


async def do_authentication(connection: Connection) -> AuthKey:
    """Perform the MTProto auth key creation handshake."""
    nonce = os.urandom(16)
    new_nonce = os.urandom(32)

    res_pq = await _send_unencrypted(connection, ReqPqMulti(nonce=nonce))
    server_nonce = res_pq.server_nonce
    pq_int = int.from_bytes(
        res_pq.pq.encode("latin1") if isinstance(res_pq.pq, str) else res_pq.pq,
        "big",
    )
    p, q = factorize(pq_int)

    inner_data = PQInnerData(
        pq=res_pq.pq,
        p=_pq_string(p),
        q=_pq_string(q),
        nonce=nonce,
        server_nonce=server_nonce,
        new_nonce=new_nonce,
    )
    fingerprint = res_pq.server_public_key_fingerprints[0]
    encrypted_data = rsa_encrypt(bytes(inner_data), fingerprint)

    dh_params = await _send_unencrypted(
        connection,
        ReqDHParams(
            nonce=nonce,
            server_nonce=server_nonce,
            p=_pq_string(p),
            q=_pq_string(q),
            public_key_fingerprint=fingerprint,
            encrypted_data=encrypted_data.decode("latin1"),
        ),
    )

    if hasattr(dh_params, "new_nonce_hash"):
        raise ConnectionError("DH params failed")

    answer = _decrypt_server_dh(
        dh_params.encrypted_answer.encode("latin1")
        if isinstance(dh_params.encrypted_answer, str)
        else dh_params.encrypted_answer,
        nonce,
        server_nonce,
        new_nonce,
    )
    inner = ServerDHInnerData.from_reader(BinaryReader(answer))
    g_a = int.from_bytes(
        inner.g_a.encode("latin1") if isinstance(inner.g_a, str) else inner.g_a,
        "big",
    )
    dh_prime = int.from_bytes(
        inner.dh_prime.encode("latin1")
        if isinstance(inner.dh_prime, str)
        else inner.dh_prime,
        "big",
    )

    b = int.from_bytes(os.urandom(256), "big") % (dh_prime - 1) or 1
    g_b = pow(_G, b, dh_prime)
    auth_key_int = pow(g_a, b, dh_prime)
    auth_key = auth_key_int.to_bytes(256, "big")

    client_inner = ClientDHInnerData(
        nonce=nonce,
        server_nonce=server_nonce,
        retry_id=0,
        g_b=g_b.to_bytes(256, "big").decode("latin1"),
    )
    encrypted_client = _encrypt_client_dh(
        bytes(client_inner), nonce, server_nonce, new_nonce
    )

    result = await _send_unencrypted(
        connection,
        SetClientDHParams(
            nonce=nonce,
            server_nonce=server_nonce,
            encrypted_data=encrypted_client.decode("latin1"),
        ),
    )

    if not hasattr(result, "new_nonce_hash1"):
        raise ConnectionError(f"DH gen failed: {result}")

    return AuthKey(auth_key)


def _decrypt_server_dh(
    data: bytes, nonce: bytes, server_nonce: bytes, new_nonce: bytes
) -> bytes:
    tmp_key = sha256(new_nonce + server_nonce) + sha256(server_nonce + new_nonce)
    from sent.crypto.aes import decrypt_ige

    return decrypt_ige(tmp_key[:32], tmp_key[32:48] + tmp_key[48:64], data)


def _encrypt_client_dh(
    data: bytes, nonce: bytes, server_nonce: bytes, new_nonce: bytes
) -> bytes:
    tmp_key = sha256(new_nonce + server_nonce) + sha256(server_nonce + new_nonce)
    from sent.crypto.aes import encrypt_ige

    return encrypt_ige(tmp_key[:32], tmp_key[32:48] + tmp_key[48:64], data)


async def _send_unencrypted(connection: Connection, request) -> object:
    body = bytes(request)
    msg_id = (int(time.time()) << 32) | (os.urandom(4)[0] << 24)
    message = struct.pack("<q", 0) + struct.pack("<q", msg_id) + struct.pack("<i", len(body)) + body
    await connection.send(message)
    response = await connection.recv()
    reader = BinaryReader(response[20:])
    return read_object(reader)
