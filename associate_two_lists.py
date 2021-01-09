import get_Discord_members
import get_FC_members
import CSV1
import csv
import os


def get_lists(source):

    member_list = []
    if source == "Discord":
        member_list = get_Discord_members.get_Discord_members()
    if source == "XIV_API":
        member_list = get_FC_members.get_FC_members()
    filename = CSV1.CSV_list(member_list, source)
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
    correct_name = None
    for name in Discord_list:
        print(f"Who is {name} in the FC?")
        stupid_answer = 0
        while result:
            answer = input()
            if stupid_answer == 10:
                return 'Nope, try again next time.'
            if answer not in FC_list:
                print("Please input an existing name.")
                stupid_answer += 1
            else:
                correct_name = answer
                print("name added")
                result = False
        completed_list[name] = correct_name
        result = True
    return completed_list
