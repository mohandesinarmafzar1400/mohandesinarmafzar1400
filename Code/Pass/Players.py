from Modules import *




class Player(ScrollView,AsyncImage,Screen):
    
    def __init__(self,**kwargs):
        super(Player, self).__init__(**kwargs)
        self.source='Pic\\Players.jpg'
        self.add_widget(Button(text='Let`s go',on_press=self.Create_Widget,font_size=50,background_color=(1,0,0,1)))

    def Create_Widget(self,instance):
        Pic=[]
        global TP , Team_select
        for i in range(len(TP)):
            if (TP[i]["team_key"] == Team_select):    
                if len(TP[i]["players"]) != 0:
                    for j in range(len(TP[i]["players"])):
                        player_image=TP[i]["players"][j]["player_image"]
                        player_name=TP[i]["players"][j]["player_name"]
                        player_number=TP[i]["players"][j]["player_number"]
                        player_type=TP[i]["players"][j]["player_type"]
                        player_age=TP[i]["players"][j]["player_age"]
                        player_match_played=TP[i]["players"][j]["player_match_played"]
                        player_goals=TP[i]["players"][j]["player_goals"]
                        player_injured=TP[i]["players"][j]["player_injured"]
                        Pic.append([ player_image, player_name, player_number, player_type, player_age, \
                            player_match_played, player_goals, player_injured ])
                    self.clear_widgets()
                    RAN = len(Pic)*.5
                    self.source='Pic\\Players.jpg'
                    self.root=GridLayout(cols=1,size_hint_y=RAN,padding=50)
                    for i in range(len( Pic)):
                        self.root.add_widget(Player_Lay( Pic[i][0], Pic[i][1], Pic[i][2], Pic[i][3], Pic[i][4],\
                            Pic[i][5], Pic[i][6], Pic[i][7]))
                    self.root.add_widget(Button(text="[u][i][size=70][color=FF9945]Previous Page[/color]",\
                        markup=True,on_press=self.Previous_page,size_hint=(1,.4),background_color=(0,0,0,0)))
                    self.add_widget(self.root)
                    break
                else :
                    self.clear_widgets()
                    self.source='Pic\\Players.jpg'
                    self.root=GridLayout(cols=1,size_hint_y=1,padding=50)
                    self.root.add_widget(Label(text="[size=50][b][i][color=000000]Your Team Select But We could not players, Sorry ;)[/color][/i][/b][/size]",\
                        markup=True))
                    
                    self.root.add_widget(Button(text="[u][i][size=70][color=FF9945]Previous Page[/color]",\
                        markup=True,on_press=self.Previous_page,size_hint=(1,.4),background_color=(0,0,0,0)))
                    self.add_widget(self.root)

    @staticmethod
    def CI(Tep,CI):
        global Team_select, TP
        Team_select = CI
        TP = Tep

    def Previous_page(self,instant):
        self.manager.transition.direction = 'right'
        self.manager.current = "Team"
    
class Player_Lay(GridLayout):
    def __init__(self,player_Image,player_name,player_number,player_type,player_age,\
        player_match_played,player_goals,player_injured,**kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        #Add Widget In GridLayout
        self.Layout=GridLayout(cols=8)
        self.add_widget(Top())
        self.Layout.add_widget(AsyncImage(source=player_Image,size_hint=(1,1),keep_ratio=True))
        self.Layout.add_widget(Label(text="[size=50][b][i][color=000000]"+ player_name +"[/color][/i][/b][/size]",\
        markup=True))
        self.Layout.add_widget(Label(text="[size=50][b][i][color=000000]"+ player_number +"[/color][/i][/b][/size]",\
        markup=True))
        self.Layout.add_widget(Label(text="[size=50][b][i][color=000000]"+ player_type +"[/color][/i][/b][/size]",\
        markup=True))
        self.Layout.add_widget(Label(text="[size=50][b][i][color=000000]"+ player_age +"[/color][/i][/b][/size]",\
        markup=True))
        self.Layout.add_widget(Label(text="[size=50][b][i][color=000000]"+ player_match_played +"[/color][/i][/b][/size]",\
        markup=True))
        self.Layout.add_widget(Label(text="[size=50][b][i][color=000000]"+ player_goals +"[/color][/i][/b][/size]",\
        markup=True))
        self.Layout.add_widget(Label(text="[size=50][b][i][color=000000]"+ player_injured +"[/color][/i][/b][/size]",\
        markup=True))
        self.add_widget(self.Layout)

class Top(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        #Add Widget In GridLayout
        self.Layout=GridLayout(cols=8)
        self.Layout.add_widget(Label(text="[size=25][b][i][color=40E0D0] Player Image [/color][/i][/b][/size]",\
        markup=True))
        self.Layout.add_widget(Label(text="[size=25][b][i][color=40E0D0] Player Name [/color][/i][/b][/size]",\
        markup=True))
        self.Layout.add_widget(Label(text="[size=25][b][i][color=40E0D0] Player Number [/color][/i][/b][/size]",\
        markup=True))
        self.Layout.add_widget(Label(text="[size=25][b][i][color=40E0D0] Player Type [/color][/i][/b][/size]",\
        markup=True))
        self.Layout.add_widget(Label(text="[size=25][b][i][color=40E0D0] Player Age [/color][/i][/b][/size]",\
        markup=True))
        self.Layout.add_widget(Label(text="[size=25][b][i][color=40E0D0] Player_match_played [/color][/i][/b][/size]",\
        markup=True))
        self.Layout.add_widget(Label(text="[size=25][b][i][color=40E0D0] Player Goals [/color][/i][/b][/size]",\
        markup=True))
        self.Layout.add_widget(Label(text="[size=25][b][i][color=40E0D0] Player Injured [/color][/i][/b][/size]",\
        markup=True))
        self.add_widget(self.Layout)
# class Countries(App):
#     def build(self):
#         Window.maximize()
#         return Player()

# Countries().run()