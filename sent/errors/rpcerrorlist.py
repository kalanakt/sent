"""Auto-generated RPC error classes (expanded subset)."""

from sent.errors.common import (
    ChannelPrivateError,
    ChatWriteForbiddenError,
    FloodWaitError,
    MessageIdInvalidError,
    PhoneCodeExpiredError,
    PhoneCodeInvalidError,
    RPCError,
    SessionPasswordNeededError,
    UserDeactivatedError,
)


class AuthKeyDuplicatedError(RPCError):
    def __init__(self):
        super().__init__("AUTH_KEY_DUPLICATED", 406)


class BotMethodInvalidError(RPCError):
    def __init__(self):
        super().__init__("BOT_METHOD_INVALID", 400)


class ChannelInvalidError(RPCError):
    def __init__(self):
        super().__init__("CHANNEL_INVALID", 400)


class ChatAdminRequiredError(RPCError):
    def __init__(self):
        super().__init__("CHAT_ADMIN_REQUIRED", 400)


class FileReferenceExpiredError(RPCError):
    def __init__(self):
        super().__init__("FILE_REFERENCE_EXPIRED", 400)


class MediaEmptyError(RPCError):
    def __init__(self):
        super().__init__("MEDIA_EMPTY", 400)


class MessageNotModifiedError(RPCError):
    def __init__(self):
        super().__init__("MESSAGE_NOT_MODIFIED", 400)


class PeerIdInvalidError(RPCError):
    def __init__(self):
        super().__init__("PEER_ID_INVALID", 400)


class PhoneNumberInvalidError(RPCError):
    def __init__(self):
        super().__init__("PHONE_NUMBER_INVALID", 400)


class SlowModeWaitError(RPCError):
    def __init__(self, seconds: int = 0):
        self.seconds = seconds
        super().__init__(f"SLOWMODE_WAIT_{seconds}", 420)


class UsernameInvalidError(RPCError):
    def __init__(self):
        super().__init__("USERNAME_INVALID", 400)


class UsernameNotOccupiedError(RPCError):
    def __init__(self):
        super().__init__("USERNAME_NOT_OCCUPIED", 400)


class UserBannedInChannelError(RPCError):
    def __init__(self):
        super().__init__("USER_BANNED_IN_CHANNEL", 400)


class UserNotParticipantError(RPCError):
    def __init__(self):
        super().__init__("USER_NOT_PARTICIPANT", 400)


class PhoneNumberUnoccupiedError(RPCError):
    def __init__(self):
        super().__init__("PHONE_NUMBER_UNOCCUPIED", 400)


RPC_ERRORS = {
    "FLOOD_WAIT": FloodWaitError,
    "SLOWMODE_WAIT": SlowModeWaitError,
    "SESSION_PASSWORD_NEEDED": SessionPasswordNeededError,
    "PHONE_CODE_INVALID": PhoneCodeInvalidError,
    "PHONE_CODE_EXPIRED": PhoneCodeExpiredError,
    "PHONE_NUMBER_INVALID": PhoneNumberInvalidError,
    "PHONE_NUMBER_UNOCCUPIED": PhoneNumberUnoccupiedError,
    "USER_DEACTIVATED": UserDeactivatedError,
    "CHAT_WRITE_FORBIDDEN": ChatWriteForbiddenError,
    "CHANNEL_PRIVATE": ChannelPrivateError,
    "MESSAGE_ID_INVALID": MessageIdInvalidError,
    "AUTH_KEY_DUPLICATED": AuthKeyDuplicatedError,
    "BOT_METHOD_INVALID": BotMethodInvalidError,
    "CHANNEL_INVALID": ChannelInvalidError,
    "CHAT_ADMIN_REQUIRED": ChatAdminRequiredError,
    "FILE_REFERENCE_EXPIRED": FileReferenceExpiredError,
    "MEDIA_EMPTY": MediaEmptyError,
    "MESSAGE_NOT_MODIFIED": MessageNotModifiedError,
    "PEER_ID_INVALID": PeerIdInvalidError,
    "USERNAME_INVALID": UsernameInvalidError,
    "USERNAME_NOT_OCCUPIED": UsernameNotOccupiedError,
    "USER_BANNED_IN_CHANNEL": UserBannedInChannelError,
    "USER_NOT_PARTICIPANT": UserNotParticipantError,
}

__all__ = [
    "AuthKeyDuplicatedError",
    "BotMethodInvalidError",
    "ChannelInvalidError",
    "ChatAdminRequiredError",
    "FileReferenceExpiredError",
    "MediaEmptyError",
    "MessageNotModifiedError",
    "PeerIdInvalidError",
    "PhoneNumberInvalidError",
    "PhoneNumberUnoccupiedError",
    "RPC_ERRORS",
    "SlowModeWaitError",
    "UsernameInvalidError",
    "UsernameNotOccupiedError",
    "UserBannedInChannelError",
    "UserNotParticipantError",
]
