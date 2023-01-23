# -*- coding: utf-8 -*-

import requests

import sent.types
import sent.util
import sent.telegram
import sent

API_URL = "https://api.telegram.org/bot{0}/{1}"
FILE_URL = "https://api.telegram.org/file/bot{0}/{1}"

CONNECT_TIMEOUT = 3.5
READ_TIMEOUT = 9999


def _make_request(token, method_name, method='get', params=None, files=None, base_url=API_URL):
    """
    Make a request to the specified API endpoint using the given method and parameters.

    :param token: The token to use for authentication.
    :param method_name: The name of the API method to call.
    :param method: The HTTP method to use for the request (defaults to 'get').
    :param params: Additional parameters to include in the request.
    :param files: Files to upload in the request.
    :param base_url: The base URL of the API endpoint (defaults to API_URL).
    :return: The response of the request.
    """
    request_url = base_url.format(token, method_name)
    read_timeout = READ_TIMEOUT
    if params:
        if 'timeout' in params:
            read_timeout = params['timeout'] + 10
    result = requests.request(method, request_url, params=params,
                              files=files, timeout=(CONNECT_TIMEOUT, read_timeout))
    return _check_result(method_name, result)['result']


def _check_result(method_name, result):
    if result.status_code != 200:
        msg = 'The server returned HTTP {0} {1}. Response body:\n[{2}]' \
            .format(result.status_code, result.reason, result.text.encode('utf8'))
        raise ApiException(msg, method_name, result)

    try:
        result_json = result.json()
    except:
        msg = 'The server returned an invalid JSON response. Response body:\n[{0}]' \
            .format(result.text.encode('utf8'))
        raise ApiException(msg, method_name, result)

    if not result_json['ok']:
        msg = 'Error code: {0} Description: {1}' \
            .format(result_json['error_code'], result_json['description'])
        raise ApiException(msg, method_name, result)
    return result_json


def get_me(token):
    method_url = r'getMe'
    return _make_request(token, method_url)


def log_out(token):
    method_url = r'logOut'
    return _make_request(token, method_url)


def close(token):
    method_url = r'close'
    return _make_request(token, method_url)


def download_file(token, file_path):
    url = FILE_URL.format(token, file_path)
    result = requests.get(url)
    if result.status_code != 200:
        msg = 'The server returned HTTP {0} {1}. Response body:\n[{2}]' \
            .format(result.status_code, result.reason, result.text)
        raise ApiException(msg, 'Download file', result)
    return result.content


def set_webhook(token, url=None, certificate=None):
    method_url = r'setWebhook'
    payload = {
        'url': url if url else "",
    }
    files = None
    if certificate:
        files = {'certificate': certificate}

    return _make_request(token, method_url, params=payload, files=files)


def get_updates(token, offset=None, limit=None, timeout=None):
    method_url = r'getUpdates'
    payload = {}
    if offset:
        payload['offset'] = offset
    if limit:
        payload['limit'] = limit
    if timeout:
        payload['timeout'] = timeout
    return _make_request(token, method_url, params=payload)


# send | edit | copy | forward ->  messages & media

def send_message(token, chat_id, text, reply_to_message_id=None, reply_markup=None, disable_web_page_preview=None,
                 disable_notification=None, protect_content=None, entities=None, parse_mode=None, allow_sending_without_reply=None, message_thread_id=None):
    method_url = r'sendMessage'
    payload = {'chat_id': str(chat_id), 'text': text}
    if disable_web_page_preview:
        payload['disable_web_page_preview'] = disable_web_page_preview
    if reply_to_message_id:
        payload['reply_to_message_id'] = reply_to_message_id
    if reply_markup:
        payload['reply_markup'] = _convert_markup(reply_markup)
    if parse_mode:
        payload['parse_mode'] = parse_mode
    if message_thread_id:
        payload['message_thread_id'] = message_thread_id
    if entities:
        payload['entities'] = entities
    if protect_content:
        payload['protect_content'] = protect_content
    if allow_sending_without_reply:
        payload['allow_sending_without_reply'] = allow_sending_without_reply
    if disable_notification:
        payload['disable_notification'] = disable_notification
    return _make_request(token, method_url, params=payload, method='post')


def forward_message(token, chat_id, from_chat_id, message_id, disable_notification=None, protect_content=None, message_thread_id=None):
    method_url = r'forwardMessage'
    payload = {'chat_id': chat_id,
               'from_chat_id': from_chat_id, 'message_id': message_id}
    if disable_notification:
        payload['disable_notification'] = disable_notification
    if protect_content:
        payload['protect_content'] = protect_content
    if message_thread_id:
        payload['message_thread_id'] = message_thread_id
    return _make_request(token, method_url, params=payload)


def copy_message(token, chat_id, from_chat_id, message_id, reply_markup=None, allow_sending_without_reply=None, reply_to_message_id=None, caption=None, parse_mode=None, caption_entities=None, disable_notification=None, protect_content=None, message_thread_id=None):
    method_url = r'copyMessage'
    payload = {'chat_id': chat_id,
               'from_chat_id': from_chat_id, 'message_id': message_id}
    if disable_notification:
        payload['disable_notification'] = disable_notification
    if protect_content:
        payload['protect_content'] = protect_content
    if reply_markup:
        payload['reply_markup'] = reply_markup
    if allow_sending_without_reply:
        payload['allow_sending_without_reply'] = allow_sending_without_reply
    if reply_to_message_id:
        payload['reply_to_message_id'] = reply_to_message_id
    if caption_entities:
        payload['caption_entities'] = caption_entities
    if parse_mode:
        payload['parse_mode'] = parse_mode
    if message_thread_id:
        payload['message_thread_id'] = message_thread_id
    return _make_request(token, method_url, params=payload)


def send_photo(token, chat_id, photo, caption=None, parse_mode=None, caption_entities=None, has_spoiler=None,
               disable_notification=None, protect_content=None, allow_sending_without_reply=None, reply_to_message_id=None, reply_markup=None, message_thread_id=None):
    method_url = r'sendPhoto'
    payload = {'chat_id': chat_id}
    files = None
    if not sent.util.is_string(photo):
        files = {'photo': photo}
    else:
        payload['photo'] = photo
    if caption:
        payload['caption'] = caption
    if has_spoiler:
        payload['has_spoiler'] = has_spoiler
    if protect_content:
        payload['protect_content'] = protect_content
    if allow_sending_without_reply:
        payload['allow_sending_without_reply'] = allow_sending_without_reply
    if message_thread_id:
        payload['message_thread_id'] = message_thread_id
    if parse_mode:
        payload['parse_mode'] = parse_mode
    if caption_entities:
        payload['caption_entities'] = caption_entities
    if disable_notification:
        payload['disable_notification'] = disable_notification
    if reply_to_message_id:
        payload['reply_to_message_id'] = reply_to_message_id
    if reply_markup:
        payload['reply_markup'] = reply_markup
    return _make_request(token, method_url, params=payload, files=files, method='post')


def send_audio(token, chat_id, audio, caption=None, parse_mode=None, caption_entities=None, duration=None, performer=None, title=None, thumb=None, disable_notification=None, protect_content=None, reply_to_message_id=None,
               allow_sending_without_reply=None, reply_markup=None, message_thread_id=None):
    method_url = r'sendAudio'
    payload = {'chat_id': chat_id}
    files = None
    if not sent.util.is_string(audio):
        files = {'audio': audio}
    else:
        payload['audio'] = audio
    if duration:
        payload['duration'] = duration
    if caption:
        payload['caption'] = caption
    if parse_mode:
        payload['parse_mode'] = parse_mode
    if caption_entities:
        payload['caption_entities'] = caption_entities
    if thumb:
        payload['thumb'] = thumb
    if protect_content:
        payload['protect_content'] = protect_content
    if allow_sending_without_reply:
        payload['allow_sending_without_reply'] = allow_sending_without_reply
    if message_thread_id:
        payload['message_thread_id'] = message_thread_id
    if performer:
        payload['performer'] = performer
    if title:
        payload['title'] = title
    if reply_to_message_id:
        payload['reply_to_message_id'] = reply_to_message_id
    if reply_markup:
        payload['reply_markup'] = _convert_markup(reply_markup)
    if disable_notification:
        payload['disable_notification'] = disable_notification
    return _make_request(token, method_url, params=payload, files=files, method='post')


