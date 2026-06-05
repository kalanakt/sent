"""Reply and inline keyboard button helpers."""

from __future__ import annotations

from typing import List


class Button:
    """Helper for building Telegram reply/inline keyboards."""

    @staticmethod
    def inline(text: str, *, data: bytes = None, url: str = None):
        from sent.tl.types.all import KeyboardButtonCallback, KeyboardButtonUrl

        if url:
            return KeyboardButtonUrl(text=text, url=url)
        return KeyboardButtonCallback(text=text, data=data or text.encode())

    @staticmethod
    def text(text: str):
        from sent.tl.types.all import KeyboardButton

        return KeyboardButton(text=text)

    @staticmethod
    def request_phone(text: str):
        from sent.tl.types.all import KeyboardButtonRequestPhone

        return KeyboardButtonRequestPhone(text=text)

    @staticmethod
    def request_location(text: str):
        from sent.tl.types.all import KeyboardButtonRequestGeoLocation

        return KeyboardButtonRequestGeoLocation(text=text)

    @staticmethod
    def build(rows: List[List], *, inline: bool = False):
        from sent.tl.types.all import ReplyInlineMarkup, ReplyKeyboardMarkup

        keyboard_rows = []
        for row in rows:
            keyboard_rows.append(
                type("KeyboardButtonRow", (), {"buttons": row})()
            )
        if inline:
            return ReplyInlineMarkup(rows=keyboard_rows)
        return ReplyKeyboardMarkup(
            rows=keyboard_rows,
            resize=True,
            single_use=False,
            selective=False,
        )


def parse_markdown(text: str):
    """Basic markdown to plain text (entities not yet applied)."""
    return text
