import json

with open('file.json','r') as file:
    data = json.load(file)
    print(data['surname'],data['name'],data['age'])