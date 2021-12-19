import requests
import json
key="3980369688e7fb941e68bad8dbbdb384dd7bde8a3c9a7b39c0d02265843ef864"
url = "https://apiv3.apifootball.com/?action=get_countries&APIkey="

response = requests.request("GET", url+key)
res=json.loads(response.text)
print(res[0]["country_id"])
print(type(res[0]))