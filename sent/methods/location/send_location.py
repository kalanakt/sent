import requests

class SendLocation:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def send_location(self, chat_id, latitude, longitude, live_period=None, disable_notification=None, reply_to_message_id=None, reply_markup=None):
        url = f'{self.base_url}/sendLocation'
        data = {'chat_id': chat_id, 'latitude': latitude, 'longitude': longitude}
        if live_period:
            data['live_period'] = live_period
        if disable_notification:
            data['disable_notification'] = disable_notification
        if reply_to_message_id:
            data['reply_to_message_id'] = reply_to_message_id
        if reply_markup:
            data['reply_markup'] = reply_markup
        response = requests.post(url, json=data)
        return response.json()

# from send_location import SendLocation
#
# api = SendLocation('YOUR_TOKEN')
#
# response = api.send_location(chat_id=12345678, latitude=37.78, longitude=-122.41)
