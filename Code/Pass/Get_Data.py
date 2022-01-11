import requests
import json

#Key Api
key = "8b077c33a92505c20da9bd1aba253b5f0835fb5ea63998d65b178bb0f39f70a3"

#Get All Data As For Country
def Countries():
    url_Cou = "https://apiv3.apifootball.com/?action=get_countries&APIkey="
    response_Cou = requests.request ( "GET" , url_Cou + key )
    res = json.loads ( response_Cou.text )
    return res

#Get All Data As For Competitions
def Competitions( id ):
    #complete in Function Competitions => {}
    url_Com = "https://apiv3.apifootball.com/?action=get_leagues&country_id={}&APIkey="
    url_Com = url_Com.format(id)
    response_Cou = requests.request ( "GET" , url_Com + key )
    res = json.loads ( response_Cou.text )
    return res

#Get All Data As For Teams
def Teams( id ):
    #complete in Function Teams => {}
    url_Tea = "https://apiv3.apifootball.com/?action=get_teams&league_id={}&APIkey="
    url_Tea = url_Tea.format( id )
    response_Tea = requests.request( "GET" , url_Tea+key )
    res = json.loads( response_Tea.text )
    return res

# #Get All Data As For Players
# def Player( id ):
#     #complete with Player ID in Funtion Pla => {}
#     url_Pla= "https://apiv3.apifootball.com/?action=get_players&player_id={}&APIkey="
#     url_Pla = url_Pla.format(id)
#     response_Pla = requests.request( "GET" , url_Pla + key )
#     res = json.loads( response_Pla.text )
#     return res
