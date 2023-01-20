import requests

class GetChat:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def get_chat(self, chat_id):
        url = f'{self.base_url}/getChat'
        params = {'chat_id': chat_id}
        response = requests.get(url, params=params)
        return response.json()


# from get_chat import GetChat
#
# api = GetChat('YOUR_TOKEN')
#
# response = api.get_chat(chat_id=12345678)
# result = response['result']
