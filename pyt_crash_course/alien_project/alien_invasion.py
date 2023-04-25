import sys

import pygame 

def run_game():
    # iniciamos la pantalla 
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Alien invasion")

    # Iniciamos el loop principal del juego
    while True:

        #Esperando el evento de cierre
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        pygame.display.flip() # actualiza 

run_game()