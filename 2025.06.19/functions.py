def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello {username}!")

greet_user('Danny')
greet_user('Jesse')

def display_messages():
    message = "I learn how to write a funcion in python and the difference between arguments and parameters."
    print(message)

display_messages()

def favorite_book(book):
    print(f"One of my favorite books is {book}.")

books = ['Unit Testing', 'DDD', 'Refactory', 'Enterprise patterns']
for book in books:
    favorite_book(book=book)

def test_fun_params(a ='a', b="cc"):
    print(f"{a} - {b}")

test_fun_params("cc")

def make_shirt(size = 'large', message = 'I love python'):
    print(f"Shirt size is {size} and text on it is {message}")

make_shirt('medium', "I love ruby")

make_shirt(size = 'small', message = 'I love java as well')

make_shirt()
make_shirt('medium')
make_shirt('small', 'I love c#')