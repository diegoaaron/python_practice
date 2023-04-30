import pygame 
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien

def run_game():

    # iniciamos la pantalla 
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien invasion")

    # Creamos una nave
    ship = Ship(ai_settings, screen)
    # Grupo que almacena las balas
    bullets = Group()
    alien = Alien(ai_settings, screen)

    # Iniciamos el loop principal del juego
    while True:

        #Esperando el evento de cierre
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        
        # reescribiendo el lienzo en cada pase del loop
        gf.update_screen(ai_settings, screen, ship, alien ,bullets)

run_game()