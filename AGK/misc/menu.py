from ..speech import SAPI, auto
from ..mainframe import keyboard
import pygame
class menu_item(object):
	def __init__(self,text,name,is_tts):
		self.text=text
		self.name=name
		self.is_tts=is_tts

class menu(object):
	def __init__(self, sapi=False):
		self.position=0
		self.items=[]
		self.sapi=sapi

	def add_item_tts(self,text,name):
		self.items.append(menu_item(text,name,True))

	def run(self,intro):
		self.speak(intro)
		self.position=-1

		while 1:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key==pygame.K_UP:
						if self.position<=0:
							self.position=0
						else:
							self.position-=1
						self.speak(self.items[self.position].text)
					if event.key==pygame.K_DOWN:
						if self.position<len(self.items)-1:
							self.position+=1
						self.speak(self.items[self.position].text)

					if event.key==pygame.K_RETURN:
						return self.items[self.position]

					if event.key==pygame.K_ESCAPE:
						return -1

#internal funcs
	def speak(self,text):
		if self.sapi==False:
			auto.speak(text)
		else:
			SAPI.speak(text)