import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
#anotherSurface = DISPLAYSURF.convert_alpha()
pygame.display.set_caption('Drawing')

#Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#draw on surface object

#this fills the display with white
DISPLAYSURF.fill(WHITE)
#this draws a regular green pentagon with points at the given coordinates
pygame.draw.polygon(DISPLAYSURF, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
#this draws a blue line with points at the coordinates, with width 4
pygame.draw.line(DISPLAYSURF, BLUE, (60, 60), (120, 60), 4)

pygame.draw.line(DISPLAYSURF, BLUE, (120, 60), (60, 120))
pygame.draw.line(DISPLAYSURF, BLUE, (60, 120), (120, 120), 4)
#draw blue circle, centre point, radius, fill pattern(?)
pygame.draw.circle(DISPLAYSURF, BLUE, (300, 50), 20, 0)
pygame.draw.ellipse(DISPLAYSURF, RED, (300, 250, 40, 80), 1)
pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50))

pixObj = pygame.PixelArray(DISPLAYSURF)
pixObj [480][380] = BLACK
pixObj [482][382] = BLACK
pixObj [484][384] = BLACK
pixObj [486][386] = BLACK
pixObj [488][388] = BLACK
del pixObj


#start main code
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		pygame.display.update()
