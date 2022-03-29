
# -----------------------------------------------------------------------
def dz1(bot, chat_id):
    bot.send_message(chat_id, 'Grigorii')
# -----------------------------------------------------------------------
def dz2(bot, chat_id):
    bot.send_message(chat_id, "Grigorii" * 5)
# -----------------------------------------------------------------------
def dz3(bot, chat_id,message):
    bot.send_message(chat_id, 'Your name?')
    bot.register_next_step_handler(message, reg_name,bot)
# -----------------------------------------------------------------------
def dz4(bot, chat_id,message):
    bot.send_message(chat_id, 'Your age?')
    bot.register_next_step_handler(message, reg_age2,bot)
# -----------------------------------------------------------------------
def dz5(bot, chat_id,message):
    bot.send_message(chat_id, 'Your Name?')
    bot.register_next_step_handler(message, reg_name2,bot)

def dz6(bot, chat_id, message):
    bot.send_message(chat_id, 'Your Name?')
    bot.register_next_step_handler(message, reg_name3,bot)
# -----------------------------------------------------------------------


#__________________________________________________
def reg_name(message,bot):
    global name
    global reg_age
    name = message.text
    bot.send_message(message.chat.id, 'Your age?')
    bot.register_next_step_handler(message, reg_age,bot)

def reg_age(message,bot):
    global age
    age = message.text
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.chat.id,"Вводите цифры!!!!")
    bot.send_message(message.chat.id, ' Hello ' + name + ' Little Big age ' + ' ' + str(age) + ' ')
    age=0
#__________________________________________________
def reg_age2(message,bot):
    global age2
    age2 = message.text
    while age2 == 0:
        try:
            age2 = int(message.text)
        except Exception:
            bot.send_message(message.chat.id,"Вводите цифры!!!!")
    if int(age2)>18:
        bot.send_message(message.chat.id, ' Real Big Human ' + ' ' + str(age2) + ' ')
    else:
        bot.send_message(message.chat.id, ' Small Baby Human ' + ' ' + str(age2) + ' ')
    age2=0


 #-----------------------------------------------------------------------
# -----------------------------------------------------------------------#
def reg_name2(message,bot):
    global name2
    name2 = message.text
    name2=name2[7::-1]
    bot.send_message(message.chat.id, "Наоборот вот так"+' '+name2)
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------#
def reg_name3(message,bot):
    global name3
    count =0
    name3 = message.text
    for i in name3:
        count+=1
    bot.send_message(message.chat.id, 'Your age?')
    bot.register_next_step_handler(message, reg_age3,bot,count)

def reg_age3(message,bot,count):
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
    age3=str(age3)
    count=str(count)
    sum=str(sum)
    mult=str(mult)
    bot.send_message(message.chat.id, ' We count letters ' + str(count) + ' Add your age ' + ' ' + str(sum) + ' ' + ' Multiply your age '+str(mult))
# -----------------------------------------------------------------------
#def my_input(bot, chat_id, txt, ResponseHandler):
  #  message = bot.send_message(chat_id, text=txt)
  #  bot.register_next_step_handler(message, ResponseHandler)
# -----------------------------------------------------------------------
#def my_inputInt(bot, chat_id, txt, ResponseHandler):

 #   message = bot.send_message(chat_id, text=txt)
 #   bot.register_next_step_handler(message, my_inputInt_SecondPart, botQuestion=bot, txtQuestion=txt, ResponseHandler=ResponseHandler)
   # # bot.register_next_step_handler(message, my_inputInt_return, bot, txt, ResponseHandler)  # то-же самое, но короче

#def my_inputInt_SecondPart(message, botQuestion, txtQuestion, ResponseHandler):
 #   chat_id = message.chat.id
 #   try:
 #       var_int = int(message.text)
 #       # данные корректно преобразовались в int, можно вызвать обработчик ответа, и передать туда наше число
 #       ResponseHandler(botQuestion, chat_id, var_int)
  #  except ValueError:
 #       botQuestion.send_message(chat_id,
 #                        text="Можно вводить ТОЛЬКО целое число в десятичной системе исчисления (символами от 0 до 9)!\nПопробуйте еще раз...")
 #       my_inputInt(botQuestion, chat_id, txtQuestion, ResponseHandler)  # это не рекурсия, но очень похоже
 #       # у нас пара процедур, которые вызывают друг-друга, пока пользователь не введёт корректные данные,
 #       # и тогда этот цикл прервётся, и управление перейдёт "наружу", в ResponseHandler

# -----------------------------------------------------------------------
