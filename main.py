import json
import re


#                                 --- Employees ---


with open('test.json') as json_file:

    employees = json.load(json_file)['employers']

    print(employees)









