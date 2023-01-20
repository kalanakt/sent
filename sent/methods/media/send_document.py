import requests

class SendDocument:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def send_document(self, chat_id, document, thumb=None, caption=None, parse_mode=None, caption_entities=None, disable_content_type_detection=None, disable_notification=None, reply_to_message_id=None, reply_markup=None):
        url = f'{self.base_url}/sendDocument'
        data = {'chat_id': chat_id, 'document': document}
        if thumb:
            data['thumb'] = thumb
        if caption:
            data['caption'] = caption
        if parse_mode:
            data['parse_mode'] = parse_mode
        if caption_entities:
            data['caption_entities'] = caption_entities
        if disable_content_type_detection:
            data['disable_content_type_detection'] = disable_content_type_detection
        if disable_notification:
            data['disable_notification'] = disable_notification
        if reply_to_message_id:
            data['reply_to_message_id'] = reply_to_message_id
        if reply_markup:
            data['reply_markup'] = reply_markup
        response = requests.post(url, json=data)
        return response.json()
