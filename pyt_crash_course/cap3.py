# definiendo variables

print("Hello Python world!")

message = "Hello Python CRASH world!"
print(message)

name = "ADA lovelace"
print(name.title())

print(name.upper())

print(name.lower())

first_name = "ada"
last_name = "lovelace"

full_name = first_name + " " + last_name

print(full_name.title())

print("Hello " + full_name.upper() + "!")


print("\t tabulacion")
print("\n saldo de linea \"")
print()

full_st = " pythonn   "

sd = full_st.rstrip()

print("1" + sd + "2")

age = 23

message2 = "feliz " + str(age) + " cumpleaños"

print(message2)

# import this


bicicletas = ["a", "b", "c"]

print(bicicletas[-1])


print(bicicletas[0].title())

bicicletas[0] = "d"

print(bicicletas)

bicicletas.append("f")

print(bicicletas)

bicicletas.insert(1, "x")

print(bicicletas)

del bicicletas[0]

print(bicicletas)

print(bicicletas.pop())

final = bicicletas.pop()

print("sale: " + final + " queda: " + str(bicicletas))

xd = str(bicicletas)

print(xd[0])

bicicletas = ['honda', 'yamaha', 'suzuki']

first_owned = bicicletas.pop(-1)

print("mi primera bicicleta fue:" + first_owned + " !")

bicicletas.remove('honda')

print(bicicletas)

# Ejercicios

invitados = ["Erenesto", "Carlos", "Eva"]

print("Vienes a cenar " + invitados[0] + " es hoy a las 8 p.m.")
print("Vienes a cenar " + invitados[1] + " es hoy a las 8 p.m.")
print("Vienes a cenar " + invitados[2] + " es hoy a las 8 p.m.")

print("")
print("Lamentablemente " + invitados[1] + " no podra asistir")

del invitados[1]

invitados.insert(1,"Pamela")

print("")
print("Vienes a cenar " + invitados[1] + " es hoy a las 8 p.m.")

invitados.insert(0,"Camilo")
invitados.insert(2,"Pablo")
invitados.append("Karla")

invitado_retirado = invitados.pop()

print("Lo siento " + invitado_retirado + " la cena se cancelo")

invitado_retirado = invitados.pop()

print("Lo siento " + invitado_retirado + " la cena se cancelo")

invitado_retirado = invitados.pop()

print("Lo siento " + invitado_retirado + " la cena se cancelo")

invitado_retirado = invitados.pop()

print("Lo siento " + invitado_retirado + " la cena se cancelo")

del invitados[-1]
del invitados[-1]

print("")
print(str(invitados))


cars = ['bmw', 'audi', 'toyota', 'subaru']

cars.sort()

print(cars)

cars.sort(reverse=True)

print(cars)

print(sorted(cars))

print("el tamaño de la lista es: " + str(len(cars)))
print("------------------------")

# Ejercicio

lugares = ["belgica", "uk", "alemania", "finlandia", "rusia"]

print(lugares)

print("lista ordenada: " + str(sorted(lugares)))
print("lista original: " + str(lugares))

print("------------------------")
print("lista ordenada: " + str(sorted(lugares, reverse=True)))
print("lista original: " + str(lugares))

print("------------------------")
lugares.reverse()
print("lista en reversa: " + str(lugares))

print("------------------------")
lugares.reverse()
print("lista en reversa: " + str(lugares))

print("------------------------")
lugares.sort()
print("lista en orden alfabetico: " + str(lugares))

print("------------------------")
lugares.sort(reverse=True)
print("lista en orden alfabetico invertido: " + str(lugares))