import json

with open('names.NAMES') as f:
    data = json.load(f)
    firstName = data["names"][0]["firstName"]
    surName = data["names"][1]["surName"]
    fullName = firstName + " " + surName

print("The stored name is " + fullName + ".")