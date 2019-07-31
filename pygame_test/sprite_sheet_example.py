import math, random, sys
import pygame
from pygame.locals import *
import copy


# a function that can exit the program
def events():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


# define display surface
width, height = 1366, 768
half_width, half_height = width / 2, height / 2
area = width * height

# define colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)


# initialize display
pygame.init()
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
FPS = 60


# define a sprite class
class SpriteSheet:
    def __init__(self, filename, cols, rows):
        """

        :param filename: path of sprite sheet image file
        :param cols: number of cols of the sprite sheet
        :param rows: number of rows of the sprite sheet
        """
        self.sheet = pygame.image.load(filename).convert_alpha()

        self.cols = cols
        self.rows = rows
        self.total_cell_count = cols * rows

        self.rect = self.sheet.get_rect()
        w = self.cell_width = self.rect.width / self.cols
        h = self.cell_height = self.rect.height / self.rows
        hw, hh = self.cell_center = w / 2, h / 2

        self.cells = list((index % self.cols * self.cell_width, int(index / self.cols) * self.cell_width, w, h) for index in range(self.total_cell_count))
        print('total cell: ', len(self.cells))
        # create a list of offsets
        self.handles = list([(0, 0), (-hw, 0), (-w, 0), (0, -hh), (-hw, -hh), (-w, -hh), (0, -h), (-hw, -h), (-w, -h)])

    def draw(self, surface, cell_index, x, y, handle=0):

        surface.blit(self.sheet, (x + self.handles[handle][0], y + self.handles[handle][1]), self.cells[cell_index])



# create a sprite sheet class object
# s = SpriteSheet('img/RainbowIslandsCharacter.png', 7, 4)
s = SpriteSheet('img/zombie_death.jpg', 8, 3)
CENTER_HANDLE = 4

index = 0

# main loop
while True:
    events()
    s.draw(screen, index % s.total_cell_count, half_width, half_height, CENTER_HANDLE)
    index += 1

    # pygame.draw.circle(screen, WHITE, (int(half_width), int(half_height)), 2, 0)
    pygame.display.update()
    CLOCK.tick(FPS)
    screen.fill(WHITE)

