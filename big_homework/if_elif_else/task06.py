month = int(input())

if 0 < month < 3 or month == 12:
    print('Зима')
elif 2 < month < 6 :
    print('Весна')
elif 5 < month < 9 :
    print('Лето')
else:
    print('Осень')