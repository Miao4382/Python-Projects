import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, game_settings, screen, ship):
        """create a bullet object at the ship's current position (when its initialized)"""

        super().__init__()
        self.screen = screen

        # create a bullet rect at (0, 0) and then set correct position (at the ship)
        self.rect = pygame.Rect(0, 0, game_settings.bullet_width, game_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # store the bullet's position as a decimal value
        self.y = float(self.rect.y)

        # get other settings from game setting file
        self.color = game_settings.bullet_color
        self.speed_factor = game_settings.bullet_speed_factor

    def update(self):
        """update the bullet's position"""
        # update the decimal position of the bullet
        self.y -= self.speed_factor  # bullet travels vertically
        # update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
