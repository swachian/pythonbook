from car import Car

class Battery:
    def __init__(self, battery_size = 40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.") 

    def upgrade_battery(self):
        self.battery_size = 65

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.x = '0'
        self.battery = Battery()

    def describe_battery(self):
        self.battery.describe_battery()
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model} {self.battery}"
        return long_name.title()
    
    def getRange(self):
        self.battery.get_range()

    def upgrade_battery(self):
        self.battery.upgrade_battery()


