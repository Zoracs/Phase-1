import get_Discord_members
import get_FC_members
import CSV
import csv
import os

def get_lists(source):
    
    member_list = []
    if source == "Discord":
        member_list = get_Discord_members.get_Discord_members()
    if source == "XIV_API":
        member_list = get_FC_members.get_FC_members()
    filename = CSV.CSV_list(member_list, source)
    return_value = []
    with open(filename, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in csvreader:
            return_value = row
    os.remove(filename)
    return [item.strip(' ') for item in return_value]


def establish_relationship_between_the_lists():

    Discord_list = get_lists("Discord")
    FC_list = get_lists("XIV_API")
    completed_list = {}
    result = True
    for name in Discord_list:
        print(f"Who is {name} in the FC?")
        while result:
            if input() not in FC_list:
                print("Please input an existing name.")
            else:
                result = False
        completed_list[name] = input()
        result = True
    print(str(completed_list))


establish_relationship_between_the_lists()

