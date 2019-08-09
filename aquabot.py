import requests, urllib
import json
import time, random

# inspect.cleandoc to remove tabs from multiline strings
import inspect

from messages_list import messages_list


# telegram API key
BOT_TOKEN = ""
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/"


# default 1 hour interval time between notifications
interval_seconds = 3600


# this function returns the response from a url
def send_request_to_url(url):
    response = requests.get(url)
    response = response.content.decode("utf8")
    return response


# this function returns the json response from a url as a python dict
def get_json_from_url(url):
    response = send_request_to_url(url)
    response_json_dict = json.loads(response)
    return response_json_dict


# message to be sent to the user
def get_message():
    message_to_be_sent = random.choice(messages_list)
    return message_to_be_sent


# get all the updates from the getUpdates call
def get_updates(offset = None):
    url = BASE_URL + 'getUpdates?timeout=100'
    if offset:
        url += f'&offset={offset}'
    updates = get_json_from_url(url)
    return updates


# todo: process messages from the user
def get_chat_id(updates):
    chat_id = updates["result"][0]["message"]["chat"]["id"]
    return chat_id


# get the text and chat_id from the latest update
def get_latest_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


# get the latest update_id from the getUpdates call
def get_latest_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)


# function to send a message to the respective chat_id
def send_message(message, chat_id):
    message = urllib.parse.quote_plus(message.encode("utf8"))
    url = BASE_URL + f"sendMessage?text={message}&chat_id={chat_id}"
    send_request_to_url(url)


# def handle_user_messages(updates):
#     for update in updates["result"]:
#         try:
#             text = update["message"]["text"]
#             chatid = update["message"]["chat"]["id"]
#             if text == '/setInterval':
#                 is_under_command = True
#                 command_name = 'setInterval'
#                 set_interval()
#             else:
#                 message = """I was unable to comprehend your command.
#                           Try one of these following commands instead: \n
#                           /setInterval : You can use this command to change
#                           the interval between each notification. \n"""
#                 message = inspect.cleandoc(message)
#                 send_message(message, chatid)
#
#         except Exception as e:
#             print(e)
#
#
# def set_interval():
#     chatid = get_chat_id(get_updates())
#     message = "How many seconds of an interval do you want between each notification?"
#     send_message(message, chatid)
#     time.sleep(1)
#     latest_text_and_id = get_latest_chat_id_and_text(get_updates())
#     interval = latest_text_and_id[0]
#     message = f"Interval has been updated to {interval} seconds"
#     send_message(message, chatid)


def notify_user(interval):
    # todo: add /stop command to pause sending messages
    while True:
        send_message(get_message(), get_chat_id(get_updates()))
        time.sleep(interval)


# todo: add counter to count total glasses of water drunk on the day /waterCount
# todo: ask the user for interval /setInterval
# interval = 3 # 3600 seconds = 1 hour
# notify_user(interval)

# def main():
#     last_update_id = None
#     while True:
#         print("Getting updates")
#         updates = get_updates(last_update_id)
#         if len(updates["result"]) > 0:
#             last_update_id = get_latest_update_id(updates) + 1
#             is_under_command = False
#             handle_user_messages(updates)
#

def main():
    notify_user(3600) # set default interval of 1 hour

if __name__ == '__main__':
    main()
