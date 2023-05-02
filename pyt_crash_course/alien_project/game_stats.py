class GameStats():
    """Registra estadisticas de Alien Invasion"""

    def __init__(self, ai_settings):
        """Inicializando las estadísticas"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # maximo score
        self.high_score = 0
        
        # Iniciando el juego con estado activo
        self.game_active = False

    def reset_stats(self):
        """Inicializando estadisticas que cambian durante el juego"""
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
