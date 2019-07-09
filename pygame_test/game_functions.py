import sys
import pygame
import math  # for rotation angle calculation
import random
from bullet_pistol import BulletPistol


def blit_player(player, screen):
    """
    This function deals with the rotation of the player's character along with mouse
    
    Ideas:
        To display the player onto the screen, we have to call screen.blit(image, rect). The image is the "surface" of the player, while the rect is the rectangle of the player. Rotation will only affect the rotated angle of player's image surface. To achieve this, we first get the position of mouse pointer using:
            pygame.mouse.get_pos()
        This will return a tuple, which is (x, y), containing x and y value of mouse's position. Then we can get the coordinate of player.rect's center: 
            (player.rect.centerx, player.rect.centery)
        We have two points, which is the mouse pointer and the center of player's character's center. We can obtain the rotation angle:
            angle = math.atan2(player.rect.centery - mouse_position[1], player.rect.centerx - mouse_position[0]) * 57.29
        
        Pay attention the angle returned by math.atan2() is in rad, we have to convert it to degrees.
        
        Then we rotate player's image to reflect this change. One important thing is, we shouldn't modify the original image (stored in player's object). Here, we use another variable to hold the rotated player's image:
            player_rotated_image = pygame.transform.rotate(player.image, 180 - angle)
        
        Then, we blit this rotated image to the screen, rather than the original image. This is because we have to keep the original image so we can use it as a reference to calculate the rotated angle.
        
        Before we blit, we have to get the new rect, since when the image is rotated, "the image will be padded larger to hold the new size", which means a larger rect is created that surrounds the image.
        
    Parameters:
        player: 
    """
    
    # get mouse coordinate
    mouse_position = pygame.mouse.get_pos()
    # calculate angle
    angle = math.atan2(player.rect.centery - mouse_position[1], player.rect.centerx - mouse_position[0]) * 57.29
    # rotate player's image surface 
    player_rotated_image = pygame.transform.rotate(player.image, 180 - angle)
    
    # update player's rect
    player_updated_rect = (player.rect.centerx - player_rotated_image.get_rect().width / 2, player.rect.centery - player_rotated_image.get_rect().height / 2)
    
    # blit the new position
    screen.blit(player_rotated_image, player_updated_rect)
    

def check_keydown_events(event, player):
    """
    This function will check which key is pressed down, and then perform corresponding operations.
    """
    
    if event.key == pygame.K_w:
        player.moving_up = True
    
    if event.key == pygame.K_a:
        player.moving_left = True    

    if event.key == pygame.K_s:
        player.moving_down = True

    if event.key == pygame.K_d:
        player.moving_right = True
        

def check_keyup_events(event, player):
    if event.key == pygame.K_w:
        player.moving_up = False
    
    if event.key == pygame.K_a:
        player.moving_left = False  

    if event.key == pygame.K_s:
        player.moving_down = False

    if event.key == pygame.K_d:
        player.moving_right = False
        
def check_mousedown(event):
    # left click
    if event.button == 1:
        s = pygame.mixer.Sound('sfx/weapons/p228.wav')
        s.play(0)
        
def check_events(player):
    """
    Check the broad category and call corresponding methods to do the specific work
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, player)
        
        if event.type == pygame.KEYUP:
            check_keyup_events(event, player)
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            check_mousedown(event)

            
def update_screen(background, player, screen):
    """
    Redraw screens (after items on the screen are updated)
    """
    
    # plot background
    screen.blit(background, (0, 0))
    
    # update and draw player's character
    blit_player(player, screen)
    
    # draw the updated screen 
    pygame.display.flip()
    