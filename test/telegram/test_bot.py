# test_bot.py
import sent
TOKEN = '5912234148:AAFSJ-6reLRM3zqqYRtFxmZiAXgqW29BwL0'
chat_id = 1288398723


def test_bot_token():
    bot = sent.Telegram(TOKEN)
    assert bot.token == TOKEN


def test_bot_message():
    bot = sent.Telegram(TOKEN)
    assert bot.send_message(chat_id=chat_id, text="Hello World!")
