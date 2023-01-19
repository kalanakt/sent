from sent.telegram import Telegram

chatid = 1288398723

bot = Telegram('5912234148:AAFSJ-6reLRM3zqqYRtFxmZiAXgqW29BwL0')
bot.send_message(chatid, 'Hello, World!')

response = bot.get_me()

bot.start_polling()

# import unittest
# from unittest.mock import patch
# from sent.telegram import Telegram
#
# class TestTelegramAPI(unittest.TestCase):
#     @patch('telegram_api.requests.post')
#     def test_send_message(self, mock_post):
#         mock_response = mock_post.return_value
#         mock_response.json.return_value = {'ok': True, 'result': 'message sent'}
#         api = Telegram('YOUR_TOKEN')
#         response = api.send_message('12345678', 'Hello, World!')
#         self.assertEqual(response, {'ok': True, 'result': 'message sent'})
#         mock_post.assert_called_with('https://api.telegram.org/botYOUR_TOKEN/sendMessage', json={'chat_id': '12345678', 'text': 'Hello, World!'})
