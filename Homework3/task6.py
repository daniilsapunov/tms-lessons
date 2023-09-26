dict = {'January' : 31,
        'February' : 28,
        'March' : 31,
        'April' : 30 ,
        'May': 31,
        'June' : 30,
        'July' : 31 ,
        'August' : 31,
        'September' : 30,
        'October' : 31,
        'November' : 30,
        'December' : 31}

print('first month, second day')
month = input()
day = int(input())


print(month in dict and day == dict.get(month))