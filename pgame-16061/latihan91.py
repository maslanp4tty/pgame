import pygame

pygame.init()
screen = pygame.display.set_mode ((600,480))
done= False
warna_bg = (240,24,55)

pygame.display.set_caption  ("hallo app")

while not done:
	for event in pygame.event.get():
		if event.type ==pygame.QUIT:
			done = true
		if event .type ==pygame.KEYDOWN and \
	event. key == pygame.K_ESCAPE:
			done = true

	screen.fill(warna_bg)
	pygame.draw.line(screen, (0,0,255), (0,0),(600,480))

	pygame.display.flip()