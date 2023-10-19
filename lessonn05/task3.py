lst = [1,2,3,4,5,6,7,8,9,0]
def list_sum(lst):
    summ = 0
    for i in lst:
        summ += i
    return summ

list_sum(lst)
assert list_sum([1,2,3,4]) == 10
