"""User account example with event handlers."""

import asyncio
import os

from sent import TelegramClient, events

API_ID = int(os.environ.get("TELEGRAM_API_ID", "0"))
API_HASH = os.environ.get("TELEGRAM_API_HASH", "")


async def main():
    client = TelegramClient("my_account", API_ID, API_HASH)

    @client.on(events.NewMessage(incoming=True, pattern=r"(?i).*hello"))
    async def hello_handler(event):
        sender = await event.get_sender()
        name = getattr(sender, "first_name", "there")
        await event.reply(f"Hey {name}!")

    @client.on(events.NewMessage(outgoing=True))
    async def log_outgoing(event):
        print(f"Sent: {event.text}")

    await client.start()
    me = await client.get_me()
    print(f"Logged in as {me.first_name} (id={me.id})")
    await client.send_message("me", "Hello, myself!")
    await client.run_until_disconnected()


if __name__ == "__main__":
    asyncio.run(main())
