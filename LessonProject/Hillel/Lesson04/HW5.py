users_input_str = input('Введіть ціле число: ')
users_input = False
if users_input_str[0] in '-':
    if users_input_str[1:].isdigit():
        users_input = users_input_str
    else:
        print('не вірне введення')
else:
    if users_input_str.isdigit():
        users_input = users_input_str
    else:
        print('не вірне введення')

if users_input:
    result_template = 'Ви ввели {} число'
    print(result_template.format(0)[:-6]) if int(users_input) == 0 else print(result_template.format('парне')) if int(users_input) % 2 == 0 else print(result_template.format('непарне'))

# Альтернативний варіант, який спрощує тернарний вираз, та відповідає PEP 8 (коротше 120 символів),
# Але відходить від завдання і трохи модифікує шаблон.
#
# if users_input:
#     result_template = 'Ви ввели {}'
#     result = 0 if int(users_input) == 0 else 'парне число' if int(users_input) % 2 == 0 else 'непарне число'
#     print(result_template.format(result))
