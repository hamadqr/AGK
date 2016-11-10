import pygame
def pressed():
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			return event.key