from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.image import AsyncImage
from kivy.uix.screenmanager import Screen
from a import *
import json

Country_id=-1




class Country(Screen,AsyncImage):
    
    op = open( "Data\Countries.txt" , "r")
    out = op.read()
    jsn_Country = json.loads(out)

    Pic=[]
    for i in range(len(jsn_Country)):
        temp_img = jsn_Country[i]["country_logo"]
        temp_name = jsn_Country[i]["country_name"]
        temp_id = jsn_Country[i]["country_id"]
        Pic.append([temp_img,temp_name,temp_id])
    

    def __init__(self,**kwargs):
        super(Country, self).__init__(**kwargs)
        
        self.source='Pic/3090.jpg'
        self.root = GridLayout(cols=1)
        self.TI=(TextInput(multiline=False,font_size=50,size_hint=(1,.09)))
        self.root.add_widget(self.TI)
        self.root.add_widget(Button(text="[size=100][b][i][color=00FFD5]Select Countries[/color][/i][/b][/size]",font_size=50,markup=True, \
            size_hint=(1,.09),on_press=self.func))
        self.Child=GridLayout(cols=3,size_hint_y=1)
        for i in range(9):
            self.Child.add_widget(Country_Lay(Country.Pic[i][0],Country.Pic[i][1]))
        self.root.add_widget(self.Child)
        self.add_widget(self.root)
    def func(self,instant):
        name=self.TI.text
        name=name.capitalize()
        for i in range(len(Country.Pic)):
            if name == Country.Pic[i][1]:
                global Country_id
                Country_id=Country.Pic[i][2]
                self.manager.current = 'Login'


class Country_Lay(GridLayout):
    def __init__(self,sour,txt,**kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.add_widget(AsyncImage(source=sour))
        self.add_widget(Label(text="[size=50][b][i][color=00FE17]"+ txt +"[/color][/i][/b][/size]",markup=True))
        
# class Countries(App):
#     def build(self):
#         Window.maximize()
#         return Country()

# Countries().run()