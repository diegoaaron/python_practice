from random import choice

class RandomWalk():
    """Clase para generar caminatas randon"""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk"""
        self.num_points = num_points

        # Toda caminata empieza en el origen de coordenadas
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculando todos los puntos para caminar"""

        while len(self.x_values) < self.num_points:
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # dando el primer paso

            if x_step == 0 and y_step == 0:
                print("ocurrio x = 0 e y = 0")
                continue

            # calculando el siguiente paso

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)