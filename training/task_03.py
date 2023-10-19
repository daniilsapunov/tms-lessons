# Решите прошлую задачу, в которой теперь пользователь
# может вводить буквы в любом регистре. Вам по прежнему
# нужно удалить все гласные. При этом вывести результат нужно
# вывести сохранив изначальный регистр.
# Пример:
# Ввод пользователя: a B c d E F
# Результат программы: ['B', 'c', 'd', 'F']


from call import input_list


def remove_vowels() -> [str]:

    return list(filter(lambda x: x.lower() != 'a' and x.lower() != 'e' and x.lower() != 'i' and x.lower() != 'o' and x.lower() != 'u' and x.lower() != 'y' , input_list()))

print(remove_vowels())


