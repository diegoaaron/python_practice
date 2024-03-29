import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self,ai_settings , screen):
        """inicializando la nave y configurando su posicion"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # cargando y configurando la imagen
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #definir valor decimal para nave central
        self.center = float(self.rect.centerx)

        # etiqueta de movimiento continuo
        self.moving_right = False
        self.moving_left = False

        # iniciando cada nave abaja y al centro del lienzo
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def update(self):
        """Actualizando la posicion de la nave"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        
        # actualiza la recta desde self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Dibujando la nave en la posicion actual"""
        self.screen.blit(self.image, self.rect)
    
    def center_ship(self):
        """Center the ship on the screen"""
        self.center = self.screen_rect.centerx
