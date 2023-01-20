import requests

class SetChatDescription:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def set_chat_description(self, chat_id, description):
        url = f'{self.base_url}/setChatDescription'
        data = {'chat_id': chat_id, 'description': description}
        response = requests.post(url, json=data)
        return response.json()


# from set_chat_description import SetChatDescription
#
# api = SetChatDescription('YOUR_TOKEN')
#
# response = api.set_chat_description(chat_id=12345678, description='This is a chat description')
# result = response['result']
