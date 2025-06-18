alien_color = 'red'

point = 0
if alien_color == 'green':
    point = 5
elif alien_color == 'yellow':
    point = 10
else:
    point = 15

print(f"You just earned {point} points")

age = 20
stage = ''
if age < 2:
    stage = 'baby'
elif age >= 2 and age <4:
    stage = 'toddler'
elif age >=4 and age < 13:
    stage = 'kid'
elif age >= 13 and age < 20:
    stage = 'teenager'
elif age >= 20 and age < 65:
    stage = 'adult'
elif age >= 65:
    stage = 'elder'

print(f"Your stage is {stage}")
