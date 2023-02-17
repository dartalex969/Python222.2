



import json
import re

# Сотрудники берутся из .json файла.
# Преобразуются в список словарей (см. employees)

with open('test.json') as json_file:
    employees = json.load(json_file)['employees']
    print('Список сотрудников:')
    print('-------------------')
    for i in employees:
        for j in i:
            print(j,i[j])
        print()

    while True:
        print('''Ввод нового сотрудника - 1
Редактирование данных - 2
Удаление сотрудника - 3
Удаление сотрудника - 4
Поиск по фамилии - 5
Вывод информации обо всех сотрудниках по возрасту - 6
Вывод информации обо всех сотрудниках по первой букве фамилии - 7
Сохранение данных - 8
Выход - 0''')
        choose = int(input('Выберите вариант: '))

        if choose == 0:
            result = {'employees':employees}
            json_object = json.dumps(result)
            with open('test.json','w') as f1, open('test/test2.txt','w') as f2:
                f1.write(json_object)
                # for i in employees:
                #     f2.writelines()
                #     print()

            break
        elif choose == 10:
            result = {'employees': employees}
            json_object = json.dumps(result)
            with open('test.json','w') as f1:
                f1.write(json_object)


def file(file: list):

    def get(*args):
        name, age1 = "", 0
        for i in args[:2]:
            if type(i) == int and age1 == 0:
                age1 = i
            if type(i) == str and name == "":
                name = "".join(i)
        def bukvi(file1: list):
            res = list(filter(lambda x: True if x["name"][0].upper() == str(name).upper() else False, file1))
            return res


        def voztast(file1: list):
            res = list(filter(lambda x: True if int(x["age"]) == int(age1) else False, file1))
            return res


        def all(file1: list):
            res = list(filter(lambda x: True if x["name"][0].upper() == name.upper() else False, file1))
            res = list(filter(lambda x: True if int(x["age"]) == int(age1) else False, res))
            return res

        if age1 == 0 and name != "":
            return bukvi(file)
        if age1 != 0 and name == "":
            return voztast(file)
        if name != "" and age1 != 0:
            return all(file)
    return get

s = file(employees)
print(s())


def find_employees():
    surname = input('Введите фамилию: ')
    for i in employees:
        if i.get('surname') == surname:
            for key in i:
                print(f"{key}:{i[key]}")


find_employees()