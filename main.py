import json
import re

# Сотрудники берутся из .json файла.
# Преобразуются в список словарей (см. employees)
with open('test.json') as json_file:
    employees = json.load(json_file)['employers']
    print(employees)










