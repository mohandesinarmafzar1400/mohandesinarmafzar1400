from logging import root
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder
from kivy.core.window import Window

#Builder.load_file("Nation_1.kv")

class SV(ScrollView):
    def __init__(self,**kwargs):
        super(SV, self).__init__(**kwargs)
        root=GridLayout(cols=1,size_hint_y=15,padding=30)
        for i in range(10):
            root.add_widget(Button(text="Hello asdkjaskljd laskjdlksajdlk sajldkjsaldjasls",font_size= 50,))

        #self.texture_size[1]
        #,text_size=(self.width,None)
        
        
        self.add_widget(root)
    pass

class Nation(App):
    def build(self):
        Window.maximize()
        return SV()

Nation().run()