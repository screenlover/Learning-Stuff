from die import Die
import plotly.express as px

# d6
d6 = Die()
# d20
d20 = Die(20)

title = "Results of Rolling a pair of D6 and D20 1000 times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}

results = []
for roll in range(1000):
    result = (d6.roll(), d20.roll(),)
    results.append(result)
    
frequencies = []
poss_results = range(1, max([d6.num_sides, d20.num_sides])+1)
for value in poss_results:
    frequency = 0
    for i in results:
        frequency += i.count(value)
    frequencies.append(frequency)

fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# fig.write_html('/home/fromtheabyss/Área de trabalho/Documents/computacao/Análise de Sistemas/Algoritmos e Lógica de Programação/Python/Python Crash Course 3rd ed/Chapters 15/rolling_dice/dice_visual_d6d20.html')
fig.show()