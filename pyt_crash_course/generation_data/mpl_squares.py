import matplotlib.pyplot as plt

imput_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(imput_values ,squares, linewidth = 5)

# configurando parametro sde la gráfica

plt.title("Cuadrados", fontsize = 24)
plt.xlabel("Valores", fontsize = 14)
plt.ylabel("Cuadrados", fontsize = 14)

plt.tick_params(axis = 'both', labelsize = 14)

plt.show()