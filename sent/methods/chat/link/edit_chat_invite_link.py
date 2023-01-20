import requests

class EditChatInviteLink:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def edit_chat_invite_link(self, chat_id, link, expire_time=None):
        url = f'{self.base_url}/editChatInviteLink'
        data = {'chat_id': chat_id, 'link':link}
        if expire_time:
            data['expire_time'] = expire_time
        response = requests.post(url, json=data)
        return response.json()


# from edit_chat_invite_link import EditChatInviteLink
#
# api = EditChatInviteLink('YOUR_TOKEN')
#
# response = api.edit_chat_invite_link(chat_id=12345678,link="https://t.me/joinchat/XXXXXXXXXXXXXXXXXXXXXX")
# invite_link = response['result']
