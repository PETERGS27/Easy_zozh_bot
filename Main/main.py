import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    bzubtn = types.KeyboardButton('Рассчитать БЖУ')
    helpbtn = types.KeyboardButton('Показать все команды')
    markup.row(bzubtn, helpbtn)
    bot.send_message(message.chat.id, f'Здравствуй, {message.from_user.first_name} этот бот создан для облегчения жизни ЗОЖников.\n\
Вот список функций:\n\
/start - Запуск бота\n\
/help - Показать все команды\n\
/getbzu - Рассчитать БЖУ\n\
Для начала работы выберите необходимую функцию.', reply_markup=markup)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, f'/start - Запуск бота\n\
/help - Показать все команды\n\
/getbzu - Рассчитать БЖУ')

bot.infinity_polling()