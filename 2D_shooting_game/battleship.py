import pygame


class Battleship:
    def __init__(self, screen, game_settings):
        """try to add another ship"""
        self.screen = screen
        self.game_settings = game_settings

        # load battleship image and get its rect
        self.image = pygame.image.load('img/battleship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # set battleship's starting position
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.top

    def update(self):
        """
        Currently no updates
        :return:
        """
        pass

    def blitme(self):
        """
        Draw the ship at its current location
        :return:
        """

        self.screen.blit(self.image, self.rect)