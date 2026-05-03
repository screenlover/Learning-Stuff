import plotly.express as px
from random_walk import RandomWalk


rw = RandomWalk(50000)
rw.fill_walk()

ax = px.scatter(rw.x_values, rw.y_values)


ax.show()




