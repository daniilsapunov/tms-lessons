from task1 import input_list

def my_map():
    l = list(map(lambda asd: round(asd/100), input_list()))
    print(l)
my_map()