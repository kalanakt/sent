"""TL types package — auto-generated."""

import importlib

_MODULES = [
    "account",
    "aicompose",
    "all",
    "auth",
    "bots",
    "channels",
    "chatlists",
    "contacts",
    "fragment",
    "help",
    "messages",
    "payments",
    "phone",
    "photos",
    "premium",
    "smsjobs",
    "stats",
    "stickers",
    "storage",
    "stories",
    "updates",
    "upload",
    "users",
]

for _mod in _MODULES:
    importlib.import_module("sent.tl.types." + _mod)