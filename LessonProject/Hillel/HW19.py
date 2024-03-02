import json
import csv
import random

phone_codes = ['095', '066', '098', '096', '050', '097']


def build_line(dict_item):
    _id = dict_item[0]
    name = dict_item[1][0]
    age = dict_item[1][1]
    probability = random.randint(1,100)
    if probability > 25:
        telephone = '+3(' + random.choice(phone_codes) + ')' + str(random.randint(1, 9999999)).rjust(7, '0')
    else:
        telephone = None
    line = [_id, name, age, telephone]
    return line


with open('my_dict.json') as json_file:
    json_data = json.load(json_file)

header_row = ["ID", "Ім'я", "Вік", "Телефон"]
data_for_printing = [header_row]
for item in json_data.items():
    data_for_printing.append(build_line(item))

with open('my_dict.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerows(data_for_printing)
