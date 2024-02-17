inputdata = ('Країна', 'шалаш', 'Летел', 'вертольот', 'УЧУ', 'мем', 'мова')
palindrome = 'Країна'[::-1]

outputdata = tuple(filter(lambda x: x.lower() == x.lower()[::-1], inputdata))
print(outputdata)