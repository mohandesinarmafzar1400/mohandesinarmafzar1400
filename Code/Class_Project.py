class Player():
    def __init__(self):
        self.first_name=''
        self.last_name=''
        self.age=0
        self.foot=''
        self.position=''
        self.country_team=''
        self.club_team=''
    def get_all(self):
        return [self.first_name,self.last_name,self.age,self.foot,self.position,self.country_team,self.club_team]
    def set_all(self,first_name,last_name,age,foot,position,country_team,club_team):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.foot=foot
        self.position=position
        self.country_team=country_team
        self.club_team=club_team


class Member_User:
    def __init__(self):
        self.User=''
        self.Pass=''
        self.first_name=''
        self.last_name=''
        self.last_search=''
    def get_info(self):
        return print(self.first_name,self.last_name)
    def set_info(self,first_name,last_name,last_search):
        self.first_name=first_name
        self.last_name=last_name
        self.last_search=last_search
    def set_user_pass(self,User,Pass):
        self.User=User
        self.Pass=Pass
    def show_player(self,__class__):
        return __class__.get_all()
    def compare(self,__class1__,__class2__):
        return __class1__.get_all(),__class2__.get_all()
    def Random_player(self):
        #Get 10 Name Player Of Database Player
        pass
    @staticmethod
    def Update():
        #Clear DB Player and get new Data
        pass

    
class Member_guess():
    def Random_player(self):
        pass
