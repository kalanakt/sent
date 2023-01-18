# TMWAD

A Fast Telegram API for Lighweight bots

## Installation
To install this package, use pip:


```shell
pip install tmwad
```

## Usage

Here is an example of how to use the package:

```py
from tmwad.telegram import Telegram

token = 'BOT_TOJJEN' # bot token from bot father
chatid = 'CHAT_ID'  # chat id of user | group | channel

bot = Telegram(token)
bot.send_message(chatid, 'Hello, World!') # bot set message to chatid
```

## Documentation

For more detailed information about how to use this package, please refer to the full documentation at: [link to documentation]

## Contributing

We welcome contributions to this package. To contribute, please fork the repository, make your changes, and submit a pull request.

## License

This package is open-sourced under the MIT license

## Issues

If you encounter any issues or bugs, please open an issue in the issue tracker.
