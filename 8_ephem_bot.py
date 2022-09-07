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

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from datetime import date

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}

def constellation_planet(update, context):
    planets = {"Mercury": ephem.Mercury("2019/09/12"), 
    		"Venus": ephem.Venus("2019/09/12"), 
    		"Mars" : ephem.Mars("2019/09/12"), 
    		"Jupiter": ephem.Jupiter("2019/09/12"), 
    		"Saturn": ephem.Saturn("2019/09/12"), 
    		"Uranus": ephem.Uranus("2019/09/12"), 
    		"Neptune": ephem.Neptune("2019/09/12")}
 
    user_text = str(update.message.text.split()[1]).lower().capitalize()  
 
    if user_text in planets:
    	print(ephem.constellation(planets[user_text]))

    day = date.today().split("-")
    print(day)
 
    today = f"{day[0]}/{day[1]}/{day[2]}"
    print("Today's date:", today)
    print(user_text)
    update.message.reply_text("Today's date:", today)
    update.message.reply_text(user_text)

def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater("5646045755:AAFR0NKINklHCJ5xszFQhj4o8gDrCIIoZ6U", request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("planet", constellation_planet))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
