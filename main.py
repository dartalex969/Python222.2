import json
import re

# Сотрудники берутся из .json файла.
# Преобразуются в список словарей (см. employees)
with open('test.json') as json_file:
    employees = json.load(json_file)['employers']
    print(employees)


def add_employee(employees):
    if (len(employees)):
        keys = employees[0].keys()
    else:
        pass
        return
    new_employee = {}
    for key in keys:
        value = input(f'Enter {key} of employee: ')
        new_employee[key] = value
    if new_employee not in employees:
        employees.append(new_employee)





add_employee(employees)
print(employees)


# def edit_employee(employees):
#     surname = input('Введите фамилию сотрудника, данные которого нужно изменить: ')
#     for employee in employees:
#         if employee['surname'] == surname:
#             name = input('Введите новое имя сотрудника: ')
#             age = input('Введите новый возраст сотрудника: ')
#             position = input('Введите новую должность: ')
#             employee['name'] = name
#             employee['age'] = age
#             employee['position'] = position
#             print('Данные сотрудника успешно изменены.')
#             return
#     print('Сотрудник с такой фамилией не найден.')

# def edit_employee(employees):
#     surname = input('Введите фамилию сотрудника, данные которого нужно изменить: ')
#
#
# edit_employee(employees)
# print(employees)









