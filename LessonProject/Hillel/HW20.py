import csv
import openpyxl
from openpyxl.styles import Alignment

csv_data = []
with open('my_dict.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        csv_data.append(row)

for item in enumerate(csv_data):
    item[1].pop(2)
    if item[0] > 0:
        item[1][0] = int(item[1][0])

title_row = []
counter = 1
while counter < len(csv_data):
    title_row.append(f'Person {counter}')
    counter += 1
title_row.insert(0, None)

wb = openpyxl.Workbook()
ws = wb.active
ws.append(title_row)
for column_index, row in enumerate(csv_data):
    for row_index, value in enumerate(row):
        cell = ws.cell(row=row_index + 2, column=column_index + 1)
        cell.value = value
        cell.alignment = Alignment(horizontal='left')
wb.save('my_dict.xlsx')