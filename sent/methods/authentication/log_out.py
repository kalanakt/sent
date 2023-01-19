import requests

class LogOut:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def log_out(self):
        url = f'{self.base_url}/logOut'
        response = requests.post(url)
        return response.json()
