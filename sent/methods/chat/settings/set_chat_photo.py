import requests

class SetChatPhoto:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def set_chat_photo(self, chat_id, photo):
        url = f'{self.base_url}/setChatPhoto'
        files = {'photo': photo}
        data = {'chat_id': chat_id}
        response = requests.post(url, data=data, files=files)
        return response.json()


# from set_chat_photo import SetChatPhoto
#
# api = SetChatPhoto('YOUR_TOKEN')
#
# with open('path/to/photo.jpg', 'rb') as photo:
#     response = api.set_chat_photo(chat_id=12345678, photo=photo)
# result = response['result']
