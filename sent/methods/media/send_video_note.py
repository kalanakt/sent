import requests

class SendVideoNote:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def send_video_note(self, chat_id, video_note, duration=None, length=None, thumb=None, disable_notification=None, reply_to_message_id=None, reply_markup=None):
        url = f'{self.base_url}/sendVideoNote'
        data = {'chat_id': chat_id, 'video_note': video_note}
        if duration:
            data['duration'] = duration
        if length:
            data['length'] = length
        if thumb:
            data['thumb'] = thumb
        if disable_notification:
            data['disable_notification'] = disable_notification
        if reply_to_message_id:
            data['reply_to_message_id'] = reply_to_message_id
        if reply_markup:
            data['reply_markup'] = reply_markup
        response = requests.post(url, json=data)
        return response.json()


# from send_video_note import SendVideoNote
#
# api = SendVideoNote('YOUR_TOKEN')
#
# response = api.send_video_note(chat_id=12345678, video_note=open('path/to/video_note.mp4', 'rb'))
