import sys
import pygame
from bullet import Bullet


def check_keydown_events(event, game_settings, screen, ship, bullets):
    """respond to key press"""
    if event.key == pygame.K_RIGHT or event.key == ord('d'):
        # set the moving status of the ship
        ship.moving_right = True

    if event.key == pygame.K_LEFT or event.key == ord('a'):
        # set the moving status of the ship
        ship.moving_left = True

    if event.key == pygame.K_UP or event.key == ord('w'):
        # set the moving status of the ship
        ship.moving_up = True

    if event.key == pygame.K_DOWN or event.key == ord('s'):
        # set the moving status of the ship
        ship.moving_down = True
        
    if event.key == pygame.K_SPACE:
        # create a new bullet and it to the bullets group
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)

    if event.key == pygame.K_ESCAPE:
        # pull up settings screen with option to quit game?
        sys.exit()


def check_keyup_events(event, ship):
    """respond to key releases"""
    if event.key == pygame.K_RIGHT or event.key == ord('d'):
        # reset the moving status of the ship
        ship.moving_right = False
        ship.acceleration = 0

    if event.key == pygame.K_LEFT or event.key == ord('a'):
        # reset the moving status of the ship
        ship.moving_left = False
        ship.acceleration = 0

    if event.key == pygame.K_UP or event.key == ord('w'):
        # reset the moving status of the ship
        ship.moving_up = False
        ship.acceleration = 0

    if event.key == pygame.K_DOWN or event.key == ord('s'):
        # reset the moving status of the ship
        ship.moving_down = False
        ship.acceleration = 0


def check_events(game_settings, screen, ship, bullets):
    """response to key presses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(game_settings, screen, ship, bullets):
    """Update items on the screen and draw new screen"""
    # screen.fill(game_settings.bg_color)
    bg = pygame.image.load('bg.jpg')
    screen.blit(bg, (0, 0))
    
    # redraw ship
    ship.blitme()
    
    # delete bullets that are out of screen and redraw all bullets 
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
        
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    # draw the updated screen
    pygame.display.flip()
