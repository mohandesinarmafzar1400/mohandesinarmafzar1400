from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.image import AsyncImage
from functools import partial

Competition_id=-1
Pic=[]


#RAN = len(Pic)*.2
class Competition(ScrollView):
    def __init__(self,**kwargs):
        super(Competition, self).__init__(**kwargs)
        root=GridLayout(cols=1,size_hint_y=1,padding=50)
        root.add_widget(Label(text="[size=100][b][i][color=00FFD5]Select Competition[/color][/i][/b][/size]",font_size=50,markup=True))
        root.add_widget(Competition_Lay("Spain","300","Copa_del_Rey","2020/2021","https://upload.wikimedia.org/wikipedia/commons/a/a7/Logo-Copa-del-Rey-300.jpg","https://upload.wikimedia.org/wikipedia/commons/a/a7/Logo-Copa-del-Rey-300.jpg"))
        
        self.add_widget(root)
    
class Competition_Lay(GridLayout):
    def __init__(self,country_name,league_id,league_name,league_season,league_logo,country_logo,**kwargs):
        super().__init__(**kwargs)
        self.id = league_id
        self.cols = 6
        #Add Widget In GridLayout
        #League logo
        self.add_widget(AsyncImage(source=league_logo,size_hint=(2,1),keep_ratio=True))
        #Country logo
        self.add_widget(AsyncImage(source=country_logo,size_hint=(2,1),keep_ratio=True))
        #League Name
        self.add_widget(Label(text="[size=20][b][i][color=FC0404]"+ league_name +"[/color][/i][/b][/size]",\
        markup=True))
        #League Season
        self.add_widget(Label(text="[size=20][b][i][color=FC0404]"+ league_season +"[/color][/i][/b][/size]",\
        markup=True))
        #Country Name
        self.add_widget(Label(text="[size=20][b][i][color=FC0404]"+ country_name +"[/color][/i][/b][/size]",\
        markup=True))
        
        #Button Select
        self.add_widget(Button(text="[size=20][b][i][color=FC0404]Select[/color][/i][/b][/size]",\
        font_size=50,markup=True,background_color=(0,0,0,0),on_press=partial(self.my_function)))
        
    #Function When click button
    def my_function(self,instant):
            global Competition_id
            Competition_id =self.id

class Countries(App):
    def build(self):
        Window.maximize()
        return Competition()

Countries().run()