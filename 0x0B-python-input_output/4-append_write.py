#!/usr/bin/python3
"""
This module contains a function that
writes a string to a text file (UTF8)
and returns the number of characters written
"""


def append_write(filename="", text=""):
    """function that
    writes a string to a text file (UTF8)
    and returns the number of characters written
    Args:
        filename (str, optional): path to file. Defaults to "".
        text (str, optional): text to write. Defaults to "".
    """
    with open(filename, encoding="utf-8", mode="a") as a_file:
        return (a_file.write(text))
