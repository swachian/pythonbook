class Restaurant:

    def __init__(self, restaurant_type, cuisine_type):
        self.restaurant_type = restaurant_type
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.__login_attempts = 0

    def describe_restaurant(self):
        print(f"The restaurant is {self.restaurant_type} and {self.cuisine_type}")

    def open_restaurant(self):
        print("The restaurant is open")
    
    def reset_login_attempts(self):
        self.__login_attempts = 0
    
    def increment_login_attempts(self):
        self.__login_attempts += 1

my_restaurant = Restaurant("Mexico", "China")
print(my_restaurant.cuisine_type)
print(my_restaurant.restaurant_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_restaurant2 = Restaurant("curry", "USA")
my_restaurant3 = Restaurant("vegetables", "France")

my_restaurant2.describe_restaurant()
my_restaurant3.describe_restaurant()

my_restaurant3.number_served = 3
print(vars(my_restaurant3))

my_restaurant3.increment_login_attempts()
print(vars(my_restaurant3))
my_restaurant3.reset_login_attempts()
print(vars(my_restaurant3))
my_restaurant3.__login_attempts = 5
print(vars(my_restaurant3))

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_type, cuisine_type, flavors):
        super().__init__(restaurant_type, cuisine_type)
        self.flavors = flavors
    
    def set_flavors(self, flavors):
        self.flavors2 = flavors


iceCreamStand = IceCreamStand('ice', 'Italy', ['vanilla', 'strawberry'])
print(vars(iceCreamStand))
iceCreamStand.set_flavors(2)
print(vars(iceCreamStand))