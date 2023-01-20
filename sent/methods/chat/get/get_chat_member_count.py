import requests

class GetChatMemberCount:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def get_chat_member_count(self, chat_id):
        url = f'{self.base_url}/getChatMemberCount'
        params = {'chat_id': chat_id}
        response = requests.get(url, params=params)
        return response.json()

# from get_chat_member_count import GetChatMemberCount
#
# api = GetChatMemberCount('YOUR_TOKEN')
#
# response = api.get_chat_member_count(chat_id=12345678)
# result = response['result']
