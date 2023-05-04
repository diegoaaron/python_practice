from die import Die

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

print(frecuencies)