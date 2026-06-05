"""Exception hierarchy for sent."""

from __future__ import annotations


class SentError(Exception):
    """Base exception for sent library."""


class AuthKeyError(SentError):
    """Authorization key is invalid or missing."""


class RPCError(SentError):
    """Telegram RPC error."""

    def __init__(self, message: str, code: int = 0):
        self.code = code
        self.message = message
        super().__init__(f"RPCError {code}: {message}")


class FloodWaitError(RPCError):
    """Rate limited by Telegram."""

    def __init__(self, seconds: int, message: str = ""):
        self.seconds = seconds
        super().__init__(message or f"FLOOD_WAIT_{seconds}", 420)


class AuthKeyUnregisteredError(AuthKeyError):
    pass


class SessionPasswordNeededError(SentError):
    """Two-factor authentication is enabled."""

    def __init__(self, hint: str = ""):
        self.hint = hint
        super().__init__("Two-step verification is enabled")


class PhoneCodeInvalidError(RPCError):
    def __init__(self):
        super().__init__("PHONE_CODE_INVALID", 400)


class PhoneCodeExpiredError(RPCError):
    def __init__(self):
        super().__init__("PHONE_CODE_EXPIRED", 400)


class UserDeactivatedError(RPCError):
    def __init__(self):
        super().__init__("USER_DEACTIVATED", 401)


class ChatWriteForbiddenError(RPCError):
    def __init__(self):
        super().__init__("CHAT_WRITE_FORBIDDEN", 403)


class ChannelPrivateError(RPCError):
    def __init__(self):
        super().__init__("CHANNEL_PRIVATE", 403)


class MessageIdInvalidError(RPCError):
    def __init__(self):
        super().__init__("MESSAGE_ID_INVALID", 400)


def rpc_message_to_error(message: str, code: int) -> RPCError:
    from sent.errors.rpcerrorlist import RPC_ERRORS

    for key, cls in RPC_ERRORS.items():
        if message.startswith(key):
            if cls.__name__ == "FloodWaitError":
                try:
                    seconds = int(message.split("_")[-1])
                except ValueError:
                    seconds = 60
                return FloodWaitError(seconds, message)
            if cls.__name__ == "SlowModeWaitError":
                try:
                    seconds = int(message.split("_")[-1])
                except ValueError:
                    seconds = 60
                return cls(seconds)
            if cls is SessionPasswordNeededError:
                return SessionPasswordNeededError()
            return cls()
    return RPCError(message, code)
