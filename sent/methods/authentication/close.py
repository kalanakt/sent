import requests

class Close:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def close(self):
        url = f'{self.base_url}/close'
        response = requests.post(url)
        return response.json()
