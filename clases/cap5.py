# condicional if 
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if (car == "bmw"):
        print(car.upper())
    else:
        print(car.title())

# la condicional if diferencia entre mayusculas y minusuclas

auto = "Audi"

if ("audi" == auto):
    print("son inguales")
else:
    print("son diferentes")

if ("audi" == auto.lower()):
    print("son iguales")
else:
    print("son diferentes")

# usando not

n = 30

if n != 31:
    print("es difeferente de 30")
else:
    print("es igual a 30")

# usando and

a = 50
b = "l"

if a == 50 and b != "a":
    print("a y b cumplieron la condicion")

# validando valores en una lista

banned_users = ['andrew', 'carolina', 'david']
usuario = "marie"

if usuario in banned_users:
    print("usted esta baneado")

if usuario not in banned_users:
    print("usted no esta baneado")

# Ejercicios

car = "honda"
print("es car == honda? yo digo que si")
if car == "honda":
    print("el carro si es honda")


# EL-IF

age = 12

if a < 4:
    print("El numero es menor a 4")
elif a < 19:
    print("El numero es menor a 19 pero mayor o igual a 4")
else:
    print("El numero es mayor o igual a 19")


# conbinando FOR IN con IF 

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_toppings in requested_toppings:
    if requested_toppings == "green peppers":
        print("Disculpa, no tnenemos pepinillos, ahora")
    else:
        print("agregando" + requested_toppings + ".")

print("\npizza terminada!")