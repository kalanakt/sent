import sent
TOKEN = '5912234148:AAFSJ-6reLRM3zqqYRtFxmZiAXgqW29BwL0'
chat_id = 1288398723

print("Ho")
bot = sent.Telegram(TOKEN, plugins=dict(root="plugins"))

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    
if __name__ == "__main__":
    bot.polling()
