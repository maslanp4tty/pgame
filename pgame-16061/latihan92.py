import pygame

pygame.init()
screen = pygame.display.set_mode ((600,480))
done= False
warna_bg = (251, 127, 80)

pygame.display.set_caption  ("hallo app")

while not done:
	for event in pygame.event.get():
		if event.type ==pygame.QUIT:
			done = true
		if event .type ==pygame.KEYDOWN and \
	event. key == pygame.K_ESCAPE:
			done = true

	screen.fill(warna_bg)
	pygame.draw.line(screen, (0,0,255), (0,0),(300,380))
	pygame.draw.line(screen, (0,0,255), (0,20),(300,320))
	pygame.display.flip()