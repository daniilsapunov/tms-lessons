import csv

header = ('name','surname','gender')
info = ['daniil','sapunov','m']

with open('info.csv','w') as file:
    writer = csv.writer(file,delimiter=',')
    writer.writerow(header)
    writer.writerow(info)