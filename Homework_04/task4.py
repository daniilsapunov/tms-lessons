import random

n = int(input('Enter number'))
number = random.randint(0, 100)

while True:
    if number == n:
        print('U are GOD')
        break
    elif n < number:
        n = int(input('your number should be bigger'))
    elif n > number:
        n = int(input('your number should be smaller'))




