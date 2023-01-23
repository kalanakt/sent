# sent

A Fast Telegram API for Lighweight bots

## Installation

To install this package, use pip:


```
pip install sent
```

## Usage

Here is an example of how to use the package:

```py
from sent.telegram import Telegram

token = 'BOT_TOJJEN' # bot token from bot father
chatid = 'CHAT_ID'  # chat id of user | group | channel

bot = Telegram(token)

bot.send_message(chatid, "Wow !!!")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?", protect_content=True)


bot.polling()
```

## Documentation

For more detailed information about how to use this package, please refer to the full documentation at

## Contributing

We welcome contributions to this package. To contribute, please fork the repository, make your changes, and submit a pull request.

## License

This package is open-sourced under the MIT license

## Issues

If you encounter any issues or bugs, please open an issue in the issue tracker.
