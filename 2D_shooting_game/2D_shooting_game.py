import pygame
from setting import Settings  # for game settings
from player import PlayerPistol
import game_functions as gf


# create a game setting object
game_settings = Settings()

# initialize pygame and the main screen
pygame.init()
screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
pygame.display.set_caption(game_settings.caption)

# run_game()
gf.welcome_screen(game_settings, screen)
