import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from CA import *
from Login import *
from Country import *
class Main(App):  # display the welcome screen
    def build(self):
        Window.maximize()
        sm = ScreenManager()
        sm.add_widget(Login_Lay(name='Login'))
        sm.add_widget(CA_Lay(name='Create Account'))
        sm.add_widget(Country(name='Country'))
        
        
        return sm


if __name__ == '__main__':
    Main().run()