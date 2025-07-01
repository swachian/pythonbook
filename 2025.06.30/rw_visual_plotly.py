import plotly.express as px

from random_walk import RandomWalk

rw = RandomWalk(5_000)
rw.fill_walk()

title = "Results of Rolling a D6 and a D10 50,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=rw.x_values, y=rw.y_values, title=title, labels=labels)

fig.update_layout(xaxis_dtick=1)



fig.show()