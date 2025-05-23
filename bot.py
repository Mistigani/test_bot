import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from hendlers import greet_user, guess_number, send_cat_picture, user_coordinates, talk_to_me
import sttings

logging.basicConfig(filename="bot.log", level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")


def main():
    mybot = Updater(sttings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("guess", guess_number))
    dp.add_handler(CommandHandler("cat", send_cat_picture))
    dp.add_handler(MessageHandler(Filters.regex('^(Прислать котика)$'), send_cat_picture))
    dp.add_handler(MessageHandler(Filters.location, user_coordinates))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
