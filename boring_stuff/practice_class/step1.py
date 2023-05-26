# Escribir la identación utilizando 4 espacios y no un TAB (configurar TAB para que haga 4 espacios)
# Se debe utilizar 80 caracteres como máximo por linea (algunos utilizano 100 caracteres)
# Utilizar las lineas en blanco para facilitar la lectura de codigo
# Utilizar un espacio para realizar compraciones como IF AGE < 4: en vez de iF AGE<4:
# Las clases deben ser nombradas con el formato CamelCase
# Las instancias de clase y modulos deben nombrarse en minusculas y separadas por _

# variable: forma más básica de almacenar información
# pass: palabra reservada que funciona como relleno de codigo

perry = "toffy"

print(perry)

def ladrar():
    pass

# parametro: elemento definido en una función, necesario para su funcionamiento

# argumento: valor pasado a una función cuando es invocada.

# Tipos de configuración para los argumentos 

# argumento posicional: es la configuración por defecto y consiste en pasar los argumentos en el orden en que sus parámetros 
# están definidos.

def descripcion_mascota(raza, nombre):
    print("La mascota es: " + nombre)
    print("Es de raza: " + raza)

descripcion_mascota("pastor aleman", "toffy")

# argumento keywoard: Es cuando un argumento es pasado en el formato "parametro=argumento", haciendo irrelevante el orden 
# en que se definieron los parametros al crear la funcion. 

print("-----------------------1")

def des_mascota(raza, nombre):
    print("la mascota es " + nombre)
    print("es de raza " + raza)

des_mascota(nombre="toffina", raza="dogo")

des_mascota("doberman", nombre="toffy")

# argumento por defecto: una función puede tener parametros con valores por defecto, los cuales su utilizadas si al invocar la función no se le pasa un argumento para ese parámetro. Los parametros con valores por defecto deben definirse al final.

print("-----------------------2")

def descrip_mascota(nombre, raza="pequines"):
    print("mi mascota es " + nombre)
    print("es de raza: " + raza)

descrip_mascota("toffy")
descrip_mascota("toffy", "doberman")

# return: palabra reservada que permite devolver un valor al finalizar una función

print("-----------------------3")

def get_nombre(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name

l = get_nombre("luis", "rojas")

print(l)

def last_s(a, b=3):
    total = a + b
    return total

x = last_s(5)
print(x)

# argunmentos pasados arbitrariamente: se pueden tener un parametro que acepte una cantidad invariable de argumentos, los cuales almacenara en una tupla. Para eso ponemos un * delante del nombre del parametro. Este parametro debe ir al final de la fucnión, despues de cualquier valor por defecto.

print("-----------------------4")

def haciendo_pizza(size, *toppings):
    print("\n haciendo una pizza de " + str(size) + " elementos")
    for topping in toppings:
        print("- " + topping)

haciendo_pizza(3, "a", "b", "c")