def send_document(token, chat_id, document, thumb=None, caption=None, parse_mode=None, caption_entities=None, disable_content_type_detection=None, disable_notification=None, 
                  protect_content=None, reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, message_thread_id=None):
    method_url = r'sendDocument'
    payload = {'chat_id': chat_id}
    files = None
    if not sent.util.is_string(document):
        files = {'document': document}
    else:
        payload['document'] = document
    if disable_content_type_detection:
        payload['disable_content_type_detection'] = disable_content_type_detection
    if caption:
        payload['caption'] = caption
    if parse_mode:
        payload['parse_mode'] = parse_mode
    if caption_entities:
        payload['caption_entities'] = caption_entities
    if thumb:
        payload['thumb'] = thumb
    if protect_content:
        payload['protect_content'] = protect_content
    if allow_sending_without_reply:
        payload['allow_sending_without_reply'] = allow_sending_without_reply
    if message_thread_id:
        payload['message_thread_id'] = message_thread_id
    if reply_to_message_id:
        payload['reply_to_message_id'] = reply_to_message_id
    if reply_markup:
        payload['reply_markup'] = _convert_markup(reply_markup)
    if disable_notification:
        payload['disable_notification'] = disable_notification
    return _make_request(token, method_url, params=payload, files=files, method='post')


def send_video(token, chat_id, video, duration=None, width=None, height=None, thumb=None, caption=None, parse_mode=None, caption_entities=None, has_spoiler=None, supports_streaming=None,
               disable_notification=None, protect_content=None, reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, message_thread_id=None):
    method_url = r'sendVideo'
    payload = {'chat_id': chat_id}
    files = None
    if not sent.util.is_string(video):
        files = {'video': video}
    else:
        payload['video'] = video
    if duration:
        payload['duration'] = duration
    if caption:
        payload['caption'] = caption
    if width:
        payload['width'] = width
    if height:
        payload['height'] = height
    if thumb:
        payload['thumb'] = thumb
    if parse_mode:
        payload['parse_mode'] = parse_mode
    if caption_entities:
        payload['caption_entities'] = caption_entities
    if has_spoiler:
        payload['has_spoiler'] = has_spoiler
    if supports_streaming:
        payload['supports_streaming'] = supports_streaming
    if protect_content:
        payload['protect_content'] = protect_content
    if allow_sending_without_reply:
        payload['allow_sending_without_reply'] = allow_sending_without_reply
    if message_thread_id:
        payload['message_thread_id'] = message_thread_id
    if reply_to_message_id:
        payload['reply_to_message_id'] = reply_to_message_id
    if reply_markup:
        payload['reply_markup'] = _convert_markup(reply_markup)
    if disable_notification:
        payload['disable_notification'] = disable_notification
    return _make_request(token, method_url, params=payload, files=files, method='post')

def send_animation(token, chat_id, animation, duration=None, width=None, height=None, thumb=None, caption=None, parse_mode=None, caption_entities=None, has_spoiler=None,
               disable_notification=None, protect_content=None, reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, message_thread_id=None):
    method_url = r'sendAnimation'
    payload = {'chat_id': chat_id}
    files = None
    if not sent.util.is_string(animation):
        files = {'animation': animation}
    else:
        payload['animation'] = animation
    if duration:
        payload['duration'] = duration
    if caption:
        payload['caption'] = caption
    if width:
        payload['width'] = width
    if height:
        payload['height'] = height
    if thumb:
        payload['thumb'] = thumb
    if parse_mode:
        payload['parse_mode'] = parse_mode
    if caption_entities:
        payload['caption_entities'] = caption_entities
    if has_spoiler:
        payload['has_spoiler'] = has_spoiler
    if protect_content:
        payload['protect_content'] = protect_content
    if allow_sending_without_reply:
        payload['allow_sending_without_reply'] = allow_sending_without_reply
    if message_thread_id:
        payload['message_thread_id'] = message_thread_id
    if reply_to_message_id:
        payload['reply_to_message_id'] = reply_to_message_id
    if reply_markup:
        payload['reply_markup'] = _convert_markup(reply_markup)
    if disable_notification:
        payload['disable_notification'] = disable_notification
    return _make_request(token, method_url, params=payload, files=files, method='post')


def send_voice(token, chat_id, voice, caption=None, parse_mode=None, caption_entities=None, duration=None, disable_notification=None, protect_content=None,
               reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, message_thread_id=None):
    method_url = r'sendVoice'
    payload = {'chat_id': chat_id}
    files = None
    if not sent.util.is_string(voice):
        files = {'voice': voice}
    else:
        payload['voice'] = voice
    if duration:
        payload['duration'] = duration
    if caption:
        payload['caption'] = caption
    if parse_mode:
        payload['parse_mode'] = parse_mode
    if caption_entities:
        payload['caption_entities'] = caption_entities
    if protect_content:
        payload['protect_content'] = protect_content
    if allow_sending_without_reply:
        payload['allow_sending_without_reply'] = allow_sending_without_reply
    if message_thread_id:
        payload['message_thread_id'] = message_thread_id
    if reply_to_message_id:
        payload['reply_to_message_id'] = reply_to_message_id
    if reply_markup:
        payload['reply_markup'] = _convert_markup(reply_markup)
    if disable_notification:
        payload['disable_notification'] = disable_notification
    return _make_request(token, method_url, params=payload, files=files, method='post')


def send_video_note(token, chat_id, video_note, duration=None, length=None, thumb=None,
               disable_notification=None, protect_content=None, reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, message_thread_id=None):
    method_url = r'sendVideo'
    payload = {'chat_id': chat_id}
    files = None
    if not sent.util.is_string(video_note):
        files = {'video_note': video_note}
    else:
        payload['video_note'] = video_note
    if duration:
        payload['duration'] = duration
    if length:
        payload['length'] = length
    if thumb:
        payload['thumb'] = thumb
    if protect_content:
        payload['protect_content'] = protect_content
    if allow_sending_without_reply:
        payload['allow_sending_without_reply'] = allow_sending_without_reply
    if message_thread_id:
        payload['message_thread_id'] = message_thread_id
    if reply_to_message_id:
        payload['reply_to_message_id'] = reply_to_message_id
    if reply_markup:
        payload['reply_markup'] = _convert_markup(reply_markup)
    if disable_notification:
        payload['disable_notification'] = disable_notification
    return _make_request(token, method_url, params=payload, files=files, method='post')


def send_media_group(token, chat_id, media, disable_notification=None, protect_content=None,
               reply_to_message_id=None, allow_sending_without_reply=None, message_thread_id=None):
    method_url = r'sendMediaGroup'
    payload = {'chat_id': chat_id, 'media': media}
    if protect_content:
        payload['protect_content'] = protect_content
    if allow_sending_without_reply:
        payload['allow_sending_without_reply'] = allow_sending_without_reply
    if message_thread_id:
        payload['message_thread_id'] = message_thread_id
    if reply_to_message_id:
        payload['reply_to_message_id'] = reply_to_message_id
    if disable_notification:
        payload['disable_notification'] = disable_notification
    return _make_request(token, method_url, params=payload, method='post')


