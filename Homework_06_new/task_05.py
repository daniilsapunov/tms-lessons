def my_decorator(func):
    def wrap(x):
        print(f'Функция получила на вход значение {x}')
        y = func(x)
        print(f'Результат функции {y}')
        return y
    return wrap


@my_decorator
def my_func(x):
    return x ** 2


y = my_func(3)
print(f'y = {y}')

