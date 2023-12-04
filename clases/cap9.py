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
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("No puede reducir el odometro")

    # funcion para imcrementar el odometro
    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("este carro tiene un tanque de 80L")


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.fill_gas_tank()

# se puede modificar direcatmente una variable o se puede definir una funcion en la clase
my_new_car.odometer_reading = 44
my_new_car.read_odometer()

# modificando utilizando una funcion
my_new_car.update_odometer(55)
my_new_car.read_odometer()

# Herencia: Creando una clase hija

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70 # agregando variabels propias en la clase hija

    def describe_battery(self):
        print("este carro tiene " + str(self.battery_size) + " KWh")

    # modificando metodo heredado
    def fill_gas_tank(self):
        print("este carro no tiene tanque de gas")

my_tesla = ElectricCar("tesla", "model s", 2017)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()

