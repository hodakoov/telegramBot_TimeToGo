import DataInDB
import datetime

week_day = ['Понедельник',
            'Вторник',
            'Среда',
            'Четверг',
            'Пятница',
            'Суббота',
            'Воскресенье']

def week(day):
    result = []
    for i in range(day, 0, -1):
        # if datetime.date.today().weekday() == 5:
        #     date = datetime.date.today() - datetime.timedelta(days=i) - datetime.timedelta(days=1)
        # elif datetime.date.today().weekday() == 6:
        #     date = datetime.date.today() - datetime.timedelta(days=i) - datetime.timedelta(days=2)
        # else:
        #     date = datetime.date.today() - datetime.timedelta(days=i)
        if (datetime.date.today() - datetime.timedelta(days=i)).weekday() == 5:
            pass
        elif (datetime.date.today() - datetime.timedelta(days=i)).weekday() == 6:
            pass
        else:
            date = datetime.date.today() - datetime.timedelta(days=i)
            info = (DataInDB.search_db_for_history(date))
            name = info[0][0]
            out_week = week_day[info[0][2]]
            turn = info[0][3]
            if turn == 0:
                result.append(f'{out_week} ({date}) ездил {name} по очереди')
            if turn == 1:
                result.append(f'{out_week} ({date}) ездил {name} вне очереди')

    return result


# если вытаскиваешь даты и там нет инфы то ничего не выдавать, т.е проверка через try, except

# print(week(7))

