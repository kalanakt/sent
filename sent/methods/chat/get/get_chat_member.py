import requests

class GetChatMember:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def get_chat_member(self, chat_id, user_id):
        url = f'{self.base_url}/getChatMember'
        params = {'chat_id': chat_id, 'user_id': user_id}
        response = requests.get(url, params=params)
        return response.json()


# from get_chat_member import GetChatMember
#
# api = GetChatMember('YOUR_TOKEN')
#
# response = api.get_chat_member(chat_id=12345678, user_id=987654321)
# result = response['result']
