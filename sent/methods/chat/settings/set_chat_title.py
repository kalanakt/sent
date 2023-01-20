import requests

class SetChatTitle:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def set_chat_title(self, chat_id, title):
        url = f'{self.base_url}/setChatTitle'
        data = {'chat_id': chat_id, 'title': title}
        response = requests.post(url, json=data)
        return response.json()


# from set_chat_title import SetChatTitle
#
# api = SetChatTitle('YOUR_TOKEN')
#
# response = api.set_chat_title(chat_id=12345678, title='Chat Title')
# result = response['result']
