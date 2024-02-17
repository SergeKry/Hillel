values = [1, 2, '3', 'forth', 'end', 99, True, None]

modified_values = list(map(lambda x: str(x) if isinstance(x, int) and not isinstance(x, bool) else x, values))
print(modified_values)
