from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text().rstrip()
print(contents)

print('--------------')
pi_string = ''
for line in contents.splitlines():
    pi_string += line.lstrip()

print(pi_string)

path_million = Path('pi_million_digits.txt')
contents = path_million.read_text()
print(contents[0:52])

birth_day = input("Please input your birthday, in the form yymmdd: ")
if birth_day in contents:
    index = contents.find(birth_day)
    print(f"Your birthday appears in the first million digits of pi! The position is {index}.")
else:
    print("Not in")