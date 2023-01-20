import requests

class EditMessageLiveLocation:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def edit_message_live_location(self, latitude, longitude, chat_id=None, message_id=None, inline_message_id=None, reply_markup=None):
        url = f'{self.base_url}/editMessageLiveLocation'
        data = {'latitude': latitude, 'longitude': longitude}
        if chat_id:
            data['chat_id'] = chat_id
        if message_id:
            data['message_id'] = message_id
        if inline_message_id:
            data['inline_message_id'] = inline_message_id
        if reply_markup:
            data['reply_markup'] = reply_markup
        response = requests.post(url, json=data)
        return response.json()


# from edit_message_live_location import EditMessageLiveLocation
#
# api = EditMessageLiveLocation('YOUR_TOKEN')
#
# response = api.edit_message_live_location(chat_id=12345678, message_id=987654321, latitude=37.78, longitude=-122.41)
