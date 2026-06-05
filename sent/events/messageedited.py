"""MessageEdited event."""

from sent.events.common import EventBuilder, register_event
from sent.events.newmessage import MessageEvent


@register_event
class MessageEdited(EventBuilder):
    def build(self, update, others=None, client=None):
        if not hasattr(update, "message") or not update.message:
            return None
        if not getattr(update.message, "edit_date", None):
            return None
        event = MessageEvent(client, update.message, update)
        if not self.filter(event):
            return None
        return event
