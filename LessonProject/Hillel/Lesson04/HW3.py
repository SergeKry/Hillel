users_text = input('Enter two words here: ')
part1 = users_text.split(' ')[0]
part2 = users_text.split(' ')[1]
text1 = '!%s %s?' % (part2.upper(), part1.capitalize())
text2 = '!{1} {0}?'.format(part1.capitalize(), part2.upper())
text3 = f'!{part2.upper()} {part1.capitalize()}?'
print(users_text, text1, text2, text3, sep='<<<>>>')

# writing to a file
with open('hw4_output.txt', mode='w') as file:
    file.write('<<<>>>'.join([users_text, text1, text2, text3]))

