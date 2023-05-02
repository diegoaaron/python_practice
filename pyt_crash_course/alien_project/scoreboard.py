import pygame.font

class Scoreboard():
    """Una clase que reporta informacion"""

    def __init__(self, ai_settings, screen, stats):
        """Inicializando atributos"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Configurando fuentes para información
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepara  score inicial
        self.prep_score()

    def prep_score(self):
        """Poniendo el score en una imagen"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # Mostrando el score en la parte superior derecha
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)

    