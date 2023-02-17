import json
import re

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
            if len(res) == 0:
                return "не чо нету"
            return res


        def voztast(file1: list):
            res = list(filter(lambda x: True if int(x["age"]) == int(age1) else False, file1))
            if len(res) == 0:
                return "не чо нету"
            return res


        def all(file1: list):
            res = list(filter(lambda x: True if x["name"][0].upper() == name.upper() else False, file1))
            res = list(filter(lambda x: True if int(x["age"]) == int(age1) else False, res))
            if len(res) == 0:
                return "не чо нету"
            return res

        if age1 == 0 and name != "":
            return bukvi(file)
        if age1 != 0 and name == "":
            return voztast(file)
        if name != "" and age1 != 0:
            return all(file)
    return get

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
Поиск по фамилии - 4
Вывод информации обо всех сотрудниках по возрасту - 5
Вывод информации обо всех сотрудниках по первой букве фамилии - 6
Сохранение данных - 7
Выход - 0''')
        choose = int(input('Выберите вариант: '))

        if choose == 0:
            result = {'employees':employees}
            json_object = json.dumps(result)
            with open('test.json', 'w') as f1, open('test/test2.txt', 'w') as f2:
                f1.write(json_object)
                testF = ''
                for i in employees:
                    for j in i:
                        testF += str(j)
                        testF += ' '
                        testF += str(i[j]) + '\n'
                    testF += '\n'
                f2.write(testF)
            break

        elif choose == 6:
            funk = file(employees)
            for i in funk(int(input("Чо надо? Введи число: "))):
                print()
                for vel in i.value():
                    print(vel, end=" ")
                print()



        elif choose == 7:
            funk1 = file(employees)
            for i in funk1(input("Введи букву :")):
                print()
                for vel in i.value():
                    print(vel, end=" ")
                print()

        elif choose == 10:
            result = {'employees': employees}
            json_object = json.dumps(result)
            with open('test.json', 'w') as f1, open('test/test2.txt', 'w') as f2:
                f1.write(json_object)
                testF = ''
                for i in employees:
                    for j in i:
                        testF += str(j)
                        testF += ' '
                        testF += str(i[j]) + '\n'
                    testF += '\n'
                f2.write(testF)

