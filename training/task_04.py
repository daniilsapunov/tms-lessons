# Пользователь вводит произвольное количество слов через пробел.
# Затем (на следующей строке) вводит один символ (разделитель).
# Вам нужно написать функцию my_join, которая принимает список из
# строк и символ-разделить, и возвращает строку, в которой все
# слова из списка соединены через символ разделитель.
# Пример ввода пользователя:
# hello this is my string
# @
# Вывод программы: hello@this@is@my@string
# Используйте функцию reduce.

from functools import reduce

def my_join(input_list: list[str],sep: str):
    return reduce(lambda x, y: x + sep + y, input_list)

print(my_join('Hello my name danila'.split(),'$'))

