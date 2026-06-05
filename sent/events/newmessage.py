"""NewMessage event."""

from __future__ import annotations

from sent.events.common import EventBuilder, EventCommon, register_event


@register_event
class NewMessage(EventBuilder):
    """Event fired on new incoming/outgoing messages."""

    def build(self, update, others=None, client=None):
        from sent.client.message import Message

        if hasattr(update, "message"):
            msg = update.message
        elif hasattr(update, "messages") and update.messages:
            msg = update.messages[0]
        else:
            return None

        event = MessageEvent(client, msg, update)
        if not self.filter(event):
            return None
        return event


class MessageEvent(EventCommon):
    """New message event instance."""

    def __init__(self, client, message, update):
        super().__init__(client, update)
        self.message = message
        self.text = getattr(message, "message", "") or ""
        self.raw_text = self.text
        self.out = getattr(message, "out", False)
        peer = getattr(message, "peer_id", None)
        if peer is not None:
            from sent.client.entity import get_peer_id

            self.chat_id = get_peer_id(peer)
        else:
            self.chat_id = getattr(message, "chat_id", None)
        self.sender_id = getattr(message, "sender_id", None) or getattr(
            getattr(message, "from_id", None), "user_id", None
        )

    @property
    def id(self):
        return self.message.id

    async def reply(self, text: str, **kwargs):
        return await self.client.send_message(self.chat_id, text, reply_to=self.id, **kwargs)

    async def respond(self, text: str, **kwargs):
        return await self.client.send_message(self.chat_id, text, **kwargs)

    async def delete(self):
        return await self.client.delete_messages(self.chat_id, [self.id])

    async def edit(self, text: str, **kwargs):
        return await self.client.edit_message(self.chat_id, self.id, text, **kwargs)

    async def forward_to(self, entity, **kwargs):
        return await self.client.forward_messages(entity, self.message, **kwargs)

    async def get_chat(self):
        return await self.client.get_entity(self.chat_id)

    async def get_sender(self):
        if self.sender_id:
            return await self.client.get_entity(self.sender_id)
        return None

    async def download_media(self, file=None, **kwargs):
        return await self.client.download_media(self.message, file=file, **kwargs)

    async def mark_read(self):
        return await self.client.send_read_acknowledge(self.chat_id, max_id=self.id)
