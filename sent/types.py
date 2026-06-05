"""Re-export all TL types."""

import importlib
import pkgutil

import sent.tl.types as _types_pkg
from sent.tl.types.all import *  # noqa: F401,F403

for _importer, modname, _ispkg in pkgutil.iter_modules(_types_pkg.__path__):
    if modname != "all":
        importlib.import_module(f"sent.tl.types.{modname}")
