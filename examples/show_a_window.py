#import
import pygame
from AGK.mainframe import window, keyboard
#create a window.
w=window.window("test window")
w.show()
while 1:
	if keyboard.pressed()==pygame.K_ESCAPE:
		break