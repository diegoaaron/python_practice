import sys

import pygame 

def run_game():
    # iniciamos la pantalla 
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Alien invasion")

    # configurando color del lienzo
    bg_color = (230, 230, 230)

    # Iniciamos el loop principal del juego
    while True:

        #Esperando el evento de cierre
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # reescribiendo el lienzo en cada pase del loop
        screen.fill(bg_color)

        pygame.display.flip() # actualiza el lienzo

run_game()