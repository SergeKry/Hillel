import random
import math


def get_int(text, error, parameter=0):
    while True:
        integer = input(f'{text}')
        if integer.isdigit() and int(integer) > parameter:
            integer = int(integer)
            break
        else:
            print(error)
    return integer


def start_game(tries, answer, game_range):
    result = False
    print(f'\nTHE GAME BEGINS\nMy number is somewhere between 1 and {game_range}. Number of tries: {tries}')
    while tries > 0:
        guess = get_int('Enter your guess: ', 'Wrong input. Please enter a positive integer')
        tries -= 1
        if guess == answer:
            result = True
            break
        elif guess != answer and tries == 0:
            break
        elif guess > game_range:
            tries += 1
            print('Your number is bigger than the range you chose. Be careful')
        elif guess < answer:
            print(f'Your guess is smaller. {tries} tries left')
        else:
            print(f'Your guess is bigger. {tries} tries left')
    return result


range_error = 'Input error. This should be an integer bigger than 2'
users_range = get_int('What is maximum number that computer can choose?: ', range_error, 1)
user_tries = int(math.log2(users_range))
computer_choice = random.randrange(1, users_range)
game_result = start_game(user_tries, computer_choice, users_range)
if game_result:
    print('\nYou win!!!')
else:
    print(f'\nYou loose. Correct answer was {computer_choice}')
