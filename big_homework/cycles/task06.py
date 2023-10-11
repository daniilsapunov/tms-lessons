my_dict = {'a': 9, 'b': 11, 'c': 0}
bigger = my_dict['a']
print(bigger)

for key,value in my_dict.items():
    if value > bigger:
        bigger = value

print(bigger)

