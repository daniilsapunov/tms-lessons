from functools import reduce
from task1 import input_list

def summ():
    summa = reduce(lambda x,y: x+y,input_list(),0)
    print(summa)
summ()
