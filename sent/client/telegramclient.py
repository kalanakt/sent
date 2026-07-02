"""High-level Telegram client combining all method mixins."""

from __future__ import annotations

from sent.client.auth import AuthMethods
from sent.client.bots import BotMethods
from sent.client.chats import ChatMethods
from sent.client.dialogs import DialogMethods
from sent.client.downloads import DownloadMethods
from sent.client.messages import MessageMethods
from sent.client.telegrambaseclient import TelegramBaseClient
from sent.client.updates import UpdateMethods
from sent.client.uploads import UploadMethods
from sent.client.users import UserMethods


class TelegramClient(
    TelegramBaseClient,
    AuthMethods,
    MessageMethods,
    UploadMethods,
    DownloadMethods,
    UserMethods,
    ChatMethods,
    DialogMethods,
    BotMethods,
    UpdateMethods,
):
    """Async MTProto client for Telegram."""

    def __init__(self, *args, **kwargs):
        TelegramBaseClient.__init__(self, *args, **kwargs)
        UpdateMethods.__init_update_handlers(self)

    async def start(self, *args, **kwargs):
        """Connect and authenticate (interactive, bot token, or programmatic).

        Calls ``connect()`` then delegates to ``AuthMethods.start`` for login.
        """
        await self.connect()
        return await AuthMethods.start(self, *args, **kwargs)
