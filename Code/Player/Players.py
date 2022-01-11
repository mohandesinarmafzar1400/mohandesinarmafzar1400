from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.image import AsyncImage
from kivy.uix.button import Button

Pic=[]

RAN = len(Pic)*.5
class Player(ScrollView):
    def __init__(self,**kwargs):
        super(Player, self).__init__(**kwargs)
        root=GridLayout(cols=1,size_hint_y=.5,padding=50)
        root.add_widget(Player_Lay("https://apiv3.apifootball.com/badges/players/58284_sergio-camus.jpg","Sergio Camus","1","2","Defenders","24","16","0","No","Atletico Madrid"))
        self.add_widget(root)
    
class Player_Lay(GridLayout,AsyncImage):
    def __init__(self,player_Image,player_name,player_number,player_type,player_age,\
        player_match_played,player_goals,player_minutes,player_injured,team_name,**kwargs):
        super().__init__(**kwargs)
        self.source = "https://www.planetware.com/wpimages/2020/02/france-in-pictures-beautiful-places-to-photograph-eiffel-tower.jpg"
        self.id = id
        self.cols = 1
        #Add Widget In GridLayout
        self.Layout=GridLayout(cols=5)
        self.Layout.add_widget(AsyncImage(source=player_Image,size_hint=(1,1),keep_ratio=True))
        self.Layout.add_widget(Label(text="[size=20][b][i][color=00FE17]"+ player_name +"[/color][/i][/b][/size]",\
        markup=True))
        self.Layout.add_widget(Label(text="[size=20][b][i][color=00FE17]"+ player_number +"[/color][/i][/b][/size]",\
        markup=True))
        self.Layout.add_widget(Label(text="[size=20][b][i][color=00FE17]"+ player_type +"[/color][/i][/b][/size]",\
        markup=True))
        self.Layout.add_widget(Label(text="[size=20][b][i][color=00FE17]"+ player_age +"[/color][/i][/b][/size]",\
        markup=True))
        self.Layout.add_widget(Label(text="[size=20][b][i][color=00FE17]"+ player_match_played +"[/color][/i][/b][/size]",\
        markup=True))
        self.Layout.add_widget(Label(text="[size=20][b][i][color=00FE17]"+ player_goals +"[/color][/i][/b][/size]",\
        markup=True))
        self.Layout.add_widget(Label(text="[size=20][b][i][color=00FE17]"+ player_minutes +"[/color][/i][/b][/size]",\
        markup=True))
        self.Layout.add_widget(Label(text="[size=20][b][i][color=00FE17]"+ player_injured +"[/color][/i][/b][/size]",\
        markup=True))
        self.Layout.add_widget(Label(text="[size=20][b][i][color=00FE17]"+ team_name +"[/color][/i][/b][/size]",\
        markup=True))
        self.add_widget(self.Layout)
    #Function When click button
    def my_function(self,instant):
            global Country_id
            Country_id =self.id
class Countries(App):
    def build(self):
        Window.maximize()
        return Player()

Countries().run()