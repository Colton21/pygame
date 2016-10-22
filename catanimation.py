import pygame
import sys
from pygame.locals import *

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

# setup window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (255, 255, 255)

catImg = pygame.image.load('cat.png')
catx = 10
caty = 10
direction = 'right'

DISPLAYSURF.fill(WHITE)

colour = WHITE

# main loop
while True:
    DISPLAYSURF.fill(colour)

    if direction == 'right':
        catx += 5
        if catx == 280:
            direction = 'down'
            DISPLAYSURF.fill(BLUE)
            colour = BLUE
    # remember that pixels increase to the right and down!!!
    elif direction == 'down':
        caty += 5
        if caty == 220:
            direction = 'left'
            DISPLAYSURF.fill(RED)
            colour = RED
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'
            DISPLAYSURF.fill(BLACK)
            colour = BLACK
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction = 'right'
            DISPLAYSURF.fill(WHITE)
            colour = WHITE

    DISPLAYSURF.blit(catImg, (catx, caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

    fpsClock.tick(FPS)
