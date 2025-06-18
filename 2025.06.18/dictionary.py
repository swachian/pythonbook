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
    'last_name': "Hanson",
    'age': 46,
    'city': "Cobenhagen"
    }

# print(person.items())
for key, value in person.items():
    print(f"{key} : {value}")