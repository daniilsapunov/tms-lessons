from function import input_list
from functools import reduce

# Дан список чисел. Найти его сумму.

# res = 0
# for i in input_list():
#     res += i
#
# result = reduce(lambda i,result: i + result, input_list(),0)
# print(res)
# print(result)


# Дан список чисел. Найти минимальное число.
#
# minimal = 9999
#
# for i in input_list():
#     if i < minimal:
#         minimal = i
#
# mini = reduce(lambda x,y: min(x,y), input_list())
#
# print(mini,minimal)

# Дан список чисел. Найти произведение всех элементов.

# proiz = reduce(lambda x,y: x * y,input_list())
# o = 1
# for i in input_list():
#     o = o * i
#
# print(o,proiz)
# С помощью функции reduce и range найти факториал числа 5.

fact = reduce(lambda x,y:x * y,range(1,6))
print(fact)
# * Напишите свою реализацию функции my_reduce. Для
# простоты можно сделать третий параметр обязательным.

def my_reduce(func, iterible,value):
    result = value
    for i in iterible:
        result = func(result,i)
    return result

print(my_reduce(lambda x,y:x * y,input_list(),1))
