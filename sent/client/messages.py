"""Message sending and editing methods."""

from __future__ import annotations

import random
from typing import List


class MessageMethods:
    """Mixin providing message-related methods."""

    async def send_message(
        self,
        entity,
        message: str,
        *,
        reply_to: int = None,
        parse_mode: str = None,
        link_preview: bool = True,
        file=None,
        thumb=None,
        force_document: bool = False,
        buttons=None,
        silent: bool = None,
        schedule=None,
        comment_to: int = None,
    ):
        """Send a text message to a user, chat, or channel.

        Args:
            entity: Username, ID, or TL peer to send to.
            message: Text content of the message.
            reply_to: Message ID to reply to.
            parse_mode: Markdown parse mode for formatting.
            link_preview: Whether to show link previews.
            file: Optional file path or bytes to attach.
            buttons: Inline or reply keyboard markup.
            silent: Send without notification sound.
            schedule: Unix timestamp to schedule the message.
            comment_to: Post ID to comment on in a channel discussion.

        Returns:
            The sent Message object.
        """
        entity = await self.get_input_entity(entity)
        if parse_mode:
            from sent.client.buttons import parse_markdown

            message = parse_markdown(message)

        if file is not None:
            return await self.send_file(
                entity,
                file,
                caption=message,
                reply_to=reply_to,
                buttons=buttons,
                silent=silent,
            )

        from sent.tl.functions.messages import MessagesSendMessage

        result = await self(
            MessagesSendMessage(
                peer=entity,
                message=message,
                random_id=self._random_id(),
                reply_to=self._build_reply_to(reply_to) if reply_to else None,
                no_webpage=not link_preview,
                silent=silent,
                schedule_date=schedule,
                reply_markup=self._build_reply_markup(buttons),
            )
        )
        return self._get_message_from_updates(result)

    async def edit_message(
        self,
        entity,
        message: int,
        text: str = None,
        *,
        buttons=None,
        parse_mode: str = None,
    ):
        entity = await self.get_input_entity(entity)
        if parse_mode and text:
            from sent.client.buttons import parse_markdown

            text = parse_markdown(text)
        from sent.tl.functions.messages import MessagesEditMessage

        result = await self(
            MessagesEditMessage(
                peer=entity,
                id=getattr(message, "id", message),
                message=text,
                reply_markup=self._build_reply_markup(buttons),
            )
        )
        return self._get_message_from_updates(result)

    async def delete_messages(self, entity, message_ids: List[int], *, revoke: bool = True):
        entity = await self.get_input_entity(entity)
        if not isinstance(message_ids, list):
            message_ids = [message_ids]
        message_ids = [getattr(m, "id", m) for m in message_ids]

        cls_name = entity.__class__.__name__
        if "Channel" in cls_name or "InputPeerChannel" in cls_name:
            from sent.tl.functions.channels import ChannelsDeleteMessages

            return await self(ChannelsDeleteMessages(channel=entity, id=message_ids))

        from sent.tl.functions.messages import MessagesDeleteMessages

        return await self(MessagesDeleteMessages(id=message_ids, revoke=revoke))

    async def forward_messages(
        self,
        entity,
        messages,
        from_peer=None,
        *,
        silent: bool = None,
        schedule=None,
    ):
        entity = await self.get_input_entity(entity)
        if not isinstance(messages, list):
            messages = [messages]
        ids = [getattr(m, "id", m) for m in messages]
        if from_peer is None and messages:
            msg = messages[0]
            from_peer = getattr(msg, "peer_id", None) or getattr(msg, "chat_id", None)
        from_peer = await self.get_input_entity(from_peer)

        from sent.tl.functions.messages import MessagesForwardMessages

        result = await self(
            MessagesForwardMessages(
                from_peer=from_peer,
                id=ids,
                random_id=[self._random_id() for _ in ids],
                to_peer=entity,
                silent=silent,
                schedule_date=schedule,
            )
        )
        return self._get_message_from_updates(result)

    async def get_messages(
        self,
        entity,
        ids=None,
        *,
        limit: int = None,
        offset_date=None,
        offset_id: int = 0,
        max_id: int = 0,
        min_id: int = 0,
        search: str = None,
        from_user=None,
        reverse: bool = False,
    ):
        entity = await self.get_input_entity(entity)
        if ids is not None:
            if not isinstance(ids, list):
                ids = [ids]
            ids = [getattr(i, "id", i) for i in ids]
            from sent.tl.functions.messages import MessagesGetMessages

            result = await self(MessagesGetMessages(id=ids))
            return result.messages if hasattr(result, "messages") else result

        if search:
            from sent.tl.functions.messages import MessagesSearch

            result = await self(
                MessagesSearch(
                    peer=entity,
                    q=search,
                    filter=None,
                    min_date=0,
                    max_date=0,
                    offset_id=offset_id,
                    add_offset=0,
                    limit=limit or 100,
                    max_id=max_id,
                    min_id=min_id,
                    hash=0,
                    from_id=await self.get_input_entity(from_user) if from_user else None,
                )
            )
            return getattr(result, "messages", [])

        from sent.tl.functions.messages import MessagesGetHistory

        result = await self(
            MessagesGetHistory(
                peer=entity,
                offset_id=offset_id,
                offset_date=offset_date or 0,
                add_offset=0,
                limit=limit or 100,
                max_id=max_id,
                min_id=min_id,
                hash=0,
            )
        )
        messages = getattr(result, "messages", [])
        return list(reversed(messages)) if reverse else messages

    async def iter_messages(self, entity, **kwargs):
        entity = await self.get_input_entity(entity)
        offset_id = kwargs.get("offset_id", 0)
        limit = kwargs.get("limit", 100)
        reverse = kwargs.get("reverse", False)
        while True:
            messages = await self.get_messages(
                entity, limit=limit, offset_id=offset_id, **{
                    k: v for k, v in kwargs.items()
                    if k not in ("offset_id", "limit")
                }
            )
            if not messages:
                break
            for msg in messages:
                yield msg
            offset_id = messages[-1].id if not reverse else messages[0].id
            if len(messages) < limit:
                break

    async def pin_message(self, entity, message, *, notify: bool = False):
        entity = await self.get_input_entity(entity)
        msg_id = getattr(message, "id", message)
        from sent.tl.functions.messages import MessagesUpdatePinnedMessage

        return await self(
            MessagesUpdatePinnedMessage(peer=entity, id=msg_id, silent=not notify)
        )

    async def unpin_message(self, entity, message=None):
        entity = await self.get_input_entity(entity)
        if message is None:
            from sent.tl.functions.messages import MessagesUnpinAllMessages

            return await self(MessagesUnpinAllMessages(peer=entity))
        from sent.tl.functions.messages import MessagesUpdatePinnedMessage

        return await self(
            MessagesUpdatePinnedMessage(peer=entity, id=0, silent=True)
        )

    async def send_poll(
        self,
        entity,
        question: str,
        options: List[str],
        *,
        multiple_choice: bool = False,
        quiz: bool = False,
        correct_answer: int = None,
    ):
        entity = await self.get_input_entity(entity)
        from sent.tl.functions.messages import MessagesSendMedia
        from sent.tl.types.all import InputMediaPoll, Poll, PollAnswer, TextWithEntities

        answers = [
            PollAnswer(text=TextWithEntities(text=o, entities=[]), option=bytes([i]))
            for i, o in enumerate(options)
        ]
        poll = Poll(
            id=random.randint(0, 2**63 - 1),
            question=TextWithEntities(text=question, entities=[]),
            answers=answers,
            closed=False,
            public_voters=False,
            multiple_choice=multiple_choice,
            quiz=quiz,
        )
        result = await self(
            MessagesSendMedia(
                peer=entity,
                media=InputMediaPoll(poll=poll, correct_answers=[correct_answer] if correct_answer is not None else []),
                message="",
                random_id=self._random_id(),
            )
        )
        return self._get_message_from_updates(result)

    async def send_reaction(self, entity, message, reaction):
        entity = await self.get_input_entity(entity)
        msg_id = getattr(message, "id", message)
        from sent.tl.functions.messages import MessagesSendReaction
        from sent.tl.types.all import ReactionEmoji

        if isinstance(reaction, str):
            reaction = [ReactionEmoji(emoticon=reaction)]
        result = await self(
            MessagesSendReaction(
                peer=entity,
                msg_id=msg_id,
                reaction=reaction,
            )
        )
        return result

    async def set_typing(self, entity, action=None):
        entity = await self.get_input_entity(entity)
        from sent.tl.functions.messages import MessagesSetTyping
        from sent.tl.types.all import SendMessageTypingAction

        return await self(
            MessagesSetTyping(
                peer=entity,
                action=action or SendMessageTypingAction(),
            )
        )

    async def send_read_acknowledge(self, entity, *, max_id: int = 0):
        entity = await self.get_input_entity(entity)
        cls_name = entity.__class__.__name__
        if "Channel" in cls_name or "InputPeerChannel" in cls_name:
            from sent.tl.functions.channels import ChannelsReadHistory

            return await self(ChannelsReadHistory(channel=entity, max_id=max_id))
        from sent.tl.functions.messages import MessagesReadHistory

        return await self(MessagesReadHistory(peer=entity, max_id=max_id))

    def conversation(self, entity, *, timeout: float = 60.0):
        from sent.client.conversation import Conversation

        return Conversation(self, entity, timeout=timeout)

    def _get_message_from_updates(self, updates):
        if hasattr(updates, "updates"):
            for u in updates.updates:
                if hasattr(u, "message"):
                    return u.message
        if hasattr(updates, "message"):
            return updates.message
        return updates

    def _build_reply_to(self, reply_to):
        from sent.tl.types.all import InputReplyToMessage

        return InputReplyToMessage(reply_to_msg_id=reply_to)

    def _build_reply_markup(self, buttons):
        if buttons is None:
            return None
        if hasattr(buttons, "_bytes"):
            return buttons
        return buttons

    def _random_id(self) -> int:
        return random.randint(-(2**63), 2**63 - 1)
