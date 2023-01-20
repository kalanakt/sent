import requests

class unpinAllForumTopicMessages:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def unpin_all_forum_topic_messages(self, chat_id, message_thread_id):
        url = f'{self.base_url}/unpinAllForumTopicMessages'
        data = {'chat_id': chat_id, 'message_thread_id': message_thread_id}
        response = requests.post(url, json=data)
        return response.json()
