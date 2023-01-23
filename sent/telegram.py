# -*- coding: utf-8 -*-
from __future__ import print_function

from sent import api, util, types

import threading
import time
import re
import sys
import six


class Telegram:
    def __init__(self, token, threaded=True, skip_pending=False):
        self.token = token
        self.update_listener = []
        self.skip_pending = skip_pending

        self.__stop_polling = threading.Event()
        self.last_update_id = 0
        self.exc_info = None

        self.message_subscribers_messages = []
        self.message_subscribers_callbacks = []
        self.message_subscribers_lock = threading.Lock()

        # key: chat_id, value: handler list
        self.message_subscribers_next_step = {}
        self.pre_message_subscribers_next_step = {}

        self.message_handlers = []
        self.inline_handlers = []
        self.chosen_inline_handlers = []
        self.callback_query_handlers = []

        self.threaded = threaded
        if self.threaded:
            self.worker_pool = util.ThreadPool()

    def set_webhook(self, url=None, certificate=None):
        return api.set_webhook(self.token, url, certificate)

    def remove_webhook(self):
        return self.set_webhook()  # No params resets webhook

    def get_updates(self, offset=None, limit=None, timeout=20):
        json_updates = api.get_updates(
            self.token, offset, limit, timeout)
        ret = []
        for ju in json_updates:
            ret.append(types.Update.de_json(ju))
        return ret

    def __skip_updates(self):
        total = 0
        updates = self.get_updates(offset=self.last_update_id, timeout=1)
        while updates:
            total += len(updates)
            for update in updates:
                if update.update_id > self.last_update_id:
                    self.last_update_id = update.update_id
            updates = self.get_updates(
                offset=self.last_update_id + 1, timeout=1)
        return total

    def __retrieve_updates(self, timeout=20):
        if self.skip_pending:
            self.skip_pending = False
        updates = self.get_updates(
            offset=(self.last_update_id + 1), timeout=timeout)
        self.process_new_updates(updates)

    def process_new_updates(self, updates):
        new_messages = []
        new_inline_querys = []
        new_chosen_inline_results = []
        new_callback_querys = []
        for update in updates:
            if update.update_id > self.last_update_id:
                self.last_update_id = update.update_id
            if update.message:
                new_messages.append(update.message)
            if update.inline_query:
                new_inline_querys.append(update.inline_query)
            if update.chosen_inline_result:
                new_chosen_inline_results.append(update.chosen_inline_result)
            if update.callback_query:
                new_callback_querys.append(update.callback_query)
        if len(new_messages) > 0:
            self.process_new_messages(new_messages)
        if len(new_inline_querys) > 0:
            self.process_new_inline_query(new_inline_querys)
        if len(new_chosen_inline_results) > 0:
            self.process_new_chosen_inline_query(new_chosen_inline_results)
        if len(new_callback_querys) > 0:
            self.process_new_callback_query(new_callback_querys)

    def process_new_messages(self, new_messages):
        self._append_pre_next_step_handler()
        self.__notify_update(new_messages)
        self._notify_command_handlers(self.message_handlers, new_messages)
        self._notify_message_subscribers(new_messages)
        self._notify_message_next_handler(new_messages)

    def process_new_inline_query(self, new_inline_querys):
        self._notify_command_handlers(self.inline_handlers, new_inline_querys)

    def process_new_chosen_inline_query(self, new_chosen_inline_querys):
        self._notify_command_handlers(
            self.chosen_inline_handlers, new_chosen_inline_querys)

    def process_new_callback_query(self, new_callback_querys):
        self._notify_command_handlers(
            self.callback_query_handlers, new_callback_querys)

    def __notify_update(self, new_messages):
        for listener in self.update_listener:
            self.__exec_task(listener, new_messages)

    def polling(self, none_stop=False, interval=0, timeout=20):
        if self.threaded:
            self.__threaded_polling(none_stop, interval, timeout)
        else:
            self.__non_threaded_polling(none_stop, interval, timeout)

    def __threaded_polling(self, none_stop=False, interval=0, timeout=3):
        self.__stop_polling.clear()
        error_interval = .25

        polling_thread = util.WorkerThread(name="PollingThread")
        or_event = util.OrEvent(
            polling_thread.done_event,
            polling_thread.exception_event,
            self.worker_pool.exception_event
        )

        while not self.__stop_polling.wait(interval):
            or_event.clear()
            try:
                polling_thread.put(self.__retrieve_updates, timeout)

                or_event.wait()  # wait for polling thread finish, polling thread error or thread pool error

                polling_thread.raise_exceptions()
                self.worker_pool.raise_exceptions()

                error_interval = .25
            except api.ApiException as e:
                if not none_stop:
                    self.__stop_polling.set()
                else:
                    polling_thread.clear_exceptions()
                    self.worker_pool.clear_exceptions()
                    time.sleep(error_interval)
                    error_interval *= 2
            except KeyboardInterrupt:
                self.__stop_polling.set()
                polling_thread.stop()
                break

    def __non_threaded_polling(self, none_stop=False, interval=0, timeout=3):
        self.__stop_polling.clear()
        error_interval = .25

        while not self.__stop_polling.wait(interval):
            try:
                self.__retrieve_updates(timeout)
                error_interval = .25
            except api.ApiException as e:
                if not none_stop:
                    self.__stop_polling.set()
                else:
                    time.sleep(error_interval)
                    error_interval *= 2
            except KeyboardInterrupt:
                self.__stop_polling.set()
                break

    def __exec_task(self, task, *args, **kwargs):
        if self.threaded:
            self.worker_pool.put(task, *args, **kwargs)
        else:
            task(*args, **kwargs)

    def stop_polling(self):
        self.__stop_polling.set()

    def set_update_listener(self, listener):
        self.update_listener.append(listener)

    def get_me(self):
        result = api.get_me(self.token)
        return types.User.de_json(result)

    def log_out(self):
        return api.log_out(self.token)

    def close(self):
        return api.close(self.token)

    def download_file(self, file_path):
        return api.download_file(self.token, file_path)

    def send_message(self, chat_id, text, reply_to_message_id=None, reply_markup=None, disable_web_page_preview=None,
                     disable_notification=None, protect_content=None, entities=None, parse_mode=None, allow_sending_without_reply=None, message_thread_id=None):
        return types.Message.de_json(
            api.send_message(self.token, chat_id, text, reply_to_message_id,
                             reply_markup, disable_web_page_preview, disable_notification, protect_content, entities, parse_mode, allow_sending_without_reply, message_thread_id))

    def forward_message(self, chat_id, from_chat_id, message_id, disable_notification=None, protect_content=None, message_thread_id=None):
        return types.Message.de_json(
            api.forward_message(self.token, chat_id, from_chat_id, message_id, disable_notification, protect_content, message_thread_id))

    def copy_message(self, chat_id, from_chat_id, message_id, reply_markup=None, allow_sending_without_reply=None, reply_to_message_id=None, caption=None, parse_mode=None, caption_entities=None, disable_notification=None, protect_content=None, message_thread_id=None):
        return types.Message.de_json(
            api.copy_message(self.token, chat_id, from_chat_id, message_id, reply_markup, allow_sending_without_reply, reply_to_message_id, caption, parse_mode, caption_entities, disable_notification, protect_content, message_thread_id))

    def send_photo(self, chat_id, photo, caption=None, parse_mode=None, caption_entities=None, has_spoiler=None,
                   disable_notification=None, protect_content=None, allow_sending_without_reply=None, reply_to_message_id=None, reply_markup=None, message_thread_id=None):
        return types.Message.de_json(
            api.send_photo(self.token, chat_id, photo, caption=None, parse_mode=None, caption_entities=None, has_spoiler=None,
                           disable_notification=None, protect_content=None, allow_sending_without_reply=None, reply_to_message_id=None, reply_markup=None, message_thread_id=None))

    def send_audio(self, chat_id, audio, caption=None, parse_mode=None, caption_entities=None, duration=None, performer=None, title=None, thumb=None, disable_notification=None, protect_content=None, reply_to_message_id=None,
                   allow_sending_without_reply=None, reply_markup=None, message_thread_id=None):
        return types.Message.de_json(
            api.send_audio(self.token, chat_id, audio, caption=None, parse_mode=None, caption_entities=None, duration=None, performer=None, title=None, thumb=None, disable_notification=None, protect_content=None, reply_to_message_id=None,
                           allow_sending_without_reply=None, reply_markup=None, message_thread_id=None))

    def send_document(self, chat_id, document, thumb=None, caption=None, parse_mode=None, caption_entities=None, disable_content_type_detection=None, disable_notification=None,
                      protect_content=None, reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, message_thread_id=None):
        return types.Message.de_json(
            api.send_document(self.token, chat_id, document, thumb=None, caption=None, parse_mode=None, caption_entities=None, disable_content_type_detection=None, disable_notification=None,
                              protect_content=None, reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, message_thread_id=None))

    def send_sticker(self, chat_id, data, reply_to_message_id=None, reply_markup=None, disable_notification=None):
        return types.Message.de_json(
            api.send_data(self.token, chat_id, data, 'sticker', reply_to_message_id, reply_markup,
                          disable_notification))

    def send_animation(self, chat_id, animation, duration=None, width=None, height=None, thumb=None, caption=None, parse_mode=None, caption_entities=None, has_spoiler=None,
                       disable_notification=None, protect_content=None, reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, message_thread_id=None):
        return types.Message.de_json(
            api.send_animation(self.token, chat_id, animation, duration=None, width=None, height=None, thumb=None, caption=None, parse_mode=None, caption_entities=None, has_spoiler=None,
                               disable_notification=None, protect_content=None, reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, message_thread_id=None))

    def send_voice(self, chat_id, voice, caption=None, parse_mode=None, caption_entities=None, duration=None, disable_notification=None, protect_content=None,
                   reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, message_thread_id=None):
        return types.Message.de_json(
            api.send_voice(self.token, chat_id, voice, caption=None, parse_mode=None, caption_entities=None, duration=None, disable_notification=None, protect_content=None,
                           reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, message_thread_id=None))

    def send_video_note(self, chat_id, video_note, duration=None, length=None, thumb=None,
                        disable_notification=None, protect_content=None, reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, message_thread_id=None):
        return types.Message.de_json(
            api.send_video_note(self.token, chat_id, video_note, duration=None, length=None, thumb=None,
                                disable_notification=None, protect_content=None, reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, message_thread_id=None))

    def send_media_group(self, chat_id, media, disable_notification=None, protect_content=None,
                         reply_to_message_id=None, allow_sending_without_reply=None, message_thread_id=None):
        return types.Message.de_json(
            api.send_media_group(self.token, chat_id, media, disable_notification=None, protect_content=None,
                                 reply_to_message_id=None, allow_sending_without_reply=None, message_thread_id=None))

    def send_location(self, chat_id, latitude, longitude, horizontal_accuracy=None, live_period=None, heading=None, proximity_alert_radius=None, disable_notification=None, protect_content=None,
                      reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, message_thread_id=None):
        return types.Message.de_json(
            api.send_location(self.token, chat_id, latitude, longitude, horizontal_accuracy=None, live_period=None, heading=None, proximity_alert_radius=None, disable_notification=None, protect_content=None,
                              reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, message_thread_id=None))

    def send_video(self, chat_id, video, duration=None, width=None, height=None, thumb=None, caption=None, parse_mode=None, caption_entities=None, has_spoiler=None, supports_streaming=None,
                   disable_notification=None, protect_content=None, reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, message_thread_id=None):
        return types.Message.de_json(
            api.send_video(self.token, chat_id, video, duration=None, width=None, height=None, thumb=None, caption=None, parse_mode=None, caption_entities=None, has_spoiler=None, supports_streaming=None,
                           disable_notification=None, protect_content=None, reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, message_thread_id=None))

    def send_venue(self, chat_id, latitude, longitude, title, address, foursquare_id=None, foursquare_type=None, google_place_id=None, google_place_type=None, disable_notification=None,
                   protect_content=None, reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, message_thread_id=None):
        return types.Message.de_json(
            api.send_venue(self.token, chat_id, latitude, longitude, title, address, foursquare_id=None, foursquare_type=None, google_place_id=None, google_place_type=None, disable_notification=None,
                           protect_content=None, reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, message_thread_id=None)
        )

    def send_contact(self, chat_id, phone_number, first_name, last_name=None, vcard=None, disable_notification=None,
                     protect_content=None, reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, message_thread_id=None):
        return types.Message.de_json(
            api.send_contact(self.token, chat_id, phone_number, first_name, last_name=None, vcard=None, disable_notification=None,
                             protect_content=None, reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, message_thread_id=None)
        )

    def send_poll(self, chat_id, question, options, is_anonymous=None, type=None, allows_multiple_answers=None, correct_option_id=None, explanation=None, explanation_parse_mode=None, explanation_entities=None, open_period=None, close_date=None,
                  is_closed=None, disable_notification=None, protect_content=None, reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, message_thread_id=None):
        return types.Message.de_json(
            api.send_poll(self.token, chat_id, question, options, is_anonymous=None, type=None, allows_multiple_answers=None, correct_option_id=None, explanation=None, explanation_parse_mode=None, explanation_entities=None, open_period=None, close_date=None,
                          is_closed=None, disable_notification=None, protect_content=None, reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, message_thread_id=None)
        )

    def send_dice(self, chat_id, emoji=None, disable_notification=None, protect_content=None, reply_to_message_id=None, allow_sending_without_reply=None,
                  reply_markup=None, message_thread_id=None):
        return types.Message.de_json(
            api.send_dice(self.token, chat_id, emoji=None, disable_notification=None, protect_content=None, reply_to_message_id=None, allow_sending_without_reply=None,
                          reply_markup=None, message_thread_id=None)
        )

    def send_chat_action(self, chat_id, action, message_thread_id):
        return api.send_chat_action(self.token, chat_id, action, message_thread_id)

    def get_user_profile_photos(self, user_id, offset=None, limit=None):
        result = api.get_user_profile_photos(
            self.token, user_id, offset, limit)
        return types.UserProfilePhotos.de_json(result)

    def get_file(self, file_id):
        return types.File.de_json(api.get_file(self.token, file_id))

    def ban_chat_member(self, chat_id, user_id, until_date=None, revoke_messages=None):
        return api.ban_chat_member(self.token, chat_id, user_id, until_date=None, revoke_messages=None)

    def unban_chat_member(self, chat_id, user_id, only_if_banned=None):
        return api.unban_chat_member(self.token, chat_id, user_id, only_if_banned=None)

    def restrict_chat_member(token, chat_id, user_id, permissions, until_date=None):
        return api.restrict_chat_member(token, chat_id, user_id, permissions, until_date=None)

    def promote_chat_member(self, chat_id, user_id, is_anonymous=None, can_manage_chat=None, can_post_messages=None, can_edit_messages=None, can_delete_messages=None,
                            can_manage_video_chats=None, can_restrict_members=None, can_promote_members=None, can_change_info=None, can_invite_users=None, can_pin_messages=None, can_manage_topics=None):
        return api.promote_chat_member(self.token, chat_id, user_id, is_anonymous=None, can_manage_chat=None, can_post_messages=None, can_edit_messages=None, can_delete_messages=None,
                                       can_manage_video_chats=None, can_restrict_members=None, can_promote_members=None, can_change_info=None, can_invite_users=None, can_pin_messages=None, can_manage_topics=None)

    def set_admininistrator_custom_title(self, chat_id, user_id, custom_title):
        return api.set_admininistrator_custom_title(self.token, chat_id, user_id, custom_title)

    def ban_chat_sender_chat(self, chat_id, sender_chat_id):
        return api.ban_chat_sender_chat(self.token, chat_id, sender_chat_id)

    def leave_chat(self, chat_id):
        return api.leave_chat(self.token, chat_id)

    def unban_chat_sender_chat(self, chat_id, sender_chat_id):
        return api.unban_chat_sender_chat(self.token, chat_id, sender_chat_id)

    def set_chat_permissions(self, chat_id, permissions):
        return api.set_chat_permissions(self.token, chat_id, permissions)

    def create_chat_invite_link(self, chat_id, name=None, expire_date=None, member_limit=None, creates_join_request=None):
        return api.create_chat_invite_link(self.token, chat_id, name=None, expire_date=None, member_limit=None, creates_join_request=None)

    def edit_chat_invite_link(self, chat_id, name=None, expire_date=None, member_limit=None, creates_join_request=None):
        return api.edit_chat_invite_link(self.token, chat_id, name=None, expire_date=None, member_limit=None, creates_join_request=None)

    def revoke_chat_invite_link(self, chat_id, invite_link):
        return api.revoke_chat_invite_link(self.token, chat_id, invite_link)

    def revoke_chat_invite_link(self, chat_id, invite_link):
        return api.revoke_chat_invite_link(self.token, chat_id, invite_link)

    def approve_chat_join_request(self, chat_id, user_id):
        return api.approve_chat_join_request(self.token, chat_id, user_id)

    def decline_chat_join_request(self, chat_id, user_id):
        return api.decline_chat_join_request(self.token, chat_id, user_id)

    def set_chat_photo(self, chat_id, photo):
        return api.set_chat_photo(self.token, chat_id, photo)

    def delete_chat_photo(self, chat_id):
        return api.delete_chat_photo(self.token, chat_id)

    def set_chat_title(self, chat_id, title):
        return api.set_chat_title(self.token, chat_id, title)

    def set_chat_description(self, chat_id, description):
        return api.set_chat_description(self.token, chat_id, description)

    def set_chat_sticker_set(self, chat_id, sticker_set_name):
        return api.set_chat_sticker_set(self.token, chat_id, sticker_set_name)

    def delete_chat_sticker_set(self, chat_id):
        return api.delete_chat_sticker_set(self.token, chat_id)

    def pin_chat_message(self, chat_id, message_id, disable_notification=None):
        return api.pin_chat_message(self.token, chat_id, message_id, disable_notification=None)

    def unpin_chat_message(self, chat_id, message_id=None):
        return api.unpin_chat_message(self.token, chat_id, message_id=None)

    def unpin_all_chat_messages(self, chat_id):
        return api.unpin_all_chat_messages(self.token, chat_id)

    def get_chat(self, chat_id):
        return api.get_chat(self.token, chat_id)

    def get_chat_administrators(self, chat_id):
        return api.get_chat_administrators(self.token, chat_id)

    def get_chat_member_count(self, chat_id):
        return api.get_chat_member_count(self.token, chat_id)

    def get_chat_member(self, chat_id):
        return api.get_chat_member(self.token, chat_id)

    def get_chat_administrators(self, chat_id):
        return api.get_chat_administrators(self.token, chat_id)

    def get_chat_administrators(self, chat_id):
        return api.get_chat_administrators(self.token, chat_id)

    def get_chat_administrators(self, chat_id):
        return api.get_chat_administrators(self.token, chat_id)

    def get_forum_topic_icon_stickers(self):
        return api.get_forum_topic_icon_stickers(self.token)

    def create_forum_topic(self, chat_id, name, icon_color=None, icon_custom_emoji_id=None):
        return api.create_forum_topic(self.token, chat_id, name, icon_color=None, icon_custom_emoji_id=None)

    def edit_forum_topic(self, chat_id, message_thread_id, name=None, icon_custom_emoji_id=None):
        return api.edit_forum_topic(self.token, chat_id, message_thread_id, name=None, icon_custom_emoji_id=None)

    def close_forum_topic(self, chat_id, message_thread_id):
        return api.close_forum_topic(self.token, chat_id, message_thread_id)

    def reopen_forum_topic(self, chat_id, message_thread_id):
        return api.reopen_forum_topic(self.token, chat_id, message_thread_id)

    def delete_forum_topic(self, chat_id, message_thread_id):
        return api.delete_forum_topic(self.token, chat_id, message_thread_id)

    def unpin_all_forum_topic_messages(self, chat_id, message_thread_id):
        return api.unpin_all_forum_topic_messages(self.token, chat_id, message_thread_id)

    def edit_genral_forum_topic(self, chat_id, name):
        return api.edit_genral_forum_topic(self.token, chat_id, name)

    def close_genral_forum_topic(self, chat_id):
        return api.close_genral_forum_topic(self.token, chat_id)

    def reopen_genral_forum_topic(self, chat_id):
        return api.reopen_genral_forum_topic(self.token, chat_id)

    def hide_genral_forum_topic(self, chat_id):
        return api.hide_genral_forum_topic(self.token, chat_id)

    def unhide_genral_forum_topic(self, chat_id):
        return api.unhide_genral_forum_topic(self.token, chat_id)

    def set_my_commands(self, commands, scope=None, language_code=None):
        return api.set_my_commands(self.token, commands, scope=None, language_code=None)

    def delete_my_commands(self, scope=None, language_code=None):
        return api.delete_my_commands(self.token, scope=None, language_code=None)

    def get_my_commands(self, scope=None, language_code=None):
        return api.get_my_commands(self.token, scope=None, language_code=None)

    def set_chat_menu_button(self, menu_button=None, chat_id=None):
        return api.set_chat_menu_button(self.token, menu_button=None, chat_id=None)

    def get_chat_menu_button(self, chat_id=None):
        return api.get_chat_menu_button(self.token, chat_id=None)

    def set_my_default_administrator_rights(self, rights=None, for_channels=None):
        return api.set_my_default_administrator_rights(self.token, rights=None, for_channels=None)

    def get_my_default_administrator_rights(self, for_channels=None):
        return api.get_my_default_administrator_rights(self.token, for_channels=None)

    def edit_message_text(self, text, chat_id=None, message_id=None, inline_message_id=None, parse_mode=None,
                          entities=None, disable_web_page_preview=None, reply_markup=None):
        results = api.edit_message_text(self.token, text, chat_id=None, message_id=None, inline_message_id=None, parse_mode=None,
                                        entities=None, disable_web_page_preview=None, reply_markup=None)
        if type(results) == bool:
            return results
        return types.Message.de_json(results)

    def edit_message_caption(self, caption, chat_id=None, message_id=None, inline_message_id=None,
                             parse_mode=None, caption_entities=None, reply_markup=None):
        return api.edit_message_caption(self.token, caption, chat_id=None, message_id=None, inline_message_id=None,
                                        parse_mode=None, caption_entities=None, reply_markup=None)

    def edit_message_media(self, media, chat_id=None, message_id=None, reply_markup=None):
        return api.edit_message_media(self.token, media, chat_id=None, message_id=None, reply_markup=None)

    def edit_message_replay_markup(self, chat_id=None, message_id=None, inline_message_id=None, reply_markup=None):
        return api.edit_message_replay_markup(self.token, chat_id=None, message_id=None, inline_message_id=None, reply_markup=None)

    def stop_poll(self, message_id, chat_id, reply_markup=None):
        return api.stop_poll(self.token, message_id, chat_id, reply_markup=None)

    def delete_message(self, chat_id, message_id):
        return api.delete_message(self.token, chat_id, message_id)

    def send_sticker(self, chat_id, sticker, disable_notification=None, protect_content=None,
                     reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, message_thread_id=None):
        return api.send_sticker(self.token, chat_id, sticker, disable_notification=None, protect_content=None,
                                reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, message_thread_id=None)

    def get_sticker_set(self, name):
        return api.get_sticker_set(self.token, name)

    def get_custom_emoji_stickers(self, custom_emoji_ids):
        return api.get_custom_emoji_stickers(self.token, custom_emoji_ids)

    def upload_sticker_file(self, user_id, png_sticker):
        return api.upload_sticker_file(self.token, user_id, png_sticker)

    def create_new_sticker_set(self, user_id, name, title, emojis, png_sticker=None, tgs_sticker=None, webm_sticker=None, sticker_type=None, mask_position=None):
        return api.create_new_sticker_set(self.token, user_id, name, title, emojis, png_sticker=None, tgs_sticker=None, webm_sticker=None, sticker_type=None, mask_position=None)

    def add_sticker_to_set(self, user_id, name, emojis, png_sticker=None, tgs_sticker=None, webm_sticker=None, mask_position=None):
        return api.add_sticker_to_set(self.token, user_id, name, emojis, png_sticker=None, tgs_sticker=None, webm_sticker=None, mask_position=None)

    def set_sticker_position_in_set(self, sticker, position):
        return api.set_sticker_position_in_set(self.token, sticker, position)

    def delete_sticker_from_set(self, sticker):
        return api.delete_sticker_from_set(self.token, sticker)

    def set_sticker_set_thumb(self, name, user_id, thumb=None):
        return api.set_sticker_set_thumb(self.token, name, user_id, thumb=None)

    def answer_inline_query(self, inline_query_id, results, cache_time=None, is_personal=None, next_offset=None,
                            switch_pm_text=None, switch_pm_parameter=None):
        return api.answer_inline_query(self.token, inline_query_id, results, cache_time=None, is_personal=None, next_offset=None,
                                       switch_pm_text=None, switch_pm_parameter=None)

    def send_invoice(self, chat_id, title, description, payload, provider_self, currency, prices,
                     max_tip_amount=None, suggested_tip_amounts=None, start_parameter=None, provider_data=None,
                     photo_url=None, photo_size=None, photo_width=None, photo_height=None,
                     need_name=None, need_phone_number=None, need_email=None, need_shipping_address=None,
                     send_phone_number_to_provider=None, send_email_to_provider=None,
                     is_flexible=None,
                     disable_notification=None, protect_content=None, reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, message_thread_id=None):
        return api.send_invoice(self.token, chat_id, title, description, payload, provider_self.token, currency, prices,
                                max_tip_amount=None, suggested_tip_amounts=None, start_parameter=None, provider_data=None,
                                photo_url=None, photo_size=None, photo_width=None, photo_height=None,
                                need_name=None, need_phone_number=None, need_email=None, need_shipping_address=None,
                                send_phone_number_to_provider=None, send_email_to_provider=None,
                                is_flexible=None,
                                disable_notification=None, protect_content=None, reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, message_thread_id=None)

    def create_invoice_link(self, title, description, payload, provider_self, currency, prices,
                            max_tip_amount=None, suggested_tip_amounts=None, provider_data=None,
                            photo_url=None, photo_size=None, photo_width=None, photo_height=None,
                            need_name=None, need_phone_number=None, need_email=None, need_shipping_address=None,
                            send_phone_number_to_provider=None, send_email_to_provider=None,
                            is_flexible=None):
        return api.create_invoice_link(self.token, title, description, payload, provider_self.token, currency, prices,
                                       max_tip_amount=None, suggested_tip_amounts=None, provider_data=None,
                                       photo_url=None, photo_size=None, photo_width=None, photo_height=None,
                                       need_name=None, need_phone_number=None, need_email=None, need_shipping_address=None,
                                       send_phone_number_to_provider=None, send_email_to_provider=None,
                                       is_flexible=None)

    def answer_shipping_query(self, shipping_query_id, ok, shipping_options=None, error_message=None):
        return api.answer_shipping_query(self.token, shipping_query_id, ok, shipping_options=None, error_message=None)

    def answer_pre_checkout_query(self, pre_checkout_query_id, ok, error_message=None):
        return api.answer_pre_checkout_query(self.token, pre_checkout_query_id, ok, error_message=None)

    def answer_callback_query(self, callback_query_id, text=None, show_alert=None, url=None, cache_time=None):
        return api.answer_callback_query(self.token, callback_query_id, text=None, show_alert=None, url=None, cache_time=None)

    def set_passport_data_errors(self, user_id, errors):
        return api.set_passport_data_errors(self.token, user_id, errors)

    def set_game_score(self, user_id, score, force=None, disable_edit_message=None, chat_id=None, message_id=None, inline_message_id=None):
        return api.set_game_score(self.token, user_id, score, force=None, disable_edit_message=None, chat_id=None, message_id=None, inline_message_id=None)

    def get_game_hight_score(self, user_id, chat_id=None, message_id=None, inline_message_id=None):
        return api.get_game_hight_score(self.token, user_id, chat_id=None, message_id=None, inline_message_id=None)

    def reply_to(self, message, text, entities=None, parse_mode=None, reply_markup=None, allow_sending_without_reply=None, protect_content=None, disable_notification=None, disable_web_page_preview=None, **kwargs):
        return self.send_message(message.chat.id, text, reply_to_message_id=message.message_id, entities=entities, parse_mode=parse_mode, reply_markup=reply_markup, allow_sending_without_reply=allow_sending_without_reply, protect_content=protect_content, disable_notification=disable_notification, disable_web_page_preview=disable_web_page_preview, **kwargs)

    def register_for_reply(self, message, callback):
        with self.message_subscribers_lock:
            self.message_subscribers_messages.insert(0, message.message_id)
            self.message_subscribers_callbacks.insert(0, callback)
            if len(self.message_subscribers_messages) > 10000:
                self.message_subscribers_messages.pop()
                self.message_subscribers_callbacks.pop()

    def _notify_message_subscribers(self, new_messages):
        for message in new_messages:
            if not message.reply_to_message:
                continue

            reply_msg_id = message.reply_to_message.message_id
            if reply_msg_id in self.message_subscribers_messages:
                index = self.message_subscribers_messages.index(reply_msg_id)
                self.message_subscribers_callbacks[index](message)

                with self.message_subscribers_lock:
                    index = self.message_subscribers_messages.index(
                        reply_msg_id)
                    del self.message_subscribers_messages[index]
                    del self.message_subscribers_callbacks[index]

    def register_next_step_handler(self, message, callback):
        chat_id = message.chat.id
        if chat_id in self.pre_message_subscribers_next_step:
            self.pre_message_subscribers_next_step[chat_id].append(callback)
        else:
            self.pre_message_subscribers_next_step[chat_id] = [callback]

    def _notify_message_next_handler(self, new_messages):
        for message in new_messages:
            chat_id = message.chat.id
            if chat_id in self.message_subscribers_next_step:
                handlers = self.message_subscribers_next_step[chat_id]
                for handler in handlers:
                    self.__exec_task(handler, message)
                self.message_subscribers_next_step.pop(chat_id, None)

    def _append_pre_next_step_handler(self):
        for k in self.pre_message_subscribers_next_step.keys():
            if k in self.message_subscribers_next_step:
                self.message_subscribers_next_step[k].extend(
                    self.pre_message_subscribers_next_step[k])
            else:
                self.message_subscribers_next_step[k] = self.pre_message_subscribers_next_step[k]
        self.pre_message_subscribers_next_step = {}

    def message_handler(self, commands=None, regexp=None, func=None, content_types=['text']):
        def decorator(handler):
            self.add_message_handler(
                handler, commands, regexp, func, content_types)
            return handler

        return decorator

    def add_message_handler(self, handler, commands=None, regexp=None, func=None, content_types=None):
        if content_types is None:
            content_types = ['text']

        filters = {'content_types': content_types}
        if regexp:
            filters['regexp'] = regexp
        if func:
            filters['lambda'] = func
        if commands:
            filters['commands'] = commands

        handler_dict = {
            'function': handler,
            'filters': filters
        }

        self.message_handlers.append(handler_dict)

    def inline_handler(self, func):
        def decorator(handler):
            self.add_inline_handler(handler, func)
            return handler

        return decorator

    def add_inline_handler(self, handler, func):
        filters = {'lambda': func}

        handler_dict = {
            'function': handler,
            'filters': filters
        }

        self.inline_handlers.append(handler_dict)

    def chosen_inline_handler(self, func):
        def decorator(handler):
            self.add_chosen_inline_handler(handler, func)
            return handler

        return decorator

    def add_chosen_inline_handler(self, handler, func):
        filters = {'lambda': func}

        handler_dict = {
            'function': handler,
            'filters': filters
        }

        self.chosen_inline_handlers.append(handler_dict)

    def callback_query_handler(self, func):
        def decorator(handler):
            self.add_callback_query_handler(handler, func)

        return decorator

    def add_callback_query_handler(self, handler, func):
        filters = {'lambda': func}

        handler_dict = {
            'function': handler,
            'filters': filters
        }

        self.callback_query_handlers.append(handler_dict)

    @staticmethod
    def _test_message_handler(message_handler, message):
        for filter, filter_value in six.iteritems(message_handler['filters']):
            if not Telegram._test_filter(filter, filter_value, message):
                return False
        return True

    @staticmethod
    def _test_filter(filter, filter_value, message):
        if filter == 'content_types':
            return message.content_type in filter_value
        if filter == 'regexp':
            return message.content_type == 'text' and re.search(filter_value, message.text)
        if filter == 'commands':
            return message.content_type == 'text' and util.extract_command(message.text) in filter_value
        if filter == 'lambda':
            return filter_value(message)
        return False

    def _notify_command_handlers(self, handlers, new_messages):
        for message in new_messages:
            for message_handler in handlers:
                if self._test_message_handler(message_handler, message):
                    self.__exec_task(message_handler['function'], message)
                    break
