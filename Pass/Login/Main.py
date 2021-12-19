from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file('test.kv')

class test(Widget):
	def Reg(self):
		print("reg")
	def CA(self):
    		print("CA")

class Main(App):
	Window.size=(1380,780)
	Window.top = 100
	Window.left = 250
	title=" My Application"
	def build(self):
		return test()

Main().run()