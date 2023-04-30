import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Responde a tecla presionada"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def fire_bullet(ai_settings, screen, ship, bullets):
    """Lanzar una bala dentro del limite"""
    # Creando una bala y agregandola al grupo de balas
    if len(bullets) < ai_settings.bullets_alllowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """Responde  a tecla soltada"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    """Respuesta a los eventos de teclado y mouse"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_bullets(bullets):
    """Actualiza la posicion de las balas y las depura"""
    # Actualiza la posicion de las balas 
    bullets.update()

    # Obteniendo las balas a desaparecer
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def update_screen(ai_settings, screen, ship, bullets):
    """Actualiza imagen de la nave en la pantalla"""
    screen.fill(ai_settings.bg_color)

    # Dibujando todas las balas
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()

    pygame.display.flip()


