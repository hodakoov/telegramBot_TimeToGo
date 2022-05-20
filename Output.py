# Вывод надо сделать следующий: если запрос пришел до 8 часов утра, то вывести информцию на сегодняшний день
# Если после то вывести информацию на завтра !!!!!ПРАВИТЬ!!!!

import DataInDB
import datetime
import time


def result():
    week = ['Понедельник',
            'Вторник',
            'Среда',
            'Четверг',
            'Пятница',
            'Суббота',
            'Воскресенье']

    if '00:00:00' <= time.strftime('%H:%M:%S') <= '07:59:59' and 0 <= datetime.date.today().weekday() <= 4:
        search_day = datetime.date.today()
        name_day = "Сегодня"
    elif '08:00:00' <= time.strftime('%H:%M:%S') <= '23:59:59' and datetime.date.today().weekday() == 4:
        search_day = datetime.date.today() + datetime.timedelta(days=3)
        name_day = "В"
    elif '00:00:00' <= time.strftime('%H:%M:%S') <= '23:59:59' and datetime.date.today().weekday() == 5:
        search_day = datetime.date.today() + datetime.timedelta(days=2)
        name_day = "В"
    elif '00:00:00' <= time.strftime('%H:%M:%S') <= '23:59:59' and datetime.date.today().weekday() == 6:
        search_day = datetime.date.today() + datetime.timedelta(days=1)
        name_day = "В"
    else:
        search_day = datetime.date.today() + datetime.timedelta(days=1)
        name_day = "Завтра"


    search_weekday = DataInDB.search_db('day_of_the_week', search_day)
    search_name = DataInDB.search_db('user_name', search_day)


    return f"{name_day} {week[search_weekday]}  — едем на машине {search_name[:len(search_name)-1] + 'ы'}", search_day





