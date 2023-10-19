def input_list(promt:"", set:" ", element_type: int):
    print(promt)
    result = []
    for i in input().split():
        result.append((int(i)))
    return result
my_list = input_list("hello","!!",str)
print(input_list("hello","!!",str))