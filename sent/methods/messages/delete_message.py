import requests

class deleteMessage:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def delete_message(self, chat_id, message_id):
        """
        Use this method to delete messages sent by the bot or via the bot (for inline bots).
        """
        url = f'{self.base_url}/deleteMessage'
        data = {'chat_id': chat_id, 'message_id': message_id}
        response = requests.post(url, json=data)
        return response.json()
