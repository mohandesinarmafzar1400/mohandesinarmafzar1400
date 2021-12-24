import requests
import json
#complete
url = "https://apiv3.apifootball.com/?action=get_countries&APIkey="
key = "8b077c33a92505c20da9bd1aba253b5f0835fb5ea63998d65b178bb0f39f70a3"
response = requests.request("GET", url+key)
res=json.loads(response.text)
print(res[0]["country_id"])