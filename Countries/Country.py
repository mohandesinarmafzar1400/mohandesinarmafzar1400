from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.image import AsyncImage
from a import *

Country_id=-1
Pic=[]

for i in range(len(y)):
    temp_img = "Pic/" + y[i]["country_name"] +".png"
    temp_name = y[i]["country_name"]
    temp_id = y[i]["country_id"]
    Pic.append([temp_img,temp_name,temp_id])
RAN = len(Pic)*.111
class Country(ScrollView,AsyncImage):
    def __init__(self,**kwargs):
        super(Country, self).__init__(**kwargs)
        self.source='3090.jpg'
        
        self.root=GridLayout(cols=1,size_hint_y=RAN)
        self.root.add_widget(Label(text="[size=100][b][i][color=00FFD5]Select Countries[/color][/i][/b][/size]",font_size=50,markup=True))
        self.Child=GridLayout(cols=3,size_hint_y=RAN)
        for i in range(len(Pic)):
            self.Child.add_widget(Country_Lay(Pic[i][0],Pic[i][1],Pic[i][2]))
        self.root.add_widget(self.Child)
        self.add_widget(self.root)
    
class Country_Lay(GridLayout,Button,AsyncImage):
    def __init__(self,sour,txt,id,**kwargs):
        super().__init__(**kwargs)
        self.id = id
        self.cols = 2
        self.source = sour
        self.text="[size=50][b][i][color=00FE17]"+ txt +"[/color][/i][/b][/size]"
        self.markup=True
        self.background_color=(0,0,0,0)
        self.on_press=self.my_function
    #Function When click button
    def my_function(self):
            global Country_id
            Country_id =self.id
            print(Country_id)
class Countries(App):
    def build(self):
        Window.maximize()
        return Country()

Countries().run()