"""Re-export all TL RPC functions."""

from __future__ import annotations

import importlib

_PACKAGE = "sent.tl.functions"


def __getattr__(name: str):
    return getattr(importlib.import_module(_PACKAGE), name)


def __dir__():
    return dir(importlib.import_module(_PACKAGE))
