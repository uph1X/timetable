import telebot
from telebot import types
import random
import xlrd
from datetime import date
import calendar



bot = telebot.TeleBot('5644571180:AAHF_bxgRFh3T9Hfs9i9onNhlz20-jF7bR4')
@bot.message_handler(commands=['start'])

def send_welcome(message):
    stic = open('C:/Users/kfify/Downloads/TelegramBot/applecatrun-apple-cat.webp', 'rb') #при скачивании GIF-файла здесь нужно указать путь на него на своём устройстве
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Вывести расписание на сегодня")
    markup.add(but1)

    bot.reply_to(message, "Привет, {0.first_name}\nДавай посмотрим, чем я могу быть полезен".format(message.from_user)
  ,parse_mode='html',reply_markup=markup)
    bot.send_sticker(message.chat.id,stic)
import telebot
from telebot import types
import random
import xlrd
from datetime import date
import calendar


bot = telebot.TeleBot('5644571180:AAHF_bxgRFh3T9Hfs9i9onNhlz20-jF7bR4')
@bot.message_handler(commands=['start'])

def send_welcome(message):
    stic = open('C:/Users/kfify/Downloads/TelegramBot/applecatrun-apple-cat.webp', 'rb') #чтение файла в двоичном формате

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Вывести расписание на сегодня")
    markup.add(but1)

    bot.reply_to(message, "Привет, {0.first_name}\nДавай посмотрим, чем я могу быть полезен".format(message.from_user)
  ,parse_mode='html',reply_markup=markup)
    bot.send_sticker(message.chat.id,stic)




@bot.message_handler(func = lambda message: True)
def menu(message):
    if message.chat.type == 'private':
        if message.text == "Вывести расписание на сегодня":

            my_date = date.today()
            weekday = my_date.weekday()
            if(weekday >= 5):
                bot.send_message(message.chat.id, "Ура, выходные!!")
            else:
                rb = xlrd.open_workbook('C:/Users/kfify/Downloads/TelegramBot/1_KURS_OSEN_2022_g.xls', formatting_info=True)
                sheet = rb.sheet_by_index(weekday)
                for rownum in range(sheet.nrows):
                    #rand = int(random.randint(0,rownum))
                    row = sheet.row_values(rownum)
                    bot.send_message(message.chat.id, row)
            
        else:
            bot.send_message(message.chat.id, "Я не знаю, что и ответить")



bot.polling(none_stop = True)
