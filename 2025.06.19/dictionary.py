alien_0 = {
    'color': 'green', 
    'points': 5
    }
new_points = alien_0['points']
print(f"You just earned {new_points} points!")
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

del alien_0['color']
print(alien_0)

person = {
    'first_name': "David",
    'last_name': "David",
    'age': 46,
    'city': "Cobenhagen"
    }

# print(person.items())
for key, value in person.items():
    print(f"{key} : {value}")

for value in person.values():
    print(f"{value}")

for value in set(person.values()):
    print(f"{value}")

rivers = {'nile': 'egypt', 'yellow river': 'china', 'Thawus': 'england'}
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")
for river in rivers.keys():
    print(f"The {river.title()}") 
for country in rivers.values():
    print(f"The {country.title()}") 

countries = {'china', 'american', 'egypt'}
values = rivers.values()
for country in countries:
    if country in values:
        print(f"{country.title()} has been filled")
    else:
        print(f"please try to learn rivers info of {country.title()}")

aliens = []
for alien_number in range(30):
    new_alien = {'id': alien_number, 'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print('...')
print(f'Total number of aliens: {len(aliens)}')