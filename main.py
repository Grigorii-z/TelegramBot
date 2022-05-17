import bs4
import telebot  # pyTelegramBotAPI	4.3.1
import requests
from io import BytesIO
from bs4 import BeautifulSoup
from telebot import types
from random import *
import dz
from menu import Menu ,Users
import pygame
import menu
import pars
import pygame2
from time import sleep as s




bot = telebot.TeleBot('5251849132:AAGbDfq2jbNcphLKj1b7Zk0JEddPu9inKEI')  # Создаем экземпляр бота @Ivanov_Ivan_1MD19_bot

# -----------------------------------------------------------------------
# Функция, обрабатывающая команду /start
@bot.message_handler(commands="start")
def command(message, res=False):
    chat_id = message.chat.id
    bot.send_sticker(chat_id, "CAACAgIAAxkBAAIaeWJEeEmCvnsIzz36cM0oHU96QOn7AAJUAANBtVYMarf4xwiNAfojBA")
    txt_message = f"Привет, {message.from_user.first_name}! Я тестовый бот для курса программирования на языке Python"
    bot.send_message(chat_id, text=txt_message, reply_markup=Menu.getMenu(chat_id, "Главное меню").markup)

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
    item13 = types.KeyboardButton('Карту!')

    markup.add(item1,item2,item3,item4,item5,item6,item7,item8,item9,item10,item11,item12,item13)

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


@bot.message_handler(content_types=['text'])
def bot_message(message):
    chat_id = message.chat.id
    cur_user = Users.getUser(chat_id)
    if cur_user == None:
        cur_user = Users(chat_id, message.json["from"])
    result = goto_menu(chat_id, message.text)

    if result == True:
        return

    cur_menu = Menu.getCurMenu(chat_id)

    if cur_menu != None and message.text in cur_menu.buttons:
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
        elif message.text =='ПОИСК ЮТУБ':
            pars.dzyt(bot,chat_id,message)
        elif message.text =='10 Задание':
            dz.dz10(bot, chat_id, message)
        elif message.text =='XO':
            ma(message)
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
        elif message.text == "Карту!":
            game21 = pygame.getGame(chat_id)
            if game21 == None:  # если мы случайно попали в это меню, а объекта с игрой нет
                goto_menu(chat_id, "Выход")
                return

            text_game = game21.get_cards(1)
            bot.send_media_group(chat_id, media=getMediaCards(game21))  # получим и отправим изображения карт
            bot.send_message(chat_id, text=text_game)

            if game21.status != None:  # выход, если игра закончена
                pygame.stopGame(chat_id)
                goto_menu(chat_id, "Выход")
                return

        elif message.text == "Стоп!":
            pygame.stopGame(chat_id)
            goto_menu(chat_id, "Выход")
            return


@bot.callback_query_handler(func = lambda call: True)
# def answer(call):
#     if call.data == 'yes':
#         markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
#         item_id = types.KeyboardButton('ЮТУБ')
#         item_username = types.KeyboardButton('ТикТок')
#
#         markup_reply.add(item_id, item_username)
#         bot.send_message(call.message.chat.id, 'Нажмите на одну из кнопок',
#             reply_markup = markup_reply)
#     elif call.data == 'no':
#         pass
def query_handler(call):
    global board, players
    if call.data == '1':
        call_data(0, 0, call=call)
    elif call.data == '2':
        call_data(0, 1, call=call)
    elif call.data == '3':
        call_data(0, 2, call=call)
    elif call.data == '4':
        call_data(1, 0, call=call)
    elif call.data == '5':
        call_data(1, 1, call=call)
    elif call.data == '6':
        call_data(1, 2, call=call)
    elif call.data == '7':
        call_data(2, 0, call=call)
    elif call.data == '8':
        call_data(2, 1, call=call)
    elif call.data == '9':
        call_data(2, 2, call=call)
    else:
        bot.answer_callback_query(call.message.chat.id, 'Игра завершена!')

