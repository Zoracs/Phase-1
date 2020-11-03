import requests

def get_Discord_members():
    headers = {"Authorization": ""} #remember to add bot key
    try:  
        r = requests.get("https://discord.com/api/guilds//members?limit=99", headers=headers) #remember to add guild ID
    except:
        print("Discord API is currently unavailable.")
    sortedList = []
    print(str(r))
    for x in r.json():
        if x["nick"] is None:
           sortedList.append(x["user"]["username"])
        else:
            sortedList.append(x["nick"])
    for name in sortedList:
        print(name)
    return sortedList    
