# 2025.06.17 To practise string operations
name = '\nEric  \n\n'
helloStr = f"Hello {name}, would you like to learn some Python today?"
print(helloStr)

print(f"{name.lower()}")
print(f"{name.upper()}")
print(f"{name.title()}")

print('Albert Einstein once said, "A person who never made a mistake never tried' \
' anything new"')

quote = f'{name} once said, "A person who never made a mistake never tried' \
' anything new"'
print(quote)

quote = f'{name.lstrip()} once said, "A person who never made a mistake never tried' \
' anything new"'
print(quote)

quote = f'{name.strip()} once said, "A person who never made a mistake never tried' \
' anything new"'
print(quote)

file_name = 'python_notes.txt'
print(f"{file_name.removesuffix('.txt')}")