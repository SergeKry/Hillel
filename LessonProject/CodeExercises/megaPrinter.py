print('Mega Printer')
zero = ['  ***  ',
        ' *   * ',
        '*     *',
        '*     *',
        '*     *',
        ' *   * ',
        '  ***  ']
one = ['  *  ',
       ' **  ',
       '* *  ',
       '  *  ',
       '  *  ',
       '  *  ',
       '*****']
two = ['  ***  ',
       '*     *',
       '*     *',
       '     * ',
       '   *   ',
       '*      ',
       '*******']
three = ['  **** ',
         ' *    *',
         '      *',
         ' ***** ',
         '      *',
         '*     *',
         '  ***  ']
four = ['      *',
        '    * *',
        '  *   *',
        '*******',
        '      *',
        '      *',
        '      *']
five = ['*******',
        '*      ',
        '*      ',
        ' ***** ',
        '      *',
        '*     *',
        ' ***** ']
six = [' ***** ',
       '*     *',
       '*      ',
       '****** ',
       '*     *',
       '*     *',
       ' ***** ']
seven = ['*******',
         '      *',
         '     * ',
         '    *  ',
         '   *   ',
         '  *    ',
         ' *     ']
eight = ['  ****  ',
         ' *    * ',
         ' *    * ',
         '  ****  ',
         '*      *',
         '*      *',
         ' ****** ']
nine = ['  ***** ',
        '*      *',
        '*      *',
        ' *******',
        '       *',
        '*      *',
        ' ****** ']

number = input('Enter your number: ')
numbers_dict = {0: zero, 1: one, 2: two, 3: three, 4: four, 5: five, 6: six, 7: seven, 8: eight, 9: nine}


def get_input(userinput):
    userlist = [numbers_dict.get(k) for k in [int(i) for i in userinput]]
    return userlist


list_numbers = get_input(number)


def draw_line(linecount):
    line = ''
    for digit in list_numbers:
        line += f'{digit[linecount]}  '
    return print(line)


line_count = 0
while line_count < 7:
    draw_line(line_count)
    line_count += 1
