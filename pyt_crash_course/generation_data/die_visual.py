from die import Die
import pygal

die = Die()

results = []

for roll_num in range(100):
    result = die.roll()
    results.append(result)

# Analizando resultados
frecuencies = []

for value in range(1, die.num_sides + 1):
    frecuency = results.count(value)
    frecuencies.append(frecuency)

# Mostrando resultados

hist = pygal.Bar()

hist._title = "Resultados de datos"
hist.x_labels = ["1", "2", "3", "4", "5", "6"]
hist._x_title = "Resultado"
hist._y_title = "Frecuencia del resultado"

hist.add('D6', frecuencies)
hist.render_to_file('die_visual.svg')
