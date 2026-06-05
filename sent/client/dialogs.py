"""Dialog listing methods."""

from __future__ import annotations


class DialogMethods:
    """Mixin providing dialog methods."""

    async def get_dialogs(self, *, limit: int = 100):
        from sent.tl.functions.messages import MessagesGetDialogs

        result = await self(
            MessagesGetDialogs(
                offset_date=0,
                offset_id=0,
                offset_peer=self._get_empty_input_peer(),
                limit=limit,
                hash=0,
            )
        )
        return getattr(result, "dialogs", [])

    async def iter_dialogs(self, *, limit: int = 100):
        dialogs = await self.get_dialogs(limit=limit)
        for dialog in dialogs:
            yield dialog

    def _get_empty_input_peer(self):
        from sent.tl.types.all import InputPeerEmpty

        return InputPeerEmpty()
