import requests

class editGeneralForumTopic:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def edit_general_forum_topic(self, chat_id, name):
        url = f'{self.base_url}/editGeneralForumTopic'
        data = {'chat_id': chat_id, 'name': name}
        response = requests.post(url, json=data)
        return response.json()
