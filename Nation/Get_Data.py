import requests
import json
#complete
url = "https://apiv3.apifootball.com/?action=get_countries&APIkey="
#complete in Function Com => {}
url_Com = "https://apiv3.apifootball.com/?action=get_leagues&country_id={}&APIkey="
#complete in Function Tea => {}
url_Tea = "https://apiv3.apifootball.com/?action=get_teams&league_id={}&APIkey="
#complete with Player ID in Funtion Pla => {}
url_Pla= "https://apiv3.apifootball.com/?action=get_players&player_id={}&APIkey="

print("ok")

key = "8b077c33a92505c20da9bd1aba253b5f0835fb5ea63998d65b178bb0f39f70a3"
#Get All Data As For Country
#def Cou():
response_Cou = requests.request("GET", url+key)
res=json.loads(response_Cou.text)
print(type(res))
#return res
#Get All Data As For Competitions
def Tea():
    response_Tea = requests.request("GET", url_Com+key)
    res=json.loads(response_Tea.text)
    return res
def Pla():
    response_Pla = requests.request("GET", url_Pla+key)
    res=json.loads(response_Pla.text)
    return res

Cou()
# A = Cou()
# for i in A:
#     print(i)