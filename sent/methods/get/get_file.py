import requests

class GetFile:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def get_file(self, file_id):
        url = f'{self.base_url}/getFile'
        data = {'file_id': file_id}
        response = requests.post(url, json=data)
        return response.json()


# from get_file import GetFile
#
# api = GetFile('YOUR_TOKEN')
#
# response = api.get_file(file_id='12345678')
