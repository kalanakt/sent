import requests


class reopenForumTopic:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def reopen_forum_topic(self, chat_id, message_thread_id):
        url = f'{self.base_url}/reopenForumTopic'
        data = {'chat_id': chat_id, 'message_thread_id': message_thread_id}
        response = requests.post(url, json=data)
        return response.json()
