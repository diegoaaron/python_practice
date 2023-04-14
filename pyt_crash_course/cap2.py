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

# pag 44