# Вариант 1 - самый простой чат бот, просто отзывается

import telebot  # pyTelegramBotAPI	4.3.1
from telebot import types
from random import *

name=''
age=0
age2=0
count=0
mult = 1
sum = 0
name4=''
age5=0
gameb = ['Камень','Ножницы','Бумага']
bot = telebot.TeleBot('5251849132:AAGbDfq2jbNcphLKj1b7Zk0JEddPu9inKEI')  # Создаем экземпляр бота @Ivanov_Ivan_1MD19_bot

# -----------------------------------------------------------------------
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message):
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

    markup.add(item1,item2,item3,item4,item5,item6,item7,item8,item9,item10)

    bot.send_message(message.chat.id, 'Hello Student, {0.first_name}'.format(message.from_user), reply_markup = markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == '1 Задание':
            bot.send_message(message.chat.id,'Grigorii')
        elif message.text == '2 Задание':
            #bot.send_message(message.chat.id, 'Grigorii2')
            bot.send_message(message.chat.id, "Grigorii"*5)
        elif message.text =='3 Задание':
            bot.send_message(message.chat.id, 'Your name?')
            bot.register_next_step_handler(message, reg_name)
        elif message.text =='4 Задание':
            bot.send_message(message.chat.id, 'Your age?')
            bot.register_next_step_handler(message, reg_age2)
        elif message.text =='5 Задание':
            bot.send_message(message.chat.id, 'Your Name?')
            bot.register_next_step_handler(message, reg_name2)
        elif message.text =='6 Задание':
            bot.send_message(message.chat.id, 'Your Name?')
            bot.register_next_step_handler(message, reg_name3)
        elif message.text =='7 Задание':
            bot.send_message(message.chat.id, 'Your Name?')
            bot.register_next_step_handler(message, reg_name4)
        elif message.text =='8 Задание':
            bot.send_message(message.chat.id, 'Your Name?')
            bot.register_next_step_handler(message, reg_name5)
        elif message.text =='9 Задание':
            bot.send_message(message.chat.id, '2+2*2?')
            bot.register_next_step_handler(message, reg_ans)
        elif message.text =='10 Задание':
            bot.send_message(message.chat.id, 'Камень, ножницы или бумага?')
            bot.register_next_step_handler(message, reg_game)
        #elif message.text == 'О Авторе':
            #bot.send_message(message.chat.id, 'Хотите узнать больше о проектах автора и его соц. сетях?',
                #eply_markup = markup_inline)



@bot.message_handler(commands = ['get_info','info'])
def get_user_info(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_yes = types.InlineKeyboardButton(text = 'ДА' , callback_data = 'yes')
    item_no = types.InlineKeyboardButton(text='НЕТ', callback_data='no')
    bot.send_message(message.chat.id, 'Хотите узнать больше о проектах автора и его соц. сетях?',
                     reply_markup=markup_inline)
    markup_inline.add(item_yes,item_no)

@bot.callback_query_handler(func = lambda call: True)
def answer(call):
    if call.data == 'yes':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item_id = types.KeyboardButton('ЮТУБ')
        item_username = types.KeyboardButton('ТикТок')

        markup_reply.add(item_id,item_username)
        bot.send_message(call.message.chat.id, 'Нажмите на одну из кнопок',
            reply_markup = markup_reply)
    elif call.data == 'no':
        pass
@bot.message_handler(content_types = ['text'])
def get_text(message):
    if bot_message.text == 'ЮТУБ':
        bot.send_message(message.chat.id,'Окей летсгоу')
    elif bot_message.text == 'ТикТок':
        bot.send_message(message.chat.id, 'Окей летсгоу ТИк')
def reg_name(message):
    global name
    name = message.text
    bot.send_message(message.chat.id, 'Your age?')
    bot.register_next_step_handler(message, reg_age)

def reg_name2(message):
    global name2
    name2 = message.text
    name2=name2[7::-1]
    bot.send_message(message.from_user.id, "Наоборот вот так"+' '+name2)

def reg_name3(message):
    global name3
    global count
    name3 = message.text
    for i in name3:
        count+=1
    bot.send_message(message.chat.id, 'Your age?')
    bot.register_next_step_handler(message, reg_age3)

def reg_age3(message):
    global age3
    age3=int(message.text)

    global mult
    global sum
    sum = 0
    mult = 1
    c = 0

    while age3 > 0:
        c = age3 % 10
        age3 = age3 // 10
        sum += c
        mult = mult * c
    bot.send_message(message.from_user.id, ' We count letters ' + str(count) + ' Add your age ' + ' ' + str(sum) + ' ' + ' Multiply your age '+str(mult))

def reg_name4(message):
    global name4
    name4 = message.text
    if name4.islower() == True:
        bot.send_message(message.from_user.id, 'Есть нижний регитср')
    elif name4.isupper()==True:
        bot.send_message(message.from_user.id, 'Есть верхний регитср')
    else:
        bot.send_message(message.from_user.id, 'Есть верхний регитср и нижний')

def reg_name5(message):
    global name5
    name5 = message.text
    for i in name5:
        if i == " ":
            bot.send_message(message.from_user.id, 'Введите имя без пробелов')

        elif i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9":
            bot.send_message(message.from_user.id, 'Введите имя без цифр')

    bot.send_message(message.chat.id, 'Your age?')
    bot.register_next_step_handler(message, reg_age5)



def reg_age(message):
    global age
    #age = message.text
    while age ==0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id,"Вводите цифры!!!!")
    bot.send_message(message.from_user.id, ' Hello ' + name + ' Little Big age ' + ' ' + str(age) + ' ')
    age=0

def reg_age2(message):
    global age2
    #age = message.text
    while age2 ==0:
        try:
            age2 = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id,"Вводите цифры!!!!")
    if age2>18:
        bot.send_message(message.from_user.id, ' Real Big Human ' + ' ' + str(age2) + ' ')
    else:
        bot.send_message(message.from_user.id, ' Small Baby Human ' + ' ' + str(age2) + ' ')
    age2=0

