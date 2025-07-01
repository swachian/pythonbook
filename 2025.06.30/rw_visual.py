import matplotlib.pyplot as plt

from random_walk import RandomWalk

rw = RandomWalk(5_000)
rw.fill_walk()

plt.style.use('classic')
fig, ax = plt.subplots(figsize=(15, 9))
point_numbers = range(rw.num_points)
ax.plot(rw.x_values, rw.y_values, linewidth=3)
# ax.scatter(rw.x_values, rw.y_values, s=1, c=point_numbers, cmap=plt.cm.Greens, edgecolors='none')
ax.scatter(rw.x_values[-1], rw.y_values[-1], s=15, c='red', edgecolors='none')
ax.scatter(rw.x_values[0], rw.y_values[0], s=15, c='blue', edgecolors='none')

ax.set_aspect('equal')
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()