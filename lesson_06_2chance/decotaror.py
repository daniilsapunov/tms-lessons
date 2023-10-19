# Скопируйте к себе функции из комментария к слайду.
# Вам даны реализации базовых математических операций с целыми числами.
# Вопрос: что будет, если передать в эти функции что-то другое вместо чисел.
# Например вызвать minus('hello', [123]).
# Ваша задача сделать так, чтобы при вызове каждой функции проводилась
# проверка типов переменных x и y c помощью выражения isinstance(x, int).
# В случае, если одна из переменных НЕ является целым числом - печатаем
# сообщение об ошибке "Expected int type" в консоль и возвращали None.
# Для простоты можно сначала изменить код одной из функций так,
# чтобы она сама делала эти проверки.
# Конечная цель - выполнить требования задачи НЕ меняя код самих функций,
# а создать функцию-декоратор check_types,
# пометив каждую из функций вашим декоратором (@check_types)
#


def check_types(func):
    def new_func(x,y):
        if not isinstance(x,int) or not isinstance(y,int):
            print("Expected int type")
            return None
        return func(x,y)
    return new_func
@check_types
def plus(x, y):
    return x + y
@check_types
def minus(x, y):
    return x - y
@check_types
def mult(x, y):
    return x * y
@check_types
def div(x, y):
    return x / y

print(plus(123,'123'))
print(minus(4.5,'gg'))
print(mult(12,12))
print(div(666,222))
print(plus([],{}))
print(plus(4.5,4.5))