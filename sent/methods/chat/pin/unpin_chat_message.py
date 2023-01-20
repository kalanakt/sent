import requests

class UnpinChatMessage:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def unpin_chat_message(self, chat_id):
        url = f'{self.base_url}/unpinChatMessage'
        data = {'chat_id': chat_id}
        response = requests.post(url, json=data)
        return response.json()

# from unpin_chat_message import UnpinChatMessage
#
# api = UnpinChatMessage('YOUR_TOKEN')
#
# response = api.unpin_chat_message(chat_id=12345678)
# result = response['result']
