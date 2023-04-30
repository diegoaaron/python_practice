import pygame
from pygame.sprite import _Group, Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_settings, screen, ship):
        # Creando un disparo en la actual posicion de la nave
        super(Bullet, self).__init__()
        self.screen = screen

        # Creando a bullet rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Almacenando la posicion de la bala como un valor decimal
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Moviendo la bala en la pantalla"""
        # Actualizando la posicion decimal de la bala
        self.y -= self.speed_factor
        # Actualizando la posicion recta
        self.rect.y = self.y

    def draw_bullet(self):
        """Dibujando la bala en la pantalla"""
        pygame.draw.rect(self.screen, self.color, self.rect)

