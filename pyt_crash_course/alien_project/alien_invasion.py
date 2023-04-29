import pygame 
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():

    # iniciamos la pantalla 
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien invasion")

    # Creamos una nave
    ship = Ship(ai_settings, screen)

    # Iniciamos el loop principal del juego
    while True:

        #Esperando el evento de cierre
        gf.check_events(ship)
        ship.update()
        
        # reescribiendo el lienzo en cada pase del loop
        gf.update_screen(ai_settings, screen, ship)

run_game()