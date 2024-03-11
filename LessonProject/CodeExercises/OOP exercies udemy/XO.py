class Game:
    def __init__(self):
        self.slots_x = ['', '', '', '', '', '', '', '', '']
        self.slots_o = ['', '', '', '', '', '', '', '', '']
        self.win = ([True, True, True, False, False, False, False, False, False],
                    [False, False, False, True, True, True, False, False, False],
                    [False, False, False, False, False, False, True, True, True],
                    [True, False, False, True, False, False, True, False, False],
                    [False, True, False, False, True, False, False, True, False],
                    [False, False, True, False, False, True, False, False, True],
                    [True, False, False, False, True, False, False, False, True],
                    [False, False, True, False, True, False, True, False, False])

    def fill_field_x(self):
        while True:
            try:
                slot = int(input('Player X. Enter your slot number: ')) - 1
                if 0 <= slot <= 8 and self.slots_x[slot] == '' and self.slots_o[slot] == '':
                    self.slots_x[slot] = 'X'
                else:
                    print('Invalid slot index. Please enter a free slot with index 1-9:')
                    continue
            except ValueError:
                print('slot index should be number')
                continue
            else:
                break

    def fill_field_o(self):
        while True:
            try:
                slot = int(input('Player O. Enter your slot number: ')) - 1
                if 0 <= slot <= 8 and self.slots_x[slot] == '' and self.slots_o[slot] == '':
                    self.slots_o[slot] = 'O'
                else:
                    print('Invalid slot index. Please enter a free slot with index 1-9:')
                    continue
            except ValueError:
                print('slot index should be number')
                continue
            else:
                break

    def check_winner_x(self):
        player_slots = [bool(item) for item in self.slots_x]
        if player_slots in self.win:
            return True

    def check_winner_o(self):
        player_slots = [bool(item) for item in self.slots_o]
        if player_slots in self.win:
            return True

    def draw_field(self):
        field = self.slots_x[:]
        for index, value in enumerate(field):
            if value == '':
                field[index] = self.slots_o[index]
        print(f'{field[0].center(3)}|{field[1].center(3)}|{field[2].center(3)}')
        print('-' * 12)
        print(f'{field[3].center(3)}|{field[4].center(3)}|{field[5].center(3)}')
        print('-' * 12)
        print(f'{field[6].center(3)}|{field[7].center(3)}|{field[8].center(3)}')


game = Game()
game.draw_field()
while True:
    game.fill_field_x()
    game.draw_field()
    print([bool(item) for item in game.slots_x])
    if game.check_winner_x():
        print('X is WINNER')
        break
    game.fill_field_o()
    game.draw_field()
    if game.check_winner_o():
        print('O is WINNER')
