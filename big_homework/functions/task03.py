
def simple_compare(x:int,y:int) -> bool:
    if x < y:
        return True
    else:
        return False

assert simple_compare(1,2) == True
assert simple_compare(11,0) == False