import requests

class BanChatMember:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def ban_chat_member(self, chat_id, user_id, until_date=None):
        url = f'{self.base_url}/banChatMember'
        data = {'chat_id': chat_id, 'user_id': user_id}
        if until_date:
            data['until_date'] = until_date
        response = requests.post(url, json=data)
        return response.json()



# from ban_chat_member import BanChatMember
#
# api = BanChatMember('YOUR_TOKEN')
#
# response = api.ban_chat_member(chat_id=12345678, user_id=12345678)
