import requests

class BanChatSenderChat:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def ban_chat_sender_chat(self, chat_id, user_id, until_date=None):
        url = f'{self.base_url}/banChatSenderChat'
        data = {'chat_id': chat_id, 'user_id': user_id}
        if until_date:
            data['until_date'] = until_date
        response = requests.post(url, json=data)
        return response.json()


# from ban_chat_sender_chat import BanChatSenderChat
#
# api = BanChatSenderChat('YOUR_TOKEN')
#
# response = api.ban_chat_sender_chat(chat_id=12345678, user_id=12345678, until_date=1609372400)
