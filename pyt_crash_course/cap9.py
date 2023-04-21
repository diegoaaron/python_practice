# Definiendo una clase
# El metodo __init___() es el constructor de la clase y por ende es el primer
# metodo ejecutado al crear una instancia de la clase 
# el parametro self, se pasa automaticamente por lo cual no debemos indicarlo
# al crear una instancia de la clase

class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sit(self):
        print(self.name.title() + " is now sitting")

    def roll_over(self):
        print(self.name.title() + " rolled over!")

# creando instancias de la clase 

my_dog = Dog("toffy", 4)
you_dog = Dog("lucy", 3)

print("mi perro se llama " + my_dog.name.title() + ".")
print("mi perro se tiene " + str(my_dog.age) + " años.")
my_dog.sit()


# Clase Car

class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print("este carro tiene " + str(self.odometer_reading) + " miles on int")

    # funcion para actualizar una variable 
    def update_odometer(self, mileage):
        self.odometer_reading = mileage


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# se puede modificar direcatmente una variable o se puede definir una funcion en la clase
my_new_car.odometer_reading = 44
my_new_car.read_odometer()

# modificando utilizando una funcion
my_new_car.update_odometer(55)
my_new_car.read_odometer()

