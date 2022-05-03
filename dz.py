from random import *
from selenium import webdriver


gameb = ['Камень', 'Ножницы', 'Бумага']


# -----------------------------------------------------------------------
def dz1(bot, chat_id):
    bot.send_message(chat_id, 'Grigorii')


# -----------------------------------------------------------------------
def dz2(bot, chat_id):
    bot.send_message(chat_id, "Grigorii" * 5)


# -----------------------------------------------------------------------
def dz3(bot, chat_id, message):
    bot.send_message(chat_id, 'Your name?')
    bot.register_next_step_handler(message, reg_name, bot)


# -----------------------------------------------------------------------
def dz4(bot, chat_id, message):
    bot.send_message(chat_id, 'Your age?')
    bot.register_next_step_handler(message, reg_age2, bot)


# -----------------------------------------------------------------------
def dz5(bot, chat_id, message):
    bot.send_message(chat_id, 'Your Name?')
    bot.register_next_step_handler(message, reg_name2, bot)


# -----------------------------------------------------------------------
def dz6(bot, chat_id, message):
    bot.send_message(chat_id, 'Your Name?')
    bot.register_next_step_handler(message, reg_name3, bot)


# -----------------------------------------------------------------------
def dz7(bot, chat_id, message):
    bot.send_message(chat_id, 'Your Name?')
    bot.register_next_step_handler(message, reg_name4, bot)


# __________________________________________________
def dz8(bot, chat_id, message):
    bot.send_message(chat_id, 'Your Name?')
    bot.register_next_step_handler(message, reg_name5, bot)


# __________________________________________________
def dz9(bot, chat_id, message):
    bot.send_message(chat_id, '2+2*2?')
    bot.register_next_step_handler(message, reg_ans, bot)


# __________________________________________________
def dz10(bot, chat_id, message):
    bot.send_message(chat_id, 'Камень, ножницы или бумага?')
    bot.register_next_step_handler(message, reg_game, bot)


# __________________________________________________
def dzyt(bot, chat_id, message):
    driver = webdriver.Chrome()
    msg = bot.send_message(chat_id, "Введите YouTube канал")
    bot.register_next_step_handler(message, search_from_channel, bot=bot, driver=driver)


# __________________________________________________
def reg_name(message, bot):
    global name
    global reg_age
    name = message.text
    bot.send_message(message.chat.id, 'Your age?')
    bot.register_next_step_handler(message, reg_age, bot)


# __________________________________________________
def search_from_channel(message, bot, driver):
    bot.send_message(message.chat.id, "Начинаю поиск")
    driver.get(message.text + "/videos")
    videos = driver.find_elements_by_id("video-title")
    for i in range(len(videos)):
        bot.send_message(message.chat.id, videos[i].get_attribute('href'))
        if i == 5:
            break


def reg_age(message, bot):
    global age
    age = message.text
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.chat.id, "Вводите цифры!!!!")
    bot.send_message(message.chat.id, ' Hello ' + name + ' Little Big age ' + ' ' + str(age) + ' ')
    age = 0


# __________________________________________________
def reg_age2(message, bot):
    global age2
    age2 = message.text
    while age2 == 0:
        try:
            age2 = int(message.text)
        except Exception:
            bot.send_message(message.chat.id, "Вводите цифры!!!!")
    if int(age2) > 18:
        bot.send_message(message.chat.id, ' Real Big Human ' + ' ' + str(age2) + ' ')
    else:
        bot.send_message(message.chat.id, ' Small Baby Human ' + ' ' + str(age2) + ' ')
    age2 = 0


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------#
def reg_name2(message, bot):
    global name2
    name2 = message.text
    name2 = name2[7::-1]
    bot.send_message(message.chat.id, "Наоборот вот так" + ' ' + name2)


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------#
def reg_name3(message, bot):
    global name3
    count = 0
    name3 = message.text
    for i in name3:
        count += 1
    bot.send_message(message.chat.id, 'Your age?')
    bot.register_next_step_handler(message, reg_age3, bot, count)


def reg_age3(message, bot, count):
    global age3
    age3 = int(message.text)

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
    age3 = str(age3)
    count = str(count)
    sum = str(sum)
    mult = str(mult)
    bot.send_message(message.chat.id, ' We count letters ' + str(count) + ' Add your age ' + ' ' + str(
        sum) + ' ' + ' Multiply your age ' + str(mult))


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
def reg_name4(message, bot):
    global name4
    name4 = message.text
    if name4.islower() == True:
        bot.send_message(message.chat.id, 'Есть нижний регитср')
    elif name4.isupper() == True:
        bot.send_message(message.chat.id, 'Есть верхний регитср')
    else:
        bot.send_message(message.chat.id, 'Есть верхний регитср и нижний')


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
def reg_name5(message, bot):
    global name5
    name5 = message.text
    for i in name5:
        if i == " ":
            bot.send_message(message.chat.id, 'Введите имя без пробелов')

        elif i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9":
            bot.send_message(message.chat.id, 'Введите имя без цифр')

    bot.send_message(message.chat.id, 'Your age?')
    bot.register_next_step_handler(message, reg_age5, bot)


def reg_age5(message, bot):
    global age5
    age5 = int(message.text)
    while age5 == 0:
        try:
            age5 = int(message.text)
        except Exception:
            bot.send_message(message.chat.id, "Вводите коректные цифры!!!!")
    if age5 < 150 and age5 > 0:
        bot.send_message(message.chat.id,
                         ' Твоё имя без ошибок ' + name5 + ' Нормальный возраст ' + ' ' + str(age5) + ' ')


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
def reg_ans(message, bot):
    global age
    age = int(message.text)
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.chat.id, "Вводите цифры!!!!")
    if age == 6:
        bot.send_message(message.chat.id, "Corecr Answer")
    else:
        bot.send_message(message.chat.id, "Try more:(")
    age = 0


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
def reg_game(message, bot):
    global game
    global gameb
    global value
    value = choice(gameb)
    game = message.text
    if game == 'Камень' or game == 'камень':
        if value == 'Камень' or value == 'камень':
            bot.send_message(message.chat.id, 'Ничья)))')
        if value == 'Ножницы' or value == 'ножницы':
            bot.send_message(message.chat.id, 'Вы победили, я поставил ножницы')
        if value == 'Бумага' or value == 'бумага':
            bot.send_message(message.chat.id, 'Вы проиграли , я поставил бумагу')
    if game == 'Ножницы' or game == 'ножницы':
        if value == 'Камень' or value == 'камень':
            bot.send_message(message.chat.id, 'Вы проиграли , я поставил камень')
        if value == 'Ножницы' or value == 'ножницы':
            bot.send_message(message.chat.id, 'Ничья))')
        if value == 'Бумага' or value == 'бумага':
            bot.send_message(message.chat.id, 'Вы выиграли , я поставил бумагу')
    if game == 'Бумага' or game == 'бумага':
        if value == 'Камень' or value == 'камень':
            bot.send_message(message.chat.id, 'Вы выиграли , я поставил камень')
        if value == 'Ножницы' or value == 'ножницы':
            bot.send_message(message.chat.id, 'Вы проиграли , я поставил ножницы')
        if value == 'Бумага' or value == 'бумага':
            bot.send_message(message.chat.id, 'Ничья)))')
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
