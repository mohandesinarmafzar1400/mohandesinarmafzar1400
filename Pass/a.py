import json
b = open( "Data\Countries.txt" , "r")
a = b.read()
jsn_Country = json.loads(a)


