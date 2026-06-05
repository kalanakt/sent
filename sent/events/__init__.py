"""Event system for sent."""

from sent.events.common import EventBuilder, EventCommon, register_event
from sent.events.newmessage import NewMessage
from sent.events.messageedited import MessageEdited
from sent.events.messagedeleted import MessageDeleted
from sent.events.messageread import MessageRead
from sent.events.callbackquery import CallbackQuery
from sent.events.inlinequery import InlineQuery
from sent.events.chataction import ChatAction
from sent.events.raw import Raw
from sent.events.userupdate import UserUpdate
from sent.events.album import Album

__all__ = [
    "EventBuilder",
    "EventCommon",
    "register_event",
    "NewMessage",
    "MessageEdited",
    "MessageDeleted",
    "MessageRead",
    "CallbackQuery",
    "InlineQuery",
    "ChatAction",
    "Raw",
    "UserUpdate",
    "Album",
]
