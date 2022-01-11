import json
op = open( "Data\Text.txt" , "r")
out = op.read()
print(type(out))
jsn_Country = json.loads( out )
print(jsn_Country[1]["country_logo"])
