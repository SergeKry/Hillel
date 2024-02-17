import random


def get_int(message, minimum, default):
    while True:
        try:
            input_str = input(message)
            if not input_str and default is not None:
                return default
            i = int(input_str)
            if i < minimum:
                print('must be >=', minimum)
            else:
                return i
        except ValueError:
            print('Wrong input. Value Error')


rows = get_int('Number of rows: ', 1, None)
columns = get_int('Number of columns: ', 1, None)
minimum = get_int('Enter minimum number (or press Enter for 1)', -100000, 0)
max_default = 100
if minimum > max_default:
    max_default *= 2
maximum = get_int(f'Enter maximum number (or just Enter for {max_default}) :', minimum, max_default)

row = 0
while row < rows:
    line = ''
    column = 0
    while column < columns:
        rand_int = random.randint(minimum, maximum)
        rand_str = str(rand_int).rjust(10)
        column += 1
        line += rand_str
    print(line)
    row += 1
