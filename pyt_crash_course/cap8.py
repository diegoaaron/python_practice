# parametro: denominacion que la funcion necesita para trabajar internamente
# argumento: elemento que es pasado a una funcion cuando se la llama.

# funcion con parametros

def greet_user(username):
    print("Hola, " + username.title() + "!")

greet_user("jordan")

# Tipos de argumentos
# Argumentos posicionales: Es cuando los argumentos pasados a una funcion son asociados con los 
# parametros en base al orden de los argumentos. Se debe respetar el orden de los parametros

def descripcion_mascota(raza, nombre):
    print("Mi mascota " + nombre)
    print("es de raza " + raza)

descripcion_mascota("pastor aleman", "toffy")

# Argumentos keyword: Es cuando los argumentos son enviados en la forma nombre-valor. El orden
# ahora puede ser irrelevante

def descripcion_mascota2(raza, nombre):
    print("Mi mascota " + nombre)
    print("es de raza " + raza)

descripcion_mascota2(nombre="sparky",raza="jack russel terrier")

# Valor por defecto: Al crear un funcion se pueden definir valores por defecto para cada parametro.
# Si al llamar a la funcion un argumento no es pasado para la funcion, se utiliza el valor por defecto
# definido para el parametro. los parametros con valor por defecto deben ir al final.

def descripcion_mascota3(nombre,raza="pequines"):
    print("Mi mascota " + nombre)
    print("es de raza " + raza)

descripcion_mascota3(nombre="sparky")
descripcion_mascota3(nombre="sparky",raza="jack russel terrier")

# RETURN: permite devolver eun valor despues de ejecutar la funcion, es vez de inprimir directamente
# el resulto

def get_nombre_formateado(first_name, last_name, middle_name=""):
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name

    return full_name

nombre_completo = get_nombre_formateado("jimi", "hendrix")
print(nombre_completo)



