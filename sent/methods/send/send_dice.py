import requests

class SendDice:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def send_dice(self, chat_id, emoji=None, disable_notification=None, reply_to_message_id=None, reply_markup=None):
        url = f'{self.base_url}/sendDice'
        data = {'chat_id': chat_id}
        if emoji:
            data['emoji'] = emoji
        if disable_notification:
            data['disable_notification'] = disable_notification
        if reply_to_message_id:
            data['reply_to_message_id'] = reply_to_message_id
        if reply_markup:
            data['reply_markup'] = reply_markup
        response = requests.post(url, json=data)
        return response.json()

# from send_dice import SendDice
#
# api = SendDice('YOUR_TOKEN')
#
# response = api.send_dice(chat_id=12345678)
