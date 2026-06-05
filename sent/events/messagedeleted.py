"""Message deleted event."""

from __future__ import annotations

from sent.events.common import EventBuilder, EventCommon, register_event


@register_event
class MessageDeleted(EventBuilder):
    def build(self, update, others=None, client=None):
        cls_name = update.__class__.__name__
        if cls_name not in (
            "UpdateDeleteMessages",
            "UpdateDeleteChannelMessages",
            "UpdateDeleteScheduledMessages",
        ):
            return None
        event = MessageDeletedEvent(client, update)
        return event if self.filter(event) else None


class MessageDeletedEvent(EventCommon):
    @property
    def deleted_ids(self):
        return getattr(self.original_update, "messages", [])

    @property
    def chat_id(self):
        upd = self.original_update
        if hasattr(upd, "channel_id"):
            return -upd.channel_id
        return None
