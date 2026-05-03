import matplotlib.pyplot as plt

my_nums = [x for x in range(1, 5001)]
my_cubes = [x**3 for x in my_nums]

fig, ax = plt.subplots()

ax.plot(my_nums, my_cubes)

plt.show()