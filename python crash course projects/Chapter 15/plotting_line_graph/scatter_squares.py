import matplotlib.pyplot as plt

x_values = [(i) for i in range(1,1001)]
y_values = [(i)**2 for i in x_values]

plt.style.use("Solarize_Light2")

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues) # sets dots where x=x_values and y=y_values; sets a colormap using y as a reference


ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square", fontsize=14)

ax.tick_params(labelsize=14)

ax.axis([0, 1100, 0, 1100000])
ax.ticklabel_format(style='plain')

plt.savefig('/home/fromtheabyss/Área de trabalho/Documents/computacao/' \
'Análise de Sistemas/Algoritmos e Lógica de Programação/Python/Python Crash ' \
'Course 3rd ed/Chapters 15/plotting_line_graph/myfig.png') # Saves an image of the figure in the given directory

plt.show()