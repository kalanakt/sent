"""Message wrapper type."""

from __future__ import annotations


class Message:
    """Wrapper around a TL Message object."""

    def __init__(self, client, message):
        self.client = client
        self._message = message

    def __getattr__(self, name):
        return getattr(self._message, name)

    async def reply(self, text, **kwargs):
        return await self.client.send_message(
            self.chat_id, text, reply_to=self.id, **kwargs
        )

    async def respond(self, text, **kwargs):
        return await self.client.send_message(self.chat_id, text, **kwargs)

    async def delete(self):
        return await self.client.delete_messages(self.chat_id, [self.id])

    async def edit(self, text, **kwargs):
        return await self.client.edit_message(self.chat_id, self.id, text, **kwargs)

    @property
    def text(self):
        return getattr(self._message, "message", "") or ""

    @property
    def chat_id(self):
        peer = getattr(self._message, "peer_id", None)
        if peer is None:
            return None
        if hasattr(peer, "user_id"):
            return peer.user_id
        if hasattr(peer, "channel_id"):
            return -peer.channel_id
        if hasattr(peer, "chat_id"):
            return -peer.chat_id
        return None
