from random import randint, choice

class Die:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return randint(1, self.sides)

die6 = Die(6)
die10 = Die(10)
die20 = Die(20)

for die in [die6, die10, die20]:
    print(f"\nStart to roll {die.sides}-side die for 10 times")
    for i in range(10):
        print(die.roll())

