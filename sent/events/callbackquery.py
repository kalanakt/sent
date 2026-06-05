"""Callback query event."""

from __future__ import annotations

from sent.events.common import EventBuilder, EventCommon, register_event


@register_event
class CallbackQuery(EventBuilder):
    def build(self, update, others=None, client=None):
        cls_name = update.__class__.__name__
        if cls_name not in ("UpdateBotCallbackQuery", "UpdateInlineBotCallbackQuery"):
            return None
        if not hasattr(update, "data"):
            return None
        event = CallbackQueryEvent(client, update)
        return event if self.filter(event) else None


class CallbackQueryEvent(EventCommon):
    @property
    def id(self):
        return self.original_update.query_id

    @property
    def data(self):
        return self.original_update.data

    @property
    def chat_instance(self):
        return getattr(self.original_update, "chat_instance", None)

    @property
    def is_inline(self):
        return self.original_update.__class__.__name__ == "UpdateInlineBotCallbackQuery"

    async def answer(self, text=None, alert=False):
        if self.is_inline:
            return
        return await self.client.answer_callback_query(self.id, text=text, alert=alert)

    async def edit(self, text, **kwargs):
        msg_id = getattr(self.original_update, "msg_id", None)
        peer = getattr(self.original_update, "peer", None)
        if peer and msg_id:
            return await self.client.edit_message(peer, msg_id, text, **kwargs)

    async def delete(self):
        msg_id = getattr(self.original_update, "msg_id", None)
        peer = getattr(self.original_update, "peer", None)
        if peer and msg_id:
            return await self.client.delete_messages(peer, [msg_id])

    async def respond(self, text, **kwargs):
        peer = getattr(self.original_update, "peer", None)
        if peer:
            return await self.client.send_message(peer, text, **kwargs)
