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
        self.ship_limit = 3

        # configuracion de las balas
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direccion of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # que tan rapido es el juego
        self.speedup_scale = 1.1
        # rapidez de incremento de puntos x alien
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

        self.alien_points = 50
    
    def initialize_dynamic_settings(self):
        """Inicializando configuraciones"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # direccion 1 derecha, -1 izquierda
        self.fleet_direction = 1
    
    def increase_speed(self):
        """Incrementando la configuracion de velocidad"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale 

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)

