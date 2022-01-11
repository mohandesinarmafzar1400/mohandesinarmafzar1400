from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.lang import Builder

Builder.load_file('Middle_page.kv')

class Mp(GridLayout):
    def Next_page(self,id):
        if ( id == 1 ):
            #Next_page Is ...
            pass
        else :
            #Next_page Is ...
            pass
class Middle_page(App):
    def build(self):
        Window.maximize()
        return Mp()

Middle_page().run()