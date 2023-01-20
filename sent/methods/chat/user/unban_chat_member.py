import requests

class UnbanChatMember:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def unban_chat_member(self, chat_id, user_id):
        url = f'{self.base_url}/unbanChatMember'
        data = {'chat_id': chat_id, 'user_id': user_id}
        response = requests.post(url, json=data)
        return response.json()


# from unban_chat_member import UnbanChatMember
#
# api = UnbanChatMember('YOUR_TOKEN')
#
# response = api.unban_chat_member(chat_id=12345678, user_id=12345678)
