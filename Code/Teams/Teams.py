from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.image import AsyncImage
from functools import partial

Pic=[]
Team_id=-1
#RAN = len(Pic)*.2
class Team(ScrollView):
    def __init__(self,**kwargs):
        super(Team, self).__init__(**kwargs)
        root=GridLayout(cols=1,size_hint_y=1,padding=50)
        root.add_widget(Label(text="[size=100][b][i][color=00FFD5]Select Team[/color][/i][/b][/size]",font_size=50,markup=True))
        for i in range(1):
            root.add_widget(Team_Lay("73","Atletico Madrid","https://apiv3.apifootball.com/badges/73_atl.-madrid.jpg"))
        self.add_widget(root)
    
class Team_Lay(GridLayout):
    def __init__(self,team_key,team_name,team_badge,**kwargs):
        super().__init__(**kwargs)
        self.id = team_key
        self.cols = 2
        #Add Widget In GridLayout
        self.add_widget(AsyncImage(source=team_badge,size_hint=(1,1),keep_ratio=True))
        self.add_widget(Button(text="[size=100][b][i][color=f7ff00]"+ team_name +"[/color][/i][/b][/size]",\
        font_size=50,markup=True,background_color=(0,0,0,0),on_press=partial(self.my_function)))
        
    #Function When click button
    def my_function(self,instant):
            global Team_id
            Team_id =self.id
class Countries(App):
    def build(self):
        Window.maximize()
        return Team()

Countries().run()