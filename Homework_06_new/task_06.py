def my_decorator(func):
    def wrap(*args,**kwargs):
        print(f'Функция получила на вход значение {args} {kwargs}')
        y = func(*args,**kwargs)
        print(f'Результат функции {y}')
        return y
    return wrap


@my_decorator
def my_func(a, b, c, d):
    return a + b + c + d


y = my_func(1, 2, d=3, c=4)
print(f'y = {y}')

# Ожидаемый вывод программы:
# Функция получила на вход значение (1, 2) {'d': 3, 'c': 4}
# Результат функции: 10
# y = 10
