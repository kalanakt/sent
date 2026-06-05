"""Conversation context manager."""

from __future__ import annotations

import asyncio
from typing import Optional


class Conversation:
    """Simple conversation helper for waiting on replies."""

    def __init__(self, client, entity, *, timeout: float = 60.0):
        self.client = client
        self.entity = entity
        self.timeout = timeout
        self._event = asyncio.Event()
        self._message = None
        self._handler = None

    async def __aenter__(self):
        from sent.events import NewMessage

        entity = await self.client.get_input_entity(self.entity)
        chat_id = getattr(entity, "user_id", None) or getattr(entity, "channel_id", None) or getattr(entity, "chat_id", None)

        async def handler(event):
            if chat_id and event.chat_id != chat_id:
                return
            self._message = event
            self._event.set()

        self._handler = handler
        self.client.add_event_handler(handler, NewMessage(chats=chat_id))
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self._handler:
            self.client.remove_event_handler(self._handler)

    async def get_response(self, *, timeout: Optional[float] = None):
        try:
            await asyncio.wait_for(self._event.wait(), timeout=timeout or self.timeout)
        except asyncio.TimeoutError:
            return None
        return self._message

    async def send_message(self, text: str, **kwargs):
        return await self.client.send_message(self.entity, text, **kwargs)
