import random
transform = {0: 'R', 1: 'S', 2: 'P'}
want_to_play = True
while want_to_play:
    win = False
    user_choice = input('Make your choice (Rock(R), Scissors(S), Paper(P)): ').upper()
    comp = random.randint(0, 2)
    comp_choice = transform[comp]
    if user_choice == 'R' and comp_choice == 'S':
        win = True
        print(f'You: {user_choice} | {comp_choice} : Computer')
        print('You win')
        want_to_play = input('Do you want to play again?:(Y/N) ').lower() == 'y'
    if user_choice == 'S' and comp_choice == 'P':
        win = True
        print(f'You: {user_choice} | {comp_choice} : Computer')
        print('You win')
        want_to_play = input('Do you want to play again?:(Y/N) ').lower() == 'y'
    if user_choice == 'P' and comp_choice == 'R':
        win = True
        print(f'You: {user_choice} | {comp_choice} : Computer')
        print('You win')
        want_to_play = input('Do you want to play again?:(Y/N) ').lower() == 'y'
    if user_choice == comp_choice:
        win = True
        print(f'You: {user_choice} | {comp_choice} : Computer')
        print("It's a draw!")
        want_to_play = input('Do you want to play again?:(Y/N) ').lower() == 'y'
    if not win:
        print(f'You: {user_choice} | {comp_choice} : Computer')
        print('You loose')
        want_to_play = input('Do you want to play again?:(Y/N) ').lower() == 'y'
