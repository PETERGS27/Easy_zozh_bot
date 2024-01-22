import telebot
import config
from telebot import types
from config import bot
pol = ''
body_config = {}

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

@bot.message_handler(commands=['getbzu'])
def getbzu(message):
    markup = types.InlineKeyboardMarkup()
    menbtn = types.InlineKeyboardButton('Мужской', callback_data='men')
    womenbtn = types.InlineKeyboardButton('Женский', callback_data='women')
    markup.row(menbtn, womenbtn)
    bot.send_message(message.chat.id, f'Итак, пользователь, {message.from_user.first_name} назови свой пол:', reply_markup=markup)
    #bot.register_next_step_handler(message, ka)

@bot.callback_query_handler(func=lambda callback: True)
def callback(callback):
    if callback.data == 'men':
        body_config['pol'] = 'men'
        markup = types.InlineKeyboardMarkup()
        kabtn1 = types.InlineKeyboardButton('1,9 (тяжелый труд)', callback_data='ka1')
        kabtn2 = types.InlineKeyboardButton('1,7 (несколько ежедневных тренировок)', callback_data='ka2')
        kabtn3 = types.InlineKeyboardButton('1,63 (ежедневный тренинг)', callback_data='ka3')
        kabtn4 = types.InlineKeyboardButton('1,55 (тренировки до пяти раз)', callback_data='ka4')
        kabtn5 = types.InlineKeyboardButton('1,46 (активная работа)', callback_data='ka5')
        kabtn6 = types.InlineKeyboardButton('1,4 (систематические занятия в спортзале 1-2 раза в неделю)', callback_data='ka6')
        kabtn7 = types.InlineKeyboardButton('1,2 (активность отсутствует)', callback_data='ka7')
        markup.row(kabtn1)
        markup.row(kabtn2)
        markup.row(kabtn3)
        markup.row(kabtn4)
        markup.row(kabtn5)
        markup.row(kabtn6)
        markup.row(kabtn7)
        bot.send_message(callback.message.chat.id, f'Итак, давай определим твой уровень активности: ', reply_markup=markup)
    elif callback.data == 'women':
        body_config['pol'] = 'women'
        markup = types.InlineKeyboardMarkup()
        kabtn1 = types.InlineKeyboardButton('1,9 (тяжелый труд)', callback_data='ka1')
        kabtn2 = types.InlineKeyboardButton('1,7 (несколько ежедневных тренировок)', callback_data='ka2')
        kabtn3 = types.InlineKeyboardButton('1,63 (ежедневный тренинг)', callback_data='ka3')
        kabtn4 = types.InlineKeyboardButton('1,55 (тренировки до пяти раз)', callback_data='ka4')
        kabtn5 = types.InlineKeyboardButton('1,46 (активная работа)', callback_data='ka5')
        kabtn6 = types.InlineKeyboardButton('1,4 (систематические занятия в спортзале 1-2 раза в неделю)', callback_data='ka6')
        kabtn7 = types.InlineKeyboardButton('1,2 (активность отсутствует)', callback_data='ka7')
        markup.row(kabtn1)
        markup.row(kabtn2)
        markup.row(kabtn3)
        markup.row(kabtn4)
        markup.row(kabtn5)
        markup.row(kabtn6)
        markup.row(kabtn7)
        bot.send_message(callback.message.chat.id, f'Итак, давай определим твой уровень активности: ', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def start_buttons(message):
    if message.text.lower() == 'рассчитать бжу':
        markup = types.InlineKeyboardMarkup()
        menbtn = types.InlineKeyboardButton('Мужской', callback_data='men')
        womenbtn = types.InlineKeyboardButton('Женский', callback_data='women')
        markup.row(menbtn, womenbtn)
        bot.send_message(message.chat.id, f'Итак, пользователь, {message.from_user.first_name} назови свой пол:', reply_markup=markup)
        #bot.register_next_step_handler(message, ka)
    elif message.text.lower() == 'показать все команды':
        bot.send_message(message.chat.id, f'/start - Запуск бота\n\
/help - Показать все команды\n\
/getbzu - Рассчитать БЖУ')

bot.infinity_polling()