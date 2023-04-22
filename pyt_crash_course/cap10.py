# formateando ruta para windows con doble \

full_path = "C:\\Users\\Administrador\\Documents\\python\\python_practice\\pyt_crash_course\\pi_digits.txt"

# la palabra reservada WITH permite manejar streams de datos y evitar excepciones

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())


with open(full_path) as file_object2:
    contents = file_object2.read()
    print(contents.rstrip())