import pizza
import pizza as p
from pizza import make_pizza 
from pizza import make_pizza as mp

pizza.make_pizza(name = 'peperoni')
make_pizza(name = 'peperoni2')
mp(name = 'peperoni3')
p.make_pizza(name = "peperoni4")

# pizza.make_pizza('mushrooms', 'green peppers', 'extra cheese')
