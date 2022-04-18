import DataInDB
import datetime
import sqlite3 #только для вывода ошибки

#ночью нового дня вызвать функцию по стандартной замене

# Узнать кто ездил вчера

# print(name, out_of_turn, comfortable, yesterday)


def Default():

    yesterday = datetime.date.today() - datetime.timedelta(days=1)  # узнать вчерашнюю дату
    name = DataInDB.search_db('user_name', yesterday)  # узнал кто вчера ездил
    out_of_turn = DataInDB.search_db('out_of_turn', yesterday)  # узнать что ездили по очереди
    comfortable = DataInDB.search_db('comfortable', yesterday)

    try:
        if name == 'Валера' and out_of_turn == False:
            DataInDB.add_values_db(['Саша', False, True,
                                    datetime.date.today(),
                                    datetime.date.today().weekday()])
        if name == 'Саша' and out_of_turn == False:
            DataInDB.add_values_db(['Валера', False, True,
                                    datetime.date.today(),
                                    datetime.date.today().weekday()])
        print("Сегодня данные внесены")

    except(sqlite3.IntegrityError):
        print("На сегодня данные уже были внесены")


def DefaultTommorow():

    today = datetime.date.today()
    tommorow = datetime.date.today() + datetime.timedelta(days=1)  # узнать вчерашнюю дату
    name = DataInDB.search_db('user_name', today)  # узнал кто вчера ездил
    out_of_turn = DataInDB.search_db('out_of_turn', today)  # узнать что ездили по очереди
    comfortable = DataInDB.search_db('comfortable', today)

    try:
        if name == 'Валера' and out_of_turn == False:
            DataInDB.add_values_db(['Саша', False, True,
                                    tommorow,
                                    tommorow.weekday()])
        if name == 'Саша' and out_of_turn == False:
            DataInDB.add_values_db(['Валера', False, True,
                                    tommorow,
                                    tommorow.weekday()])
        print("Данные на завтра внесены")

    except(sqlite3.IntegrityError):
        print("На завтра данные уже были внесены")

def OutOfTurnComfortable():
    pass


def OutOfTurnNotComfortable():
    pass



