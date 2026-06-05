"""InlineQuery event."""

from sent.events.common import EventBuilder, EventCommon, register_event


@register_event
class InlineQuery(EventBuilder):
    def build(self, update, others=None, client=None):
        if not hasattr(update, "query"):
            return None
        event = InlineQueryEvent(client, update)
        if not self.filter(event):
            return None
        return event


class InlineQueryEvent(EventCommon):
    def __init__(self, client, query):
        super().__init__(client, query)
        self.query = query
        self.text = getattr(query, "query", "")
        self.id = getattr(query, "query_id", None) or getattr(query, "id", None)

    async def answer(self, results, *, cache_time=0, is_personal=False, **kwargs):
        from sent.tl.functions.messages import MessagesSetInlineBotResults

        return await self.client(
            MessagesSetInlineBotResults(
                query_id=self.id,
                results=results,
                cache_time=cache_time,
                is_personal=is_personal,
                **kwargs,
            )
        )
