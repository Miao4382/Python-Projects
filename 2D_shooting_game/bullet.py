import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """
    A class to manage bullets fired from the ship
    
    This class is derived from pygame.Sprite, so it can be grouped together in 
    an object of pygame.Sprite.Group. 
    
    To add an object of this Bullet class to one Group object, you call the 
    add() member function of Group object. Example:   
        bullets = pygame.Sprite.Group()
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)
    
    
    Attributes:
        :self.screen: 
            this is the screen to where the Bullet object is drawn
        
        :self.rect: 
            this is the rectangle of the Bullet object, created by pygame.Rect()
        
        :self.y: 
            an intermediate variable holds the y coordinates of self.rect 
            (decimal value)
        
        :self.color: 
            holds color of Bullet, copied from game_settings, will be used when 
            drawing self.rect to self.screen 
        
        :self.speed_factor: 
            holds the speed of the bullet, copied from game_settings, will be 
            used when update the position of the bullet during each game loop 
            (each frame), in function Bullet.update()
    
    
    Methods:
        __init__():
            constructor, initialization
            
        update():
            update the bullet's position (self.rect.y value). 
            
            This function is called at each game loop, or each refresh of the 
            screen. Because the bullet will keep moving once it is shot.
            
            In the game loop, the Bullet.update() is actually called by calling
            bullets.update(). Notice that bullets are the pygame.Sprite.Group 
            object we use to group all Bullet object. By calling the Group class's
            member function .update(), all members in that Group object's
            .update() method will be called automatically. So we don't have to 
            call them one by one.
        
        draw_bullet():
            This function is called when re-drawing the screen.
            When gf.update_screen() is called.
            It will draw the bullet to the screen (draw as a rectangle)
            
            Pay attention to the difference between Ship.blitme() method:            
              Ship.blitme() method:
                the member function .blit() of the main window is called to draw 
                the ship to the screen:
                
                  self.screen.blit(self.image, self.rect)
                  
              Bullet.draw_bullet() method: 
                following function is called:
                  pygame.draw.rect(self.screen, self.color, self.rect)
            
            Now you know two ways to draw a shape onto screen:
                1. screen.blit(image, rect)
                2. pygame.draw.rect(screen, color, rect)
            
            
    """

    def __init__(self, game_settings, screen, ship):
        """
        create a bullet object at the ship's current position 
        (when its initialized)
        
        Parameters:
            :game_settings: 
                will use the settings defined in the Settings class
                
            :screen: 
                needed to draw the object onto the main screen
                
            :ship:
                needed to obtain the position where should the bullet be drawn 
                (so it looks like firing from the ship)
        
        """

        super().__init__()  # call the constructor of its base class: pygame.sprite
        self.screen = screen  # self.screen is used in draw_bullet() function, to draw on main screen

        # create a bullet rect at (0, 0) and then set correct position (at the ship)
        # notice that you won't see the bullet at (0, 0) because its not been drawn yet
        self.rect = pygame.Rect(0, 0, game_settings.bullet_width, game_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # store the bullet's position as a decimal value
        # decimal value gives more precise control
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
