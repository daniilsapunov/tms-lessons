import csv

header = ('name','surname','age')
info = list(input().split())

with open('file_07.csv','w') as file:
    writer = csv.writer(file,delimiter=',')
    writer.writerow(header)
    writer.writerow(info)