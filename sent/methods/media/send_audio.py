import requests

class SendAudio:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def send_audio(self, chat_id, audio, caption=None, parse_mode=None, caption_entities=None, duration=None, performer=None, title=None, thumb=None, disable_notification=None, reply_to_message_id=None, reply_markup=None):
        url = f'{self.base_url}/sendAudio'
        data = {'chat_id': chat_id, 'audio': audio}
        if caption:
            data['caption'] = caption
        if parse_mode:
            data['parse_mode'] = parse_mode
        if caption_entities:
            data['caption_entities'] = caption_entities
        if duration:
            data['duration'] = duration
        if performer:
            data['performer'] = performer
        if title:
            data['title'] = title
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
