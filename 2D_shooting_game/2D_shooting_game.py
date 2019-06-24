import pygame
from setting import Settings
import game_functions as gf
from ship import Ship


def run_game():
    """ Initialize game and create a screen object"""

    pygame.init()  # initialize the background things needed by pygame
    game_settings = Settings()  # create an object of Setting class, and access the attributes

    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))  # create a game window

    pygame.display.set_caption(game_settings.caption)  # set the caption of the game window
    # screen.fill(game_settings.bg_color)  # .fill() will take a tuple and set background color, should be in game loop

    # make a ship, pass in following attributes: (check ship.Ship class for details)
    #   -the surface on which pygame draws the ship
    #   -game_settings (which contains settings for the ship)
    ship = Ship(screen, game_settings)

    # start the main loop for the game
    while True:

        # Watch for keyboard and mouse events
        # using a function in game_functions
        gf.check_events(ship)
        ship.update()

        # update screen and draw it
        gf.update_screen(game_settings, screen, ship)


run_game()
