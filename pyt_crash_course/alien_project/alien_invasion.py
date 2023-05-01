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
    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship ,aliens)

    # Iniciamos el loop principal del juego
    while True:

        #Esperando el evento de cierre
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, aliens)
        
        # reescribiendo el lienzo en cada pase del loop
        gf.update_screen(ai_settings, screen, ship, aliens ,bullets)

run_game()