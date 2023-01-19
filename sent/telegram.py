import requests
# from sent.methods.messages import  CopyMessage, SendMessage, ForwardMessage, EditMessageText, DeleteMessageText
from sent.methods.authentication import GetMe, LogOut, Close
from sent.methods.messages import  SendMessage

class Telegram:
    def __init__(self, token):
        self.token = token
        self.url = f"https://api.telegram.org/bot{token}/"
        self.send_message = SendMessage(token).send_message
        # self.delete_message_text = DeleteMessageText(token).delete_message_text
        # self.copy_message = CopyMessage(token).copy_message
        # self.forward_message = ForwardMessage(token).forward_message
        # self.edit_message_text = EditMessageText(token).edit_message_text
        self.get_me = GetMe(token).get_me
        self.log_out = LogOut(token).log_out
        self.close = Close(token).close
        self.offset = 0

    def start_polling(self):
        while True:
            updates = self.get_updates(offset=self.offset)
            for update in updates:
                self.handle_update(update)
                self.offset = update['update_id'] + 1

    def handle_update(self, update):
        pass


    def get_updates(self, offset=None, timeout=30):
        data = {'timeout': timeout, 'offset': offset}
        response = requests.get(self.url + 'getUpdates', data=data)
        return response.json()
