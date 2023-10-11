def simple_compare(x:int,y:int) -> bool:
    if x < y:
        return -1
    elif x == y:
        return 0
    else:
        return 1

assert simple_compare(1,2) == -1
assert simple_compare(11,0) == 1
assert simple_compare(0,0)== 0