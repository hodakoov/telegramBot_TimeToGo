import sqlite3
import datetime


connect = sqlite3.connect('sqlbase.db', check_same_thread=False) #check_same_thread - проверка того же потока, отключить
cursor = connect.cursor() #вносить изменения и читать


def creation_db():  # создание таблицы, "IF NOT EXISTS" - если уже есть не создавать по новой

    cursor.execute("""CREATE TABLE IF NOT EXISTS users (  
                id INTEGER PRIMARY KEY AUTOINCREMENT,  
                user_name TEXT,
                out_of_turn BOOLEAN,
                comfortable BOOLEAN,
                date INT UNIQUE,
                day_of_the_week INT)""")

    # id - просто нумерация, user_name - имя водителя, out_of_turn - когда ездил вне очереди,
    # comfortable - всем удобно было? True - да, date - дата поездки, day_of_the_week - день недели поездки

    connect.commit()
    # connect.close()
# creation_db()

def add_values_db(users_list): #добавление значений в таблицу

    cursor.execute(f"INSERT INTO users (user_name, out_of_turn, "
                   f"comfortable, date,  day_of_the_week) VALUES(?,?,?,?,?)", users_list)

    connect.commit()
    # connect.close()

# add_values_db(['Valery', True, False, datetime.date.today(),
#                       datetime.date.isoweekday(datetime.datetime.today())])

# datetime.datetime.today() - выдает дату с час,мин,с. ЭТО ДЛЯ ОТЛАДКИ
# datetime.date.today() - выдает только дату, ТО ЧТО НУЖНО
# try:
#     add_values_db(['Valery', True, False, datetime.datetime.today(),
#                       datetime.date.isoweekday(datetime.datetime.today())])
#     print("В базу данных добавлена новая дата")
# except(sqlite3.IntegrityError):
#     print("В базе данных уже есть информация по этой дате")


# для вывода истории поездок.
def search_db(name_column, date): # вывод данных из таблицы

    # cursor.execute("SELECT date FROM users")
    # cursor.execute("SELECT user_name FROM users WHERE user_id = ?",('2'))
    cursor.execute(f"SELECT {name_column} FROM users WHERE date = '{date}'")
    # ПРИМЕР cursor.execute("SELECT user_name FROM users WHERE date = '2022-04-16'")

    users_result = cursor.fetchall() # fetchall - метод объекта курсора для получения всех данных
    #users_result = cursor.fetchone() # fetchone - метод объекта курсора для получения только одного результата

    # print(users_result)  # вывод имени пользователя. Работать как со списками [0][2] <- внутрь лезем
    connect.commit()
    # connect.close()
    return users_result[0][0]

# print(search_db('user_name', '2022-05-10'))

# a = search_db('2022-04-16')
# print(a)
# for i in range(len(a)):
#     print(a[i])


# для изменения данных, в случае когда кто то решает ехать сам
def update_db(name_column, result_name_column, result_date): # обновление данных в таблице

    cursor.execute(f"UPDATE users SET {name_column} = ? WHERE date = ?",
                   (result_name_column, result_date))

    connect.commit()
    # connect.close()
#update_db('user_name', 'Valery', 'date', '1')


def delete_db(): # удаление таблицы полностью users
    cursor.execute("DROP TABLE users")
    connect.commit()
    connect.close()
# delete_db()