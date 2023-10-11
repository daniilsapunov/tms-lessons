from functools import reduce


def my_join(current_list, separator) -> str:
    return reduce(lambda x, y: x + separator + y, current_list)


sentence = input('Your sentence \n').split()
sep = input('your separator \n')
print(my_join(sentence, sep))

