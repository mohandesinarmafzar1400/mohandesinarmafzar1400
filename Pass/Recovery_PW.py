from Modules import *
from kivy.animation import Animation



class RPW(GridLayout,AsyncImage,Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.count = 3
        self.time = ''
        self.padding = 250
        self.spacing = 100
        self.source ='Pic\\PR.jpg'
        self.cols=1
        self.TIuname=(TextInput(hint_text="Enter The Username",multiline=False,font_size=50,size_hint = (1,.05),\
            foreground_color = (1,0,0,1),background_color = (0,0,0,0)))
        self.add_widget(self.TIuname)
        self.add_widget(Button(text="[size=50][b][i][color=03FF00] <<Next>> [/color][/i][/b][/size]", \
            markup=True,on_press=self.Next_G,background_color=(0,0,0,0),size_hint = (1,.12)))#Gender
        
        
    
    def Next_G(self,instant):
        self.uname=self.TIuname.text
        #Detail Person
        if (self.uname != ''):
            if (re.match("^[a-zA-Z0-9_.-]+$",self.uname)):
                self.DP=Select_IC("persons",self.uname)
                if (self.DP is not None):
                    self.clear_widgets()
                    self.TIG=(TextInput(hint_text="Enter The Gender (Male Or Female)",multiline=False,font_size=50,size_hint = (1,.2),\
                        foreground_color = (1,0,0,1),background_color = (0,0,0,0)))
                    self.add_widget(self.TIG)
                    self.add_widget(Button(text="[size=50][b][i][color=03FF00] <<Next>> [/color][/i][/b][/size]", \
                    markup=True,on_press=self.Next_FL,background_color=(0,0,0,0)))#FName And LName
                else :
                    self.TIuname.background_color=(1,.5,.5,1)
                    self.TIuname.text=''
                    self.TIuname.hint_text="Also " + self.uname +" does not exist"
                    self.count -= 1
                    #Check Ban Or Not
                    self.Check_ban()
            else:
                self.TIuname.text=''
                self.TIuname.hint_text = 'Only Numbers and Letters (0-9,a-z,A-Z)'
        else :
                self.TIuname.background_color=(1,.5,.1,1)
                self.TIuname.text=''
                self.TIuname.hint_text="Fill in the field "
    #Fname And LName
    def Next_FL(self,instant):
        self.G=self.TIG.text
        if (self.DP[5].casefold() == self.TIG.text.casefold()):
            self.clear_widgets()

            self.TIF=(TextInput(hint_text="Enter The First Name",multiline=False,font_size=50,size_hint = (1,.4),\
                    foreground_color = (1,0,0,1),background_color = (0,0,0,0)))
            
            self.add_widget(self.TIF)
            
            self.TIL=(TextInput(hint_text="Enter The Last Name",multiline=False,font_size=50,size_hint = (1,.4),\
                    foreground_color = (1,0,0,1),background_color = (0,0,0,0)))
            
            self.add_widget(self.TIL)
            
            self.add_widget(Button(text="[size=50][b][i][color=03FF00] <<Next>> [/color][/i][/b][/size]", \
                markup=True,on_press=self.Next_CP,background_color=(0,0,0,0)))
        
        #If Be None
        elif self.G == '':
            self.TIG.background_color=(1,.5,.1,1)
            self.TIG.text=''
            self.TIG.hint_text="Fill in the field "
        #If Not correctly
        else :
            self.TIG.text=''
            self.TIG.hint_text="Is wrong {}".format(self.G)
            self.TIG.background_color=(1,.5,.5,1)
            self.count -= 1
            #Check Ban Or Not
            self.Check_ban()

    #Change Password
    def Next_CP(self,instant):
        if ( self.DP[3] == self.TIF.text and self.DP[4] == self.TIL.text ):
            
            self.clear_widgets()
            
            self.TIP1=(TextInput(hint_text="Enter The New Password ",multiline=False,font_size=50,\
                foreground_color = (1,0,0,1),background_color = (0,0,0,0)))
            
            self.add_widget(self.TIP1)
            
            self.TIP2=(TextInput(hint_text="Repetition ",multiline=False,font_size=50,\
                foreground_color = (1,0,0,1),background_color = (0,0,0,0)))
            
            self.add_widget(self.TIP2)
            
            self.add_widget(Button(text="[size=50][b][i][color=03FF00] <<Next>> [/color][/i][/b][/size]", \
                markup=True,on_press=self.Check,background_color=(0,0,0,0)))
        
        #TIF Be NOne Or TIL
        elif ( ( self.TIF.text == '' ) or ( self.TIL.text == '' ) ):
            if (self.TIF.text == ''):
                self.TIF.background_color=(1,.5,.1,1)
                self.TIF.text=''
                self.TIF.hint_text="Fill in the field "

            if (self.TIL.text == ''):
                self.TIL.background_color=(1,.5,.1,1)
                self.TIL.text=''
                self.TIL.hint_text="Fill in the field "
        #TIF Or TIL Be incorrectly
        else :
            if ( self.DP[3] != self.TIF.text ):
                self.TIF.text=''
                self.TIF.hint_text="Is wrong {}".format(self.G)
                self.TIF.background_color=(1,.5,.5,1)
                self.count -= 1
                #Check Ban Or Not
                self.Check_ban()
            else :
                self.TIL.text=''
                self.TIL.hint_text="Is wrong {}".format(self.G)
                self.TIL.background_color=(1,.5,.5,1)
                self.count -= 1
                #Check Ban Or Not
                self.Check_ban()
    
    
    def Check(self,instant):
        if (re.match("^[a-zA-Z0-9_.-]+$",self.TIP1.text)):
            if ( self.TIP1.text == self.TIP2.text ):
                self.res=update(self.TIP1.text,self.TIuname.text)
                if self.res:
                    self.clear_widgets()
                    self.padding = 0
                    self.add_widget(Label(text="[size=100][b][i][color=03FF00] <<Wellcome>> [/color][/i][/b][/size]", \
                    markup=True))
                    self.add_widget(Label(text="[size=100][b][i][color=03FF00] <<Successful>> [/color][/i][/b][/size]", \
                    markup=True))
                    self.add_widget(Button(text="[size=100][b][i]<<Login>>[/i][/b][/size]", \
                    markup=True,on_press=self.End,background_color=(0,0,0,0),size_hint=(1,.5),color=(0,1,0,1)))
        else:
            self.TIP1.text=''
            self.TIP1.hint_text = 'Only Numbers And Letters (0-9,a-z,A-Z)'
            self.TIP2.text=''
            self.TIP2.hint_text = 'Only Numbers And Letters (0-9,a-z,A-Z)'
    
    
    def End(self,Widget,*args):
        animation = Animation(color=(1,0,0,1),duration=1)
        animation += Animation(color=(0,1,0,1),duration=1)
        animation += Animation(color=(1,1,0,1),duration=1)

        animation += Animation(color=(0,0,1,1),duration=1)
        animation += Animation(color=(1,0,1,1),duration=1)
        animation += Animation(color=(0,1,1,1),duration=1)
        animation += Animation(size_hint=(1,1),duration=3)
        animation.start(Widget)
        animation.bind(on_complete = self.Next_page)
    
    def Next_page(self,*args):
        self.manager.transition.direction = 'down'
        self.manager.current = 'Login'

    def Check_ban(self):
        if (self.count == 0):
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            self.time =current_time[0:5]
            

    
# class Main(App):
#     def build(self):
#         Window.maximize()
#         return RPW()
# Main().run()