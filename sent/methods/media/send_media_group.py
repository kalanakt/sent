import requests

class SendMediaGroup:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def send_media_group(self, chat_id, media, disable_notification=None, reply_to_message_id=None):
        url = f'{self.base_url}/sendMediaGroup'
        data = {'chat_id': chat_id, 'media': media}
        if disable_notification:
            data['disable_notification'] = disable_notification
        if reply_to_message_id:
            data['reply_to_message_id'] = reply_to_message_id
        response = requests.post(url, json=data)
        return response.json()


# from send_media_group import SendMediaGroup
#
# api = SendMediaGroup('YOUR_TOKEN')
#
# media_group = [
#     {
#         "type": "photo",
#         "media": open("path/to/photo1.jpg", "rb"),
#         "caption": "First Photo"
#     },
#     {
#         "type": "photo",
#         "media": open("path/to/photo2.jpg", "rb"),
#         "caption": "Second Photo"
#     },
#     {
#         "type": "video",
#         "media": open("path/to/video.mp4", "rb"),
#         "caption": "Video"
#     }
# ]
# response = api.send_media_group(chat_id=12345678, media=media_group)
