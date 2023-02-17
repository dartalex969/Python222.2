



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



























