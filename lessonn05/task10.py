def filter_odd_numbers(lst):
    a = [i for i in lst if i % 2 == 0]
    print(a)

lst = [1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1]
filter_odd_numbers(lst)