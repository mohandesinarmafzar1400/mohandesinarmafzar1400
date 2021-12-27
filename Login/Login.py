from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
import re
from MYSQL import *
Builder.load_file('test.kv')

class test(Widget):
	def Reg(self):
		if (re.match("^[a-zA-Z0-9_.-]+$", self.ids.fname.text)):
			result=Check_PCE(ur,pw,"persons",self.ids.fname.text)
			print(result)
			if not result :
    				#next Page
					pass
	def CA(self):
    		#Page Create Account
			pass

class Main(App):
	Window.size=(1380,780)
	Window.top = 100
	Window.left = 250
	title=" My Application"
	def build(self):
		return test()

Main().run()