import requests

def get_FC_members():
    try:
        r = requests.get("https://xivapi.com/freecompany/9228438586435663178?data=FCM")
    except:
        print("XIV.API is currently not responding.")
    sortedList = []
    for x in r.json()["FreeCompanyMembers"]:
        sortedList.append(x["Name"])
    for name in sortedList:
        print(name)
    return sortedList
