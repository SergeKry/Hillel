import random


def random_list(size=200, a=1, b=10):
    _list = []
    for i in range(0, size):
        n = random.randint(a, b)
        _list.append(n)
    return _list


def count_numbers(lst):
    result = {i: lst.count(i) for i in lst}
    return dict(sorted(result.items()))


def output(calc):
    for k, v in calc.items():
        times = (lambda x: times_dict[x % 10])(v) if v not in (11, 12, 13, 14) else 'разів'
        print(f'Число {k} зустрічається у первісному списку {v} {times}')


times_dict = {0: 'разів', 1: 'раз', 2: 'рази', 3: 'рази', 4: 'рази', 5: 'разів', 6: 'разів', 7: 'разів', 8: 'разів',
              9: 'разів', }
data = random_list()
print(f'Сгенеровані 200 айтемів: {data}\n')
calculation = count_numbers(data)
print(f'Підрахунок у словнику: {calculation}', end='\n\n')
output(calculation)
