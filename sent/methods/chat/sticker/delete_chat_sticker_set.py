import requests

class DeleteChatStickerSet:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def delete_chat_sticker_set(self, chat_id):
        url = f'{self.base_url}/deleteChatStickerSet'
        data = {'chat_id': chat_id}
        response = requests.post(url, json=data)
        return response.json()


# from delete_chat_sticker_set import DeleteChatStickerSet
#
# api = DeleteChatStickerSet('YOUR_TOKEN')
#
# response = api.delete_chat_sticker_set(chat_id=12345678)
# result = response['result']
