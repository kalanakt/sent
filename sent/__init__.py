"""sent - Async MTProto client library for Telegram."""

__version__ = "1.0.0"


def __getattr__(name):
    if name == "TelegramClient":
        from sent.client.telegramclient import TelegramClient
        return TelegramClient
    if name in ("events", "types", "functions", "errors"):
        import importlib
        return importlib.import_module(f"sent.{name}")
    raise AttributeError(f"module 'sent' has no attribute {name!r}")


__all__ = ["TelegramClient", "events", "types", "functions", "errors", "__version__"]
