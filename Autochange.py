import datetime
import DataInDB
import schedule
import time
import sqlite3 #только для вывода ошибки



def mainChange(name, out_of_turn, comfortable, day):
    # рассчитывает и занесет данные на следюущую поездку
    try:
        if name == 'Валера' and out_of_turn == False and comfortable == True:
            DataInDB.add_values_db(['Саша', False, True, day, day.weekday()])
        elif name == 'Саша' and out_of_turn == False and comfortable == True:
            DataInDB.add_values_db(['Валера', False, True, day, day.weekday()])

        elif name == 'Валера' and out_of_turn == True and comfortable == True:
            DataInDB.add_values_db(['Саша', False, True, day, day.weekday()])
        elif name == 'Саша' and out_of_turn == True and comfortable == True:
            DataInDB.add_values_db(['Валера', False, True, day, day.weekday()])

        elif name == 'Валера' and out_of_turn == True and comfortable == False:
            DataInDB.add_values_db(['Валера', False, True, day, day.weekday()])
        elif name == 'Саша' and out_of_turn == True and comfortable == False:
            DataInDB.add_values_db(['Саша', False, True, day, day.weekday()])

        print(f"Данные внесены на {day}")

    except(sqlite3.IntegrityError):
        print("ERROR! Данные уже были внесены")



def job():
    if 0 <= datetime.date.today().weekday() <= 3:  #c понедельника по четверг расчет на след день

        today = datetime.date.today()
        tommorow = datetime.date.today() + datetime.timedelta(days=1)  # узнать дату следующего дня
        name = DataInDB.search_db('user_name', today)  # узнал кто ездил
        out_of_turn = DataInDB.search_db('out_of_turn', today)  # узнать что ездили по очереди
        comfortable = DataInDB.search_db('comfortable', today)  # всем ли было удобно

        mainChange(name, out_of_turn, comfortable, tommorow)



    elif datetime.date.today().weekday() == 4: #это пятницу тут надо расчитать на понедельник сразу

        today = datetime.date.today()
        monday = datetime.date.today() + datetime.timedelta(days=3)  # узнать дату следующего понедельника
        name = DataInDB.search_db('user_name', today)  # узнал кто  ездил
        out_of_turn = DataInDB.search_db('out_of_turn', today)  # узнать что ездили по очереди
        comfortable = DataInDB.search_db('comfortable', today)  # всем ли было удобно

        mainChange(name, out_of_turn, comfortable, monday)


    else:
        print('Сегодня отдыхаем') # это выходные тут ничего не надо делать



def scheduleTime():
#     # schedule.every().days.at('17:01').do(job) #Вызов функции каждый день в 17:01
    schedule.every().days.at('08:58:00').do(job)
    # # # нужно иметь свой цикл для запуска планировщика с периодом в 1 секунду:
    while True:
        schedule.run_pending()
        time.sleep(1)