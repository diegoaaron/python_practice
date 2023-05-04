import pygal
from die import Die

die_1 = Die()
die_2 = Die()

results = []

for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analizando resultados
frecuencies = []
max_result = die_1.num_sides + die_2.num_sides

for value in range(2, max_result + 1):
    frecuency = results.count(value)
    frecuencies.append(frecuency)

hist = pygal.Bar()

hist._title = "Resultados de los datos"
hist.x_labels = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
hist._x_title = "resultado"
hist._y_title = "Frecuencia del resultado"

hist.add('D6 + D6', frecuencies)
hist.render_to_file('dice_visual.svg')