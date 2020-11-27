# import csv


def CSV_list(Username_list, Filename):
    File = open(f"{Filename}.csv", "w")
    lastEntry = len(Username_list) - 1
    if not Username_list:
        return "List is empty"
    else:
        for x in Username_list:
            # if not Username_list:
            #     return "List is empty"
            if x == Username_list[lastEntry]:
                File.write(x)
            # elif len(Username_list) == 0:
            #     raise ValueError("List is empty.")
            else:
                File.write(f"{x}, ")
    File.close()
    return f"{Filename}.csv"
