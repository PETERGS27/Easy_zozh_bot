import telebot
from telebot import types
from config import bot
import kbzu

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
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text=f'Итак, давай определим твой уровень активности: ', reply_markup=markup)
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
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text=f'Итак, давай определим твой уровень активности: ', reply_markup=markup)
    elif callback.data == 'ka1':
        body_config['ka'] = 1.9
        vozms = bot.send_message(callback.message.chat.id, f'Введите свой возраст: ')
        bot.register_next_step_handler(vozms, voz)
    elif callback.data == 'ka2':
        body_config['ka'] = 1.7
        vozms = bot.send_message(callback.message.chat.id, f'Введите свой возраст: ')
        bot.register_next_step_handler(vozms, voz)
    elif callback.data == 'ka3':
        body_config['ka'] = 1.63
        vozms = bot.send_message(callback.message.chat.id, f'Введите свой возраст: ')
        bot.register_next_step_handler(vozms, voz)
    elif callback.data == 'ka4':
        body_config['ka'] = 1.55
        vozms = bot.send_message(callback.message.chat.id, f'Введите свой возраст: ')
        bot.register_next_step_handler(vozms, voz)
    elif callback.data == 'ka5':
        body_config['ka'] = 1.46
        vozms = bot.send_message(callback.message.chat.id, f'Введите свой возраст: ')
        bot.register_next_step_handler(vozms, voz)
    elif callback.data == 'ka6':
        body_config['ka'] = 1.4
        vozms = bot.send_message(callback.message.chat.id, f'Введите свой возраст: ')
        bot.register_next_step_handler(vozms, voz)
    elif callback.data == 'ka7':
        body_config['ka'] = 1.2
        vozms = bot.send_message(callback.message.chat.id, f'Введите свой возраст: ')
        bot.register_next_step_handler(vozms, voz)
    elif callback.data == 'cel1':
        body_config['cel'] = 'phd'
        kalmes = bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text=f'Вам необходимо есть: ')
        bot.register_next_step_handler(kalmes, kalms)
    elif callback.data == 'cel2':
        body_config['cel'] = 'nbv'
        kalmes = bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text=f'Вам необходимо есть: ')
        bot.register_next_step_handler(kalmes, kalms)

def voz(message):
    vozpr = message.text
    body_config['voz'] = int(vozpr)
    rostms = bot.send_message(message.chat.id, f'Введите свой рост(см): ')
    bot.register_next_step_handler(rostms, rost)

def rost(message):
    rostpr = message.text
    body_config['rost'] = int(rostpr)
    vesms = bot.send_message(message.chat.id, f'Введите массу вашего тела в нормальных условиях(кг): ')
    bot.register_next_step_handler(vesms, ves)

def ves(message):
    vespr = message.text
    body_config['ves'] = int(vespr)
    markup = types.InlineKeyboardMarkup()
    celbtn1 = types.InlineKeyboardButton('Похудеть', callback_data='cel1')
    celbtn2 = types.InlineKeyboardButton('Набрать вес', callback_data='cel2')
    markup.row(celbtn1, celbtn2)
    bot.send_message(message.chat.id, f'Цель твоя какова, ЗОЖник: ', reply_markup=markup)

def kalms(message):
    kbzu()
    bot.send_message(message.chat.id, body_config['kal'], f'каллорий')

@bot.message_handler(content_types=['text'])
def start_buttons(message):
    if message.text.lower() == 'рассчитать бжу':
        markup = types.InlineKeyboardMarkup()
        menbtn = types.InlineKeyboardButton('Мужской', callback_data='men')
        womenbtn = types.InlineKeyboardButton('Женский', callback_data='women')
        markup.row(menbtn, womenbtn)
        bot.send_message(message.chat.id, f'Итак, пользователь, {message.from_user.first_name} назови свой пол:', reply_markup=markup)
    elif message.text.lower() == 'показать все команды':
        bot.send_message(message.chat.id, f'/start - Запуск бота\n\
/help - Показать все команды\n\
/getbzu - Рассчитать БЖУ')

bot.infinity_polling()