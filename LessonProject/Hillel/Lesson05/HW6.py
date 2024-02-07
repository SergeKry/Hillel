num = int(input('Enter a positive number (Int): '))

iteration = 1
result1 = 0
while iteration <= num:
    if iteration % 3:
        result1 += iteration ** 3
    iteration += 1
print(f'result while: {result1}')

numbers = set(range(1, num + 1))
result2 = 0
for i in numbers:
    if i % 3:
        result2 += i**3
print(f'result for: {result2}')
