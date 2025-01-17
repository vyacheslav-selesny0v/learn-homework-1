"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging, ephem

import settings

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from datetime import date

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')




def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def constellation_planet(update, context):
    today = date.today()
    planets = {"Mercury": ephem.Mercury(today), 
            "Venus": ephem.Venus(today), 
            "Mars": ephem.Mars(today), 
            "Jupiter": ephem.Jupiter(today), 
            "Saturn": ephem.Saturn(today), 
            "Uranus": ephem.Uranus(today), 
            "Neptune": ephem.Neptune(today)}


    user_text = str(update.message.text.split()[1]).lower().capitalize()  
 
    if user_text in planets:
        print(ephem.constellation(planets[user_text]))
        day_now = f"Today's date {today.year}/{today.month}/{today.day}"
        print("Today's date:", today)
        print(user_text)
        update.message.reply_text(day_now)
        update.message.reply_text(ephem.constellation(planets[user_text]))


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", constellation_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
