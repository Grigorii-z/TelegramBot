import bs4
import telebot  # pyTelegramBotAPI	4.3.1
import requests
from io import BytesIO
from bs4 import BeautifulSoup
#from selenium import webdriver
from telebot import types
from random import *
import dz
from pygame2 import get_map_cell
#from menuBot import Menu
#driver = webdriver.Chrome()


name=''
age=0
age2=0
count=0
mult = 1
sum = 0
name4=''
age5=0
gameb = ['Камень','Ножницы','Бумага']
cols, rows = 8, 8
bot = telebot.TeleBot('5251849132:AAGbDfq2jbNcphLKj1b7Zk0JEddPu9inKEI')  # Создаем экземпляр бота @Ivanov_Ivan_1MD19_bot

# -----------------------------------------------------------------------
# Функция, обрабатывающая команду /start


@bot.message_handler(commands=["zad"])
def zad(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('1 Задание')
    item2 = types.KeyboardButton('2 Задание')
    item3 = types.KeyboardButton('3 Задание')
    item4 = types.KeyboardButton('4 Задание')
    item5 = types.KeyboardButton('5 Задание')
    item6 = types.KeyboardButton('6 Задание')
    item7 = types.KeyboardButton('7 Задание')
    item8 = types.KeyboardButton('8 Задание')
    item9 = types.KeyboardButton('9 Задание')
    item10 = types.KeyboardButton('10 Задание')
    item11 = types.KeyboardButton('О Авторе')
    item12 = types.KeyboardButton('Анекдот')

    markup.add(item1,item2,item3,item4,item5,item6,item7,item8,item9,item10,item11,item12)

    bot.send_message(message.chat.id, 'Hello Student, {0.first_name}'.format(message.from_user), reply_markup = markup)



@bot.message_handler(commands = ['get_info','info'])
def info(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_yes = types.InlineKeyboardButton(text = 'ДА' , callback_data = 'yes')
    item_no = types.InlineKeyboardButton(text = 'НЕТ', callback_data='no')
    markup_inline.add(item_yes, item_no)
    bot.send_message(message.chat.id, 'Хотите узнать больше о проектах автора и его соц. сетях?',
                     reply_markup = markup_inline
                     )
@bot.message_handler(commands=['search_channel'])
def search_channel(message):
    msg = bot.send_message(message.chat.id, "Введите YouTube канал")
    bot.register_next_step_handler(msg, search_from_channel)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    chat_id = message.chat.id
    if message.chat.type == 'private':
        if message.text == '1 Задание':
            dz.dz1(bot, chat_id)
        elif message.text == '2 Задание':
            dz.dz2(bot, chat_id)
        elif message.text =='3 Задание':
            dz.dz3(bot, chat_id,message)
        elif message.text =='4 Задание':
            dz.dz4(bot, chat_id, message)
        elif message.text =='5 Задание':
            dz.dz5(bot, chat_id, message)
        elif message.text =='6 Задание':
            dz.dz6(bot, chat_id, message)
        elif message.text =='7 Задание':
            dz.dz7(bot, chat_id, message)
        elif message.text =='8 Задание':
            dz.dz8(bot, chat_id, message)
        elif message.text =='9 Задание':
            dz.dz9(bot,chat_id,message)
        elif message.text =='10 Задание':
            dz.dz10(bot, chat_id, message)
        elif message.text == 'О Авторе':
            markup_inline = types.InlineKeyboardMarkup()
            item_yes = types.InlineKeyboardButton(text='ДА', callback_data='yes')
            item_no = types.InlineKeyboardButton(text='НЕТ', callback_data='no')
            markup_inline.add(item_yes, item_no)
            bot.send_message(chat_id, 'Хотите узнать больше о проектах автора и его соц. сетях?',
                             reply_markup=markup_inline
                             )
        elif message.text == 'ЮТУБ':
            bot.send_message(message.chat.id, 'Окей летсгоу')
        elif message.text == 'ТикТок':
            bot.send_message(message.chat.id, 'Окей летсгоу ТИк')
        elif message.text == 'Анекдот':
            #bot.send_message(chat_id, text=get_anekdot())
            bot.send_message(chat_id, text=get_anekdot())

@bot.callback_query_handler(func = lambda call: True)
def answer(call):
    if call.data == 'yes':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item_id = types.KeyboardButton('ЮТУБ')
        item_username = types.KeyboardButton('ТикТок')

        markup_reply.add(item_id, item_username)
        bot.send_message(call.message.chat.id, 'Нажмите на одну из кнопок',
            reply_markup = markup_reply)
    elif call.data == 'no':
        pass

def get_text(message):
    if message.text == 'ЮТУБ':
        bot.send_message(message.chat.id,'Окей летсгоу')
    elif message.text == 'ТикТок':
        bot.send_message(message.chat.id, 'Окей летсгоу ТИк')

def search_from_channel(message):
    bot.send_message(message.chat.id, "Начинаю поиск")
    driver.get(message.text + "/videos")
    videos = driver.find_elements_by_id("video-title")
    for i in range(len(videos)):
        bot.send_message(message.chat.id, videos[i].get_attribute('href'))
        if i == 10:
            break

def get_anekdot():
    array_anekdots = []
    req_anek = requests.get('http://anekdotme.ru/random')
    if req_anek.status_code == 200:
        soup = bs4.BeautifulSoup(req_anek.text, "html.parser")
        result_find = soup.select('.anekdot_text')
        for result in result_find:
            array_anekdots.append(result.getText().strip())
    if len(array_anekdots) > 0:
        return array_anekdots[0]
    else:
        return ""
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
bot.polling(none_stop=True, interval=0) # Запускаем бота

print()