import requests

class Telegram:
    def __init__(self, token):
        self.token = token
        self.url = f"https://api.telegram.org/bot{token}/"

    def send_message(self, chat_id, text):
        data = {'chat_id': chat_id, 'text': text}
        response = requests.post(self.url + 'sendMessage', data=data)
        return response.json()

    def get_updates(self, offset=None, timeout=30):
        data = {'timeout': timeout, 'offset': offset}
        response = requests.get(self.url + 'getUpdates', data=data)
        return response.json()
