summ = 0
for i in range(101):
    summ += i
print(f'1:{summ}')

summ = 0
for i in range(100,1001):
    summ += i
print(f'2:{summ}')

summ = 0
for i in  range(100,1001,2):
    summ += i
print(f'3:{summ}')

summ = 1
for i in range(1,11):
    summ *= i
print(f'4:{summ}')

summ = 1
for i in range(10):
    summ *= 2
print(f'5:{summ}')

summ = 0
for i in range(1111):
    summ += i
    if summ > 1000:
        break
print(f'6:{summ}{i}')