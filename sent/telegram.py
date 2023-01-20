import requests

from .methods.authentication.close import Close
from .methods.authentication.get_me import GetMe
from .methods.authentication.log_out import LogOut

from .methods.chat.bot.leave_chat import LeaveChat

from .methods.chat.forum.close_forum_topic import closeForumTopic
from .methods.chat.forum.close_general_forum_topic import closeGeneralForumTopic
from .methods.chat.forum.create_forum_topic import CreateForumTopic
from .methods.chat.forum.delete_forum_topic import deleteForumTopic
from .methods.chat.forum.edit_forum_topic import editForumTopic
from .methods.chat.forum.edit_general_forum_topic import editGeneralForumTopic
from .methods.chat.forum.get_forum_topic_icon_stickers import GetForumTopicIconStickers
from .methods.chat.forum.hide_general_forum_topic import hideGeneralForumTopic
from .methods.chat.forum.reopen_forum_topic import reopenForumTopic
from .methods.chat.forum.reopen_general_forum_topic import reopenGeneralForumTopic
from .methods.chat.forum.unhide_general_forum_topic import unhideGeneralForumTopic
from .methods.chat.forum.unpin_all_forum_topic_messages import unpinAllForumTopicMessages

from .methods.chat.get.get_chat import GetChat
from .methods.chat.get.get_chat_administrators import GetChatAdministrators
from .methods.chat.get.get_chat_member import GetChatMember
from .methods.chat.get.get_chat_member_count import GetChatMemberCount

from .methods.chat.join.approve_chat_join_request import ApproveChatJoinRequest
from .methods.chat.join.decline_chat_join_request import DeclineChatJoinRequest

from .methods.chat.link.create_chat_invite_link import CreateChatInviteLink
from .methods.chat.link.edit_chat_invite_link import EditChatInviteLink
from .methods.chat.link.export_chat_invite_link import ExportChatInviteLink
from .methods.chat.link.revoke_chat_invite_link import RevokeChatInviteLink

from .methods.chat.pin.pin_chat_message import PinChatMessage
from .methods.chat.pin.unpin_all_chat_messages import UnpinAllChatMessages
from .methods.chat.pin.unpin_chat_message import UnpinChatMessage

from .methods.chat.settings.set_chat_description import SetChatDescription
from .methods.chat.settings.set_chat_photo import SetChatPhoto
from .methods.chat.settings.set_chat_title import SetChatTitle

from .methods.chat.sticker.delete_chat_sticker_set import DeleteChatStickerSet
from .methods.chat.sticker.set_chat_sticker_set import SetChatStickerSet

from .methods.chat.user.ban_chat_member import BanChatMember
from .methods.chat.user.ban_chat_sender_chat import BanChatSenderChat
from .methods.chat.user.promote_chat_member import PromoteChatMember
from .methods.chat.user.restrict_chat_member import RestrictChatMember
from .methods.chat.user.set_chat_administrator_custom_title import SetChatAdministratorCustomTitle
from .methods.chat.user.set_chat_permissions import SetChatPermissions
from .methods.chat.user.unban_chat_member import UnbanChatMember
from .methods.chat.user.unban_chat_sender_chat import UnbanChatSenderChat

from .methods.get.get_file import GetFile
from .methods.get.get_user_profile_photos import GetUserProfilePhotos

from .methods.location.edit_message_live_location import EditMessageLiveLocation
from .methods.location.send_location import SendLocation
from .methods.location.send_venue import SendVenue

from .methods.media.send_animation import SendAnimation
from .methods.media.send_audio import SendAudio
from .methods.media.send_document import SendDocument
from .methods.media.send_media_group import SendMediaGroup
from .methods.media.send_photo import sendPhoto
from .methods.media.send_video import SendVideo
from .methods.media.send_video_note import SendVideoNote
from .methods.media.send_voice import SendVoice

from .methods.messages.copy_message import copyMessage
from .methods.messages.delete_message import deleteMessage
from .methods.messages.edit_message_text import editMessageText
from .methods.messages.forward_message import forwardMessage
from .methods.messages.send_message import sendMessage

from .methods.send.send_chat_action import SendChatAction
from .methods.send.send_contact import SendContact
from .methods.send.send_dice import SendDice
from .methods.send.send_poll import SendPoll


