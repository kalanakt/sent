import requests


class SendPoll:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def send_poll(self, chat_id, question, options, is_anonymous=None, type=None, allows_multiple_answers=None, correct_option_id=None, explanation=None, explanation_parse_mode=None, open_period=None, close_date=None, is_closed=None, disable_notification=None, reply_to_message_id=None, reply_markup=None):
        url = f'{self.base_url}/sendPoll'
        data = {'chat_id': chat_id, 'question': question, 'options': options}
        if is_anonymous:
            data['is_anonymous'] = is_anonymous
        if type:
            data['type'] = type
        if allows_multiple_answers:
            data['allows_multiple_answers'] = allows_multiple_answers
        if correct_option_id:
            data['correct_option_id'] = correct_option_id
        if explanation:
            data['explanation'] = explanation
        if explanation_parse_mode:
            data['explanation_parse_mode'] = explanation_parse_mode
        if open_period:
            data['open_period'] = open_period
        if close_date:
            data['close_date'] = close_date
        if is_closed:
            data['is_closed'] = is_closed
        if disable_notification:
            data['disable_notification'] = disable_notification
        if reply_to_message_id:
            data['reply_to_message_id'] = reply_to_message_id
        if reply_markup:
            data['reply_markup'] = reply_markup
        response = requests.post(url, json=data)
        return response.json()


# from send_poll import SendPoll
#
# api = SendPoll('YOUR_TOKEN')
#
# response = api.send_poll(chat_id=12345678, question='What is your favourite color?', options=['Red', 'Green', 'Blue'])
