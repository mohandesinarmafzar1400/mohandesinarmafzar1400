from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
Builder.load_file('kv.kv')

class test(Widget):
    pass
class Main(App):
    def build(self):
        return test()

Main().run()