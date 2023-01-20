import requests

class GetForumTopicIconStickers:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def get_forum_topic_icon_stickers(self, name):
        url = f'{self.base_url}/getForumTopicIconStickers'
        data = {'name': name}
        response = requests.get(url, params=data)
        return response.json()


# from get_forum_topic_icon_stickers import GetForumTopicIconStickers
#
# api = GetForumTopicIconStickers('YOUR_TOKEN')
#
# response = api.get_forum_topic_icon_stickers(name='sticker_pack_name')
# result = response['result']