def get_text(message):
    if message.text == 'ЮТУБ':
        bot.send_message(message.chat.id,'Окей летсгоу')
    elif message.text == 'ТикТок':
        bot.send_message(message.chat.id, 'Окей летсгоу ТИк')



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
def goto_menu(chat_id, name_menu):
    # получение нужного элемента меню
    cur_menu = menu.Menu.getCurMenu(chat_id)
    if name_menu == "Выход" and cur_menu != None and cur_menu.parent != None:
        target_menu = menu.Menu.getMenu(chat_id, cur_menu.parent.name)
    else:
        target_menu = menu.Menu.getMenu(chat_id, name_menu)

    if target_menu != None:
        bot.send_message(chat_id, text=target_menu.name, reply_markup=target_menu.markup)

        # Проверим, нет ли обработчика для самого меню. Если есть - выполним нужные команды
        if target_menu.name == "Игра в 21":
            game21 = pygame.newGame(chat_id, pygame.Game21(jokers_enabled=True))  # создаём новый экземпляр игры
            text_game = game21.get_cards(2)  # просим 2 карты в начале игры
            bot.send_media_group(chat_id, media=getMediaCards(game21))  # получим и отправим изображения карт
            bot.send_message(chat_id, text=text_game)

        elif target_menu.name == "Камень, ножницы, бумага":
            gameRSP = pygame.newGame(chat_id, pygame.GameRPS())  # создаём новый экземпляр игры
            text_game = "<b>Победитель определяется по следующим правилам:</b>\n" \
                        "1. Камень побеждает ножницы\n" \
                        "2. Бумага побеждает камень\n" \
                        "3. Ножницы побеждают бумагу"
            bot.send_photo(chat_id, photo="https://i.ytimg.com/vi/Gvks8_WLiw0/maxresdefault.jpg", caption=text_game, parse_mode='HTML')

        return True
    else:
        return False
# -----------------------------------------------------------------------
def getMediaCards(game21):
    medias = []
    for url in game21.arr_cards_URL:
        medias.append(types.InputMediaPhoto(url))
    return medias
# -----------------------------------------------------------------------
def ma(message):
    global user1, user2, players, stop
    user1, user2 = None, None
    make_bot_true()
    stop = False
    bot.send_message(message.from_user.id,
                     'Это крестики-нолики!')
    loading = bot.send_message(message.from_user.id, 'Ищу пользователей...')
    players.append(message.from_user)
    s(3)
    while True:
        if len(players) <= 1:
            bot.edit_message_text(chat_id=message.from_user.id, message_id=loading.id, text='█▒▒▒▒▒▒▒▒▒')
            s(0.5)
            bot.edit_message_text(chat_id=message.from_user.id, message_id=loading.id, text='███▒▒▒▒▒▒▒')
            s(0.5)
            bot.edit_message_text(chat_id=message.from_user.id, message_id=loading.id, text='█████▒▒▒▒▒')
            s(0.5)
            bot.edit_message_text(chat_id=message.from_user.id, message_id=loading.id, text='███████▒▒▒')
            s(0.5)
            bot.edit_message_text(chat_id=message.from_user.id, message_id=loading.id, text='██████████')
            s(0.5)
        else:
            bot.send_message(message.from_user.id, 'Пользователь найден!')
            user1 = players[0]
            user2 = players[1]
            chat(message)
            break


players = []
bot_send = True


def call_data(index1, index2, call):
    global board, players
    if hod % 2 == 0 and call.message.chat.id == user2.id:
        if board[index1][index2] == '◻':
            board[index1][index2] = 'x'
            plus_hod()
            bot.edit_message_reply_markup(user2.id, message_id=us2_mes.id, reply_markup=make_board())
            bot.edit_message_reply_markup(user1.id, message_id=us1_mes.id, reply_markup=make_board())
            if check_win(board)[0] == True or check_win(board)[0] == None:
                if check_win(board)[0] == None:
                    draw = True
                else:
                    draw = False
                bot.edit_message_reply_markup(user1.id, message_id=us1_mes.id,
                                              reply_markup=make_board(end=True, draw=draw, symbol=check_win(board)))
                bot.edit_message_reply_markup(user2.id, message_id=us2_mes.id,
                                              reply_markup=make_board(end=True, draw=draw, symbol=check_win(board)))
                players.clear()
        else:
            bot.answer_callback_query(callback_query_id=call.id, text='Эта клетка уже занята!')
    elif hod % 2 != 0 and call.message.chat.id == user1.id:
        if board[index1][index2] == '◻':
            board[index1][index2] = 'o'
            plus_hod()
            bot.edit_message_reply_markup(user2.id, message_id=us2_mes.id, reply_markup=make_board())
            bot.edit_message_reply_markup(user1.id, message_id=us1_mes.id, reply_markup=make_board())
            if check_win(board)[0] == True or check_win(board)[0] == None:
                if check_win(board)[0] == None:
                    draw = True
                else:
                    draw = False
                bot.edit_message_reply_markup(user1.id, message_id=us1_mes.id,
                                              reply_markup=make_board(end=True, draw=draw, symbol=check_win(board)))
                bot.edit_message_reply_markup(user2.id, message_id=us2_mes.id,
                                              reply_markup=make_board(end=True, draw=draw, symbol=check_win(board)))
                players.clear()
        else:
            bot.answer_callback_query(callback_query_id=call.id, text='Эта клетка уже занята!')
    else:
        bot.answer_callback_query(callback_query_id=call.id, text='Не твой ход! Ожидай соперника!')


