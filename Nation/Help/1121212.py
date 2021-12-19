# app.py

import json

json_string = '''
{
  "students": [
    {
      "name": "Millie Brown",
      "active": true,
      "rollno": 11
    },
    {
      "name": "Sadie Sink",
      "active": true,
      "rollno": 10
    }
  ]
}
'''
stud_obj = json.loads(json_string)
json_obj = json.dumps(stud_obj)
print(json_obj[0])

