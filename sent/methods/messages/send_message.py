import requests

class SendMessage:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def send_message(self, chat_id, text, reply_markup=None, protect_content=None, schedule_date=None, reply_to_message_id=None, allow_sending_without_reply=None, disable_notification=None, disable_web_page_preview=None, entities=None, parse_mode=None):
        url = f'{self.base_url}/sendMessage'
        data = {'chat_id': chat_id, 'text': text}
        if reply_markup is not None:
            data['reply_markup'] = reply_markup
        if protect_content is not None:
            data['protect_content'] = protect_content
        if schedule_date is not None:
            data['schedule_date'] = schedule_date
        if reply_to_message_id is not None:
            data['reply_to_message_id'] = reply_to_message_id
        if disable_notification is not None:
            data['disable_notification'] = disable_notification
        if disable_web_page_preview is not None:
            data['disable_web_page_preview'] = disable_web_page_preview
        if entities is not None:
            data['entities'] = entities
        if parse_mode is not None:
            data['parse_mode'] = parse_mode
        if allow_sending_without_reply is not None:
            data['allow_sending_without_reply'] = allow_sending_without_reply
        response = requests.post(url, json=data)
        return response.json()
