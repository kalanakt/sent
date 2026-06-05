"""SQLite-backed session storage."""

from __future__ import annotations

import sqlite3
import time
from typing import Any, Optional, Tuple

from sent.network.dc import DEFAULT_DCS
from sent.sessions.abstract import Session


class SQLiteSession(Session):
    """Persistent session stored in SQLite."""

    def __init__(self, session_id: str):
        self.session_id = session_id
        self.filename = f"{session_id}.session"
        self._conn = sqlite3.connect(self.filename, check_same_thread=False)
        self._conn.execute("PRAGMA journal_mode=WAL")
        self._conn.execute("PRAGMA synchronous=NORMAL")
        self._create_tables()
        self._dc_id, self._server, self._port = self._load_dc()
        self._auth_key = self._load_auth_key()
        self._salt, self._session_id = self._load_mtproto_state()

    def _create_tables(self) -> None:
        self._conn.execute(
            "CREATE TABLE IF NOT EXISTS sessions ("
            "dc_id INTEGER PRIMARY KEY, server_address TEXT, port INTEGER, "
            "auth_key BLOB, salt INTEGER DEFAULT 0, session_id INTEGER DEFAULT NULL)"
        )
        self._conn.execute(
            "CREATE TABLE IF NOT EXISTS entities ("
            "id INTEGER PRIMARY KEY, hash INTEGER NOT NULL, username TEXT, "
            "phone TEXT, name TEXT, date INTEGER)"
        )
        self._conn.execute(
            "CREATE TABLE IF NOT EXISTS update_state ("
            "id INTEGER PRIMARY KEY, pts INTEGER, qts INTEGER, date INTEGER, seq INTEGER)"
        )
        self._conn.execute(
            "CREATE TABLE IF NOT EXISTS version (version INTEGER PRIMARY KEY)"
        )
        self._conn.commit()

        row = self._conn.execute("SELECT COUNT(*) FROM sessions").fetchone()
        if row[0] == 0:
            dc = DEFAULT_DCS[2]
            self._conn.execute(
                "INSERT INTO sessions VALUES (?, ?, ?, NULL, 0, NULL)",
                (dc.id, dc.ip, dc.port),
            )
            self._conn.commit()

    def _load_dc(self) -> Tuple[int, str, int]:
        row = self._conn.execute(
            "SELECT dc_id, server_address, port FROM sessions LIMIT 1"
        ).fetchone()
        return row[0], row[1], row[2]

    def _load_auth_key(self) -> Optional[bytes]:
        row = self._conn.execute("SELECT auth_key FROM sessions LIMIT 1").fetchone()
        return row[0] if row and row[0] else None

    def _load_mtproto_state(self) -> Tuple[int, Optional[int]]:
        try:
            row = self._conn.execute(
                "SELECT salt, session_id FROM sessions LIMIT 1"
            ).fetchone()
            if row:
                return row[0] or 0, row[1]
        except sqlite3.OperationalError:
            pass
        return 0, None

    def set_dc(self, dc_id: int, server_address: str, port: int) -> None:
        self._dc_id, self._server, self._port = dc_id, server_address, port
        self._conn.execute(
            "UPDATE sessions SET dc_id=?, server_address=?, port=?",
            (dc_id, server_address, port),
        )

    def get_dc(self) -> Tuple[int, str, int]:
        return self._dc_id, self._server, self._port

    def auth_key(self) -> Optional[bytes]:
        return self._auth_key

    def set_auth_key(self, auth_key: Optional[bytes]) -> None:
        self._auth_key = auth_key
        self._conn.execute("UPDATE sessions SET auth_key=?", (auth_key,))

    def save(self) -> None:
        self._conn.commit()

    def close(self) -> None:
        self._conn.close()

    def get_input_entity(self, key) -> Optional[Any]:
        if isinstance(key, str):
            row = self._conn.execute(
                "SELECT id, hash, username FROM entities WHERE username=? COLLATE NOCASE",
                (key.lstrip("@"),),
            ).fetchone()
        else:
            row = self._conn.execute(
                "SELECT id, hash, username FROM entities WHERE id=?", (key,)
            ).fetchone()
        if not row:
            return None
        entity_id, access_hash, username = row
        if entity_id > 0:
            from sent.tl.types.all import InputPeerUser

            return InputPeerUser(user_id=entity_id, access_hash=access_hash)
        from sent.tl.types.all import InputPeerChannel

        return InputPeerChannel(channel_id=abs(entity_id), access_hash=access_hash)

    def cache_input_entity(self, entity) -> None:
        entity_id = None
        access_hash = getattr(entity, "access_hash", 0) or 0
        username = getattr(entity, "username", None)
        if hasattr(entity, "user_id"):
            entity_id = entity.user_id
        elif hasattr(entity, "channel_id"):
            entity_id = -entity.channel_id
        elif hasattr(entity, "chat_id"):
            entity_id = -entity.chat_id
        elif hasattr(entity, "id"):
            entity_id = entity.id
            if getattr(entity, "broadcast", None) or getattr(entity, "megagroup", None):
                entity_id = -entity.id
        if entity_id is None:
            return
        self._conn.execute(
            "INSERT OR REPLACE INTO entities (id, hash, username, phone, name, date) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (
                entity_id,
                access_hash,
                username,
                getattr(entity, "phone", None),
                getattr(entity, "first_name", None) or getattr(entity, "title", None),
                int(time.time()),
            ),
        )

    def get_update_state(self) -> Tuple[int, int, int, int]:
        row = self._conn.execute(
            "SELECT pts, qts, date, seq FROM update_state WHERE id=0"
        ).fetchone()
        return row if row else (0, 0, 0, 0)

    def set_update_state(self, pts: int, qts: int, date: int, seq: int) -> None:
        self._conn.execute(
            "INSERT OR REPLACE INTO update_state VALUES (0, ?, ?, ?, ?)",
            (pts, qts, date, seq),
        )

    def get_salt(self) -> int:
        return self._salt

    def set_salt(self, salt: int) -> None:
        self._salt = salt
        self._conn.execute("UPDATE sessions SET salt=?", (salt,))

    def get_session_id(self) -> Optional[int]:
        return self._session_id

    def set_session_id(self, session_id: int) -> None:
        self._session_id = session_id
        self._conn.execute("UPDATE sessions SET session_id=?", (session_id,))

    def set_mtproto_state(self, salt: int, session_id: int) -> None:
        """Update salt and session_id in a single write."""
        self._salt = salt
        self._session_id = session_id
        self._conn.execute(
            "UPDATE sessions SET salt=?, session_id=?",
            (salt, session_id),
        )
