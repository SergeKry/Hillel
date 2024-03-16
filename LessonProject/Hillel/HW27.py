def geometric_progression(start, denominator, steps=6):
    counter = steps
    if start == 0 or denominator == 0:
        yield 'start and denominator cannot be zero'
        counter = 0
    while counter > 0:
        if counter == steps:
            yield start
            counter -= 1
        else:
            result = start * denominator
            yield result
            counter -= 1
            start = result


progression = []
for number in geometric_progression(-2, -5):
    progression.append(number)
print(progression)

progression = []
for number in geometric_progression(10, 3):
    progression.append(number)
print(progression)
