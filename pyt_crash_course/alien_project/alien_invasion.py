import sys

import pygame 
from settings import Settings

def run_game():

    # iniciamos la pantalla 
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(ai_settings.screen_width, ai_settings.screen_height)
    pygame.display.set_caption("Alien invasion")

    # Iniciamos el loop principal del juego
    while True:

        #Esperando el evento de cierre
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # reescribiendo el lienzo en cada pase del loop
        screen.fill(ai_settings.bg_color)

        pygame.display.flip() # actualiza el lienzo

run_game()