import json
name, surname, age = list(input().split())
data = {'name':name,'surname': surname,'age':age}
with open('file_04.json','w') as file:
    json.dump(data,file)