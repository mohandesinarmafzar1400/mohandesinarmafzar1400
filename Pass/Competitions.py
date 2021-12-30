from Modules import *
from Get_Data import *
from Global_Var import *
from Teams import *

class Competition(ScrollView,AsyncImage,Screen):
    Pic=[]
    def __init__(self,**kwargs):    
        super().__init__(**kwargs)
        self.source='Pic\\Competition.jpg'
        self.add_widget(Button(text='Let`s go',on_press=self.Create_Widget,font_size=50,background_color=(0,0,0,0)))
        

    @staticmethod    
    def CI(CI):
        global Country_id
        Country_id = CI
    def Create_Widget(self,instant):
        global Country_id
        if (Country_id != -1):
            result=Competitions(Country_id)
            for i in range(len(result)):
                temp_Cid=result[i]["country_id"]
                temp_CN=result[i]["country_name"]
                temp_Lid=result[i]["league_id"]
                temp_LN=result[i]["league_name"]
                temp_LS=result[i]["league_season"]
                temp_LLog=result[i]["league_logo"]
                temp_CLog=result[i]["country_logo"]
                Competition.Pic.append([temp_Cid, temp_CN, temp_Lid, temp_LN, temp_LS, temp_LLog, temp_CLog])
        self.clear_widgets()
        
        RAN = len(Competition.Pic)*.3
        if (len(Competition.Pic)) <= 3 :
            RAN *= 2
        self.source = 'Pic\\Competition.jpg'
        self.root=GridLayout(cols=1,size_hint_y=RAN,padding=50)
        self.root.add_widget(Label(text="[size=100][b][i][color=00FFD5]Select Competition[/color][/i][/b][/size]",font_size=50,markup=True,size_hint=(1,.1)))
        self.Child=GridLayout(cols=1,size_hint_y=RAN)
        for i in range(len( Competition.Pic)):
            self.Child.add_widget(Competition_Lay( Competition.Pic[i][1], Competition.Pic[i][2], Competition.Pic[i][3],\
                 Competition.Pic[i][4], Competition.Pic[i][5], Competition.Pic[i][6]))
        self.root.add_widget(self.Child)
        self.last=GridLayout(cols=2,size_hint=(1,((RAN/len(Competition.Pic)/2))))
        self.TI=(TextInput(hint_text="Enter The Competition Name",multiline=False,font_size=50))
        self.last.add_widget(self.TI)
        self.last.add_widget(Button(text="[u][i][size=50][color=FF9945]Select[/color][/size][/i][/u]",markup=True,on_press=self.Next_page,size_hint=(.5,1)))
        self.root.add_widget(self.last)
        self.root.add_widget(Button(text="[u][i][size=50][color=FF9945]Previous Page[/color][/size][/i][/u]",background_color=(0,0,0,0),markup=True,on_press=self.Previous_page,size_hint=(1,((RAN/len(Competition.Pic)/2)))))
        self.add_widget(self.root)
        
    def Next_page(self,instant):
        temp=self.TI.text.casefold()
        for i in range(len(Competition.Pic)):
            if temp == Competition.Pic[i][3].casefold():
                global Competition_id
                Competition_id = Competition.Pic[i][2]
                Team.CI(Competition_id)
                self.manager.transition.direction = 'left'
                self.manager.current = 'Team'
                break
            else:
                self.TI.background_color=(1,.5,.5,1)
                self.TI.text=""
                self.TI.hint_text="You did not choose the name of the Competitons correctly"
                self.TI.font_size=40
    
    def Previous_page(self,instant):
        self.manager.transition.direction = 'right'
        self.manager.current = 'Country'
        
                
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
        self.add_widget(Label(text="[size=50][b][i][color=00dcff]" + league_name +"[/color][/i][/b][/size]",markup=True))
        #League Season
        self.add_widget(Label(text="[size=20][b][i][color=00dcff]"+ league_season +"[/color][/i][/b][/size]",\
        markup=True))
        #Country Name
        self.add_widget(Label(text="[size=20][b][i][color=00dcff]"+ country_name +"[/color][/i][/b][/size]",\
        markup=True))
        
        
    

# class Countries(App):
#     def build(self):
#         Window.maximize()
#         return Competition()

# Countries().run()