from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file('test.kv')


class test(Widget):
    def Create(self):
        print(self.ids.fname.text,self.ids.lname.text,
            self.ids.uname.text,self.ids.PW.text)

class Main(App):
    '''Window.fullscreen = True
    Window.maximize()'''
    """Window.fullscreen = 'auto'
    title=" My Application"""
    Window.maximize()
    def build(self):
        return test()


Main().run()