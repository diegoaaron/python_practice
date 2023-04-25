# modulo settings - almacena las diferentes características del juego

class Settings():
    """Clase que almacena todas las configuraciones de Alien Invasion"""

    def __init__(self):
        """Inicializa el juego"""
        # configuraciones de pantalla
        self.screen_width = 800
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        