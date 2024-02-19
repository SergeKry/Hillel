def get_int(msg):
    while True:
        try:
            input_str = input(msg)
            if input_str:
                input_int = int(input_str)
                return input_int
            else:
                return False
        except ValueError:
            print('Wrong input. Please enter a number')


user_numbers = []
while True:
    number = get_int('Enter a number (or Enter to finish): ')
    if not number:
        break
    else:
        user_numbers.append(number)
count = len(user_numbers)
summ = sum(user_numbers)
lowest = min(user_numbers)
highest = max(user_numbers)
mean = summ / count
print(f'numbers: {user_numbers}')
print(f'count = {count}, sum = {summ}, lowest = {lowest}, highest = {highest}, mean = {mean}')
