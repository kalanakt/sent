"""Base event classes."""

from __future__ import annotations

import re
from typing import Any, Callable, List, Optional, Pattern, Union


class EventCommon:
    """Base class for all events."""

    def __init__(self, client, update):
        self.client = client
        self.original_update = update


class EventBuilder:
    """Base event builder with filtering."""

    def __init__(
        self,
        chats=None,
        *,
        func: Optional[Callable] = None,
        incoming: Optional[bool] = None,
        outgoing: Optional[bool] = None,
        pattern: Optional[Union[str, Pattern]] = None,
        from_users=None,
        forwards: Optional[bool] = None,
    ):
        self.chats = chats if chats is None else (
            [chats] if not isinstance(chats, (list, tuple, set)) else list(chats)
        )
        self.func = func
        self.incoming = incoming
        self.outgoing = outgoing
        self.pattern = re.compile(pattern) if isinstance(pattern, str) else pattern
        self.from_users = from_users if from_users is None else (
            [from_users] if not isinstance(from_users, (list, tuple, set)) else list(from_users)
        )
        self.forwards = forwards

    def build(self, update, others=None, client=None):
        raise NotImplementedError

    def filter(self, event) -> bool:
        if self.func and not self.func(event):
            return False
        if self.pattern and hasattr(event, "message"):
            text = getattr(event.message, "message", "") or ""
            if not self.pattern.search(text):
                return False
        if self.incoming is not None and hasattr(event, "out"):
            if self.incoming and event.out:
                return False
            if not self.incoming and not event.out:
                return False
        if self.outgoing is not None and hasattr(event, "out"):
            if self.outgoing and not event.out:
                return False
            if not self.outgoing and event.out:
                return False
        if self.chats is not None and hasattr(event, "chat_id"):
            if event.chat_id not in self.chats:
                return False
        if self.from_users is not None and hasattr(event, "sender_id"):
            if event.sender_id not in self.from_users:
                return False
        if self.forwards is not None and hasattr(event, "message"):
            fwd = getattr(event.message, "fwd_from", None)
            if self.forwards and not fwd:
                return False
            if not self.forwards and fwd:
                return False
        return True

    def __call__(self, func):
        func._event_builder = self
        return func


def register_event(cls):
    cls._event_name = cls.__name__
    return cls
