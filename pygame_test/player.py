import pygame


class PlayerPistol:
    """
    This class is the default player's character class (holding a pistol)

    Attributes (self.):

    """

    def __init__(self, screen, game_settings):
        """
        Initialization of Player class

        Parameters:
            :screen: this is the surface where the character will be drawn
            :game_settings: containing character settings
        """

        # set screen and game_settings
        self.screen = screen
        self.game_settings = game_settings

        # load character image and get its rect
        self.image = pygame.image.load('img/player_pistol.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # set player's starting position (center of the screen)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        """
        Draw the player at its current location
        """
        
        self.screen.blit(self.image, self.rect)
