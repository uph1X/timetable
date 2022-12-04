import telebot
from telebot import types
import random
import xlrd
from datetime import date
import calendar



bot = telebot.TeleBot('5644571180:AAHF_bxgRFh3T9Hfs9i9onNhlz20-jF7bR4')
@bot.message_handler(commands=['start'])

def send_welcome(message):
    stic = open('C:/Users/kfify/Downloads/TelegramBot/applecatrun-apple-cat.webp', 'rb') 
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Вывести расписание на сегодня")
    markup.add(but1)

    bot.reply_to(message, "Привет, {0.first_name}\nДавай посмотрим, чем я могу быть полезен".format(message.from_user)
  ,parse_mode='html',reply_markup=markup)
    bot.send_sticker(message.chat.id,stic)
