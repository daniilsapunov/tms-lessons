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

print('Enter one of January, February, March, April, May, June, July, August, September, October, November, and December')
month = input()
print(dict.get(month))