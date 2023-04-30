import json
import os


def get_invoice():
    link_data = os.path.abspath('data/operations.json')
    with open(link_data, encoding='utf-8') as file:
        response = json.loads(file.read())[-5:]
        return response
