from Modules import *
from Players import *

class Team(ScrollView,AsyncImage,Screen):
    Pic=[]
    

    def __init__(self,**kwargs):
        super(Team, self).__init__(**kwargs)
        self.source='Pic\\Teams.jpg'
        self.add_widget(Button(text='Let`s go',on_press=self.Create_Widget,font_size=50,background_color=(0,0,0,0)))

    def CI(CI):
        global Competition_id
        Competition_id = CI
    
    def Create_Widget(self,instant):
        global Competition_id
        self.TP=Teams(Competition_id) 
        ######
        for i in range(len(self.TP)):
            temp_key=self.TP[i]["team_key"]
            temp_name=self.TP[i]["team_name"]
            temp_badge=self.TP[i]["team_badge"]
            Team.Pic.append([temp_key,temp_name,temp_badge])
        self.clear_widgets()
        RAN = len( Team.Pic)*.2
        self.source='Pic\\Teams.jpg'
        self.root=GridLayout(cols=1,size_hint_y=RAN,padding=50)
        self.root.add_widget(Label(text="[size=100][b][i][color=00FFD5]Choose Team[/color][/i][/b][/size]",\
            markup=True,size_hint=(1,.1)))
        
        for i in range(len(Team.Pic)):
            self.root.add_widget(Team_Lay( Team.Pic[i][1], Team.Pic[i][2]))
        #Add All Data In Widget 
        self.last=GridLayout(cols=2,size_hint_y=((RAN/len( Team.Pic))*2))
        self.TI=(TextInput(hint_text="Enter The Team Name",multiline=False,font_size=50))
        self.last.add_widget(self.TI)
        #For Call Function Next_page 
        self.last.add_widget(Button(text="[u][i][size=70][color=FF9945]Select[/color]",\
            markup=True,on_press=self.Next_page,size_hint=(.5,1)))
        #For Call Function Previous_page 
        self.root.add_widget(self.last)
        self.root.add_widget(Button(text="[u][i][size=70][color=000000]Previous Page[/color]",\
            markup=True,on_press=self.Previous_page,size_hint=(1,.4),background_color=(0,0,0,0)))
        self.add_widget(self.root)


    #For Next Page  If select Correctly Name Team=> Competition
    def Next_page(self,instant):
        temp=self.TI.text.casefold()
        for i in range(len(Team.Pic)):
            if temp == Team.Pic[i][1].casefold() :
                global Team_select
                Team_select = Team.Pic[i][0]
                Player.CI(self.TP,Team_select)
                self.manager.current = 'Player'
                self.manager.transition.direction = 'left'
                break
            else:
                self.TI.background_color=(1,.5,.5,1)
                self.TI.text=""
                self.TI.hint_text="You did not choose the name of the Competitons correctly"
                self.TI.font_size=40
    


    #For Back Page => Country
    def Previous_page(self,instant):
        self.manager.current = 'Competition'
        self.manager.transition.direction = 'right'


class Team_Lay(GridLayout):
    def __init__(self,team_name,team_badge,**kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        #Add Widget In GridLayout
        self.add_widget(AsyncImage(source=team_badge))
        self.add_widget(Label(text="[size=50][b][i][color=f7ff00]"+ team_name +"[/color][/i][/b][/size]",\
        font_size=50,markup=True))
        
    
# class Countries(App):
#     def build(self):
#         Window.maximize()
#         return Team()

# Countries().run()