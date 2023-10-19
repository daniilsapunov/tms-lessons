def sum_and_max(*args):
    s = sum(args)
    m = max(args)
    return (s,m)

print(sum_and_max(*(1,2,5,6,9,12)))

