import requests

class copyMessage:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def copy_message(self, chat_id, from_chat_id, message_id, reply_markup=None, allow_sending_without_reply=None, reply_to_message_id=None, protect_content=None, disable_notification=None, caption_entities=None, parse_mode=None, caption=None, message_thread_id=None):
        url = f'{self.base_url}/copyMessage'
        data = {'chat_id': chat_id, 'from_chat_id': from_chat_id, 'message_id': message_id}
        if reply_markup:
            data['reply_markup'] = reply_markup
        if allow_sending_without_reply:
            data['allow_sending_without_reply'] = allow_sending_without_reply
        if reply_to_message_id:
            data['reply_to_message_id'] = reply_to_message_id
        if protect_content:
            data['protect_content'] = protect_content
        if disable_notification:
            data['disable_notification'] = disable_notification
        if caption_entities:
            data['caption_entities'] = caption_entities
        if parse_mode:
            data['parse_mode'] = parse_mode
        if caption:
            data['caption'] = caption
        if message_thread_id:
            data['message_thread_id'] = message_thread_id
        response = requests.post(url, json=data)
        return response.json()
