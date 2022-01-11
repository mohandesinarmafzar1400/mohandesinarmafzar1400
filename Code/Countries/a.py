import json
#f = open("Text.txt", "r")
b = open( "Text.txt" , "r")
a = b.read()
y = json.loads(a)

# import os

# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))