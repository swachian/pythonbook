from pathlib import Path


path = Path('programming.txt')
path.write_text("I love programming." + str(5))

contents = ""
while True:
    name = input("please enter your name: ")
    if name == 'quit':
        break
    contents += name + "\n"
    

path = Path('guest.txt')
path.write_text(contents)


