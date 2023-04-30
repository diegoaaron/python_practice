# modulo settings - almacena las diferentes características del juego

class Settings():
    """Clase que almacena todas las configuraciones de Alien Invasion"""

    def __init__(self):
        """Inicializa el juego"""
        # configuraciones de pantalla
        self.screen_width = 600
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 0.2

        # configuracion de las balas
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)