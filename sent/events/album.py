"""Album (grouped media) event."""

from __future__ import annotations

from sent.events.common import EventBuilder, register_event
from sent.events.newmessage import MessageEvent


@register_event
class Album(EventBuilder):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._buffer = {}

    def build(self, update, others=None, client=None):
        message = getattr(update, "message", None)
        if message is None:
            return None
        grouped_id = getattr(message, "grouped_id", None)
        if not grouped_id:
            return None
        key = (client, grouped_id)
        self._buffer.setdefault(key, []).append(message)
        if len(self._buffer[key]) < 2:
            return None
        events = [
            MessageEvent(client, msg, update) for msg in self._buffer.pop(key)
        ]
        filtered = [e for e in events if self.filter(e)]
        return filtered or None
