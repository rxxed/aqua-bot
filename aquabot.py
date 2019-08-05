import requests, urllib
import json
import time, random


BOT_TOKEN = "" # telegram API key
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/"


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


# this function will grab the latest updates
# todo: process messages from the user
# todo: add commands
def get_updates():
    url = BASE_URL + 'getUpdates'
    updates = get_json_from_url(url)
    return updates


def get_message():
    messages_list = ["Drink water", "Did you drink water?",
                 "How about one more glass of water?",
                 "Drink water for 10 nanoseconds of good luck",
                 "Your body desires water", "H2O time motherf*cker"]
    message_to_be_sent = random.choice(messages_list)
    return message_to_be_sent


def get_chat_id():
    chat_id = get_updates()["result"][0]["message"]["chat"]["id"]
    return chat_id


def send_message(message, chat_id):
    message = urllib.parse.quote_plus(message.encode("utf8"))
    url = BASE_URL + f"sendMessage?text={message}&chat_id={chat_id}"
    send_request_to_url(url)


def notify_user(interval):
    # todo: add /stop command to pause sending messages
    i = 0
    while i < 10:
        send_message(get_message(), get_chat_id())
        time.sleep(interval)
        i += 1


# todo: add counter to count total glasses of water drunk on the day /waterCount
# todo: ask the user for interval /setInterval
interval = 3600 # 3600 seconds = 1 hour
notify_user(interval)