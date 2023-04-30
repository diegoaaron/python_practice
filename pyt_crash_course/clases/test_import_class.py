from cap9 import Car, ElectricCar # importando clases especificas
from cap9 import * # importar todas las clases

carro_importado = Car("Ferrari", "a4", 2022)

print(carro_importado.get_descriptive_name())


import cap9 # importa todo el modulo
carro_3 = cap9.Car("Ferrari", "a4", 2022)
print(carro_3.get_descriptive_name())
