"""Chat action event."""

from __future__ import annotations

from sent.events.common import EventBuilder, EventCommon, register_event


@register_event
class ChatAction(EventBuilder):
    def build(self, update, others=None, client=None):
        message = getattr(update, "message", None)
        if message is None:
            return None
        action = getattr(message, "action", None)
        if action is None:
            return None
        event = ChatActionEvent(client, update, message, action)
        return event if self.filter(event) else None


class ChatActionEvent(EventCommon):
    def __init__(self, client, update, message, action):
        super().__init__(client, update)
        self.message = message
        self.action = action
        self.action_message = message
        peer = getattr(message, "peer_id", None)
        if peer is not None:
            from sent.client.entity import get_peer_id

            self.chat_id = get_peer_id(peer)
        else:
            self.chat_id = None

    @property
    def user_joined(self):
        return self.action.__class__.__name__ == "MessageActionChatAddUser"

    @property
    def user_left(self):
        return self.action.__class__.__name__ in (
            "MessageActionChatDeleteUser",
            "MessageActionChatLeave",
        )

    @property
    def new_title(self):
        if self.action.__class__.__name__ == "MessageActionChatEditTitle":
            return getattr(self.action, "title", None)
        return None
