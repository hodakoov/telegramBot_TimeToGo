import DataInDB
import datetime


def result():

    week = ['Понедельник',
            'Вторник',
            'Среда',
            'Четверг',
            'Пятница',
            'Суббота',
            'Воскресенье']

    search_today = datetime.date.today()
    search_weekday = DataInDB.search_db('day_of_the_week', search_today)
    search_name = DataInDB.search_db('user_name', search_today)

    return f"{week[search_weekday].capitalize()}  — едем на машине {search_name[:len(search_name)-1] + 'ы'}"

def result_tommorow():

    week = ['Понедельник',
            'Вторник',
            'Среда',
            'Четверг',
            'Пятница',
            'Суббота',
            'Воскресенье']

    search_today = datetime.date.today() + datetime.timedelta(days=1)
    search_weekday = DataInDB.search_db('day_of_the_week', search_today)
    search_name = DataInDB.search_db('user_name', search_today)

    return f"{week[search_weekday].capitalize()}  — едем на машине {search_name[:len(search_name)-1] + 'ы'}"
