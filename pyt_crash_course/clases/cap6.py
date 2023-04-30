# definiendo un diccionario

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {}

print(alien_0['color'])
print(alien_0['points'])
print("-------------------------------")

# Agregando valores

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_1['color'] = 'blue'
print(alien_1)
print("-------------------------------")

# Modificando los valores

alien_0['color'] = 'pink'
print(alien_0)

alien_1['color'] = 'red'
print(alien_1)
print("-------------------------------")

# Retirando elementos del diccionario
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['color']
print(alien_0)
print("-------------------------------")

# definiendo un diccionario mas ordenado

favorite_languages = {
    'jen': 'python',
    'sara': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

print(favorite_languages)
print("-------------------------------")

# recorriendo un diccionario

for key, value in favorite_languages.items():
    print("clave: " + key + " - valor: " + value + "\n")

print("-------------------------------")

for name, language in favorite_languages.items():
    print(name.title() + " tiene como lenguaje favorito: " + language.title())

print("-------------------------------")

# recorriendo solo las CLAVES o VALORES de un diccionario

for key in favorite_languages.keys():
    print("llave: " + key.title())

print("-------------------------------")

for value in favorite_languages.values():
    print("value: " + value.title())

print("-------------------------------")

# nesting - consiste en poner diccionarios dentro de una lista

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens_list = [alien_0, alien_1, alien_2]
print(aliens_list)
print("-------------------------------")

# Ejercicio

new_aliens = []

for aliens_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    new_aliens.append(new_alien)

for alien in new_aliens[:5]:
    print(alien)

print("-------------------------------")

print("total de aliens: " + str(len(new_aliens)))
print("-------------------------------")

# nesting de una lista en un diccionario

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

print("Tu orden de " + pizza['crust'] + "-curst pizza tiene lo siguiente: ")
for topping in pizza['toppings']:
    print("\n" + topping)

print("-------------------------------")

# nesting de un diccionario en otro diccionario

users = {
'aeinstein': {
'first': 'albert',
'last': 'einstein',
'location': 'princeton',
},
'mcurie': {
'first': 'marie',
'last': 'curie',
'location': 'paris',
}
}

for user_name, user_info in users.items():
    print("\nUsername: " + user_name)

    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\nfull name: " + full_name)
    print("\nlocation: "  + location)

print("-------------------------------")

