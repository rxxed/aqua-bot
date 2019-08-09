import time
import inspect

from messages_list import messages_list
from utils import *


# default 1 hour interval time between notifications
# interval_seconds = 3600



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
    notify_user(1) # set default interval of 1 hour

if __name__ == '__main__':
    main()
