"""Abstract session interface."""

from __future__ import annotations

import abc
from typing import Any, Optional, Tuple


class Session(abc.ABC):
    """Abstract session storage."""

    @abc.abstractmethod
    def set_dc(self, dc_id: int, server_address: str, port: int) -> None:
        pass

    @abc.abstractmethod
    def get_dc(self) -> Tuple[int, str, int]:
        pass

    @abc.abstractmethod
    def auth_key(self) -> Optional[bytes]:
        pass

    @abc.abstractmethod
    def set_auth_key(self, auth_key: Optional[bytes]) -> None:
        pass

    @abc.abstractmethod
    def save(self) -> None:
        pass

    @abc.abstractmethod
    def close(self) -> None:
        pass

    # Entity cache
    @abc.abstractmethod
    def get_input_entity(self, key) -> Optional[Any]:
        pass

    @abc.abstractmethod
    def cache_input_entity(self, entity) -> None:
        pass

    # Update state
    @abc.abstractmethod
    def get_update_state(self) -> Tuple[int, int, int, int]:
        pass

    @abc.abstractmethod
    def set_update_state(self, pts: int, qts: int, date: int, seq: int) -> None:
        pass

    def get_salt(self) -> int:
        return 0

    def set_salt(self, salt: int) -> None:
        pass

    def get_session_id(self) -> Optional[int]:
        return None

    def set_session_id(self, session_id: int) -> None:
        pass
