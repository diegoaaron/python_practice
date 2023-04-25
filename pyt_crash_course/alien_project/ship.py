import pygame

class Ship():

    def __init__(self, screen):
        """inicializando la nave y configurando su posicion"""
        self.screen = screen

        # cargando y configurando la imagen
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # iniciando cada nave abaja y al centro del lienzo
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Dibujando la nave en la posicion actual"""
        self.screen.blit(self.image, self.rect)