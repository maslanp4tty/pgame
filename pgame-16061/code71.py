#pemrograman game praktikum 7
#latihan code 7.1 : pygame

import pygame, sys
from pygame. locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode ((400, 300))

pygame.display.set_caption ('hello world!')

while true: # main game loop
	for event in pygame.event.get():
	if event.type ==QUIT:
		pygame.quit()
		sys.exit()
	pygame.display.update()
