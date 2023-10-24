import json


info = {'name':'Daniil','surname':'Sapunov','age':'19'}

with open('file.json','w') as file:
    json.dump(info, file)