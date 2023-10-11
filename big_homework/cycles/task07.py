my_dict = {'a': 9, 'b': 11, 'c': 0}
bigger_value = None
max_key = None

for key,value in my_dict.items():
    if value > bigger_value or bigger_value is None:
        bigger_value = value
        max_key = key

print(max_key)
