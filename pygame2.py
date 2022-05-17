from telebot import types
from time import sleep as s

class XO:
    def __init__(self, bot,message):

        self.bot_send = True
        self.objBot = bot
        self.board = None
        self.players = []
        self.hod = 0
        self.user1 = None
        self.user2 = None
        self.stop = False
        self.us1_mes = None
        self.us2_mes = None
        self.b1= None
        self.b2= None
        self.b3= None
        self.b4= None
        self.b5= None
        self.b6= None
        self.b7= None
        self.b8= None
        self.b9= None
        self.ma(message)

    def ma(self,message):
        self.make_bot_true()
        self.stop = False
        self.objBot.send_message(message.from_user.id,
                         'Это крестики-нолики!')
        loading = self.objBot.send_message(message.from_user.id, 'Ищу пользователей...')
        self.players.append(message.from_user.id)
        s(3)
        while True:
            if len(self.players) <= 1:
                self.objBot.edit_message_text(chat_id=message.from_user.id, message_id=loading.id, text='█▒▒▒▒▒▒▒▒▒')
                s(0.5)
                self.objBot.edit_message_text(chat_id=message.from_user.id, message_id=loading.id, text='███▒▒▒▒▒▒▒')
                s(0.5)
                self.objBot.edit_message_text(chat_id=message.from_user.id, message_id=loading.id, text='█████▒▒▒▒▒')
                s(0.5)
                self.objBot.edit_message_text(chat_id=message.from_user.id, message_id=loading.id, text='███████▒▒▒')
                s(0.5)
                self.objBot.edit_message_text(chat_id=message.from_user.id, message_id=loading.id, text='██████████')
                s(0.5)
            else:
                self.objBot.send_message(message.from_user.id, 'Пользователь найден!')
                self.user1 = self.players[0]
                self.user2 = self.players[1]
                self.chat(message)
                break

    def chat(self,message):

        self.board = [['◻'] * 3 for i in range(3)]
        self.players = [self.user1, self.user2]
        self.hod = 0
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        self.b1 = types.InlineKeyboardButton(text='◻', callback_data=1)
        self.b2 = types.InlineKeyboardButton(text='◻', callback_data=2)
        self.b3 = types.InlineKeyboardButton(text='◻', callback_data=3)
        self.b4 = types.InlineKeyboardButton(text='◻', callback_data=4)
        self.b5 = types.InlineKeyboardButton(text='◻', callback_data=5)
        self.b6 = types.InlineKeyboardButton(text='◻', callback_data=6)
        self.b7 = types.InlineKeyboardButton(text='◻', callback_data=7)
        self.b8 = types.InlineKeyboardButton(text='◻', callback_data=8)
        self.b9 = types.InlineKeyboardButton(text='◻', callback_data=9)
        keyboard.add(self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8, self.b9)
        if self.bot_send:
            self.make_bot_false(self)
            self.us1_mes = self.objBot.send_message(self.user1.id, f'Играйте! Ты - Нолик! Ты  играешь против {self.user2.first_name}',
                                       reply_markup=keyboard)
            self.us2_mes = self.objBot.send_message(self.user2.id, f'Играйте! Ты - Крестик! Ты играешь против {self.user1.first_name}',
                                       reply_markup=keyboard)
        self.objBot.register_next_step_handler(message, self.ma)

    def query_handler(self,call):
        global board, players
        if call.data == '1':
            self.call_data(0, 0, call=call)
        elif call.data == '2':
            self.call_data(0, 1, call=call)
        elif call.data == '3':
            self.call_data(0, 2, call=call)
        elif call.data == '4':
            self.call_data(1, 0, call=call)
        elif call.data == '5':
            self.call_data(1, 1, call=call)
        elif call.data == '6':
            self.call_data(1, 2, call=call)
        elif call.data == '7':
            self.call_data(2, 0, call=call)
        elif call.data == '8':
            self.call_data(2, 1, call=call)
        elif call.data == '9':
            self.call_data(2, 2, call=call)
        else:
            self.objBot.answer_callback_query(call.message.chat.id, 'Игра завершена!')

    def call_data(self,index1, index2, call):

        if self.hod % 2 == 0 and call.message.chat.id == self.user2.id:
            if self.board[index1][index2] == '◻':
                self.board[index1][index2] = 'x'
                self.plus_hod()
                self.objBot.edit_message_reply_markup(self.user2.id, message_id=self.us2_mes.id, reply_markup=self.make_board())
                self.objBot.edit_message_reply_markup(self.user1.id, message_id=self.us1_mes.id, reply_markup=self.make_board())
                if self.check_win(self.board)[0] == True or self.check_win(self.board)[0] == None:
                    if self.check_win(self.board)[0] == None:
                        draw = True
                    else:
                        draw = False
                    self.objBot.edit_message_reply_markup(self.user1.id, message_id=self.us1_mes.id,
                                                  reply_markup=self.make_board(end=True, draw=draw, symbol=self.check_win(self.board)))
                    self.objBot.edit_message_reply_markup(self.user2.id, message_id=self.us2_mes.id,
                                                  reply_markup=self.make_board(end=True, draw=draw, symbol=self.check_win(self.board)))
                    self.players.clear()
            else:
                self.objBot.answer_callback_query(callback_query_id=call.id, text='Эта клетка уже занята!')
        elif self.hod % 2 != 0 and call.message.chat.id == self.user1.id:
            if self.board[index1][index2] == '◻':
                self.board[index1][index2] = 'o'
                self.plus_hod()
                self.objBot.edit_message_reply_markup(self.user2.id, message_id=self.us2_mes.id, reply_markup=self.make_board())
                self.objBot.edit_message_reply_markup(self.user1.id, message_id=self.us1_mes.id, reply_markup=self.make_board())
                if self.check_win(self.board)[0] == True or self.check_win(self.board)[0] == None:
                    if self.check_win(self.board)[0] == None:
                        draw = True
                    else:
                        draw = False
                    self.objBot.edit_message_reply_markup(self.user1.id, message_id=self.us1_mes.id,
                                                  reply_markup=self.make_board(end=True, draw=draw, symbol=self.check_win(self.board)))
                    self.objBot.edit_message_reply_markup(self.user2.id, message_id=self.us2_mes.id,
                                                  reply_markup=self.make_board(end=True, draw=draw, symbol=self.check_win(self.board)))
                    self.players.clear()
            else:
                self.objBot.answer_callback_query(callback_query_id=call.id, text='Эта клетка уже занята!')
        else:
            self.objBot.answer_callback_query(callback_query_id=call.id, text='Не твой ход! Ожидай соперника!')

    def make_bot_true(self):
        self.bot_send = True

    def make_bot_false(self):
        self.bot_send = False

    def check_win(self,board):
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

    def make_board(self,end=False, draw=False, symbol='x'):
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
        b1 = types.InlineKeyboardButton(text=self.board[0][0], callback_data=1)
        b2 = types.InlineKeyboardButton(text=self.board[0][1], callback_data=2)
        b3 = types.InlineKeyboardButton(text=self.board[0][2], callback_data=3)
        b4 = types.InlineKeyboardButton(text=self.board[1][0], callback_data=4)
        b5 = types.InlineKeyboardButton(text=self.board[1][1], callback_data=5)
        b6 = types.InlineKeyboardButton(text=self.board[1][2], callback_data=6)
        b7 = types.InlineKeyboardButton(text=self.board[2][0], callback_data=7)
        b8 = types.InlineKeyboardButton(text=self.board[2][1], callback_data=8)
        b9 = types.InlineKeyboardButton(text=self.board[2][2], callback_data=9)
        keyboard.add(b1, b2, b3, b4, b5, b6, b7, b8, b9)
        return keyboard

    def plus_hod(self):
        self.hod += 1

    def del_users(self):
        self.user1, self.user2 = None, None
        self.players.clear()