def send_location(token, chat_id, latitude, longitude, horizontal_accuracy=None, live_period=None, heading=None, proximity_alert_radius=None, disable_notification=None, protect_content=None,
                  reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, message_thread_id=None):
    method_url = r'sendLocation'
    payload = {'chat_id': chat_id,
               'latitude': latitude, 'longitude': longitude}
    if reply_to_message_id:
        payload['reply_to_message_id'] = reply_to_message_id
    if reply_markup:
        payload['reply_markup'] = _convert_markup(reply_markup)
    if disable_notification:
        payload['disable_notification'] = disable_notification
    if horizontal_accuracy:
        payload['horizontal_accuracy'] = horizontal_accuracy
    if live_period:
        payload['live_period'] = live_period
    if heading:
        payload['heading'] = heading
    if proximity_alert_radius:
        payload['proximity_alert_radius'] = proximity_alert_radius
    if protect_content:
        payload['protect_content'] = protect_content
    if allow_sending_without_reply:
        payload['allow_sending_without_reply'] = allow_sending_without_reply
    if message_thread_id:
        payload['message_thread_id'] = message_thread_id
    if disable_notification:
        payload['disable_notification'] = disable_notification
    return _make_request(token, method_url, params=payload)


# To Do
def edit_message_live_location(token, chat_id, latitude, longitude, message_id=None, inline_message_id=None, horizontal_accuracy=None, heading=None, proximity_alert_radius=None,
                 reply_markup=None):
    method_url = r'editMessageLiveLocation'
    payload = {'chat_id': chat_id,
               'latitude': latitude, 'longitude': longitude}
    if message_id:
        payload['message_id'] = message_id
    if reply_markup:
        payload['reply_markup'] = _convert_markup(reply_markup)
    if inline_message_id:
        payload['inline_message_id'] = inline_message_id
    if horizontal_accuracy:
        payload['horizontal_accuracy'] = horizontal_accuracy
    if heading:
        payload['heading'] = heading
    if proximity_alert_radius:
        payload['proximity_alert_radius'] = proximity_alert_radius
    
    return _make_request(token, method_url, params=payload)

# To Do
def stop_message_live_location(token, chat_id, message_id=None, inline_message_id=None, reply_markup=None):
    method_url = r'stopMessageLiveLocation'
    payload = {'chat_id': chat_id}
    if message_id:
        payload['message_id'] = message_id
    if reply_markup:
        payload['reply_markup'] = _convert_markup(reply_markup)
    if inline_message_id:
        payload['inline_message_id'] = inline_message_id
    
    return _make_request(token, method_url, params=payload)


def send_venue(token, chat_id, latitude, longitude, title, address, foursquare_id=None, foursquare_type=None, google_place_id=None, google_place_type=None, disable_notification=None,
               protect_content=None, reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, message_thread_id=None):
    method_url = r'sendVenue'
    payload = {'chat_id': chat_id, 'latitude': latitude,
               'longitude': longitude, 'title': title, 'address': address}
    if foursquare_id:
        payload['foursquare_id'] = foursquare_id
    if foursquare_type:
        payload['foursquare_type'] = foursquare_type
    if google_place_id:
        payload['google_place_id'] = google_place_id
    if google_place_type:
        payload['google_place_type'] = google_place_type
    if protect_content:
        payload['protect_content'] = protect_content
    if allow_sending_without_reply:
        payload['allow_sending_without_reply'] = allow_sending_without_reply
    if message_thread_id:
        payload['message_thread_id'] = message_thread_id
    if disable_notification:
        payload['disable_notification'] = disable_notification
    if reply_to_message_id:
        payload['reply_to_message_id'] = reply_to_message_id
    if reply_markup:
        payload['reply_markup'] = _convert_markup(reply_markup)
    return _make_request(token, method_url, params=payload)


def send_contact(token, chat_id, phone_number, first_name, last_name=None, vcard=None, disable_notification=None,
                 protect_content=None, reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, message_thread_id=None):
    method_url = r'sendContact'
    payload = {'chat_id': chat_id,
               'phone_number': phone_number, 'first_name': first_name}
    if last_name:
        payload['last_name'] = last_name
    if vcard:
        payload['vcard'] = vcard
    if allow_sending_without_reply:
        payload['allow_sending_without_reply'] = allow_sending_without_reply
    if protect_content:
        payload['protect_content'] = protect_content
    if message_thread_id:
        payload['message_thread_id'] = message_thread_id
    if disable_notification:
        payload['disable_notification'] = disable_notification
    if reply_to_message_id:
        payload['reply_to_message_id'] = reply_to_message_id
    if reply_markup:
        payload['reply_markup'] = _convert_markup(reply_markup)
    return _make_request(token, method_url, params=payload)


def send_poll(token, chat_id, question, options, is_anonymous=None, type=None, allows_multiple_answers=None, correct_option_id=None, explanation=None, explanation_parse_mode=None, explanation_entities=None, open_period=None, close_date=None,
              is_closed=None, disable_notification=None, protect_content=None, reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, message_thread_id=None):
    method_url = r'sendPoll'
    payload = {'chat_id': chat_id, 'question': question, 'options': options}
    if type:
        payload['message_id'] = type
    if is_anonymous:
        payload['is_anonymous'] = is_anonymous
    if allows_multiple_answers:
        payload['allows_multiple_answers'] = allows_multiple_answers
    if correct_option_id:
        payload['correct_option_id'] = correct_option_id
    if explanation:
        payload['explanation'] = explanation
    if explanation_parse_mode:
        payload['explanation_parse_mode'] = explanation_parse_mode
    if explanation_entities:
        payload['explanation_entities'] = explanation_entities
    if open_period:
        payload['open_period'] = open_period
    if close_date:
        payload['close_date'] = close_date
    if is_closed:
        payload['is_closed'] = is_closed
    if disable_notification:
        payload['disable_notification'] = disable_notification
    if protect_content:
        payload['protect_content'] = protect_content
    if reply_to_message_id:
        payload['reply_to_message_id'] = reply_to_message_id
    if allow_sending_without_reply:
        payload['allow_sending_without_reply'] = allow_sending_without_reply
    if message_thread_id:
        payload['message_id'] = message_thread_id
    if reply_markup:
        payload['reply_markup'] = _convert_markup(reply_markup)
    
    return _make_request(token, method_url, params=payload)


def send_dice(token, chat_id, emoji=None, disable_notification=None, protect_content=None, reply_to_message_id=None, allow_sending_without_reply=None,
              reply_markup=None, message_thread_id=None):
    method_url = r'sendDice'
    payload = {'chat_id': chat_id}
    if emoji:
        payload['emoji'] = emoji
    if disable_notification:
        payload['disable_notification'] = disable_notification
    if protect_content:
        payload['protect_content'] = protect_content
    if reply_to_message_id:
        payload['reply_to_message_id'] = reply_to_message_id
    if allow_sending_without_reply:
        payload['allow_sending_without_reply'] = allow_sending_without_reply
    if reply_markup:
        payload['reply_markup'] = _convert_markup(reply_markup)
    if message_thread_id:
        payload['message_thread_id'] = message_thread_id
    
    return _make_request(token, method_url, params=payload)


def send_chat_action(token, chat_id, action, message_thread_id):
    method_url = r'sendChatAction'
    payload = {'chat_id': chat_id, 'action': action}
    if message_thread_id:
        payload['message_thread_id'] = message_thread_id
    return _make_request(token, method_url, params=payload)


def get_user_profile_photos(token, user_id, offset=None, limit=None):
    method_url = r'getUserProfilePhotos'
    payload = {'user_id': user_id}
    if offset:
        payload['offset'] = offset
    if limit:
        payload['limit'] = limit
    return _make_request(token, method_url, params=payload)

