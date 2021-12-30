from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from MYSQL import *
import re
from kivy.uix.image import AsyncImage
from MYSQL import *
Builder.load_file('Kivy_file\Login.kv')

class Login_Lay(Screen):
	def Reg(self):
		uname=self.ids.uname.text
		pw=self.ids.pw.text
		if ( uname != "" and pw != "" ):
			if (re.match("^[a-zA-Z0-9_.-]+$",uname)):
				result=Check_PCE("persons",uname)
				if not result:
					person=Select_IC("persons",uname)
					
					if person[2] == pw:
						self.manager.transition.direction = 'right'
						self.manager.current = 'Country'
						
		else :	
			if (uname == ""):
				self.ids.uname.text=""
				self.ids.uname.hint_text="You have not filled"
				self.ids.uname.background_color=(1,0,0,1)
			else :
				self.ids.uname.background_color=(0,1,1,1)
			if (pw == ""):
				self.ids.pw.text=""
				self.ids.pw.hint_text="You have not filled"
				self.ids.pw.background_color=(1,0,0,1)
			else :
				self.ids.pw.background_color=(0,1,1,1)	
				
	def CA(self):
    		#Page Create Account
			self.manager.transition.direction = 'up'
			self.manager.current = 'Create Account'	
	def RP(self):
    		#Page Recover Account
			self.manager.transition.direction = 'down'
			self.manager.current = 'Recovery Password'


# class Main(App):
# 	Window.size=(1380,780)
# 	Window.top = 100
# 	Window.left = 250
# 	title=" My Application"
# 	def build(self):
# 		return Login_Lay()

# Main().run()