import requests

class RestrictChatMember:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def restrict_chat_member(self, chat_id, user_id, permissions, until_date=None):
        url = f'{self.base_url}/restrictChatMember'
        data = {'chat_id': chat_id, 'user_id': user_id, 'permissions': permissions}
        if until_date:
            data['until_date'] = until_date
        response = requests.post(url, json=data)
        return response.json()


# from restrict_chat_member import RestrictChatMember
#
# api = RestrictChatMember('YOUR_TOKEN')
#
# permissions = {'can_send_messages': False, 'can_send_media_messages': False}
# response = api.restrict_chat_member(chat_id=12345678, user_id=12345678, permissions=permissions)