def reg_age5(message):
    global age5
    #age = message.text
    while age5 == 0:
        try:
            age5 = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id,"Вводите коректные цифры!!!!")
    if age5<150 and age5>0:
        bot.send_message(message.from_user.id, ' Твоё имя без ошибок ' + name5 + ' Нормальный возраст ' + ' ' + str(age5) + ' ')

def reg_ans(message):
    global age
    #age = message.text
    while age ==0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id,"Вводите цифры!!!!")
    if age ==6:
        bot.send_message(message.from_user.id,"Corecr Answer")
    else:
        bot.send_message(message.from_user.id, "Try more:(")
    age=0
def reg_game(message):
    global game
    global gameb
    global value
    value = choice(gameb)
    game = message.text
    if game == 'Камень':
        if value == 'Камень':
            bot.send_message(message.chat.id, 'Ничья)))')
        if value == 'Ножницы':
            bot.send_message(message.chat.id, 'Вы победили, я поставил ножницы')
        if value == 'Бумага':
            bot.send_message(message.chat.id, 'Вы проиграли , я поставил бумагу')
    if game == 'Ножницы':
        if value=='Камень':
            bot.send_message(message.chat.id, 'Вы проиграли , я поставил камень')
        if value == 'Ножницы':
            bot.send_message(message.chat.id, 'Ничья))')
        if value == 'Бумага':
            bot.send_message(message.chat.id, 'Вы выиграли , я поставил бумагу')
    if game == 'Бумага':
        if value == 'Камень':
            bot.send_message(message.chat.id, 'Вы выиграли , я поставил камень')
        if value == 'Ножницы':
            bot.send_message(message.chat.id, 'Вы проиграли , я поставил ножницы')
        if value == 'Бумага':
            bot.send_message(message.chat.id, 'Ничья)))')







# -----------------------------------------------------------------------

# -----------------------------------------------------------------------
bot.polling(none_stop=True, interval=0) # Запускаем бота

print()