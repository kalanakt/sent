"""Message read event."""

from __future__ import annotations

from sent.events.common import EventBuilder, EventCommon, register_event


@register_event
class MessageRead(EventBuilder):
    def build(self, update, others=None, client=None):
        cls_name = update.__class__.__name__
        if cls_name not in (
            "UpdateReadHistoryInbox",
            "UpdateReadHistoryOutbox",
            "UpdateReadChannelInbox",
            "UpdateReadChannelOutbox",
            "UpdateReadMessagesContents",
        ):
            return None
        event = MessageReadEvent(client, update)
        return event if self.filter(event) else None


class MessageReadEvent(EventCommon):
    @property
    def max_id(self):
        return getattr(self.original_update, "max_id", 0)

    @property
    def chat_id(self):
        upd = self.original_update
        if hasattr(upd, "channel_id"):
            return -upd.channel_id
        if hasattr(upd, "peer"):
            from sent.client.entity import get_peer_id

            return get_peer_id(upd.peer)
        return None
