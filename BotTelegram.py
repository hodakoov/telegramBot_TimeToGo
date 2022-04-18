import ChangeDefault
import DateOutput
import DataInDB
import token_bot
import telebot
from telebot import types

bot = telebot.TeleBot(token_bot.token_bot_telegram())
# 855743202 мой юзер айди

@bot.message_handler(commands=['start'])
@bot.message_handler(func=lambda back: back.text == 'Назад в главное меню')
@bot.message_handler(func=lambda back: back.text == 'Кто едет')
def keyboard_start(message):
    startKBoard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    WhoTuday = types.KeyboardButton(text="Кто сегодня едет?")
    WhoTomorrow = types.KeyboardButton(text="Кто едет завтра?")
    History = types.KeyboardButton(text="История поездок")
    startKBoard.add(WhoTuday, WhoTomorrow, History)
    bot.send_message(message.chat.id, "Пора ехать на работу!", reply_markup=startKBoard)

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

@bot.message_handler(func=lambda messages: messages.text=='Кто сегодня едет?')
def whoTuday(message):
    # выдать кто сегодня едет
    ChangeDefault.Default()
    result = DateOutput.result()
    bot.send_message(message.chat.id, result) #-1001720448564 chat id close


@bot.message_handler(func=lambda messages: messages.text=='Кто едет завтра?')
def whoTomorrow(message):
    # выдать кто завтра едет
    ChangeDefault.DefaultTommorow()
    result = DateOutput.result_tommorow()
    bot.send_message(message.chat.id, result) #-1001720448564 chat id close

# @bot.message_handler(func=lambda messages: messages.text=='Сменить водителя')
# def changeDriver(message):
#     ChangeDriverKBoard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
#     Right = types.KeyboardButton(text="Да, меняем")
#     BackMenu = types.KeyboardButton(text="Назад в главное меню")
#     ChangeDriverKBoard.add(Right, BackMenu)
#     bot.send_message(message.chat.id, "Вы уверены, что меняем водителя?", reply_markup=ChangeDriverKBoard)

# @bot.message_handler(func=lambda messages: messages.text=='Да, меняем')
# def cause(message):
#     CauseKBoard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
#     Cause_1 = types.KeyboardButton(text="Надо отвезти ребенка в больницу")
#     Cause_2 = types.KeyboardButton(text="Надо будет съездить на первую")
#     Cause_3 = types.KeyboardButton(text="Другое") #может в будущем добавить возможно написать после нажатия на другое
#     CauseKBoard.add(Cause_1, Cause_2, Cause_3)
#     bot.send_message(message.chat.id, "Укажите причину", reply_markup=CauseKBoard)


bot.infinity_polling()


