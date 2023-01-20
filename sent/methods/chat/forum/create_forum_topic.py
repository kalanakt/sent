import requests

class CreateForumTopic:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def create_forum_topic(self, name, title, description, forum_id, icon_sticker_id, icon_emoji, is_public, is_sticky, is_closed):
        url = f'{self.base_url}/createForumTopic'
        data = {'name': name, 'title': title, 'description': description, 'forum_id': forum_id, 'icon_sticker_id': icon_sticker_id, 'icon_emoji': icon_emoji, 'is_public': is_public, 'is_sticky': is_sticky, 'is_closed': is_closed}
        response = requests.post(url, json=data)
        return response.json()

# from create_forum_topic import CreateForumTopic
#
# api = CreateForumTopic('YOUR_TOKEN')
#
# response = api.create_forum_topic(name='sticker_pack_name', title='title', description='topic description', forum_id=1, icon_sticker_id=1, icon_emoji='emoji', is_public=True, is_sticky=True, is_closed=True)
# result = response['result']
