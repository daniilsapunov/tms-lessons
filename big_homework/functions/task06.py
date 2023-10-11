def hello_world():
    return print('Hello world!')


def my_sum(x:int,y:int) -> int:
    return x + y


def simple_compare(x:int,y:int) -> bool:
    if x < y:
        return True
    else:
        return False


def simple_compare_improve(x: int, y: int) -> bool:
    if x < y:
        return -1
    elif x == y:
        return 0
    else:
        return 1


def fileter_negative_numbers(lst:list) -> []:
    return [num for num in numbers if num >= 0]

def input_two_number():
    x = int(input())
    y = int(input())
    return x,y

number_problem = input('Введите номер задачи : \n')

if number_problem == '1':
    hello_world()
elif number_problem == '2':
    x = int(input('Введите 1 число: \n'))
    y = int(input('Введите 2 число \n'))
    print(my_sum(x,y))
elif number_problem == '3':
    x = int(input('Введите 1 число: \n'))
    y = int(input('Введите 2 число \n'))
    print('Первое число меньше второго? Ответ: ', simple_compare(x,y))
elif number_problem == '4':
    x = int(input('Введите 1 число: \n'))
    y = int(input('Введите 2 число \n'))
    print('Результат сравнения: ', simple_compare_improve(x, y))
elif number_problem == '5':
    numbers = [int(i) for i in input('Введите числа разделенные пробелом').split()]
    print('Мы удалили отрицательные числа из списка', fileter_negative_numbers(numbers))
else:
    print('Такой задачи не существует')
