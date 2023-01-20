import requests

class SendVoice:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def send_voice(self, chat_id, voice, caption=None, parse_mode=None, caption_entities=None, duration=None, disable_notification=None, reply_to_message_id=None, reply_markup=None):
        url = f'{self.base_url}/sendVoice'
        data = {'chat_id': chat_id, 'voice': voice}
        if caption:
            data['caption'] = caption
        if parse_mode:
            data['parse_mode'] = parse_mode
        if caption_entities:
            data['caption_entities'] = caption_entities
        if duration:
            data['duration'] = duration
        if disable_notification:
            data['disable_notification'] = disable_notification
        if reply_to_message_id:
            data['reply_to_message_id'] = reply_to_message_id
        if reply_markup:
            data['reply_markup'] = reply_markup
        response = requests.post(url, json=data)
        return response.json()

# from send_voice import SendVoice
#
# api = SendVoice('YOUR_TOKEN')
#
# response = api.send_voice(chat_id=12345678, voice=open('path/to/voice.ogg', 'rb'))