def get_file(token, file_id):
    method_url = r'getFile'
    return _make_request(token, method_url, params={'file_id': file_id})


# chat actions

def ban_chat_member(token, chat_id, user_id, until_date=None, revoke_messages=None):
    method_url = 'banChatMember'
    payload = {'chat_id': chat_id, 'user_id': user_id}
    if until_date:
        payload['until_date'] = until_date
    if revoke_messages:
        payload['revoke_messages'] = revoke_messages
    return _make_request(token, method_url, params=payload, method='post')


def unban_chat_member(token, chat_id, user_id, only_if_banned=None):
    method_url = 'unbanChatMember'
    payload = {'chat_id': chat_id, 'user_id': user_id}
    if only_if_banned:
        payload['only_if_banned'] = only_if_banned
    return _make_request(token, method_url, params=payload, method='post')


def restrict_chat_member(token, chat_id, user_id, permissions, until_date=None):
    method_url = 'restrictChatMember'
    payload = {'chat_id': chat_id, 'user_id': user_id, 'permissions':permissions}
    if until_date:
        payload['until_date'] = until_date
    return _make_request(token, method_url, params=payload, method='post')


def promote_chat_member(token, chat_id, user_id, is_anonymous=None, can_manage_chat=None, can_post_messages=None, can_edit_messages=None, can_delete_messages=None,
                        can_manage_video_chats=None, can_restrict_members=None, can_promote_members=None, can_change_info=None, can_invite_users=None, can_pin_messages=None, can_manage_topics=None):
    """
    Todo: add this to permision array .
    """
    method_url = 'promoteChatMember'
    payload = {'chat_id': chat_id, 'user_id': user_id}
    if is_anonymous:
        payload['until_date'] = is_anonymous
    if can_manage_chat:
        payload['can_manage_chat'] = can_manage_chat
    if can_post_messages:
        payload['can_post_messages'] = can_post_messages
    if can_edit_messages:
        payload['can_edit_messages'] = can_edit_messages
    if can_delete_messages:
        payload['can_delete_messages'] = can_delete_messages
    if can_manage_video_chats:
        payload['can_manage_video_chats'] = can_manage_video_chats
    if can_restrict_members:
        payload['can_restrict_members'] = can_restrict_members
    if can_promote_members:
        payload['can_promote_members'] = can_promote_members
    if can_change_info:
        payload['can_change_info'] = can_change_info
    if can_invite_users:
        payload['can_invite_users'] = can_invite_users
    if can_pin_messages:
        payload['can_pin_messages'] = can_pin_messages
    if can_manage_topics:
        payload['can_manage_topics'] = can_manage_topics
    return _make_request(token, method_url, params=payload, method='post')


def set_admininistrator_custom_title(token, chat_id, user_id, custom_title):
    method_url = 'setChatAdministratorCustomTitle'
    payload = {'chat_id': chat_id, 'user_id': user_id, 'custom_title': custom_title}
    return _make_request(token, method_url, params=payload, method='post')


def ban_chat_sender_chat(token, chat_id, sender_chat_id):
    method_url = 'banChatSenderChat'
    payload = {'chat_id': chat_id, 'sender_chat_id': sender_chat_id}
    return _make_request(token, method_url, params=payload, method='post')


def unban_chat_sender_chat(token, chat_id, sender_chat_id):
    method_url = 'unbanChatSenderChat'
    payload = {'chat_id': chat_id, 'sender_chat_id': sender_chat_id}
    return _make_request(token, method_url, params=payload, method='post')


def set_chat_permissions(token, chat_id, permissions):
    method_url = 'setChatPermissions'
    payload = {'chat_id': chat_id, 'permissions': permissions}
    return _make_request(token, method_url, params=payload, method='post')


def leave_chat(token, chat_id):
    method_url = 'leaveChat'
    payload = {'chat_id': chat_id}
    return _make_request(token, method_url, params=payload, method='post')



# chat link

def create_chat_invite_link(token, chat_id, name=None, expire_date=None, member_limit=None, creates_join_request=None):
    method_url = 'createChatInviteLink'
    payload = {'chat_id': chat_id}
    if name:
        payload['name'] = name
    if expire_date:
        payload['expire_date'] = expire_date
    if member_limit:
        payload['member_limit'] = member_limit
    if creates_join_request:
        payload['creates_join_request'] = creates_join_request
    return _make_request(token, method_url, params=payload)


def edit_chat_invite_link(token, chat_id, name=None, expire_date=None, member_limit=None, creates_join_request=None):
    method_url = 'editChatInviteLink'
    payload = {'chat_id': chat_id}
    if name:
        payload['name'] = name
    if expire_date:
        payload['expire_date'] = expire_date
    if member_limit:
        payload['member_limit'] = member_limit
    if creates_join_request:
        payload['creates_join_request'] = creates_join_request
    return _make_request(token, method_url, params=payload, method='post')


def revoke_chat_invite_link(token, chat_id, invite_link):
    method_url = 'revokeChatInviteLink'
    payload = {'chat_id': chat_id, 'invite_link': invite_link}
    return _make_request(token, method_url, params=payload, method='post')


def revoke_chat_invite_link(token, chat_id, invite_link):
    method_url = 'revokeChatInviteLink'
    payload = {'chat_id': chat_id, 'invite_link': invite_link}
    return _make_request(token, method_url, params=payload, method='post')


# chat Join request

def approve_chat_join_request(token, chat_id, user_id):
    method_url = 'approveChatJoinRequest'
    payload = {'chat_id': chat_id, 'user_id': user_id}
    return _make_request(token, method_url, params=payload, method='post')


def decline_chat_join_request(token, chat_id, user_id):
    method_url = 'declineChatJoinRequest'
    payload = {'chat_id': chat_id, 'user_id': user_id}
    return _make_request(token, method_url, params=payload, method='post')


# chat info set

def set_chat_photo(token, chat_id, photo):
    method_url = 'setChatPhoto'
    files = None
    payload = {'chat_id': chat_id}
    if not sent.util.is_string(photo):
        files = {photo: photo}
    else:
        payload['photo'] = photo
        
    return _make_request(token, method_url, params=payload, files=files, method='post')


def delete_chat_photo(token, chat_id):
    method_url = 'deleteChatPhoto'
    payload = {'chat_id': chat_id}
    return _make_request(token, method_url, params=payload, method='post')


def set_chat_title(token, chat_id, title):
    method_url = 'setChatTitle'
    payload = {'chat_id': chat_id, 'title': title}
    return _make_request(token, method_url, params=payload, method='post')


def set_chat_description(token, chat_id, description):
    method_url = 'setChatDescription'
    payload = {'chat_id': chat_id, 'description': description}
    return _make_request(token, method_url, params=payload, method='post')


def set_chat_sticker_set(token, chat_id, sticker_set_name):
    method_url = 'setChatStickerSet'
    payload = {'chat_id': chat_id, 'sticker_set_name': sticker_set_name}
    return _make_request(token, method_url, params=payload, method='post')


def delete_chat_sticker_set(token, chat_id):
    method_url = 'deleteChatStickerSet'
    payload = {'chat_id': chat_id}
    return _make_request(token, method_url, params=payload, method='post')


# chat message pin

def pin_chat_message(token, chat_id, message_id, disable_notification=None):
    method_url = 'pinChatMessage'
    payload = {'chat_id': chat_id, 'message_id': message_id}
    if disable_notification:
        payload['disable_notification'] = disable_notification
    return _make_request(token, method_url, params=payload, method='post')


def unpin_chat_message(token, chat_id, message_id=None):
    method_url = 'unpinChatMessage'
    payload = {'chat_id': chat_id}
    if message_id:
        payload['message_id'] = message_id
    return _make_request(token, method_url, params=payload, method='post')


