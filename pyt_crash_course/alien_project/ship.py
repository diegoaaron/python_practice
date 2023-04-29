import pygame

class Ship():

    def __init__(self,ai_settings , screen):
        """inicializando la nave y configurando su posicion"""
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
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1

    def blitme(self):
        """Dibujando la nave en la posicion actual"""
        self.screen.blit(self.image, self.rect)
    