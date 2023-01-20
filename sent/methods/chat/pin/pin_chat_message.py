import requests

class PinChatMessage:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def pin_chat_message(self, chat_id, message_id, disable_notification=None):
        url = f'{self.base_url}/pinChatMessage'
        data = {'chat_id': chat_id, 'message_id': message_id}
        if disable_notification:
            data['disable_notification'] = disable_notification
        response = requests.post(url, json=data)
        return response.json()


# from pin_chat_message import PinChatMessage
#
# api = PinChatMessage('YOUR_TOKEN')
#
# response = api.pin_chat_message(chat_id=12345678, message_id=987654321)
# result = response['result']
