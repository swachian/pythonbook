from pathlib import Path
import json

def get_user_input():
    number = input("Please tell me your favorite number: ")
    path = Path('favorite_number.txt')
    path.write_text(json.dumps(number))
    return number

def get_stored_number():
    path = Path('favorite_number.txt')
    if path.exists():
        number = json.loads(path.read_text())
        return number
    else:
        return None


def greet_user():
    favorite_number = get_stored_number()
    if not favorite_number:
        favorite_number = get_user_input()

    print(f"Welcome back, your favorite number is: {favorite_number}")
    
greet_user()