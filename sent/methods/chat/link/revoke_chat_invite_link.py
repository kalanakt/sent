import requests

class RevokeChatInviteLink:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def revoke_chat_invite_link(self, chat_id):
        url = f'{self.base_url}/revokeChatInviteLink'
        data = {'chat_id': chat_id}
        response = requests.post(url, json=data)
        return response.json()


# from revoke_chat_invite_link import RevokeChatInviteLink
#
# api = RevokeChatInviteLink('YOUR_TOKEN')
#
# response = api.revoke_chat_invite_link(chat_id=12345678)
# invite_link = response['result']