def unpin_all_chat_messages(token, chat_id):
    method_url = 'unpinChatMessage'
    payload = {'chat_id': chat_id}
    return _make_request(token, method_url, params=payload, method='post')


# get chat details

def get_chat(token, chat_id):
    method_url = 'getChat'
    payload = {'chat_id': chat_id}
    return _make_request(token, method_url, params=payload)


def get_chat_administrators(token, chat_id):
    method_url = 'getChatAdministrators'
    payload = {'chat_id': chat_id}
    return _make_request(token, method_url, params=payload)


def get_chat_member_count(token, chat_id):
    method_url = 'getChatMemberCount'
    payload = {'chat_id': chat_id}
    return _make_request(token, method_url, params=payload)


def get_chat_member(token, chat_id):
    method_url = 'getChatMember'
    payload = {'chat_id': chat_id}
    return _make_request(token, method_url, params=payload)


def get_chat_administrators(token, chat_id):
    method_url = 'getChatAdministrators'
    payload = {'chat_id': chat_id}
    return _make_request(token, method_url, params=payload)


def get_chat_administrators(token, chat_id):
    method_url = 'getChatAdministrators'
    payload = {'chat_id': chat_id}
    return _make_request(token, method_url, params=payload)


def get_chat_administrators(token, chat_id):
    method_url = 'getChatAdministrators'
    payload = {'chat_id': chat_id}
    return _make_request(token, method_url, params=payload)



# forum topics

def get_forum_topic_icon_stickers(token):
    method_url = 'getForumTopicIconStickers'
    return _make_request(token, method_url)


def create_forum_topic(token, chat_id, name, icon_color=None, icon_custom_emoji_id=None):
    method_url = 'createForumTopic'
    payload = {'chat_id': chat_id, 'name': name}
    if icon_color:
        payload['icon_color'] = icon_color
    if icon_custom_emoji_id:
        payload['icon_custom_emoji_id'] = icon_custom_emoji_id
    return _make_request(token, method_url, params=payload)


def edit_forum_topic(token, chat_id, message_thread_id, name=None, icon_custom_emoji_id=None):
    method_url = 'editForumTopic'
    payload = {'chat_id': chat_id, 'message_thread_id': message_thread_id}
    if name:
        payload['name'] = name
    if icon_custom_emoji_id:
        payload['icon_custom_emoji_id'] = icon_custom_emoji_id
    return _make_request(token, method_url, params=payload)


def close_forum_topic(token, chat_id, message_thread_id):
    method_url = 'closeForumTopic'
    payload = {'chat_id': chat_id, 'message_thread_id': message_thread_id}
    return _make_request(token, method_url, params=payload)


def reopen_forum_topic(token, chat_id, message_thread_id):
    method_url = 'reopenForumTopic'
    payload = {'chat_id': chat_id, 'message_thread_id': message_thread_id}
    return _make_request(token, method_url, params=payload)


def delete_forum_topic(token, chat_id, message_thread_id):
    method_url = 'deleteForumTopic'
    payload = {'chat_id': chat_id, 'message_thread_id': message_thread_id}
    return _make_request(token, method_url, params=payload)


def unpin_all_forum_topic_messages(token, chat_id, message_thread_id):
    method_url = 'unpinAllForumTopicMessages'
    payload = {'chat_id': chat_id, 'message_thread_id': message_thread_id}
    return _make_request(token, method_url, params=payload)


def edit_genral_forum_topic(token, chat_id, name):
    method_url = 'editGeneralForumTopic'
    payload = {'chat_id': chat_id, 'name': name}
    return _make_request(token, method_url, params=payload)


def close_genral_forum_topic(token, chat_id):
    method_url = 'closeGeneralForumTopic'
    payload = {'chat_id': chat_id}
    return _make_request(token, method_url, params=payload)


def reopen_genral_forum_topic(token, chat_id):
    method_url = 'reopenGeneralForumTopic'
    payload = {'chat_id': chat_id}
    return _make_request(token, method_url, params=payload)


def hide_genral_forum_topic(token, chat_id):
    method_url = 'hideGeneralForumTopic'
    payload = {'chat_id': chat_id}
    return _make_request(token, method_url, params=payload)


def unhide_genral_forum_topic(token, chat_id):
    method_url = 'unhideGeneralForumTopic'
    payload = {'chat_id': chat_id}
    return _make_request(token, method_url, params=payload)


# my commands

def set_my_commands(token, commands, scope=None, language_code=None):
    method_url = 'setMyCommands'
    payload = {'commands': commands}
    if scope:
        payload['scope'] = scope
    if language_code:
        payload['language_code'] = language_code
    return _make_request(token, method_url, params=payload, method='post')


def delete_my_commands(token, scope=None, language_code=None):
    method_url = 'deleteMyCommands'
    payload = {}
    if scope:
        payload['scope'] = scope
    if language_code:
        payload['language_code'] = language_code
    return _make_request(token, method_url, params=payload, method='post')


def get_my_commands(token, scope=None, language_code=None):
    method_url = 'getMyCommands'
    payload = {}
    if scope:
        payload['scope'] = scope
    if language_code:
        payload['language_code'] = language_code
    return _make_request(token, method_url, params=payload)



# My Menu

def set_chat_menu_button(token, menu_button=None, chat_id=None):
    method_url = 'setChatMenuButton'
    payload = {}
    if menu_button:
        payload['menu_button'] = menu_button
    if chat_id:
        payload['chat_id'] = chat_id
    return _make_request(token, method_url, params=payload, method='post')

def get_chat_menu_button(token, chat_id=None):
    method_url = 'getChatMenuButton'
    payload = {}
    if chat_id:
        payload['chat_id'] = chat_id
    return _make_request(token, method_url, params=payload)


# My Rights

def set_my_default_administrator_rights(token, rights=None, for_channels=None):
    method_url = 'setMyDefaultAdministratorRights'
    payload = {}
    if rights:
        payload['menu_button'] = rights
    if for_channels:
        payload['for_channels'] = for_channels
    return _make_request(token, method_url, params=payload, method='post')


def get_my_default_administrator_rights(token, for_channels=None):
    method_url = 'getMyDefaultAdministratorRights'
    payload = {}
    if for_channels:
        payload['for_channels'] = for_channels
    return _make_request(token, method_url, params=payload)


# Updating messages

def edit_message_text(token, text, chat_id=None, message_id=None, inline_message_id=None, parse_mode=None,
                      entities=None, disable_web_page_preview=None, reply_markup=None):
    method_url = r'editMessageText'
    payload = {'text': text}
    if chat_id:
        payload['chat_id'] = chat_id
    if message_id:
        payload['message_id'] = message_id
    if inline_message_id:
        payload['inline_message_id'] = inline_message_id
    if parse_mode:
        payload['parse_mode'] = parse_mode
    if entities:
        payload['entities'] = entities
    if disable_web_page_preview:
        payload['disable_web_page_preview'] = disable_web_page_preview
    if reply_markup:
        payload['reply_markup'] = _convert_markup(reply_markup)
    return _make_request(token, method_url, params=payload)


def edit_message_caption(token, caption, chat_id=None, message_id=None, inline_message_id=None,
                         parse_mode=None, caption_entities=None, reply_markup=None):
    method_url = r'editMessageCaption'
    payload = {'caption': caption}
    if chat_id:
        payload['chat_id'] = chat_id
    if message_id:
        payload['message_id'] = message_id
    if parse_mode:
        payload['parse_mode'] = parse_mode
    if caption_entities:
        payload['caption_entities'] = caption_entities
    if inline_message_id:
        payload['inline_message_id'] = inline_message_id
    if reply_markup:
        payload['reply_markup'] = _convert_markup(reply_markup)
    return _make_request(token, method_url, params=payload)

