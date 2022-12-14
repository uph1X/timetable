import telebot
from telebot import types
import random
import xlrd
from datetime import date
from datetime import datetime
import calendar


bot = telebot.TeleBot('5644571180:AAHF_bxgRFh3T9Hfs9i9onNhlz20-jF7bR4')
@bot.message_handler(commands=['start'])

def send_welcome(message):
    stic = open('C:/Users/kfify/Downloads/TelegramBot/applecatrun-apple-cat.webp', 'rb') #здесь нужно указать путь к гифке на своём компьютере

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Вывести расписание на сегодня")
    but2 = types.KeyboardButton("Вывести расписание на завтра")
    markup.add(but1, but2)

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
                rb = xlrd.open_workbook('C:/Users/kfify/Downloads/TelegramBot/1_KURS_OSEN_2022_g.xls', formatting_info=True) #а здесь путь на расписание
                sheet = rb.sheet_by_index(weekday)
                for rownum in range(sheet.nrows):
                    #rand = int(random.randint(0,rownum))
                    row = sheet.row_values(rownum)
                    bot.send_message(message.chat.id, row)
            
        elif message.text == "Вывести расписание на завтра":
            my_date = date.today() 
            weekday = my_date.weekday() + 1
            if(weekday >= 5):
                bot.send_message(message.chat.id, "Ура, завтра выходные!!")
            else:
                rb = xlrd.open_workbook('C:/Users/kfify/Downloads/TelegramBot/1_KURS_OSEN_2022_g.xls', formatting_info=True)
                sheet = rb.sheet_by_index(weekday)
                for rownum in range(sheet.nrows):
                    row = sheet.row_values(rownum)
                    bot.send_message(message.chat.id, row)
        elif message.text.count(".") == 2:
            my_date = datetime.strptime(message.text, '%d.%m.%Y').date()
            weekday = my_date.weekday()
            if(weekday >= 5):
                bot.send_message(message.chat.id, "Этот день - выходной")
            else:
                rb = xlrd.open_workbook('C:/Users/kfify/Downloads/TelegramBot/1_KURS_OSEN_2022_g.xls', formatting_info=True) #а здесь путь на расписание
                sheet = rb.sheet_by_index(weekday)
                for rownum in range(sheet.nrows):
                    #rand = int(random.randint(0,rownum))
                    row = sheet.row_values(rownum)
                    bot.send_message(message.chat.id, row)
        else:
            bot.send_message(message.chat.id, "Я не знаю, что и ответить")



bot.polling(none_stop = True)
