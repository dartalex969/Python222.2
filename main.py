import json
import re

# Сотрудники берутся из .json файла.
# Преобразуются в список словарей (см. employees)
with open('test.json') as json_file:
    employees = json.load(json_file)['employers']
    print(employees)


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
