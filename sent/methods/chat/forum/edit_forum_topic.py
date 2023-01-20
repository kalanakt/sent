import requests

class editForumTopic:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def edit_forum_topic(self, chat_id, message_thread_id, name=None, icon_custom_emoji_id=None):
        url = f'{self.base_url}/editForumTopic'
        data = {'chat_id': chat_id, 'message_thread_id': message_thread_id}
        if name:
            data['name'] = name
        if icon_custom_emoji_id:
            data['icon_custom_emoji_id'] = icon_custom_emoji_id
        response = requests.post(url, json=data)
        return response.json()
