import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues ,edgecolors="none" ,s = 40)

# Set chart title and label
plt.title("Numeros al cuadrado", fontsize = 24)
plt.xlabel("Valores", fontsize = 14)
plt.ylabel("Cuadrados", fontsize = 14)

plt.tick_params(axis="both", which="major", labelsize = 14)

plt.show()