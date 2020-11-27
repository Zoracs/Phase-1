import csv
import os
import CSV

def test_exception_if_list_is_empty():
    empty_list = []
    assert CSV.CSV_list(empty_list, "FC-List")


def test_that_list_is_written_to_a_file():
    Filename = CSV.CSV_list(["Dr Suna", "Ichiro", "Freya Luna"], "FC-List")
    File = open(Filename, "r")
    Result = File.read()
    File.close()
    os.remove(str(Filename))
    assert Result == "Dr Suna, Ichiro, Freya Luna"