def edit_message_media(token, media, chat_id=None, message_id=None, reply_markup=None):
    method_url = r'editMessageMedia'
    payload = {'media': media}
    if chat_id:
        payload['chat_id'] = chat_id
    if message_id:
        payload['message_id'] = message_id
    if reply_markup:
        payload['reply_markup'] = _convert_markup(reply_markup)
    return _make_request(token, method_url, params=payload)

def edit_message_replay_markup(token, chat_id=None, message_id=None, inline_message_id=None, reply_markup=None):
    """
    Use this method to edit only the reply markup of messages. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned.

    Parameter	Type	Required	Description
    chat_id	Integer or String	Optional	Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    message_id	Integer	Optional	Required if inline_message_id is not specified. Identifier of the message to edit
    inline_message_id	String	Optional	Required if chat_id and message_id are not specified. Identifier of the inline message
    reply_markup	InlineKeyboardMarkup	Optional	A JSON-serialized object for an inline keyboard.
    
    """
    method_url = r'editMessageReplyMarkup'
    payload = {}
    if chat_id:
        payload['chat_id'] = chat_id
    if message_id:
        payload['message_id'] = message_id
    if inline_message_id:
        payload['inline_message_id'] = inline_message_id
    if reply_markup:
        payload['reply_markup'] = _convert_markup(reply_markup)
    return _make_request(token, method_url, params=payload)


def stop_poll(token, message_id, chat_id, reply_markup=None):
    """
    Use this method to stop a poll which was sent by the bot. On success, the stopped Poll is returned.

    Parameter	Type	Required	Description
    chat_id	Integer or String	Yes	Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    message_id	Integer	Yes	Identifier of the original message with the poll
    reply_markup	InlineKeyboardMarkup	Optional	A JSON-serialized object for a new message inline keyboard.
    """
    method_url = r'stopPoll'
    payload = {'chat_id': chat_id, 'message_id': message_id}
    if reply_markup:
        payload['reply_markup'] = _convert_markup(reply_markup)
    return _make_request(token, method_url, params=payload)

def delete_message(token, chat_id, message_id):
    """
    Use this method to delete a message, including service messages, with the following limitations:
    - A message can only be deleted if it was sent less than 48 hours ago.
    - Service messages about a supergroup, channel, or forum topic creation can't be deleted.
    - A dice message in a private chat can only be deleted if it was sent more than 24 hours ago.
    - Bots can delete outgoing messages in private chats, groups, and supergroups.
    - Bots can delete incoming messages in private chats.
    - Bots granted can_post_messages permissions can delete outgoing messages in channels.
    - If the bot is an administrator of a group, it can delete any message there.
    - If the bot has can_delete_messages permission in a supergroup or a channel, it can delete any message there.
    Returns True on success.

    Parameter	Type	Required	Description
    chat_id	Integer or String	Yes	Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    message_id	Integer	Yes	Identifier of the message to delete
    """
    method_url = r'deleteMessage'
    payload = {'chat_id': chat_id, 'message_id': message_id}
    return _make_request(token, method_url, params=payload)


# Stickers

def send_sticker(token, chat_id, sticker, disable_notification=None, protect_content=None,
                 reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, message_thread_id=None):
    
    """
    Use this method to send static .WEBP, animated .TGS, or video .WEBM stickers. On success, the sent Message is returned.

    Parameter	Type	Required	Description
    chat_id	Integer or String	Yes	Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    message_thread_id	Integer	Optional	Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
    sticker	InputFile or String	Yes	Sticker to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a .WEBP file from the Internet, or upload a new one using multipart/form-data. More information on Sending Files »
    disable_notification	Boolean	Optional	Sends the message silently. Users will receive a notification with no sound.
    protect_content	Boolean	Optional	Protects the contents of the sent message from forwarding and saving
    reply_to_message_id	Integer	Optional	If the message is a reply, ID of the original message
    allow_sending_without_reply	Boolean	Optional	Pass True if the message should be sent even if the specified replied-to message is not found
    reply_markup	InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply	Optional	Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.

    """
    method_url = r'sendSticker'
    payload = {'chat_id': chat_id,
               'sticker': sticker}
    if disable_notification:
        payload['disable_notification'] = disable_notification
    if protect_content:
        payload['protect_content'] = protect_content
    if reply_markup:
        payload['reply_markup'] = _convert_markup(reply_markup)
    if message_thread_id:
        payload['message_thread_id'] = message_thread_id
    if reply_to_message_id:
        payload['reply_to_message_id'] = reply_to_message_id
    if allow_sending_without_reply:
        payload['allow_sending_without_reply'] = allow_sending_without_reply
    return _make_request(token, method_url, params=payload)

def get_sticker_set(token, name):
    """
    Use this method to get a sticker set. On success, a StickerSet object is returned.

    Parameter	Type	Required	Description
    name	String	Yes	Name of the sticker set

    """
    method_url = 'getStickerSet'
    payload = {'name': name}
    return _make_request(token, method_url, params=payload)

def get_custom_emoji_stickers(token, custom_emoji_ids):
    """
    Use this method to get information about custom emoji stickers by their identifiers. Returns an Array of Sticker objects.

    Parameter	Type	Required	Description
    custom_emoji_ids	Array of String	Yes	List of custom emoji identifiers. At most 200 custom emoji identifiers can be specified.

    """
    method_url = 'getCustomEmojiStickers'
    payload = {'custom_emoji_ids': custom_emoji_ids}
    return _make_request(token, method_url, params=payload)


def upload_sticker_file(token, user_id, png_sticker):
    """
    Use this method to upload a .PNG file with a sticker for later use in createNewStickerSet and addStickerToSet methods (can be used multiple times). Returns the uploaded File on success.

    Parameter	Type	Required	Description
    user_id	Integer	Yes	User identifier of sticker file owner
    png_sticker	InputFile	Yes	PNG image with the sticker, must be up to 512 kilobytes in size, dimensions must not exceed 512px, and either width or height must be exactly 512px. More information on Sending Files »
    """
    method_url = r'uploadStickerFile'
    payload = {'user_id': user_id, 'png_sticker': png_sticker}
    return _make_request(token, method_url, params=payload)


def create_new_sticker_set(token, user_id, name, title, emojis, png_sticker=None, tgs_sticker=None, webm_sticker=None, sticker_type=None, mask_position=None):
    """
    Use this method to create a new sticker set owned by a user. The bot will be able to edit the sticker set thus created. You must use exactly one of the fields png_sticker, tgs_sticker, or webm_sticker. Returns True on success.

    Parameter	Type	Required	Description
    user_id	Integer	Yes	User identifier of created sticker set owner
    name	String	Yes	Short name of sticker set, to be used in t.me/addstickers/ URLs (e.g., animals). Can contain only English letters, digits and underscores. Must begin with a letter, can't contain consecutive underscores and must end in "_by_<bot_username>". <bot_username> is case insensitive. 1-64 characters.
    title	String	Yes	Sticker set title, 1-64 characters
    png_sticker	InputFile or String	Optional	PNG image with the sticker, must be up to 512 kilobytes in size, dimensions must not exceed 512px, and either width or height must be exactly 512px. Pass a file_id as a String to send a file that already exists on the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. More information on Sending Files »
    tgs_sticker	InputFile	Optional	TGS animation with the sticker, uploaded using multipart/form-data. See https://core.telegram.org/stickers#animated-sticker-requirements for technical requirements
    webm_sticker	InputFile	Optional	WEBM video with the sticker, uploaded using multipart/form-data. See https://core.telegram.org/stickers#video-sticker-requirements for technical requirements
    sticker_type	String	Optional	Type of stickers in the set, pass “regular” or “mask”. Custom emoji sticker sets can't be created via the Bot API at the moment. By default, a regular sticker set is created.
    emojis	String	Yes	One or more emoji corresponding to the sticker
    mask_position	MaskPosition	Optional	A JSON-serialized object for position where the mask should be placed on faces
    """
    
    method_url = r'createNewStickerSet'
    payload = {'user_id': user_id, 'name': name, 'title': title, 'emojis': emojis}
    if tgs_sticker:
        payload['tgs_sticker'] = tgs_sticker
    if png_sticker:
        payload['png_sticker'] = png_sticker
    if webm_sticker:
        payload['webm_sticker'] = webm_sticker
    if sticker_type:
        payload['sticker_type'] = sticker_type
    if mask_position:
        payload['mask_position'] = mask_position
    return _make_request(token, method_url, params=payload)


