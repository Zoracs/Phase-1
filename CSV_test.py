# import csv
import os
import CSV1
import pytest


def test_if_input_for_list_is_None():
    empty_list = None
    with pytest.raises(ValueError):
        assert CSV1.CSV_list(empty_list, "FC-List")


def test_exception_if_list_is_empty():
    empty_list = []
    with pytest.raises(ValueError):
        assert CSV1.CSV_list(empty_list, "FC-List")


def test_exception_when_Filename_is_above_80_characters():
    Filename = "This Filename is way to long so it hopefully spits out an error eventually, hopefully, if at all or maybe not."
    with pytest.raises(ValueError):
        assert CSV1.CSV_list(["Dr Suna", "Freya Luna"], Filename)


def test_that_list_is_written_to_a_file():
    Filename = CSV1.CSV_list(["Dr Suna", "Ichiro", "Freya Luna"], "FC-List")
    File = open(Filename, "r")
    Result = File.read()
    File.close()
    os.remove(str(Filename))
    assert Result == "Dr Suna, Ichiro, Freya Luna"
