# pag 117

mensaje = input("Ingrese algun texto: ")
print(mensaje)

promt = "Dinos quien eres para personalizar tu mensaje."
promt += "\nCual es tu primero nombre: "

name = input(promt)
print("\nHola " + name + "!")

numero = input("ingrese un numero para ver si es impar: ")
numero = int(numero)

if numero % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")

# utilizando WHILE para recibir datos indefinidos

message = ""

prompt = "Indicanos algo a repetir: "
prompt += "\nIngresesa 'quit' para salir del programa: "

while message != 'quit':
    message = input(prompt)
    print(message)

# utilizando BREAK y WHILE para recibir datos indefinidos

message = ""

prompt = "Indicanos algo a repetir: "
prompt += "\nIngresesa 'quit' para salir del programa: "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("lo ingresado es: " + city)

# Llenando un diccionario utilizando WHILE
respuestas = {}
polling_active = True

while polling_active:
    nombre = input("Ingrese el nombre: ")
    apellido = input("\nAhora ingrese su apellido: ")
    respuestas[nombre] = apellido

    continuar = input("Desea seguir ingresando valores: SI/NO")
    if continuar in ("no","NO","No","nO"):
        polling_active = False
    
print("La lista final es: ")
print(respuestas)
