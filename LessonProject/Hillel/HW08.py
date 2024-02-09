import random
import math


def get_int(text):
    while True:
        integer = input(f'{text}')
        if integer.isdigit() and int(integer) > 0:
            integer = int(integer)
            break
        else:
            print('Wrong input. Please enter a positive integer')
    return integer


def get_range(text):
    while True:
        desired_range = get_int(text)
        if desired_range > 1:
            break
        else:
            print('Maximum number cannot be so small. Make your range wider')
    return desired_range


def start_game(tries, answer, game_range):
    result = False
    print(f'\nTHE GAME BEGINS\nMy number is somewhere between 1 and {game_range}. Number of tries: {tries}')
    while tries > 0:
        guess = get_int('Enter your guess: ')
        tries -= 1
        if guess == answer:
            result = True
            break
        elif guess != answer and tries == 0:
            break
        elif guess < answer:
            print(f'Your guess is smaller. {tries} tries left')
        else:
            print(f'Your guess is bigger. {tries} tries left')
    return result


users_range = get_range('What is maximum number that computer can choose?: ')
user_tries = int(math.log2(users_range))
computer_choice = random.randrange(1, users_range)
game_result = start_game(user_tries, computer_choice, users_range)
if game_result:
    print('\nYou win!!!')
else:
    print(f'\nYou loose. Correct answer was {computer_choice}')

