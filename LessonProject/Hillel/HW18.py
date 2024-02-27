import random
import json

names = ['Bob', 'John', 'Mike', 'Nancy', 'David', 'Robert']
my_dict = {}
for item in names:
    my_dict.update({random.randint(1000000, 9999999): (item, random.randint(1, 99))})


with open('my_dict.json', mode='w', encoding='utf-8') as file:
    json.dump(my_dict, file)
