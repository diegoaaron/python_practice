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

