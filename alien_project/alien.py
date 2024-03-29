import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Clase que representa a un solo alien"""

    def __init__(self, ai_settings, screen):
        """Inicializando el alien y su posicion"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Cargando la imagen del alien
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Iniciando cada nueva linea cerca de la esquina izquierda superior
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Guardando el alien en la posicion correcta
        self.x = float(self.rect.x)
    
    def blitme(self):
        """Dibujando el alien en la posicion actual"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Mover el alien a la derecha"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Retorna True si el alien esta en medio de la pantalla"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True