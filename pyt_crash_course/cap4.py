magicians = ['alice', 'david', 'carolina']

for mago in magicians:
    print(mago.title() + ", fue un gran mago")
    print("No puedo esperar nuevos trucos del " + mago.title() + "\n")


pizza = ["a", "b", "c"]

for pi in pizza:
    print("La pizza " + pi.upper() + " es deliciosa")
print("Las pizzas son deliciosas")

print("listas numericas")

list_numero = list(range(1,10))
print(list_numero)

for value in range(1,5):
    print(value)

cuadrados = []

for n in range(1,11):
    cuadrados.append(n**2)

print(cuadrados)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print("el minimo valor es: " + str(min(digits)))

print("el maximo valor es: " + str(max(digits)))

print("la suma de valores es: " + str(sum(digits)))

# List Comprehension
cuadrados2 = [value**2 for value in range(10,21) if value % 2 == 0]

print(cuadrados2)

# Slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("de 0 a 3")
print(players[0:3])

print("de 2 hasta el final")
print(players[2:])
print(players[-3:])

for n in players[2:]:
    print(n.title())

