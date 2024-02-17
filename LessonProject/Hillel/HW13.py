import functools
from datetime import datetime


def time_measure(func):
    def wrapper():
        now = datetime.now()
        func()
        print(f'measured time: {datetime.now() - now}\n')
    return wrapper


@time_measure
def iterations_with_loop():
    numbers = range(1, test_number + 1)
    result = 0
    for i in numbers:
        if i % 3:
            result += i ** 3
    print(f'{result} loop')


@time_measure
def iterations_with_reduce():
    numbers = range(1, test_number + 1)
    result = functools.reduce(lambda a, b: a + b**3 if b % 3 else a + 0, numbers, 0)
    print(f'{result} reduce')


test_number = 5555555

iterations_with_loop()
iterations_with_reduce()
