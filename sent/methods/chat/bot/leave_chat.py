import requests

class LeaveChat:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def leave_chat(self, chat_id):
        url = f'{self.base_url}/leaveChat'
        data = {'chat_id': chat_id}
        response = requests.post(url, json=data)
        return response.json()


# from leave_chat import LeaveChat
#
# api = LeaveChat('YOUR_TOKEN')
#
# response = api.leave_chat(chat_id=12345678)
# result = response['result']
