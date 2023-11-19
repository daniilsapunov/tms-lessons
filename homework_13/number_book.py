import sqlite3


def create_new_table():
    with sqlite3.connect('sqlite_for_number.db') as connection:
        result = connection.execute(
            """CREATE TABLE IF NOT EXISTS user (
            name VARCHAR PRIMARY KEY,
            number VARCHAR);"""
        )


def add_new_user(name,number):
    with sqlite3.connect('sqlite_for_number.db') as connection:
        result = connection.execute(
          """INSERT INTO user 
          VALUES  (?, ?);""",
            (name, number))


def print_table():
    with sqlite3.connect('sqlite_for_number.db') as connection:
        result = connection.execute(
            'SELECT * FROM user ORDER BY name;')
        print(result.fetchall())


def swap_number(name, number):
    with sqlite3.connect('sqlite_for_number.db') as connection:
        result = connection.execute(
            """UPDATE user 
            SET number = ?
            WHERE name = ?; """,
            (number, name)
        )



if __name__ == '__main__':
    create_new_table()
    while True:
        answer = input('0. Выйти из программы \n'
          '1. Добавить новый контакт \n'
          '2. Вывести весь список контактов в алфавитном порядке.\n'
          '3. Обновить номер контакта \n')
        if answer == '0':
            exit()
        elif answer == '1':
            name = input('Введите имя')
            number = input('Введите номер')
            add_new_user(name,number)
        elif answer == '2':
            print_table()
        elif answer == '3':
            name = input('Введите имя изменяемого контакта')
            number = input('введите номер')
            swap_number(name,number)
        else:
            print('PLS ENTER NUMBER 0 - 3')
