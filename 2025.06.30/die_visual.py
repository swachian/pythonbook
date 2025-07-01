from die import Die
import plotly.express as px
from functools import reduce

class Dies:
    def __init__(self):
        self.dies = []
        self.results = []
    
    def add_dice(self, num):
        die = Die(num)
        self.dies.append(die)

    def roll(self):
        self.results = [reduce(lambda acc, die: acc * die.roll() , self.dies, 1) for roll_num in range(10_00)]

    def max_results(self):
        return reduce(lambda acc, die: acc * die.num_sides, self.dies, 1)
    
    def poss_results(self):
        return range(1, self.max_results() + 1)

    def frequencies(self):
        return [self.results.count(value) for value in self.poss_results()]

dies = Dies()
dies.add_dice(6)
dies.add_dice(6)

dies.roll()

title = "Results of Rolling a D6 and a D10 50,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=dies.poss_results(), y=dies.frequencies(), title=title, labels=labels)

fig.update_layout(xaxis_dtick=1)
fig.show()

# print(frequencies)

fig.write_html('dice_visual_d6d10.html')