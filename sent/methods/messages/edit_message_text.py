import requests

class editMessageText:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def edit_message_text(self, text, chat_id=None, message_id=None, inline_message_id=None, reply_markup=None, parse_mode=None, entities=None, disable_web_page_preview=None):
        """
        Use this method to edit text messages sent by the bot or via the bot (for inline bots).
        """
        url = f'{self.base_url}/editMessageText'
        data = {'text': text}
        if chat_id:
            data['chat_id'] = chat_id
        if message_id:
            data['message_id'] = message_id
        if inline_message_id:
            data['inline_message_id'] = inline_message_id
        if reply_markup:
            data['reply_markup'] = json.dumps(reply_markup)
        if parse_mode:
            data['parse_mode'] = parse_mode
        if entities:
            data['entities'] = json.dumps(entities)
        if disable_web_page_preview:
            data['disable_web_page_preview'] = disable_web_page_preview
        response = requests.post(url, json=data)
        return response.json()
