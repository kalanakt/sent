import requests

class SetChatAdministratorCustomTitle:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def set_chat_administrator_custom_title(self, chat_id, user_id, custom_title):
        url = f'{self.base_url}/setChatAdministratorCustomTitle'
        data = {'chat_id': chat_id, 'user_id': user_id, 'custom_title': custom_title}
        response = requests.post(url, json=data)
        return response.json()

# from set_chat_administrator_custom_title import SetChatAdministratorCustomTitle
#
# api = SetChatAdministratorCustomTitle('YOUR_TOKEN')
#
# response = api.set_chat_administrator_custom_title(chat_id=12345678, user_id=12345678, custom_title='Chat Administrator')
