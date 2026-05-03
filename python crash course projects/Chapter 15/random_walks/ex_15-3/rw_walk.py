import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10,10))
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, linewidth=1)
    ax.set_aspect('equal')

    ax.scatter(0, 0, c='green', edgecolors='none', s=100) # Starting point
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100) # Ending point

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Stay running? [Y/n] ")
    if keep_running == 'n':
        break
