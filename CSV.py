# import csv


def CSV_list(Username_list, Filename):
    File = open(f"{Filename}.csv", "w")
    lastEntry = len(Username_list) - 1
    if len(Filename) > 80:
        raise ValueError("Your Filename is too long, mate.")
    if len(Username_list) == 0:
        raise ValueError("Your list is empty.")
    # if not Username_list:
    #     return "List is empty"
    else:
        for x in Username_list:
            if x == Username_list[lastEntry]:
                File.write(x)
            else:
                File.write(f"{x}, ")
    File.close()
    return f"{Filename}.csv"
