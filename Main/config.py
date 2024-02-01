import telebot
import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('api')
bot = telebot.TeleBot(TOKEN)