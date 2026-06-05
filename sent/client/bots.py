"""Bot-specific methods."""

from __future__ import annotations


class BotMethods:
    async def answer_callback_query(self, query_id, text=None, alert=False):
        from sent.tl.functions.bots import BotsSetBotCallbackAnswer

        return await self(
            BotsSetBotCallbackAnswer(
                query_id=query_id,
                message=text,
                alert=alert,
            )
        )

    async def answer_inline_query(
        self,
        query_id,
        results,
        *,
        cache_time: int = 0,
        is_gallery: bool = False,
        is_personal: bool = False,
    ):
        from sent.tl.functions.messages import MessagesSetInlineBotResults

        return await self(
            MessagesSetInlineBotResults(
                gallery=is_gallery,
                private=is_personal,
                query_id=query_id,
                results=results,
                cache_time=cache_time,
            )
        )

    async def click(self, message, button):
        """Click an inline button on a message."""
        markup = getattr(message, "reply_markup", None)
        if markup is None:
            raise ValueError("Message has no reply markup")
        for row in getattr(markup, "rows", []):
            for btn in getattr(row, "buttons", []):
                if getattr(btn, "text", None) == button or btn == button:
                    data = getattr(btn, "data", None)
                    if data:
                        from sent.tl.functions.messages import MessagesGetBotCallbackAnswer

                        return await self(
                            MessagesGetBotCallbackAnswer(
                                peer=await self.get_input_entity(message.peer_id),
                                msg_id=message.id,
                                data=data,
                            )
                        )
        raise ValueError(f"Button {button!r} not found")
