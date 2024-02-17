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
    input_listed = [int(i) for i in userinput]
    userlist = []
    for item in input_listed:
        drawing_modified = [i.replace('*', f'{item}') for i in numbers_dict[item]]
        userlist.append(drawing_modified)
    return userlist


def draw_line(linecount):
    line = ''
    for digit in list_numbers:
        line += f'{digit[linecount]}  '
    return print(line)


list_numbers = get_input(number)
line_count = 0
while line_count < 7:
    draw_line(line_count)
    line_count += 1
