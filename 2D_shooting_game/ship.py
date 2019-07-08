import pygame


class Ship:
    # screen is needed to put Ship class into the game window
    # game_settings is needed to access ship related setting
    def __init__(self, screen, game_settings):
        """initialize the ship and set its starting position"""
        self.screen = screen
        self.game_settings = game_settings

        # load ship image and get its rect
        self.image = pygame.image.load('img/0.jpg')  # this function returns a surface, which is represented by the image it loads
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()  # we are trying to put the ship_rect into screen_rect

        # set ship's starting position (center of the screen)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        # intermediate coordinate storing (for higher accuracy)
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)

        # ship moving flag, if the flag is true, the ship should be in a continuously moving status
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.acceleration = 0  # moving acceleration, will be increased each moving loop. Reset to 0 when stop moving

    def update(self):
        """check moving flag, and perform corresponding movement as stated by moving flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # set an upper bound of acceleration
            if self.acceleration < self.game_settings.ship_speed_acceleration_ratio * self.game_settings.ship_speed_factor:
                self.acceleration += self.game_settings.ship_speed_factor
            self.center_x += self.game_settings.ship_speed_factor + self.acceleration

        if self.moving_left and self.rect.left > 0:
            # set an upper bound of acceleration
            if self.acceleration < self.game_settings.ship_speed_acceleration_ratio * self.game_settings.ship_speed_factor:
                self.acceleration += self.game_settings.ship_speed_factor
            self.center_x -= self.game_settings.ship_speed_factor + self.acceleration

        if self.moving_up and self.rect.top > 0:
            # set an upper bound of acceleration
            if self.acceleration < self.game_settings.ship_speed_acceleration_ratio * self.game_settings.ship_speed_factor:
                self.acceleration += self.game_settings.ship_speed_factor
            self.center_y -= self.game_settings.ship_speed_factor + self.acceleration

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            # set an upper bound of acceleration
            if self.acceleration < self.game_settings.ship_speed_acceleration_ratio * self.game_settings.ship_speed_factor:
                self.acceleration += self.game_settings.ship_speed_factor
            self.center_y += self.game_settings.ship_speed_factor + self.acceleration

        # pass the new coordinate stored in temporary self.center_x, self.center_y to rect object
        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y

    def blitme(self):
        """
        Draw the ship at its current location"""
        # image = pygame.image.load('img/drawing.png')
        # rect = image.get_rect()
        # rect.centerx = self.screen_rect.centerx
        # rect.centery = self.screen_rect.centery
        # self.screen.blit(image, rect)

        self.screen.blit(self.image, self.rect)
