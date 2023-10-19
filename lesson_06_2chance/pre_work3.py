from function import input_list

# # Дан список чисел. Удалите из него отрицательные числа.
# f = []
#
# for i in input_list():
#     if i > 0:
#      f.append(i)
#
# nechet = [i for i in input_list() if i > 0]
#
# necchet = list(filter(lambda i: i > 0,input_list()))
#
# print(f)
# print(nechet)
# print(necchet)



#
# # 3.2. Дан список чисел. Удалите из него нечётные числа.
#
# nech = list(filter(lambda i: i % 2 == 0,input_list()))
#
# nechh = [i for i in input_list() if i % 2 == 0]
#
# f = []
#
# for i in input_list():
#     if i % 2 == 0:
#      f.append(i)
#
# print(nech)
# print(nechh)
# print(f)




# 3.3. Дан список чисел. Выведите три числа: количество
# положительных чисел, количество нулей, и количество
# отрицательных чисел. Используйте функции ﬁlter и len.


# coun = 0
# counn = 0
# counnn = 0
#
# for i in input_list():
#     if  int(i) > 0:
#      coun += 1
#     elif int(i) < 0:
#      counn += 1
#     elif int(i) == 0:
#      counnn += 1
# print(f'{coun,counn,counnn}')
#
# positive = len(list(filter(lambda i:i > 0,input_list())))
# unpositive = len(list(filter(lambda  i: i < 0, input_list())))
# zero = len(list(filter(lambda i: i == 0,input_list())))
# print(zero,unpositive,positive)


# 3.4. * Напишите свою реализацию функций my_ﬁlter,
# возвращающую список.

# def my_filter(func,iterable):
#     return [i for i in input_list() if  func(i)]
#
# print(f'3.4:{my_filter(lambda x: x % 2 == 0,input_list())}')
# 3.5. ** Напишите свою реализацию функций my_ﬁlter, которая
# вместо возвращения списка использует ключевое слово yield
# при генерации очередного элемента.

def my_filter_new(predicate, iterable):
    for i in iterable:
        if predicate(i):
            yield i

print(f'3.5(wrong usage): {my_filter_new(lambda x: x > 0, input_list())}')
print(f'3.5: {list(my_filter_new(lambda x: x > 0, input_list()))}')