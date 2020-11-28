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
