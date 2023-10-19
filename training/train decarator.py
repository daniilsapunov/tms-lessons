def decarator(origin_func):
    def wrapper(x):
        print(f'Функция получила на вход {x}')
        y = origin_func(x)
        print(f'На выходе получаем {y}')
        return y
    return wrapper


@decarator
def func(x):
    return x + x * x / (x + x)

n = func(5)
# def my_decorator(orignal_func):
#     def wrap(x):
#         print(f'Функция получила на вход значение {x}')
#         y = orignal_func(x)
#         print(f'Результат функции {y}')
#         return y
#     return wrap
#
#
# @my_decorator
# def my_func(x):
#     return x ** 2
#
#
# y = my_func(3)
# print(f'y = {y}')