from emoji import emojize
from random import randint, choice
from telegram import ReplyKeyboardMarkup, KeyboardButton

import sttings

def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(sttings.USER_EMOJI)
        return emojize(smile, language='alias')
    return user_data['emoji']


def main_keyboard():
    return ReplyKeyboardMarkup([['Прислать котика', KeyboardButton('Прислать мои координаты', request_location=True)]])


def play_random_numbers(user_number):
    bot_number = randint(user_number - 10, user_number + 10)
    if user_number > bot_number:
        message = f"Ты загадал {user_number}, я загадал {bot_number}, ты выиграл!"
    elif user_number == bot_number:
        message = f"Ты загадал {user_number}, я загадал {bot_number}, ничья!"
    else:
        message = f"Ты загадал {user_number}, я загадал {bot_number}, я выиграл!"
    return message
