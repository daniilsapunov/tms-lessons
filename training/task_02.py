# Пользователь вводит произвольное количество маленьких
# латинских букв через пробел.
# Напишите функцию remove_vowels, которая принимает список
# из этих букв и удаляет из него все гласные буквы.
# Выведите результат работы на экран.
# Пример:
# Ввод пользователя: a b c d e f
# Результат программы: ['b', 'c', 'd', 'f']
# Используйте функцию ﬁlter.
# Список всех гласных английского языка: a, e, i, o, u

from call import input_list


def remove_vowels() -> [str]:
    return list(filter(lambda x: x != 'a' and x != 'e' and x != 'i' and x != 'o' and x != 'u' and x != 'y' , input_list()))

print(remove_vowels())