class Telegram:
    def __init__(self, token):
        self.token = token
        self.url = f"https://api.telegram.org/bot{token}/"
        self.send_message = sendMessage(token).send_message
        self.delete_message = deleteMessage(token).delete_message
        self.copy_message = copyMessage(token).copy_message
        self.forward_message = forwardMessage(token).forward_message
        self.edit_message_text = editMessageText(token).edit_message_text
        self.get_me = GetMe(token).get_me
        self.log_out = LogOut(token).log_out
        self.close = Close(token).close
        self.leave_chat = LeaveChat(token).leave_chat
        self.close_forum_topic = closeForumTopic(token).close_forum_topic
        self.close_general_forum_topic = closeGeneralForumTopic(
            token).close_general_forum_topic
        self.create_forum_topic = CreateForumTopic(token).create_forum_topic
        self.delete_forum_topic = deleteForumTopic(token).delete_forum_topic
        self.edit_forum_topic = editForumTopic(token).edit_forum_topic
        self.edit_general_forum_topic = editGeneralForumTopic(
            token).edit_general_forum_topic
        self.get_forum_topic_icon_stickers = GetForumTopicIconStickers(
            token).get_forum_topic_icon_stickers
        self.hide_general_forum_topic = hideGeneralForumTopic(
            token).hide_general_forum_topic
        self.reopen_forum_topic = reopenForumTopic(token).reopen_forum_topic
        self.reopen_general_forum_topic = reopenGeneralForumTopic(
            token).reopen_general_forum_topic
        self.unhide_general_forum_topic = unhideGeneralForumTopic(
            token).unhide_general_forum_topic
        self.unpin_all_forum_topic_messages = unpinAllForumTopicMessages(
            token).unpin_all_forum_topic_messages
        self.get_chat = GetChat(token).get_chat
        self.get_chat_administrators = GetChatAdministrators(
            token).get_chat_administrators
        self.get_chat_member = GetChatMember(token).get_chat_member
        self.get_chat_member_count = GetChatMemberCount(
            token).get_chat_member_count
        self.approve_chat_join_request = ApproveChatJoinRequest(
            token).approve_chat_join_request
        self.decline_chat_join_request = DeclineChatJoinRequest(
            token).decline_chat_join_request
        self.create_chat_invite_link = CreateChatInviteLink(
            token).create_chat_invite_link
        self.edit_chat_invite_link = EditChatInviteLink(
            token).edit_chat_invite_link
        self.export_chat_invite_link = ExportChatInviteLink(
            token).export_chat_invite_link
        self.revoke_chat_invite_link = RevokeChatInviteLink(
            token).revoke_chat_invite_link
        self.pin_chat_message = PinChatMessage(token).pin_chat_message
        self.unpin_all_chat_messages = UnpinAllChatMessages(
            token).unpin_all_chat_messages
        self.unpin_chat_message = UnpinChatMessage(token).unpin_chat_message
        self.set_chat_description = SetChatDescription(
            token).set_chat_description
        self.set_chat_photo = SetChatPhoto(token).set_chat_photo
        self.set_chat_title = SetChatTitle(token).set_chat_title
        self.delete_chat_sticker_set = DeleteChatStickerSet(
            token).delete_chat_sticker_set
        self.set_chat_sticker_set = SetChatStickerSet(
            token).set_chat_sticker_set
        self.ban_chat_member = BanChatMember(token).ban_chat_member
        self.ban_chat_sender_chat = BanChatSenderChat(
            token).ban_chat_sender_chat
        self.promote_chat_member = PromoteChatMember(token).promote_chat_member
        self.restrict_chat_member = RestrictChatMember(
            token).restrict_chat_member
        self.set_chat_administrator_custom_title = SetChatAdministratorCustomTitle(
            token).set_chat_administrator_custom_title
        self.set_chat_permissions = SetChatPermissions(
            token).set_chat_permissions
        self.unban_chat_member = UnbanChatMember(token).unban_chat_member
        self.unban_chat_sender_chat = UnbanChatSenderChat(
            token).unban_chat_sender_chat
        self.get_file = GetFile(token).get_file
        self.get_user_profile_photos = GetUserProfilePhotos(
            token).get_user_profile_photos
        self.edit_message_live_location = EditMessageLiveLocation(
            token).edit_message_live_location
        self.send_location = SendLocation(token).send_location
        self.send_venue = SendVenue(token).send_venue
        self.send_animation = SendAnimation(token).send_animation
        self.send_audio = SendAudio(token).send_audio
        self.send_document = SendDocument(token).send_document
        self.send_media_group = SendMediaGroup(token).send_media_group
        self.send_photo = sendPhoto(token).send_photo
        self.send_video = SendVideo(token).send_video
        self.send_video_note = SendVideoNote(token).send_video_note
        self.send_voice = SendVoice(token).send_voice
        self.send_chat_action = SendChatAction(token).send_chat_action
        self.send_contact = SendContact(token).send_contact
        self.send_dice = SendDice(token).send_dice
        self.send_poll = SendPoll(token).send_poll
        self.offset = 0

    def start_polling(self):
        while True:
            updates = self.get_updates(offset=self.offset)
            if not updates['ok']:
                continue
            for update in updates['result']:
                self.update_id = update['update_id'] + 1
                message = update.get('message')
                if message:
                    self.handle_message(message)

    def handle_update(self, update):
        pass

    def get_updates(self, offset=None, timeout=30):
        data = {'timeout': timeout}
        if offset:
            data['offset'] = offset
        response = requests.get(f'{self.url}/getUpdates', json=data)
        return response.json()
