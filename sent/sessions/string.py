"""String-based portable session."""

from __future__ import annotations

import base64
import struct
import time
from typing import Any, Dict, Optional, Tuple

from sent.network.dc import DEFAULT_DCS, get_dc
from sent.sessions.abstract import Session


class StringSession(Session):
    """Session encoded as a base64 string for portability."""

    CURRENT_VERSION = "1"

    def __init__(self, string: Optional[str] = None):
        self._dc_id = 2
        dc = DEFAULT_DCS[2]
        self._server = dc.ip
        self._port = dc.port
        self._auth_key: Optional[bytes] = None
        self._entities: Dict = {}
        self._username_entities: Dict[str, Any] = {}
        self._pts = self._qts = self._date = self._seq = 0
        self._salt = 0
        self._session_id: Optional[int] = None
        if string:
            self._decode(string)

    def _decode(self, string: str) -> None:
        if string.startswith("1"):
            string = string[1:]
        data = base64.urlsafe_b64decode(string + "==")
        self._dc_id = struct.unpack("<i", data[:4])[0]
        dc = get_dc(self._dc_id)
        if dc:
            self._server = dc.ip
            self._port = dc.port
        if len(data) > 4:
            self._auth_key = data[4:]

    def save(self) -> str:
        data = struct.pack("<i", self._dc_id)
        if self._auth_key:
            data += self._auth_key
        return self.CURRENT_VERSION + base64.urlsafe_b64encode(data).decode("ascii").rstrip("=")

    def set_dc(self, dc_id: int, server_address: str, port: int) -> None:
        self._dc_id = dc_id
        self._server = server_address
        self._port = port

    def get_dc(self) -> Tuple[int, str, int]:
        return self._dc_id, self._server, self._port

    def auth_key(self) -> Optional[bytes]:
        return self._auth_key

    def set_auth_key(self, auth_key: Optional[bytes]) -> None:
        self._auth_key = auth_key

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
