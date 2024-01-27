users_text = input('Enter your text here: ')
text_modified1 = users_text[1::2]
text_modified2 = users_text[::-1].upper()
print(f'Original text: {users_text}')
print(text_modified1)
print(text_modified2)
