import sys
import pygame


def check_keydown_events(event, ship):
    """respond to key press"""
    if event.key == pygame.K_RIGHT:
        # set the moving status of the ship
        ship.moving_right = True

    if event.key == pygame.K_LEFT:
        # set the moving status of the ship
        ship.moving_left = True

    if event.key == pygame.K_UP:
        # set the moving status of the ship
        ship.moving_up = True

    if event.key == pygame.K_DOWN:
        # set the moving status of the ship
        ship.moving_down = True


def check_keyup_events(event, ship):
    """respond to key releases"""
    if event.key == pygame.K_RIGHT:
        # reset the moving status of the ship
        ship.moving_right = False
        ship.acceleration = 0

    if event.key == pygame.K_LEFT:
        # reset the moving status of the ship
        ship.moving_left = False
        ship.acceleration = 0

    if event.key == pygame.K_UP:
        # reset the moving status of the ship
        ship.moving_up = False
        ship.acceleration = 0

    if event.key == pygame.K_DOWN:
        # reset the moving status of the ship
        ship.moving_down = False
        ship.acceleration = 0


def check_events(ship):
    """response to key presses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(game_settings, screen, ship):
    """Update items on the screen and draw new screen"""
    # screen.fill(game_settings.bg_color)
    bg = pygame.image.load('img/bg.jpg')
    screen.blit(bg, (0, 0))
    ship.blitme()

    # draw the updated screen
    pygame.display.flip()