def add_sticker_to_set(token, user_id, name, emojis, png_sticker=None, tgs_sticker=None, webm_sticker=None, mask_position=None):
    """
    Use this method to add a new sticker to a set created by the bot. You must use exactly one of the fields png_sticker, tgs_sticker, or webm_sticker. Animated stickers can be added to animated sticker sets and only to them. Animated sticker sets can have up to 50 stickers. Static sticker sets can have up to 120 stickers. Returns True on success.

    Parameter	Type	Required	Description
    user_id	Integer	Yes	User identifier of sticker set owner
    name	String	Yes	Sticker set name
    png_sticker	InputFile or String	Optional	PNG image with the sticker, must be up to 512 kilobytes in size, dimensions must not exceed 512px, and either width or height must be exactly 512px. Pass a file_id as a String to send a file that already exists on the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. More information on Sending Files »
    tgs_sticker	InputFile	Optional	TGS animation with the sticker, uploaded using multipart/form-data. See https://core.telegram.org/stickers#animated-sticker-requirements for technical requirements
    webm_sticker	InputFile	Optional	WEBM video with the sticker, uploaded using multipart/form-data. See https://core.telegram.org/stickers#video-sticker-requirements for technical requirements
    emojis	String	Yes	One or more emoji corresponding to the sticker
    mask_position	MaskPosition	Optional	A JSON-serialized object for position where the mask should be placed on faces
    """
    method_url = r'addStickerToSet'
    payload = {'user_id': user_id, 'name': name, 'emojis': emojis}
    if tgs_sticker:
        payload['tgs_sticker'] = tgs_sticker
    if png_sticker:
        payload['png_sticker'] = png_sticker
    if webm_sticker:
        payload['webm_sticker'] = webm_sticker
    if mask_position:
        payload['mask_position'] = mask_position
    return _make_request(token, method_url, params=payload)


def set_sticker_position_in_set(token, sticker, position):
    """
    Use this method to move a sticker in a set created by the bot to a specific position. Returns True on success.

    Parameter	Type	Required	Description
    sticker	String	Yes	File identifier of the sticker
    position	Integer	Yes	New sticker position in the set, zero-based

    """
    method_url = 'setStickerPositionInSet'
    payload = {'sticker': sticker, 'position': position}
    return _make_request(token, method_url, params=payload, method="post")


def delete_sticker_from_set(token, sticker):
    """
    Use this method to delete a sticker from a set created by the bot. Returns True on success.

    Parameter	Type	Required	Description
    sticker	String	Yes	File identifier of the sticker
    
    """
    method_url = 'deleteStickerFromSet'
    payload = {'sticker': sticker}
    return _make_request(token, method_url, params=payload, method="post")


def set_sticker_set_thumb(token, name, user_id, thumb=None):
    """
    Use this method to set the thumbnail of a sticker set. Animated thumbnails can be set for animated sticker sets only. Video thumbnails can be set only for video sticker sets only. Returns True on success.

    Parameter	Type	Required	Description
    name	String	Yes	Sticker set name
    user_id	Integer	Yes	User identifier of the sticker set owner
    thumb	InputFile or String	Optional	A PNG image with the thumbnail, must be up to 128 kilobytes in size and have width and height exactly 100px, or a TGS animation with the thumbnail up to 32 kilobytes in size; see https://core.telegram.org/stickers#animated-sticker-requirements for animated sticker technical requirements, or a WEBM video with the thumbnail up to 32 kilobytes in size; see https://core.telegram.org/stickers#video-sticker-requirements for video sticker technical requirements. Pass a file_id as a String to send a file that already exists on the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. More information on Sending Files ». Animated sticker set thumbnails can't be uploaded via HTTP URL.

    """
    method_url = 'setStickerSetThumb'
    payload = {'name': name, 'user_id': user_id}
    files = None
    if thumb:
        if not sent.util.is_string(thumb):
            files = {'thumb': thumb}
        else:
            payload['thumb'] = thumb
    return _make_request(token, method_url, params=payload, files=files, method="post")



# Inline mode

"""
The following methods and objects allow your bot to work in inline mode.
Please see our Introduction to Inline bots for more details.

To enable this option, send the /setinline command to @BotFather and provide the placeholder text that the user will see in the input field after typing your bot's name.

InlineQuery
This object represents an incoming inline query. When the user sends an empty query, your bot could return some default or trending results.

Field	Type	Description
id	String	Unique identifier for this query
from	User	Sender
query	String	Text of the query (up to 256 characters)
offset	String	Offset of the results to be returned, can be controlled by the bot
chat_type	String	Optional. Type of the chat from which the inline query was sent. Can be either “sender” for a private chat with the inline query sender, “private”, “group”, “supergroup”, or “channel”. The chat type should be always known for requests sent from official clients and most third-party clients, unless the request was sent from a secret chat
location	Location	Optional. Sender location, only for bots that request user location

"""

def answer_inline_query(token, inline_query_id, results, cache_time=None, is_personal=None, next_offset=None,
                        switch_pm_text=None, switch_pm_parameter=None):
    method_url = 'answerInlineQuery'
    payload = {'inline_query_id': inline_query_id,
               'results': _convert_inline_results(results)}
    if cache_time:
        payload['cache_time'] = cache_time
    if is_personal:
        payload['is_personal'] = is_personal
    if next_offset is not None:
        payload['next_offset'] = next_offset
    if switch_pm_text:
        payload['switch_pm_text'] = switch_pm_text
    if switch_pm_parameter:
        payload['switch_pm_parameter'] = switch_pm_parameter
    return _make_request(token, method_url, params=payload, method='post')

# Payments

"""
Your bot can accept payments from Telegram users. 
Please see the introduction to payments for more details on the process and how to set up payments for your bot. 
Please note that users will need Telegram v.4.0 or higher to use payments (released on May 18, 2017).

"""
def send_invoice(token, chat_id, title, description, payload, provider_token, currency, prices,
                 max_tip_amount=None, suggested_tip_amounts=None, start_parameter=None, provider_data=None,
                 photo_url=None, photo_size=None, photo_width=None, photo_height=None, 
                 need_name=None, need_phone_number=None, need_email=None, need_shipping_address=None, 
                 send_phone_number_to_provider=None, send_email_to_provider=None,
                 is_flexible=None, 
                 disable_notification=None, protect_content=None, reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, message_thread_id=None):
    method_url = 'sendInvoice'
    payload = {'chat_id': chat_id, 'title': title, 'description': description,'payload': payload, 'provider_token': provider_token,'currency': currency, 'prices': prices,}
    if max_tip_amount:
        payload['max_tip_amount'] = max_tip_amount
    if suggested_tip_amounts:
        payload['suggested_tip_amounts'] = suggested_tip_amounts
    if start_parameter:
        payload['start_parameter'] = start_parameter
    if provider_data:
        payload['provider_data'] = provider_data
    if photo_url:
        payload['photo_url'] = photo_url
    if photo_size:
        payload['photo_size'] = photo_size
    if photo_width:
        payload['photo_width'] = photo_width
    if photo_height:
        payload['photo_height'] = photo_height
    if need_name:
        payload['need_name'] = need_name
    if need_phone_number:
        payload['need_phone_number'] = need_phone_number
    if need_email:
        payload['need_email'] = need_email
    if need_shipping_address:
        payload['need_shipping_address'] = need_shipping_address
    if send_phone_number_to_provider:
        payload['send_phone_number_to_provider'] = send_phone_number_to_provider
    if send_email_to_provider:
        payload['send_email_to_provider'] = send_email_to_provider
    if is_flexible:
        payload['is_flexible'] = is_flexible
    if disable_notification:
        payload['disable_notification'] = disable_notification
    if protect_content:
        payload['protect_content'] = protect_content
    if reply_to_message_id:
        payload['reply_to_message_id'] = reply_to_message_id
    if allow_sending_without_reply:
        payload['allow_sending_without_reply'] = allow_sending_without_reply
    if reply_markup:
        payload['reply_markup'] = _convert_markup(reply_markup)
    if message_thread_id:
        payload['message_thread_id'] = message_thread_id
    return _make_request(token, method_url, params=payload)


