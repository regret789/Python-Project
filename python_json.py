import json
file=open("list.py","r")
x=file.read()
finaldata=json.loads(x)

print(finaldata)