import requests

class CreateChatInviteLink:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def create_chat_invite_link(self, chat_id, expire_time=None):
        url = f'{self.base_url}/createChatInviteLink'
        data = {'chat_id': chat_id}
        if expire_time:
            data['expire_time'] = expire_time
        response = requests.post(url, json=data)
        return response.json()


# from create_chat_invite_link import CreateChatInviteLink
#
# api = CreateChatInviteLink('YOUR_TOKEN')
#
# response = api.create_chat_invite_link(chat_id=12345678)
# invite_link = response['result']
