import Output
import DataInDB
import token_bot
import telebot
from telebot import types
import Autochange


bot = telebot.TeleBot(token_bot.token_bot_telegram())
# 855743202 мой юзер айди

@bot.message_handler(commands=['start'])
@bot.message_handler(func=lambda back: back.text == 'Назад в главное меню')
def keyboard_start(message):
    startKBoard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    Who = types.KeyboardButton(text="Кто едет?")
    OutOfTurn = types.KeyboardButton(text="Поехать вне очереди")
    History = types.KeyboardButton(text="История поездок")
    startKBoard.add(Who, OutOfTurn, History)
    bot.send_message(message.chat.id, "Пора ехать на работу!", reply_markup=startKBoard)
    Autochange.scheduleTime()
    Autochange.job()

@bot.message_handler(func=lambda messages: messages.text=='История поездок')
def keyboard_history(message):
#     HistoryKBoard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
#     OneWeek = types.KeyboardButton(text="Одна неделя")
#     TwoWeek = types.KeyboardButton(text="Две недели")
#     Month = types.KeyboardButton(text="Месяц")
#     BackMenu = types.KeyboardButton(text="Назад в главное меню")
#     HistoryKBoard.add(OneWeek, TwoWeek, Month, BackMenu)
    bot.send_message(message.chat.id, "Пока не реализовано")
    # bot.send_message(message.chat.id, "Выбери за какое время выдать историю", reply_markup=HistoryKBoard)

    Autochange.job()

@bot.message_handler(func=lambda messages: messages.text=='Кто едет?')
def whoTuday(message):

    Autochange.job()
    result = Output.result()[0]
    bot.send_message(message.chat.id, result) #-1001720448564 chat id close


@bot.message_handler(func=lambda messages: messages.text=='Поехать вне очереди')
def cmd_start(message):
    start_keyboard = types.InlineKeyboardMarkup(row_width=2)
    easy = types.InlineKeyboardButton(text='Всем удобно', callback_data='Всем удобно')
    notEasy = types.InlineKeyboardButton(text='Не всем удобно', callback_data='Не всем удобно')
    exit = types.InlineKeyboardButton(text='Выйти в главное меню', callback_data='Выйти в главное меню')
    start_keyboard.add(easy, notEasy, exit)
    bot.send_message(message.chat.id, 'Всем удобно?', reply_markup=start_keyboard)

#Если получаем callback ответ с клавиатуры запускаем функцию answer_callback
@bot.callback_query_handler(func=lambda callback: callback.data)
def answer_callback(callback):
    data = Output.result()[1]

    if callback.data == 'Всем удобно':
        comfortable = True
        out_of_turn = True
        start_keyboard = types.InlineKeyboardMarkup()
        easy = types.InlineKeyboardButton(text='На машине Валеры', callback_data='На машине Валеры')
        notEasy = types.InlineKeyboardButton(text='На машине Саши', callback_data='На машине Саши')
        start_keyboard.add(easy, notEasy)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                              text='На чьей машине?', reply_markup=start_keyboard)

        DataInDB.update_db('out_of_turn', out_of_turn, data)
        DataInDB.update_db('comfortable', comfortable, data)


    elif callback.data == 'Не всем удобно':
        comfortable = False
        out_of_turn = True
        start_keyboard = types.InlineKeyboardMarkup()
        easy = types.InlineKeyboardButton(text='На машине Валеры', callback_data='На машине Валеры')
        notEasy = types.InlineKeyboardButton(text='На машине Саши', callback_data='На машине Саши')
        start_keyboard.add(easy, notEasy)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                              text='На чьей машине?', reply_markup=start_keyboard)

        DataInDB.update_db('out_of_turn', out_of_turn, data)
        DataInDB.update_db('comfortable', comfortable, data)

    if callback.data == 'На машине Валеры':
        name = 'Валера'
        start_keyboard = types.InlineKeyboardMarkup()
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                              text='Данные изменены', reply_markup=start_keyboard)

        DataInDB.update_db('user_name', name, data)


    elif callback.data == 'На машине Саши':
        name = 'Саша'
        start_keyboard = types.InlineKeyboardMarkup()
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                              text='Данные изменены', reply_markup=start_keyboard)

        DataInDB.update_db('user_name', name, data)

    if callback.data == 'Выйти в главное меню':
        start_keyboard = types.InlineKeyboardMarkup()
        bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)



bot.infinity_polling()




