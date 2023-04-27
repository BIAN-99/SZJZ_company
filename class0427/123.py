import json


def read_json(file_name):
    li = ''
    with open(file_name, 'r') as data:
        for line in data:
            li += line.strip()
        print(json.loads(li))

read_json("user.json")