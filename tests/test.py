from tmwad.telegram import Telegram

print('Enter your YOUR_TOKEN:')
token = input()
print('Enter your CHAT_ID:')
chatid = input()

bot = Telegram(token)
bot.send_message(chatid, 'Hello, World!')

print(f"message succusfully sent to {chatid} user")
