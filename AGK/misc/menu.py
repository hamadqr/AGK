from ..audio import sound
from ..speech import SAPI, auto
from ..mainframe import keyboard
import pygame
class menu_item(object):
	def __init__(self,text,name,is_tts):
		self.text=text
		self.name=name
		self.is_tts=is_tts

class menu(object):
	def __init__(self, sapi=False, home_and_end=True, wrap=False, select_with_enter=True, select_with_space=False, announce_position_info=False):
		self.position=0
		self.items=[]
		self.sapi=sapi
		self.home_and_end=home_and_end
		self.wrap=wrap
		self.item_sound=""
		self.enter_sound=""
		self.select_with_enter=select_with_enter
		self.select_with_space=select_with_space
		self.announce_position_info=announce_position_info

	def add_item_tts(self,text,name):
		self.items.append(menu_item(text,name,True))

	def run(self,intro=None,is_intro_tts=True,starting_position=-1):
		if self.enter_sound:
			self.entersnd=sound.sound()
			self.entersnd.load(self.enter_sound)
		if self.item_sound:
			self.itemsnd=sound.sound()
			self.itemsnd.load(self.item_sound)
		if intro:
			if is_intro_tts:
				self._speak(intro)
			else:
				s=sound.sound()
				s.load(intro)
				s.play()
		self.position=starting_position

		while 1:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key==pygame.K_UP:
						if self.position<=0:
							if self.wrap:
								self.position=len(self.items)-1
							else:
								self.position=0
						else:
							self.position-=1
						if self.announce_position_info:
							self._speak(self.items[self.position].text+". "+str(self.position+1)+" of "+str(len(self.items)))
						else:
							self._speak(self.items[self.position].text)
						if self.item_sound:
							self.itemsnd.stop()
							self.itemsnd.play()
					elif event.key==pygame.K_DOWN:
						if self.position<len(self.items)-1:
							self.position+=1
						elif self.position>=len(self.items)-1 and self.wrap:
							self.position=0
						if self.announce_position_info:
							self._speak(self.items[self.position].text+". "+str(self.position+1)+" of "+str(len(self.items)))
						else:
							self._speak(self.items[self.position].text)
						if self.item_sound:
							self.itemsnd.stop()
							self.itemsnd.play()
					elif event.key==pygame.K_HOME:
						self.position=0
						if self.announce_position_info:
							self._speak(self.items[self.position].text+". "+str(self.position+1)+" of "+str(len(self.items)))
						else:
							self._speak(self.items[self.position].text)
						if self.item_sound:
							self.itemsnd.stop()
							self.itemsnd.play()
					elif event.key==pygame.K_END:
						self.position=len(self.items)-1
						if self.announce_position_info:
							self._speak(self.items[self.position].text+". "+str(self.position+1)+" of "+str(len(self.items)))
						else:
							self._speak(self.items[self.position].text)
						if self.item_sound:
							self.itemsnd.stop()
							self.itemsnd.play()

					if event.key==pygame.K_RETURN and self.select_with_enter or event.key==pygame.K_SPACE and self.select_with_space:
						if self.enter_sound:
							self.entersnd.play_wait()
						return self.items[self.position]

					if event.key==pygame.K_ESCAPE:
						return -1

#internal funcs
	def _speak(self,text):
		if self.sapi==False:
			auto.speak(text)
		else:
			SAPI.speak(text)