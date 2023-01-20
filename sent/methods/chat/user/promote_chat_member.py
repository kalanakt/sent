import requests

class PromoteChatMember:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def promote_chat_member(self, chat_id, user_id, can_change_info=None, can_post_messages=None, can_edit_messages=None, can_delete_messages=None, can_invite_users=None, can_restrict_members=None, can_pin_messages=None, can_promote_members=None):
        url = f'{self.base_url}/promoteChatMember'
        data = {'chat_id': chat_id, 'user_id': user_id}
        if can_change_info:
            data['can_change_info'] = can_change_info
        if can_post_messages:
            data['can_post_messages'] = can_post_messages
        if can_edit_messages:
            data['can_edit_messages'] = can_edit_messages
        if can_delete_messages:
            data['can_delete_messages'] = can_delete_messages
        if can_invite_users:
            data['can_invite_users'] = can_invite_users
        if can_restrict_members:
            data['can_restrict_members'] = can_restrict_members
        if can_pin_messages:
            data['can_pin_messages'] = can_pin_messages
        if can_promote_members:
            data['can_promote_members'] = can_promote_members
        response = requests.post(url, json=data)
        return response.json()


# from promote_chat_member import PromoteChatMember
#
# api = PromoteChatMember('YOUR_TOKEN')
#
# response = api.promote_chat_member(chat_id=12345678, user_id=12345678, can_change_info=True, can_post_messages=True, can_promote_members=True)
