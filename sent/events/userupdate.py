"""User update event."""

from __future__ import annotations

from sent.events.common import EventBuilder, EventCommon, register_event

_USER_UPDATES = {
    "UpdateUserStatus",
    "UpdateUserName",
    "UpdateUserPhone",
    "UpdateUserTyping",
    "UpdateUserEmojiStatus",
}


@register_event
class UserUpdate(EventBuilder):
    def build(self, update, others=None, client=None):
        if update.__class__.__name__ not in _USER_UPDATES:
            return None
        event = UserUpdateEvent(client, update)
        return event if self.filter(event) else None


class UserUpdateEvent(EventCommon):
    @property
    def user_id(self):
        return getattr(self.original_update, "user_id", None)

    @property
    def status(self):
        return getattr(self.original_update, "status", None)

    @property
    def first_name(self):
        return getattr(self.original_update, "first_name", None)

    @property
    def last_name(self):
        return getattr(self.original_update, "last_name", None)
