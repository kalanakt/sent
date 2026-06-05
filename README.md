# sent

[![PyPI version](https://img.shields.io/pypi/v/sent.svg)](https://pypi.org/project/sent/)
[![Python versions](https://img.shields.io/pypi/pyversions/sent.svg)](https://pypi.org/project/sent/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![CI](https://github.com/kalanakt/sent/actions/workflows/ci.yml/badge.svg)](https://github.com/kalanakt/sent/actions/workflows/ci.yml)

**sent** is an async MTProto client library for Telegram. It speaks the raw Telegram protocol and supports both user accounts and bots with an event-driven, developer-friendly API.

## Features

- **Async MTProto 2.0** — encryption, sessions, RPC with `RpcResult` / `MsgContainer` handling
- **User accounts and bots** — phone + code login, SRP 2FA, bot token, QR login
- **Event system** — `NewMessage`, `MessageDeleted`, `MessageRead`, `CallbackQuery`, `ChatAction`, `UserUpdate`, `Album`
- **Friendly API** — `send_message`, `send_file`, `get_dialogs`, `iter_messages`, `conversation()`
- **TL layer 225** — auto-generated from the latest Telegram schema
- **Session storage** — SQLite (with entity cache), StringSession, or in-memory
- **Transport** — TCP abridged / intermediate / full, SOCKS5 proxy support

## Installation

```bash
pip install sent
```

Optional extras for faster cryptography:

```bash
pip install sent[fast]    # cryptg (recommended for production)
pip install sent[crypto]  # pycryptodome fallback
```

For local development:

```bash
git clone https://github.com/kalanakt/sent.git
cd sent
uv sync --all-extras
```

## Quick start

Get your `api_id` and `api_hash` from [my.telegram.org](https://my.telegram.org).

### Bot

```python
import asyncio
import os

from sent import TelegramClient, events

API_ID = int(os.environ["TELEGRAM_API_ID"])
API_HASH = os.environ["TELEGRAM_API_HASH"]
BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]


async def main():
    client = TelegramClient("echo_bot", API_ID, API_HASH)

    @client.on(events.NewMessage)
    async def handler(event):
        await event.reply(event.text)

    await client.start(bot_token=BOT_TOKEN)
    await client.run_until_disconnected()


asyncio.run(main())
```

See [examples/echo_bot.py](examples/echo_bot.py) for a complete echo bot.

### User account

```python
import asyncio
import os

from sent import TelegramClient, events

API_ID = int(os.environ["TELEGRAM_API_ID"])
API_HASH = os.environ["TELEGRAM_API_HASH"]


async def main():
    client = TelegramClient("my_account", API_ID, API_HASH)

    @client.on(events.NewMessage(incoming=True))
    async def handler(event):
        await event.reply("Hello!")

    await client.start()  # prompts for phone, code, and 2FA when needed
    me = await client.get_me()
    print(f"Logged in as {me.first_name}")
    await client.run_until_disconnected()


asyncio.run(main())
```

See [examples/user_bot.py](examples/user_bot.py) for a fuller user-account example.

### Conversation helper

```python
async with client.conversation("username") as conv:
    await conv.send_message("What's your name?")
    response = await conv.get_response()
    print(response.text)
```

## Development

```bash
uv sync --group test
uv run pytest test/ -v
```

Run benchmarks:

```bash
uv run python bench/run.py
```

Regenerate TL types after updating the schema:

```bash
python -m sent._codegen.generate
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for full contributor and release guidelines.

## Project links

- **Source:** https://github.com/kalanakt/sent
- **Issues:** https://github.com/kalanakt/sent/issues
- **PyPI:** https://pypi.org/project/sent/

## License

MIT — see [LICENSE](LICENSE).
