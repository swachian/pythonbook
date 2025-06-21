import logging

while True:

    number1 = input("Please input number1: ")
    number2 = input("please input number2: ")

    try:
        number1 = float(number1)
        number2 = float(number2)
    except ValueError:
        # logging.exception("Failed to parse int")
        print(f"Your input is not a number, please check and input it again")
    else:
        print(f"{number1} + {number2} = {number1 + number2}")
            