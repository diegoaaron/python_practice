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
