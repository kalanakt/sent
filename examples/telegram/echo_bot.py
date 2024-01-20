import sent

TOKEN = '6797119104:AAHB4pEbZD8C1lIafhGmCOQ-qrXYsuNr6uo'

bot = sent.TelegramClient(TOKEN)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


if __name__ == "__main__":
    bot.polling()
