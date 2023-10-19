from task1 import input_list
positive_nubers = []

positive_nubers = list(filter(lambda num: num % 2 == 0, input_list()))
print(positive_nubers)