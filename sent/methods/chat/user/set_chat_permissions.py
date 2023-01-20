import requests

import json

class SetChatPermissions:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def set_chat_permissions(self, chat_id, permissions, user_id=None):
        url = f'{self.base_url}/setChatPermissions'
        data = {'chat_id': chat_id, 'permissions': json.dumps(permissions)}
        if user_id:
            data['user_id'] = user_id
        response = requests.post(url, json=data)
        return response.json()


# from set_chat_permissions import SetChatPermissions
#
# api = SetChatPermissions('YOUR_TOKEN')
#
# permissions = {
#     'can_send_messages': False,
#     'can_send_media_messages': False,
#     'can_send_polls': False,
#     'can_send_other_messages': False,
#     'can_add_web_page_previews': False
# }
#
# response = api.set_chat_permissions(chat_id=12345678, user_id=12345678, permissions=permissions)
