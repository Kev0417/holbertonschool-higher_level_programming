#!/usr/bin/python3
"""
This module contains a function that
writes an Object to a text file, using
a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes
    an Object to a text file,
    using a JSON representation
    Returns:
        str: JSON
    """
    with open(filename, mode="w") as write_file:
        json.dump(my_obj, write_file)
