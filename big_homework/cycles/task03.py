lst = [int(i) for i in input().split()]
max = lst[0]

for i in lst:
    if i > max:
        max = i

print(max)
