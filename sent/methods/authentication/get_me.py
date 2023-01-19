import requests

class GetMe:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def get_me(self):
        url = f'{self.base_url}/getMe'
        response = requests.get(url)
        return response.json()
