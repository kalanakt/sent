import requests

class SendVideo:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def send_video(self, chat_id, video, duration=None, width=None, height=None, thumb=None, caption=None, parse_mode=None, caption_entities=None, supports_streaming=None, disable_notification=None, reply_to_message_id=None, reply_markup=None):
        url = f'{self.base_url}/sendVideo'
        data = {'chat_id': chat_id, 'video': video}
        if duration:
            data['duration'] = duration
        if width:
            data['width'] = width
        if height:
            data['height'] = height
        if thumb:
            data['thumb'] = thumb
        if caption:
            data['caption'] = caption
        if parse_mode:
            data['parse_mode'] = parse_mode
        if caption_entities:
            data['caption_entities'] = caption_entities
        if supports_streaming:
            data['supports_streaming'] = supports_streaming
        if disable_notification:
            data['disable_notification'] = disable_notification
        if reply_to_message_id:
            data['reply_to_message_id'] = reply_to_message_id
        if reply_markup:
            data['reply_markup'] = reply_markup
        response = requests.post(url, json=data)
        return response.json()
