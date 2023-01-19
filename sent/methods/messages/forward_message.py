import requests

class forwardMessage:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def forward_message(self, chat_id, from_chat_id, message_id, protect_content=None, disable_notification=None, message_thread_id=None):
        """
        Use this method to forward messages of any kind.
        """

        url = f'{self.base_url}/forwardMessage'
        data = {'chat_id': chat_id, 'from_chat_id': from_chat_id, 'message_id': message_id}
        if protect_content:
            data['protect_content'] = protect_content
        if disable_notification:
            data['disable_notification'] = disable_notification
        if message_thread_id:
            data['message_thread_id'] = message_thread_id
        response = requests.post(url, json=data)
        return response.json()
