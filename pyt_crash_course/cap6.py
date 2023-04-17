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

