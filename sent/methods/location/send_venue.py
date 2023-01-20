import requests

class SendVenue:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def send_venue(self, chat_id, latitude, longitude, title, address, foursquare_id=None, foursquare_type=None, disable_notification=None, reply_to_message_id=None, reply_markup=None):
        url = f'{self.base_url}/sendVenue'
        data = {'chat_id': chat_id, 'latitude': latitude, 'longitude': longitude, 'title': title, 'address': address}
        if foursquare_id:
            data['foursquare_id'] = foursquare_id
        if foursquare_type:
            data['foursquare_type'] = foursquare_type
        if disable_notification:
            data['disable_notification'] = disable_notification
        if reply_to_message_id:
            data['reply_to_message_id'] = reply_to_message_id
        if reply_markup:
            data['reply_markup'] = reply_markup
        response = requests.post(url, json=data)
        return response.json()
