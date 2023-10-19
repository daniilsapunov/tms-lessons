from function import input_list





# 2.1. Дан список чисел. Увеличьте каждый элемент в 100 раз.
# ff = []
# for num in input_list():
#     ff.append(num * 100)
# print(ff)
#

# number = [i * 100 for i in input_list()]
# print(number)

# number = list(map(lambda i: i * 100, input_list()))
# print(number)

# 2.2. Дан список чисел. Преобразуйте этот список в список строк.
# ff = []
# for i in input_list():
#     ff.append(str(i))
# print(ff)
#
# str_spisok = [str(i) for i in input_list()]
# print(str_spisok)
#
# str_spisokk = (list(map(lambda i:str(i),input_list())))
# print(str_spisokk)

# 2.3. Дан список чисел. Разделите каждый элемент на 100 и
# округлите до целого числа (функция round)
#
# ff = []
# for i in input_list():
#     ff.append(round(i / 100))
# print(ff)
#
# okrug = [round(i / 100) for i in input_list()]
# print(okrug)
#
# okreg1 = list(map(lambda i: round(i/100),input_list()))
# print(okreg1)

# 2.4. * Напишите свою реализацию функций my_map,
# возвращающую список.
# def my_map(func, iterable):
#     return [func(el) for el in iterable]
#
#
# print(f'2.4: {my_map(str, input_list())}')


# 2.5
# def my_map_gen(func, iterable):
#     for el in iterable:
#         yield func(el)
#

def my_map(function,iterible):
    return [function(i) for i in iterible]
print(f'f2.4 :{my_map(str,input_list())}')

# 2.5. ** Напишите свою реализацию функций my_map, которая
# вместо возвращения списка использует ключевое слово yield
# при генерации очередного элемента.

def my_map(function,iterible):
    for i in input_list():
        yield function(i)
print(f'2.5:{my_map(str,input_list())}')