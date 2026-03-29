import random
import string
import time
import requests
from datetime import date, datetime
import calendar

from enum import Enum

class s(Enum):
    punctuation = 1
    digits = 2
    ascii_letters = 3
    ascii_lowercase = 4
    ascii_uppercase = 5
    whitespace = 6

#replace your telegram id in list(chatsIds)
def send_message(message, chatIds = [12345,67890]):
    bot_token = 'bot-token'
    for chatId in chatIds:
        send_text = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chatId}&parse_mode=Markdown&text={message}'  
        response = requests.get(send_text)
        result = response.json()
        print(f"{message}\n")
        print(f"{chatId} : {result['ok']}")

def get_string(type, k=2):
    match type:
        case s.punctuation:
            return string.punctuation
        case s.digits:
            return string.digits
        case s.whitespace:
            return string.whitespace
        case s.ascii_letters:
            return string.ascii_letters
        case _:
            return "Type not found"

def token(pub_key, length=64):
    return pub_key + ''.join(list(random.choices(list(get_string(s.punctuation)), k=1))) + ''.join(random.choices(list(get_string(s.ascii_letters)), k=length))


class t(Enum):
    now = 1
    month = 2

def timestamp(type):
    match type:
        case t.now:
            return time.time_ns()
        case t.month:
            month = int(date.today().strftime("%m"))
            year = int(date.today().strftime("%Y"))
            lmd = int(calendar.monthrange(year, month)[1])
            return int(datetime(year, month, lmd, 23, 59, 59).timestamp())

def message(timestamp, expired, token):
    #place your value here
    value = f"your value"
    return value + timestamp + expired + token


message = (message(timestamp(t.now), timestamp(t.month), token("public_key")))
print(message)
# send_message(message)





















# pub key 
# time generate token
# expired token
