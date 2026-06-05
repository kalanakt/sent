"""Async MTProto echo bot example."""

import asyncio
import os

from sent import TelegramClient, events

API_ID = int(os.environ.get("TELEGRAM_API_ID", "0"))
API_HASH = os.environ.get("TELEGRAM_API_HASH", "")
BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")


async def main():
    client = TelegramClient("echo_bot", API_ID, API_HASH)

    @client.on(events.NewMessage)
    async def echo_handler(event):
        if event.text.startswith("/start"):
            await event.reply("Hello! Send me any message and I'll echo it back.")
        else:
            await event.reply(event.text)

    await client.start(bot_token=BOT_TOKEN)
    print("Bot is running...")
    await client.run_until_disconnected()


if __name__ == "__main__":
    asyncio.run(main())
