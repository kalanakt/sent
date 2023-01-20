import requests

class UnpinAllChatMessages:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def unpin_all_chat_messages(self, chat_id):
        url = f'{self.base_url}/unpinAllChatMessages'
        data = {'chat_id': chat_id}
        response = requests.post(url, json=data)
        return response.json()


# from unpin_all_chat_messages import UnpinAllChatMessages
#
# api = UnpinAllChatMessages('YOUR_TOKEN')
#
# response = api.unpin_all_chat_messages(chat_id=12345678)
# result = response['result']