def create_invoice_link(token, title, description, payload, provider_token, currency, prices,
                 max_tip_amount=None, suggested_tip_amounts=None, provider_data=None,
                 photo_url=None, photo_size=None, photo_width=None, photo_height=None, 
                 need_name=None, need_phone_number=None, need_email=None, need_shipping_address=None, 
                 send_phone_number_to_provider=None, send_email_to_provider=None,
                 is_flexible=None):
    method_url = 'createInvoiceLink'
    payload = {'title': title, 'description': description,'payload': payload, 'provider_token': provider_token,'currency': currency, 'prices': prices,}
    if max_tip_amount:
        payload['max_tip_amount'] = max_tip_amount
    if suggested_tip_amounts:
        payload['suggested_tip_amounts'] = suggested_tip_amounts
    if provider_data:
        payload['provider_data'] = provider_data
    if photo_url:
        payload['photo_url'] = photo_url
    if photo_size:
        payload['photo_size'] = photo_size
    if photo_width:
        payload['photo_width'] = photo_width
    if photo_height:
        payload['photo_height'] = photo_height
    if need_name:
        payload['need_name'] = need_name
    if need_phone_number:
        payload['need_phone_number'] = need_phone_number
    if need_email:
        payload['need_email'] = need_email
    if need_shipping_address:
        payload['need_shipping_address'] = need_shipping_address
    if send_phone_number_to_provider:
        payload['send_phone_number_to_provider'] = send_phone_number_to_provider
    if send_email_to_provider:
        payload['send_email_to_provider'] = send_email_to_provider
    if is_flexible:
        payload['is_flexible'] = is_flexible
    return _make_request(token, method_url, params=payload)


def answer_shipping_query(token, shipping_query_id, ok,  shipping_options=None, error_message=None):
    method_url = 'answerShippingQuery'
    payload = {'shipping_query_id': shipping_query_id, 'ok': ok}
    if shipping_options:
        payload['shipping_options'] = shipping_options
    if error_message:
        payload['error_message'] = error_message
    return _make_request(token, method_url, params=payload, method='post')


def answer_pre_checkout_query(token, pre_checkout_query_id, ok, error_message=None):
    method_url = 'answerPreCheckoutQuery'
    payload = {'pre_checkout_query_id': pre_checkout_query_id, 'ok': ok}
    if error_message:
        payload['error_message'] = error_message
    return _make_request(token, method_url, params=payload, method='post')


# CallbackQuery

"""
This object represents an incoming callback query from a callback button in an inline keyboard. If the button that originated the query was attached to a message sent by the bot, the field message will be present. If the button was attached to a message sent via the bot (in inline mode), the field inline_message_id will be present. Exactly one of the fields data or game_short_name will be present.

Field	Type	Description
id	String	Unique identifier for this query
from	User	Sender
message	Message	Optional. Message with the callback button that originated the query. Note that message content and message date will not be available if the message is too old
inline_message_id	String	Optional. Identifier of the message sent via the bot in inline mode, that originated the query.
chat_instance	String	Global identifier, uniquely corresponding to the chat to which the message with the callback button was sent. Useful for high scores in games.
data	String	Optional. Data associated with the callback button. Be aware that the message originated the query can contain no callback buttons with this data.
game_short_name	String	Optional. Short name of a Game to be returned, serves as the unique identifier for the game
"""

def answer_callback_query(token, callback_query_id, text=None, show_alert=None, url=None, cache_time=None):
    method_url = 'answerCallbackQuery'
    payload = {'callback_query_id': callback_query_id}
    if text:
        payload['text'] = text
    if show_alert:
        payload['show_alert'] = show_alert
    if url:
        payload['url'] = url
    if cache_time:
        payload['cache_time'] = cache_time
    return _make_request(token, method_url, params=payload, method='post')


# Telegram Passport
"""
Telegram Passport is a unified authorization method for services that require personal identification. 
Users can upload their documents once, then instantly share their data with services that require real-world ID 
(finance, ICOs, etc.). Please see the manual for details.
"""

def set_passport_data_errors(token, user_id, errors):
    method_url = 'setPassportDataErrors'
    payload = {'user_id': user_id, 'errors': errors}
    return _make_request(token, method_url, params=payload, method='post')


# Game
"""
This object represents a game. Use BotFather to create and edit games, their short names will act as unique identifiers.

Field	Type	Description
title	String	Title of the game
description	String	Description of the game
photo	Array of PhotoSize	Photo that will be displayed in the game message in chats.
text	String	Optional. Brief description of the game or high scores included in the game message. Can be automatically edited to include current high scores for the game when the bot calls setGameScore, or manually edited using editMessageText. 0-4096 characters.
text_entities	Array of MessageEntity	Optional. Special entities that appear in text, such as usernames, URLs, bot commands, etc.
animation	Animation	Optional. Animation that will be displayed in the game message in chats. Upload via BotFather
"""

def set_game_score(token, user_id, score,  force=None, disable_edit_message=None, chat_id=None, message_id=None, inline_message_id=None):
    method_url = 'setGameScore'
    payload = {'user_id': user_id, 'score': score}
    if force:
        payload['force'] = force
    if disable_edit_message:
        payload['disable_edit_message'] = disable_edit_message
    if chat_id:
        payload['chat_id'] = chat_id
    if message_id:
        payload['message_id'] = message_id
    if inline_message_id:
        payload['inline_message_id'] = inline_message_id
    return _make_request(token, method_url, params=payload)

def get_game_hight_score(token, user_id, chat_id=None, message_id=None, inline_message_id=None):
    method_url = 'getGameHighScores'
    payload = {'user_id': user_id}
    if chat_id:
        payload['chat_id'] = chat_id
    if message_id:
        payload['message_id'] = message_id
    if inline_message_id:
        payload['inline_message_id'] = inline_message_id
    return _make_request(token, method_url, params=payload, method='post')


# supt
   
def _convert_inline_results(results):
    ret = ''
    for r in results:
        if isinstance(r, sent.types.JsonSerializable):
            ret = ret + r.to_json() + ','
    if len(ret) > 0:
        ret = ret[:-1]
    return '[' + ret + ']'


def _convert_markup(markup):
    if isinstance(markup, sent.types.JsonSerializable):
        return markup.to_json()
    return markup


class ApiException(Exception):
    def __init__(self, msg, function_name, result):
        super(ApiException, self).__init__(
            "A request to the Telegram API was unsuccessful. {0}".format(msg))
        self.function_name = function_name
        self.result = result
