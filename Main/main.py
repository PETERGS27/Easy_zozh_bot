import telebot
import config
bot = telebot.TeleBot(config.TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Здравствуй, {message.from_user.first_name} этот бот создан для облегчения жизни ЗОЖников.\n\
Вот список функций:\n\
/start - Запуск бота\n\
/help - Показать все команды\n\
/getbzu - Рассчитать БЖУ\n\
Для начала работы выберите необходимую функцию.')
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, f'/start - Запуск бота\n\
/help - Показать все команды\n\
/getbzu - Рассчитать БЖУ')

bot.infinity_polling()