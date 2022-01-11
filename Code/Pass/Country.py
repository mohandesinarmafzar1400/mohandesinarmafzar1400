from Modules import *
from Competitions import *
from Global_Var import *

class Country(ScrollView,AsyncImage,Screen):
    op = open( "Data\Text.txt" , "r")
    out = op.read()
    jsn_Country = json.loads(out)
    Pic=[]

    for i in range(len(jsn_Country)):
        temp_img = "Pic\Pic_country\\" + jsn_Country[i]["country_name"] +".png"
        temp_name = jsn_Country[i]["country_name"]
        temp_id = jsn_Country[i]["country_id"]
        Pic.append([temp_img,temp_name,temp_id])
    RAN = len(Pic)*.101

    def __init__(self,**kwargs):
        
        super(Country, self).__init__(**kwargs)
        
        self.source='Pic\\3090.jpg'
        
        self.root=GridLayout(cols=1,size_hint_y=Country.RAN)
        
        self.root.add_widget(Label(text="[size=100][b][i][color=00FFD5]Select Countries[/color][/i][/b][/size]",font_size=50,markup=True,size_hint=(1,.1)))
        
        self.Child=GridLayout(cols=5,size_hint_y=Country.RAN)
        
        for i in range(len(Country.Pic)):
            self.Child.add_widget(Country_Lay(Country.Pic[i][0],Country.Pic[i][1],Country.Pic[i][2]))
        
        self.root.add_widget(self.Child)
        
        self.last=GridLayout(cols=2,size_hint=(1,.070))
        
        self.TI=(TextInput(hint_text="Enter The Country Name",multiline=False,font_size=50))
        
        self.last.add_widget(self.TI)
        
        self.last.add_widget(Button(text="[u][i][size=50][color=FF9945]Select[/color][/size][/i][/u]",markup=True,size_hint=(.5,1),\
            background_color=(0,0,0,1),on_press=self.Next_page))
        
        self.root.add_widget(self.last)
        
        self.root.add_widget(Button(text="[u][i][size=70][color=FF9945]Previous Page[/color]",markup=True,on_press=self.Previous_page,size_hint=(1,.1),background_color=(0,0,0,0)))
        
        self.add_widget(self.root)

    def Next_page(self,instant):
        temp=self.TI.text.casefold()
        
        for i in range(len(Country.Pic)):
            if temp == Country.Pic[i][1].casefold():
                global Country_id
                Country_id = Country.Pic[i][2]
                Competition.CI(Country_id)
                print(Country_id)
                self.manager.current = 'Competition'
                self.manager.transition.direction = 'left'
            else:
                self.TI.background_color=(1,.5,.5,1)
                self.TI.text=""
                self.TI.hint_text="You did not choose the name of the country correctly"
                self.TI.font_size=40
    
    def Previous_page(self,instant):
        self.manager.current = 'Login'
        self.manager.transition.direction = 'right'
        
        
class Country_Lay(GridLayout):
    def __init__(self,sour,txt,id,**kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.Img=(AsyncImage(source=sour))
        self.Lb=(Label(text="[size=50][b][i][color=00FE17]"+ txt +"[/color][/i][/b][/size]",markup=True,size_hint=(1,.15)))
        # self.add_widget(Button(text="Hello",on_press=self.func))
        self.add_widget(self.Img)
        self.add_widget(self.Lb)

# class Countries(App):
#     def build(self):
#         Window.maximize()
#         return Country()

# Countries().run()