from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.image import Image
from functools import partial
from a import *

Country_id=-1
Pic=[]

for i in range(len(y)):
    temp_img = "Pic/" + y[i]["country_name"] +".png"
    temp_name = y[i]["country_name"]
    temp_id = y[i]["country_id"]
    Pic.append([temp_img,temp_name,temp_id])
RAN = len(Pic)*.2
class SV(ScrollView):
    def __init__(self,**kwargs):
        super(SV, self).__init__(**kwargs)
        root=GridLayout(cols=1,size_hint_y=RAN,padding=50)
        root.add_widget(Label(text="[size=100][b][i][color=00FFD5]Select Countries[/color][/i][/b][/size]",font_size=50,markup=True))
        for i in range(len(Pic)):
            root.add_widget(Lay(Pic[i][0],Pic[i][1],Pic[i][2]))
        self.add_widget(root)
    
class Lay(GridLayout):
    def __init__(self,sour,txt,id,**kwargs):
        super().__init__(**kwargs)
        self.id = id
        self.cols = 2
        #Add Widget In GridLayout
        self.add_widget(Image(source=sour,size_hint=(.199,1),keep_ratio=True))
        but=(Button(text="[size=100][b][i][color=00FE17]"+ txt +"[/color][/i][/b][/size]",\
        font_size=50,markup=True,background_color=(0,0,0,0),on_press=partial(self.my_function)))
        self.add_widget(but)
    #Function When click button
    def my_function(self,instant):
            global Country_id
            Country_id =self.id
class Nation(App):
    def build(self):
        Window.maximize()
        return SV()

Nation().run()