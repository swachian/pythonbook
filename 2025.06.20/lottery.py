from random import choice
chars = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f')


class Lottery:

    def __init__(self, right_one):
        self.right_one = right_one

    def roll_until_mathch(self):
        attempts = 1
        while tuple(self.roll()) != tuple(self.right_one):
            attempts += 1
        return attempts

    def roll(self):
        willing_ticket = []

        while len(willing_ticket) < 4:
            ch = choice(chars)
            if ch in willing_ticket:
                continue
            else:
                willing_ticket.append(ch)

        return willing_ticket


lottery = Lottery((1, 2, 3, 'e'))
print(lottery.roll_until_mathch())