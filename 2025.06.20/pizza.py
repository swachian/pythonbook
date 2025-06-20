def make_pizza(**toppings):
    print(type(toppings))
    for topping, value in toppings.items():
        print(topping, value)