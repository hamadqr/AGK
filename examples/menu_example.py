import time
from AGK.misc import menu
from AGK.mainframe import window, keyboard
from AGK.speech import auto
def mainmenu():
	m=menu.menu()
	m.add_item_tts("Start game","start")
	m.add_item_tts("Exit game","exit")
	obj=m.run("Main menu")
	if obj.name=="start":
		auto.speak("You selected start.")
		time.sleep(2)
		mainmenu()

w=window.window("game")
w.show()
mainmenu()

