cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car.lower() == 'bmw':
        print(car.upper())
    else:
        print(car.title())  

car = 'audi'
if car in cars:
    print(f"{car} in cars")
else:
    print(f"{car} not in cars")

  

for ecar in cars:
    print(f"Is car == {ecar}: {car == ecar}")

print(f"Is {car} in cars: {car in cars}")
print(f"Is {car} not in cars: {car not in cars}")