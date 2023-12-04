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

# copiando una lista (se utilza slicing)

my_foods = ['pizza', 'falafel', 'carrot cake']

friend_foods = my_foods[:]

my_foods.append("ceviche")
friend_foods.append("caldo de gallina")

print(my_foods)
print(friend_foods)

# si utilizamos "=" se enlace la nueva variable al espacio de memoria donde ya eta la lista
# lo cual no genera una copia.

mis_vocales = ["a","e","i"]
las_vocales = mis_vocales;

las_vocales.append("u")

print(mis_vocales)
print(las_vocales)

print("-----------------Ejercicio 1-----------------")

numeritos = [n**2 for n in range(1,200) if n%14 == 0]
print(numeritos)

print("los primeros 3 numeros de la lista son: " + str(numeritos[:3]))

a1 = int(((len(numeritos))/2)-1)
a2 = int(((len(numeritos))/2)+2)

print("los 3 numeros del medio son: " + str(numeritos[a1:a2]))
print("los 3 ultimos numeros son: " + str(numeritos[-3:]))

print("-----------------Ejercicio 2-----------------")

las_comidas = ['pizza', 'falafel', 'carrot cake']
mis_comidas = las_comidas[:]

las_comidas.append("langosta")
mis_comidas.append("escaveche")

print(las_comidas)
print(mis_comidas)

print("Mis comidas favortias son: ")

for comida in mis_comidas:
    print("* " + comida)

print("La comida favorita de mis amigos son: ")

for comida in las_comidas:
    print("* " + comida)

# tuplas

dimensiones = (200,50)
print(dimensiones[0])
print(dimensiones[1])

for x in dimensiones:
    print(x)

# se puede sobreescribir toda una tupla

dimensiones = (222,333,444)
print("\n imprimiendo toda una nueva tupla")
for n in dimensiones:
    print(n)

comidas = ("arroz", "huevo", "fideos", "algas")

for comida in comidas:
    print("La comida es: " + comida)

comidas = ("a", "b", "c")

for x in comidas:
    print("la comida es: " + x)

