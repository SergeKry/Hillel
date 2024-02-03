while True:
    name = input("What's your name? ")
    age = input("What's your age? ")
    if not age.isdigit() or int(age) == 0:
        print("Помилка, повторіть введення")
    elif int(age) < 10:
        print(f'Привіт, шкет {name.capitalize()}')
    elif int(age) <= 18:
        print(f'Як справи, {name.capitalize()}?')
    elif int(age) < 100:
        print(f'Що бажаєте, {name.capitalize()}')
    else:
        print(f'{name.capitalize()}, ви брешете - у наш час стільки не живуть...')
    want_proceed = input('Бажаєте вийти? (Д/Y): ')
    if want_proceed.upper() in ('Y', 'Д'):
        break
