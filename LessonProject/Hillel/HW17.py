a = 'First line'
b = 'Second line'
c = 'Third line'
d = 'Fourth line'
with open('homework.txt', mode='w', encoding='utf-8') as file:
    file.write(a + '\n')
    file.write(b + '\n')
with open('homework.txt', mode='a', encoding='utf-8') as file:
    file.write(c + '\n')
    file.write(d + '\n')
