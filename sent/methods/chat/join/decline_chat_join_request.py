import requests

class DeclineChatJoinRequest:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def decline_chat_join_request(self, chat_id, user_id):
        url = f'{self.base_url}/declineChatJoinRequest'
        data = {'chat_id': chat_id, 'user_id': user_id}
        response = requests.post(url, json=data)
        return response.json()


# from decline_chat_join_request import DeclineChatJoinRequest
#
# api = DeclineChatJoinRequest('YOUR_TOKEN')
#
# response = api.decline_chat_join_request(chat_id=12345678, user_id=987654321)
# result = response['result']
