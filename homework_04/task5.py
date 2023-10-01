answer = int(input())
summa = 0

while answer != 0:
    summa += answer % 10
    answer = answer // 10

print(f'{summa}')