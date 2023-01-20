import requests

class GetUserProfilePhotos:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def get_user_profile_photos(self, user_id, offset=None, limit=None):
        url = f'{self.base_url}/getUserProfilePhotos'
        data = {'user_id': user_id}
        if offset:
            data['offset'] = offset
        if limit:
            data['limit'] = limit
        response = requests.post(url, json=data)
        return response.json()

# from get_user_profile_photos import GetUserProfilePhotos
#
# api = GetUserProfilePhotos('YOUR_TOKEN')
#
# response = api.get_user_profile_photos(user_id=12345678)
