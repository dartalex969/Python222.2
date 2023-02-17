import json
import re

# Сотрудники берутся из .json файла.
# Преобразуются в список словарей (см. employees)
with open('test.json') as json_file:
    employees = json.load(json_file)['employers']
    print(employees)


def deleting(data):
    surname = input('Введите фамилию сотрудника, которого хотите удалить: ')
    name = input('Далее имя сотрудника: ')
    age = int(input('И теперь возраст сотрудника: '))
    for i in employees:
        if i['surname'] == surname and i['name'] == name and i['age'] == age:
            employees.pop(i)
