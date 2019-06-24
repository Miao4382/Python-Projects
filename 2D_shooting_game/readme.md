# 2D Shooting Game: alien invasion
A top view 2D shooting game created using Python's Pygame Library.

## Overview
* player controls a character that appears at the center of the screen.
* player can move in four directions, controlled by using arrow keys or WSAD keys.
* player can aim and shoot by using mouse
* player can choose different weapons from armory system, at beginning, player has a default hand gun
* enemies (alien creatures) spawn at edges of the screen, and they will hunt the player down
* player will lose if taking enough damage from enemy. Player's score will be shown
* if player shoots all enemies, a new wave of enemy will respawn. Enemies are harder to kill and moves faster
* this game may have a vehicle system, player has a chance of riding an armed vehicle to fight with enemies, which lasts limited time and has its own hitpoints 

## Implementation detail
### Basic movement of player
Implement the movement of the character (controlled by arrow key), and the orientation of the character (always facing the where mouse is, it is also the shooting direction)

### Game object animation
When moving the object, they should display animations rather than static, for example, the character should look like moving its legs when moving on the screen. Also, if an enemy is killed by the player, an animation should be shown.

### Character and NPC design
Design the attributes and methods of character and NPC classes.

### Other game object design 
vehicles, weapons, warheads and bullets classes.

### interactions between projectiles and target being hit
This is the one of the core parts, since it defines how shooting/fighting behaves in this game. 

### Game resources
Game resources, including images, sounds, etc.

## Current Progress:
Currently the texture of the character is a jet fighter, it will be replaced by a human in the future.
* temporary background added: a steel board
* A jet fighter is drawn in the middle of the game window
* jet fighter movement control added, now it can move in four directions by using arrow key 
* jet fighter movement has acceleration now (will add deceleration in the future)
* jet fighter is bound inside the main game window 

## How to run this demo 
Download the 2D_shooting_game folder, create your project. Activate your environment and install pygame package (pip install pygame). Then run '2D_shooting_game.py'
