"""Update handling methods."""

from __future__ import annotations

import asyncio
import logging
from typing import Callable, List, Tuple

logger = logging.getLogger("sent.updates")


class UpdateMethods:
    """Mixin providing update/event handling."""

    def __init_update_handlers(self):
        self._event_handlers: List[Tuple] = []
        self._update_task = None
        self._album_buffer = {}

    def on(self, event: Callable):
        """Register an event handler via decorator."""

        def decorator(func):
            builder = event if hasattr(event, "build") else event()
            self.add_event_handler(func, builder)
            return func

        if callable(event) and hasattr(event, "_event_builder"):
            self.add_event_handler(event, event._event_builder)
            return event
        return decorator

    def add_event_handler(self, callback, event: Callable):
        self._event_handlers.append((event, callback))

    def remove_event_handler(self, callback, event: Callable = None):
        self._event_handlers = [
            (e, cb) for e, cb in self._event_handlers if cb != callback or (event and e != event)
        ]

    async def _handle_update(self, update):
        for inner in self._normalize_updates(update):
            for builder, callback in self._event_handlers:
                try:
                    event = builder.build(inner, client=self)
                    if event is None:
                        continue
                    if isinstance(event, list):
                        for e in event:
                            await self._invoke_callback(callback, e)
                    else:
                        await self._invoke_callback(callback, event)
                except Exception:
                    logger.exception("Error in event handler")

    def _normalize_updates(self, update):
        cls_name = update.__class__.__name__

        if cls_name in ("Updates", "UpdatesCombined"):
            for user in getattr(update, "users", []) or []:
                self._entity_cache.add(user)
            for chat in getattr(update, "chats", []) or []:
                self._entity_cache.add(chat)
            for inner in getattr(update, "updates", []) or []:
                yield inner
            return

        if cls_name == "UpdateShort":
            yield update.update
            return

        if cls_name == "UpdateShortMessage":
            from sent.tl.types.all import Message, PeerUser, UpdateNewMessage

            message = Message(
                id=update.id,
                peer_id=PeerUser(user_id=update.user_id),
                date=update.date,
                message=update.message,
                out=update.out,
                mentioned=update.mentioned,
                media_unread=update.media_unread,
                silent=update.silent,
            )
            yield UpdateNewMessage(message=message, pts=update.pts, pts_count=update.pts_count)
            return

        if cls_name == "UpdateShortChatMessage":
            from sent.tl.types.all import Message, PeerChat, UpdateNewMessage

            message = Message(
                id=update.id,
                peer_id=PeerChat(chat_id=update.chat_id),
                from_id=update.from_id,
                date=update.date,
                message=update.message,
                out=update.out,
            )
            yield UpdateNewMessage(message=message, pts=update.pts, pts_count=update.pts_count)
            return

        if cls_name == "UpdateShortSentMessage":
            from sent.tl.types.all import Message, PeerUser, UpdateNewMessage

            message = Message(
                id=update.id,
                peer_id=PeerUser(user_id=0),
                date=update.date,
                message="",
                out=True,
            )
            yield UpdateNewMessage(message=message, pts=update.pts, pts_count=update.pts_count)
            return

        yield update

    async def _invoke_callback(self, callback, event):
        result = callback(event)
        if asyncio.iscoroutine(result):
            await result

    async def run_until_disconnected(self):
        """Process updates until disconnected."""
        self._update_task = asyncio.create_task(self._update_loop())
        try:
            await self._disconnected
        except asyncio.CancelledError:
            pass
        finally:
            self._update_task.cancel()

    async def _update_loop(self):
        while self.is_connected():
            update = await self._sender.get_updates(timeout=1.0)
            if update:
                await self._handle_update(update)

    async def catch_up(self):
        """Fetch missed updates."""
        pts, qts, date, seq = self.session.get_update_state()
        from sent.tl.functions.updates import UpdatesGetDifference, UpdatesGetState

        state = await self(UpdatesGetState())
        if hasattr(state, "pts"):
            self.session.set_update_state(state.pts, state.qts, state.date, state.seq)

        diff = await self(UpdatesGetDifference(pts=pts, date=date, qts=qts))
        if hasattr(diff, "state") and diff.state:
            self.session.set_update_state(
                diff.state.pts, diff.state.qts, diff.state.date, diff.state.seq
            )
        if hasattr(diff, "new_messages"):
            for msg in diff.new_messages:
                from sent.tl.types.all import UpdateNewMessage

                await self._handle_update(UpdateNewMessage(message=msg, pts=0, pts_count=0))
        if hasattr(diff, "other_updates"):
            for upd in diff.other_updates:
                await self._handle_update(upd)

    async def _sync_update_state(self):
        from sent.tl.functions.updates import UpdatesGetState

        state = await self(UpdatesGetState())
        if hasattr(state, "pts"):
            self.session.set_update_state(state.pts, state.qts, state.date, state.seq)
