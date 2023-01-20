import requests


class SendContact:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def send_contact(self, chat_id, phone_number, first_name, last_name=None, vcard=None, disable_notification=None, reply_to_message_id=None, reply_markup=None):
        url = f'{self.base_url}/sendContact'
        data = {'chat_id': chat_id, 'phone_number': phone_number, 'first_name': first_name}
        if last_name:
            data['last_name'] = last_name
        if vcard:
            data['vcard'] = vcard
        if disable_notification:
            data['disable_notification'] = disable_notification
        if reply_to_message_id:
            data['reply_to_message_id'] = reply_to_message_id
        if reply_markup:
            data['reply_markup'] = reply_markup
        response = requests.post(url, json=data)
        return response.json()


# from send_contact import SendContact
#
# api = SendContact('YOUR_TOKEN')
#
# response = api.send_contact(chat_id=12345678, phone_number='+1234567890', first_name='John', last_name='Doe')
