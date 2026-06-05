"""RPC request state tracking."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class RequestState:
    """Tracks an in-flight RPC request."""

    request: Any
    future: asyncio.Future = field(default_factory=lambda: asyncio.get_event_loop().create_future())
    msg_id: Optional[int] = None
    container_id: Optional[int] = None
    after: Optional[Any] = None
    need_response: bool = True

    def __post_init__(self):
        try:
            loop = asyncio.get_running_loop()
            if self.future.get_loop() is not loop:
                self.future = loop.create_future()
        except RuntimeError:
            pass
