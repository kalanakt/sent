import requests

class ExportChatInviteLink:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def export_chat_invite_link(self, chat_id):
        url = f'{self.base_url}/exportChatInviteLink'
        data = {'chat_id': chat_id}
        response = requests.post(url, json=data)
        return response.json()


# from export_chat_invite_link import ExportChatInviteLink
#
# api = ExportChatInviteLink('YOUR_TOKEN')
#
# response = api.export_chat_invite_link(chat_id=12345678)
# invite_link = response['result']
