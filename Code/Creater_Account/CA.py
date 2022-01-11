from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from MYSQL import *
Builder.load_file('test.kv')


class test(Widget):
    Gender = "Male"
    def Create(self):
        fname=self.ids.fname.text
        lname=self.ids.lname.text
        uname=self.ids.uname.text
        pw=self.ids.pw.text
        ge=__class__.Gender
        temp_CA=Check_PCE("persons",uname)
        #If Fill All Field
        if ( fname!= "" and lname!= "" and uname!= "" and pw!= "" ):
            if not temp_CA:
                self.ids.uname.text=""
                self.ids.uname.hint_text="Choose another username"
                self.ids.uname.background_color=(0,0,1,1)
            else :
                Insert_Iteams("persons","uname","ps","fname","lname","gender",hash(pw),fname,lname,ge)
        #If Dont Fill All Field
        else :
            if fname == "":
                self.ids.fname.text=""
                self.ids.fname.hint_text="You have not filled"
                self.ids.fname.background_color=(1,0,0,1)
            else :
                self.ids.fname.background_color=(0,1,1,1)
            if lname == "":
                self.ids.lname.text=""
                self.ids.lname.hint_text="You have not filled"
                self.ids.lname.background_color=(1,0,0,1)
            else :
                self.ids.lname.background_color=(0,1,1,1)
            if uname == "":
                self.ids.uname.text=""
                self.ids.uname.hint_text="You have not filled"
                self.ids.uname.background_color=(1,0,0,1)
            else :
                self.ids.uname.background_color=(0,1,1,1)
            if pw == "":
                self.ids.pw.text=""
                self.ids.pw.hint_text="You have not filled"
                self.ids.pw.background_color=(1,0,0,1)
            else :
                self.ids.pw.background_color=(0,1,1,1)
    def gender(self,instance,value,gender):
        if value == True:
            __class__.Gender = gender

class Main(App):
    Window.maximize()
    def build(self):
        return test()


Main().run()