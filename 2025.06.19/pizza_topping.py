prompt_message = "Please enter the topping you want. "

active = True
while active:
    topping = input(prompt_message)
    if topping == 'quit':
        active = False
    else:
        print(f"{topping.title()} topping wil be added to your pizza.")