import matplotlib.pyplot as plt

input_values = [i for i in range(1, 8)]
squares = [i**2 for i in range(1, 8)]

plt.style.use("Solarize_Light2")

fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square", fontsize=14)

ax.tick_params(labelsize=14)



plt.show()