# formateando ruta para windows con doble \

full_path = "C:\\Users\\Administrador\\Documents\\python\\python_practice\\pyt_crash_course\\pi_digits.txt"

# la palabra reservada WITH permite manejar streams de datos y evitar excepciones

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

print("--------------------------------------")
with open(full_path) as file_object2:
    contents = file_object2.read()
    print(contents.rstrip())

# se puede recorrer linea por linea 

filename = 'pi_digits.txt'

print("--------------------------------------")
with open(filename) as file_object:
    for line in file_object:
        print(line)

# obteniendo una lista de los elementos leidos

print("--------------------------------------")
with open(filename) as file_object:
    lines = file_object.readlines()
    print(lines)


# escribiendo en un archivo

filename = "programing.txt"

print("--------------------------------------")
with open(filename, "w") as fileobject:
    fileobject.write("I love programing\n")
    fileobject.write("I love dota")

print("--------------------------------------")
with open(filename) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# utilizando ecepciones para controlar los errores 

print("--------------------------------------")
try:
    print(5/0)
except ZeroDivisionError:
    print("no dividir x cero")

print("--------------------------------------")
print("ingrese 2 numeros para dividirlos entre si")
print("ingreses 'q' para salir")

while True:
    first_number = input("\nprimer numero: ")
    if first_number == "q":
        break
    second_number = input("\nsegundo numero: ")
    if second_number == "q":
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("no puede dividir entre cero")
    else:
        print(answer)

print("--------------------------------------")
filename = "alice.txt"

try:

    with open(filename) as f_obj:
        contents = f_obj.read()
        print(contents)
except FileNotFoundError:
    print("no se encontro el archivo...")

