import requests

class SendChatAction:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def send_chat_action(self, chat_id, action):
        url = f'{self.base_url}/sendChatAction'
        data = {'chat_id': chat_id, 'action': action}
        response = requests.post(url, json=data)
        return response.json()


# from send_chat_action import SendChatAction
#
# api = SendChatAction('YOUR_TOKEN')
#
# response = api.send_chat_action(chat_id=12345678, action='typing')
