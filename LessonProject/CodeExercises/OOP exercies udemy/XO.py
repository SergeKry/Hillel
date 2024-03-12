class Game:
    def __init__(self):
        self.slots = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
        self.win = ({1: True, 2: True, 3: True},
                    {4: True, 5: True, 6: True},
                    {7: True, 8: True, 9: True},
                    {1: True, 4: True, 7: True},
                    {2: True, 5: True, 8: True},
                    {3: True, 6: True, 9: True},
                    {1: True, 5: True, 9: True},
                    {3: True, 5: True, 7: True})

    def fill_field(self, player):
        while True:
            try:
                slot = int(input(f'Player {player}. Enter your slot number: '))
                if 1 <= slot <= 9 and self.slots.get(slot) == '':
                    self.slots[slot] = player
                else:
                    print('Invalid slot index. Please enter a free slot with index 1-9:')
                    continue
            except ValueError:
                print('slot index should be number')
                continue
            else:
                break

    def check_winner(self, player):
        player_slots = {}
        for key, value in self.slots.items():
            if value == player:
                player_slots.update({key: bool(value)})
        for item in self.win:
            counter = 0
            for key, value in item.items():
                if value == player_slots.get(key):
                    counter += 1
                if counter == 3:
                    return True

    def draw_field(self):
        print(f'{self.slots[1].center(3)}|{self.slots[2].center(3)}|{self.slots[3].center(3)}')
        print('-' * 12)
        print(f'{self.slots[4].center(3)}|{self.slots[5].center(3)}|{self.slots[6].center(3)}')
        print('-' * 12)
        print(f'{self.slots[7].center(3)}|{self.slots[8].center(3)}|{self.slots[9].center(3)}')


game = Game()
game.draw_field()
game.fill_field('X')
game.draw_field()
turn = 8
final_msg = "It's a DRAW"
while turn > 0:
    game.fill_field('O')
    game.draw_field()
    if game.check_winner('O'):
        final_msg = 'O is WINNER'
        break
    turn -= 1
    game.fill_field('X')
    game.draw_field()
    if game.check_winner('X'):
        final_msg = 'X is WINNER'
        break
    turn -= 1
print(final_msg)
