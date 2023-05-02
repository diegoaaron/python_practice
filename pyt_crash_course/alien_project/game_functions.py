import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Responde a tecla presionada"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings, screen, ship, bullets):
    """Lanzar una bala dentro del limite"""
    # Creando una bala y agregandola al grupo de balas
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """Responde  a tecla soltada"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets):
    """Respuesta a los eventos de teclado y mouse"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """Inicia un nuevo juego al dar clic en play"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reseteando configuracion del juego
        ai_settings.initialize_dynamic_settings()

        # Ocultando el cursor
        pygame.mouse.set_visible(False)

        # Reseteando las estatidisticas
        stats.reset_stats()
        stats.game_active = True

        # Vaciando la lista de aliens y balas
        aliens.empty()
        bullets.empty()

        # Creando una nueva nave
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """Actualiza imagen de la nave en la pantalla"""
    screen.fill(ai_settings.bg_color)

    # Dibujando todas las balas
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    # Dibujando la tabla de puntos
    sb.show_score()

    # Dibujando el boton si el juego esta inactivo
    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """Actualiza la posicion de las balas y las depura"""
    # Actualiza la posicion de las balas 
    bullets.update()

    # Obteniendo las balas a desaparecer
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)
    
def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    """Respond to bullet-alien collisions."""
    # Valida si una bala golpeo un alien
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        # Destruye las balas y crea una nueva fila
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)

def get_number_aliens_x(ai_settings, alien_width):
    """Determinando el numero de aliens por fila"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Crea un alien y lo ubica en la fila"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """Create a full fleet of aliens."""
    # Creando un alien y encontrando el numero de aliens x fila
    # El espacio entrea aliens es igual al ancho de un alien
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    
    
    # Creando la primera fila de aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # Crear un alien y ubicarlo en la fila
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
       
        
def get_number_rows(ai_settings, ship_height, alien_height):
    """Determina el numero de filas para los alines"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """Actualizando la posicion de todos los aliens"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Viendo las coliciones de una bala y un alien
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    
    # Viendo si los aliens golpean la parte baja de la pantalla
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)

def check_fleet_edges(ai_settings, aliens):
    """Responde apropieadamente si el alien alcanzo el borde"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """Baja todo la fila y cambia de direccion"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """Respond to ship being hit by alien"""
    if stats.ships_left > 0:
        # Reduciendo ships_left
        stats.ships_left -= 1

        # Baceando la lista de aliens y balas
        aliens.empty()
        bullets.empty()

        # Creando una nueva flota y los centra
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # Pausando
        sleep(0.5)
    else:
        stats.game_active = False 
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """Valida si un alien alcanzo la parte final de la pantalla"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Tretar como si la nave fuera golpeada
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break
    