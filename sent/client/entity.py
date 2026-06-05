"""Entity resolution and caching."""

from __future__ import annotations

from collections import OrderedDict
from typing import Any, Dict, Optional


class EntityCache:
    """Cache for resolved Telegram entities with LRU eviction."""

    def __init__(self, session=None, limit: int = 5000):
        self._session = session
        self._limit = limit
        self._cache: "OrderedDict" = OrderedDict()
        self._username_cache: Dict[str, Any] = {}

    def get(self, key) -> Optional[Any]:
        if key in self._cache:
            self._cache.move_to_end(key)
            return self._cache[key]
        if self._session:
            entity = self._session.get_input_entity(key)
            if entity is not None:
                self.add(entity)
                return entity
        return None

    def add(self, entity) -> None:
        keys = []
        if hasattr(entity, "id"):
            keys.append(entity.id)
        if hasattr(entity, "user_id"):
            keys.append(entity.user_id)
        if hasattr(entity, "channel_id"):
            keys.append(entity.channel_id)
        if hasattr(entity, "chat_id"):
            keys.append(entity.chat_id)

        for key in keys:
            self._cache[key] = entity
            self._cache.move_to_end(key)

        if hasattr(entity, "username") and entity.username:
            self._username_cache[entity.username.lower()] = entity

        while len(self._cache) > self._limit:
            self._cache.popitem(last=False)

        if self._session:
            self._session.cache_input_entity(entity)

    def get_by_username(self, username: str) -> Optional[Any]:
        username = username.lstrip("@").lower()
        if username in self._username_cache:
            return self._username_cache[username]
        if self._session:
            entity = self._session.get_input_entity(username)
            if entity is not None:
                self.add(entity)
                return entity
        return None


def get_peer_id(peer) -> int:
    """Extract numeric peer ID from a peer object."""
    if isinstance(peer, int):
        return peer
    if hasattr(peer, "user_id"):
        return peer.user_id
    if hasattr(peer, "channel_id"):
        return -peer.channel_id
    if hasattr(peer, "chat_id"):
        return -peer.chat_id
    if hasattr(peer, "id"):
        return peer.id
    raise ValueError(f"Cannot extract peer ID from {peer!r}")
