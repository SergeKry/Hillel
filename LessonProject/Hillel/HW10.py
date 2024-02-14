number = 3

result = (lambda x, func: 'нуль' if x == 0 else func(x))(number, lambda x: 'парне' if x % 2 == 0 else 'не парне')
print(result)
