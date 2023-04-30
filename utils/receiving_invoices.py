import json


def get_invoice():
    with open('../data/operations.json', encoding='utf-8') as file:
        response = json.loads(file.read())[-5:]
        return response
