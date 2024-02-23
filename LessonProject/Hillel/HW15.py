def analysis(line):
    error = "Ви ввели неправильне число: {}"
    message = 'Ви ввели {} {} число: {}'
    text = line.replace(',', '.')
    alldigit_test = text.replace('.', '').replace('-', '')
    if not alldigit_test.isdigit() or text.count('.') > 1 or text.count('-') > 1:
        return error.format(line)
    sign = "від'ємне" if text[0] == '-' else "позитивне"
    if '.' in text:
        number_type = 'дробове'
        number = float(text)
    else:
        number_type = 'ціле'
        number = int(text)
    if number == 0:
        return message[0:11].format('нуль')
    else:
        return message.format(sign, number_type, number)


while True:
    line = input('Введіть число: ')
    if line.lower() in ('вихід', 'exit', 'quit', 'e', 'q'):
        break
    result = analysis(line)
    print(result)
