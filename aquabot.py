import time
import inspect

from messages_list import messages_list
from utils import *


def notify_user(interval):
    # todo: add /stop command to pause sending messages
    send_message(get_message(), get_chat_id(get_updates()))
    time.sleep(interval)


def main():
    # todo: ask user for interval
    interval = 2 # set default interval of 1 hour
    while(True):
        notify_user(interval)

if __name__ == '__main__':
    main()
