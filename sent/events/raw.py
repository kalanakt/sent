"""Raw update event."""

from sent.events.common import EventBuilder, EventCommon, register_event


@register_event
class Raw(EventBuilder):
    def build(self, update, others=None, client=None):
        event = RawEvent(client, update)
        if not self.filter(event):
            return None
        return event


class RawEvent(EventCommon):
    def __init__(self, client, update):
        super().__init__(client, update)
        self.update = update
