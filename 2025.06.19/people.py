people = []

# Define some people, and add them to the list.
person = {
    'first_name': 'eric',
    'last_name': 'matthes',
    'age': 46,
    'city': 'sitka',
    }
people.append(person)

person = {
    'first_name': 'lemmy',
    'last_name': 'matthes',
    'age': 2,
    'city': 'sitka',
    }
people.append(person)

person = {
    'first_name': 'willie',
    'last_name': 'matthes',
    'age': 11,
    'city': 'sitka',
    }
people.append(person)

for person in people:
    print(f"name is {person['first_name']} {person['last_name']}, of {person['city']}, is {person['age']} years old.")

favorite_places = {
    "Luo": ["hongkong", "shanghai", "zhangjiang"],
    "Ma": ["putuo", "hongkou", "yangpu"],
    "Hu": ["pudong", "yangpu"]
    }

for name, places in favorite_places.items():
    print(f"{name}'s favorite places are:")
    for place in places:
        print(f'- {place}')

favorite_numbers = {
    "Luo": [111, 222, 333],
    "Ma": [555, 88],
    "Hu": [3]
    }
for name, numbers in favorite_numbers.items():
    print(f"{name}'s favorite numbers are:")
    for number in numbers:
        print(f'- {number}')