import json
import re

# Сотрудники берутся из .json файла.
# Преобразуются в список словарей (см. employees)
with open('test.json') as json_file:
    employees = json.load(json_file)['employers']
    print(employees)


def find_employees():
    surname = input('Введите фамилию: ')
    for i in employees:
        if i.get('surname') == surname:
            for key in i:
                print(f"{key}:{i[key]}")


find_employees()
