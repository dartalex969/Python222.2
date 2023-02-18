import json
import re
def find_employees():
    surname = input('Введите фамилию: ')
    for i in employees:
        if i.get('surname') == surname:
            for key in i:
                print(f"{key}:{i[key]}")



def add_employee(employees):
    if (len(employees)):
        keys = employees[0].keys()
    else:
        pass
        return
    new_employee = {}
    for key in keys:
        value = input(f'Введите {key} сотрудника: ')
        new_employee[key] = value
    if new_employee not in employees:
        employees.append(new_employee)


def edit_employee(employees):
    if not employees:
        print('Список сотрудников пуст.')
        return

    last_name = input('Введите фамилию сотрудника, которого нужно отредактировать: ')
    found = False
    for employee in employees:
        if employee['first_name'] == last_name:
            found = True
            name = input('Введите имя (оставьте пустым, чтобы не изменять): ')
            if name:
                employee['name'] = name
            first_name = input('Введите фамилию (оставьте пустым, чтобы не изменять): ')
            if first_name:
                employee['first_name'] = first_name
            age = input('Введите возраст (оставьте пустым, чтобы не изменять): ')
            if age:
                employee['age'] = age
            position = input('Введите должность (оставьте пустым, чтобы не изменять): ')
            if position:
                employee['position'] = position
            print('Сотрудник отредактирован успешно.')
            break

    if not found:
        print('Сотрудник с такой фамилией не найден.')


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
        elif choose == 1:
            add_employee(employees)
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



