"""Connection package."""

from sent.network.connection.tcp import (
    Connection,
    TCPAbridged,
    TCPFull,
    TCPIntermediate,
    get_connection,
)

__all__ = ["Connection", "TCPAbridged", "TCPFull", "TCPIntermediate", "get_connection"]
