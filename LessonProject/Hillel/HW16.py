line_bytes = b'r\xc3\xa9sum\xc3\xa9'
print(line_bytes)
line_utf8 = line_bytes.decode()
print(line_utf8)
line_bytes_latin1 = line_utf8.encode('Latin1')
print(line_bytes_latin1)
line_latin1 = line_bytes_latin1.decode('Latin1')
print(line_latin1)
