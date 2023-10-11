lst = [int(i) for i in input().split()]
count = 0


for i in lst:
    if i == 0:
        count += 1

if count > 0:
    print('yes')
else:
    print('no')


