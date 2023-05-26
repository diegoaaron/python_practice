# Escribir la identación utilizando 4 espacios y no un TAB (configurar TAB para que haga 4 espacios)
# Se debe utilizar 80 caracteres como máximo por linea (algunos utilizano 100 caracteres)
# Utilizar las lineas en blanco para facilitar la lectura de codigo
# Utilizar un espacio para realizar compraciones como IF AGE < 4: en vez de iF AGE<4:
# Las clases deben ser nombradas con el formato CamelCase
# Las instancias de clase y modulos deben nombrarse en minusculas y separadas por _



perry = "toffy"

print(perry)

def ladrar():
    pass

# parametro: elemento definido en una función, necesario para su funcionamiento

# argumento: valor pasado a una función cuando es invocada.

# Tipos de argumentos

# argumento posicional: es la configuración por defecto y consiste en pasar los argumentos en el orden en que sus parámetros están definidos.

def descripcion_mascota(raza, nombre):
    print("La mascota es: " + nombre)
    print("Es de raza: " + raza)

descripcion_mascota("pastor aleman", "toffy")

# argumento keywoard: Es cuando un argumento es pasado en el formato "parametro=arugmento", haciendo irrelevante el orden en que se definieron los parametros al crear la funcion. 

print("-----------------------1")

def des_mascota(raza, nombre):
    print("la mascota es " + nombre)
    print("es de raza " + raza)

des_mascota(nombre="toffina", raza="dogo")

