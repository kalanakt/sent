import requests

class SetChatStickerSet:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def set_chat_sticker_set(self, chat_id, sticker_set_name):
        url = f'{self.base_url}/setChatStickerSet'
        data = {'chat_id': chat_id, 'sticker_set_name': sticker_set_name}
        response = requests.post(url, json=data)
        return response.json()

# from set_chat_sticker_set import SetChatStickerSet
#
# api = SetChatStickerSet('YOUR_TOKEN')
#
# response = api.set_chat_sticker_set(chat_id=12345678, sticker_set_name='example_sticker_set')
# result = response['result']