def make_bot_true():
    global bot_send
    bot_send = True


def make_bot_false():
    global bot_send
    bot_send = False


def check_win(board):
    for i in range(3):
        if board[i][1] == board[i][0] and board[i][1] == board[i][2] and board[i][1] != '◻':
            return True, board[i][0]
    for i in range(3):
        if board[1][i] == board[0][i] and board[1][i] == board[2][i] and board[1][i] != '◻':
            return True, board[1][i]
    for i in range(2):
        if board[0][0] == board[1][1] and board[1][1] != '◻' and board[1][1] == board[2][2]:
            return True, board[0][0]
        elif board[1][1] != '◻' and board[1][1] == board[0][2] and board[0][2] == board[2][0]:
            return True, board[1][1]
    if board[0][0] != '◻' and board[1][0] != '◻' and board[2][0] != '◻' and board[1][0] != '◻' and board[1][
        1] != '◻' and board[1][2] != '◻' and board[2][0] != '◻' and board[2][1] != '◻' and board[2][2] != '◻':
        return None, None
    return False, False


def make_board(end=False, draw=False, symbol='x'):
    if end:
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        if draw:
            txt = 'Конец! Ничья!'
        else:
            txt = f'Конец! Победил игрок , который играл за "{symbol[1]}"'
        b1 = types.InlineKeyboardButton(text=txt, callback_data=102)
        keyboard.add(b1)
        return keyboard
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    b1 = types.InlineKeyboardButton(text=board[0][0], callback_data=1)
    b2 = types.InlineKeyboardButton(text=board[0][1], callback_data=2)
    b3 = types.InlineKeyboardButton(text=board[0][2], callback_data=3)
    b4 = types.InlineKeyboardButton(text=board[1][0], callback_data=4)
    b5 = types.InlineKeyboardButton(text=board[1][1], callback_data=5)
    b6 = types.InlineKeyboardButton(text=board[1][2], callback_data=6)
    b7 = types.InlineKeyboardButton(text=board[2][0], callback_data=7)
    b8 = types.InlineKeyboardButton(text=board[2][1], callback_data=8)
    b9 = types.InlineKeyboardButton(text=board[2][2], callback_data=9)
    keyboard.add(b1, b2, b3, b4, b5, b6, b7, b8, b9)
    return keyboard


def plus_hod():
    global hod
    hod += 1


def del_users():
    global user1, user2
    user1, user2 = None, None
    players.clear()

def chat(message):
    global b1, b2, b3, b4, b5, b6, b7, b8, b9, hod, user1, user2, board, us1_mes, us2_mes
    board = [['◻'] * 3 for i in range(3)]
    players = [user1, user2]
    hod = 0
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    b1 = types.InlineKeyboardButton(text='◻', callback_data=1)
    b2 = types.InlineKeyboardButton(text='◻', callback_data=2)
    b3 = types.InlineKeyboardButton(text='◻', callback_data=3)
    b4 = types.InlineKeyboardButton(text='◻', callback_data=4)
    b5 = types.InlineKeyboardButton(text='◻', callback_data=5)
    b6 = types.InlineKeyboardButton(text='◻', callback_data=6)
    b7 = types.InlineKeyboardButton(text='◻', callback_data=7)
    b8 = types.InlineKeyboardButton(text='◻', callback_data=8)
    b9 = types.InlineKeyboardButton(text='◻', callback_data=9)
    keyboard.add(b1, b2, b3, b4, b5, b6, b7, b8, b9)
    if bot_send:
        make_bot_false()
        us1_mes = bot.send_message(user1.id, f'Играйте! Ты - Нолик! Ты  играешь против {user2.first_name}', reply_markup=keyboard)
        us2_mes = bot.send_message(user2.id, f'Играйте! Ты - Крестик! Ты играешь против {user1.first_name}', reply_markup=keyboard)
    bot.register_next_step_handler(message,ma)

# -----------------------------------------------------------------------
bot.polling(none_stop=True, interval=0) # Запускаем бота

print()