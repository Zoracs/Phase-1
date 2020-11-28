# import csv


def CSV_list(Username_list, Filename):
    if not Username_list:
        raise ValueError("Your input was not a list.")
    if len(Filename) > 80:
        raise ValueError("Your Filename is too long, mate.")
    File = open(f"{Filename}.csv", "w")
    lastEntry = len(Username_list) - 1
    for x in Username_list:
        if x == Username_list[lastEntry]:
            File.write(x)
        else:
            File.write(f"{x}, ")
    File.close()
    return f"{Filename}.csv"
