"""In-memory session (no persistence)."""

from __future__ import annotations

from typing import Any, Dict, Optional, Tuple

from sent.network.dc import DEFAULT_DCS
from sent.sessions.abstract import Session


class MemorySession(Session):
    """Session stored in memory only."""

    def __init__(self):
        dc = DEFAULT_DCS[2]
        self._dc_id = dc.id
        self._server_address = dc.ip
        self._port = dc.port
        self._auth_key: Optional[bytes] = None
        self._entities: Dict = {}
        self._username_entities: Dict[str, Any] = {}
        self._pts = 0
        self._qts = 0
        self._date = 0
        self._seq = 0
        self._salt = 0
        self._session_id: Optional[int] = None

    def set_dc(self, dc_id: int, server_address: str, port: int) -> None:
        self._dc_id = dc_id
        self._server_address = server_address
        self._port = port

    def get_dc(self) -> Tuple[int, str, int]:
        return self._dc_id, self._server_address, self._port

    def auth_key(self) -> Optional[bytes]:
        return self._auth_key

    def set_auth_key(self, auth_key: Optional[bytes]) -> None:
        self._auth_key = auth_key

    def save(self) -> None:
        pass

    def close(self) -> None:
        pass

    def get_input_entity(self, key) -> Optional[Any]:
        if isinstance(key, str):
            return self._username_entities.get(key.lower())
        return self._entities.get(key)

    def cache_input_entity(self, entity) -> None:
        if hasattr(entity, "user_id"):
            self._entities[entity.user_id] = entity
        elif hasattr(entity, "channel_id"):
            self._entities[entity.channel_id] = entity
        elif hasattr(entity, "chat_id"):
            self._entities[entity.chat_id] = entity
        elif hasattr(entity, "id"):
            self._entities[entity.id] = entity
        if hasattr(entity, "username") and entity.username:
            self._username_entities[entity.username.lower()] = entity

    def get_update_state(self) -> Tuple[int, int, int, int]:
        return self._pts, self._qts, self._date, self._seq

    def set_update_state(self, pts: int, qts: int, date: int, seq: int) -> None:
        self._pts, self._qts, self._date, self._seq = pts, qts, date, seq

    def get_salt(self) -> int:
        return self._salt

    def set_salt(self, salt: int) -> None:
        self._salt = salt

    def get_session_id(self) -> Optional[int]:
        return self._session_id

    def set_session_id(self, session_id: int) -> None:
        self._session_id = session_id
