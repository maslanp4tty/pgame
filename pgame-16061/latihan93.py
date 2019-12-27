import pygame

pygame.init()
screen = pygame.display.set_mode ((600,480))
done= False
warna_bg = (127,224,1)

pygame.display.set_caption  ("hallo app")

while not done:
	for event in pygame.event.get():
		if event.type ==pygame.QUIT:
			done = true
		if event .type ==pygame.KEYDOWN and \
	event. key == pygame.K_ESCAPE:
			done = true

	screen.fill(warna_bg)
	pygame.draw.rect(screen, (0,0,255),(50,20,200,100),2)
	pygame.display.flip()