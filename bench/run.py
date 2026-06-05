#!/usr/bin/env python3
"""Lightweight benchmarks for sent optimization tiers."""

from __future__ import annotations

import os
import sys
import tempfile
import timeit

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)


def _report(name: str, seconds: float, iterations: int) -> None:
    per_op_us = (seconds / iterations) * 1_000_000
    print(f"{name:40s} {iterations:>8d} iters  {seconds:>8.4f}s  {per_op_us:>10.2f} us/op")


def bench_tl_roundtrip(iterations: int = 5000) -> None:
    from sent.tl.serialization import BinaryReader, BinaryWriter
    from sent.tl.types.all import InputPeerEmpty

    obj = InputPeerEmpty()

    def run() -> None:
        raw = bytes(obj)
        restored = InputPeerEmpty.from_reader(BinaryReader(raw[4:]))
        assert isinstance(restored, InputPeerEmpty)

    elapsed = timeit.timeit(run, number=iterations)
    _report("tl_serialize_deserialize", elapsed, iterations)


def bench_vector_roundtrip(iterations: int = 2000) -> None:
    from sent.tl.serialization import BinaryReader, BinaryWriter
    from sent.tl.types.all import InputPeerEmpty

    items = [InputPeerEmpty() for _ in range(10)]

    def run() -> None:
        data = BinaryWriter.serialize_vector(items)
        result = BinaryReader(data).tgread_vector()
        assert len(result) == 10

    elapsed = timeit.timeit(run, number=iterations)
    _report("tl_vector_roundtrip", elapsed, iterations)


def bench_message_pack_unpack(iterations: int = 2000) -> None:
    from sent.crypto.auth_key import AuthKey
    from sent.network.mtprotostate import MTProtoState
    from sent.tl.types.all import Pong

    key = AuthKey(b"\xab" * 256)
    state = MTProtoState(key, session_id=12345, salt=67890)
    body = bytes(Pong(msg_id=1, ping_id=42))

    def run() -> None:
        packed = state.pack_message(body)
        msg_id, seq_no, restored = state.unpack_message(packed)
        assert len(restored) == len(body)
        assert restored == body

    elapsed = timeit.timeit(run, number=iterations)
    _report("mtproto_pack_unpack", elapsed, iterations)


def bench_sqlite_persist(iterations: int = 1000) -> None:
    from sent.sessions.sqlite import SQLiteSession

    with tempfile.TemporaryDirectory() as tmp:
        cwd = os.getcwd()
        os.chdir(tmp)
        try:
            session = SQLiteSession("bench")

            def run() -> None:
                session.set_mtproto_state(111, 222)
                session.save()

            elapsed = timeit.timeit(run, number=iterations)
            _report("sqlite_mtproto_persist", elapsed, iterations)
            session.close()
        finally:
            os.chdir(cwd)


def bench_import_sent(iterations: int = 5) -> None:
    import importlib

    def run() -> None:
        importlib.invalidate_caches()
        if "sent" in sys.modules:
            for name in list(sys.modules):
                if name == "sent" or name.startswith("sent."):
                    del sys.modules[name]
        importlib.import_module("sent")

    elapsed = timeit.timeit(run, number=iterations)
    _report("import_sent", elapsed, iterations)


def main() -> None:
    print("sent benchmark harness")
    print("-" * 72)
    bench_tl_roundtrip()
    bench_vector_roundtrip()
    bench_message_pack_unpack()
    bench_sqlite_persist()
    bench_import_sent()
    print("-" * 72)
    print("Done.")


if __name__ == "__main__":
    main()
