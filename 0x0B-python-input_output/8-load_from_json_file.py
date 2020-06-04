#!/usr/bin/python3
"""
This module contains a function
that creates an Object from a “JSON file
"""
import json


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file
    Returns:
        obj: Python data structure
    """
    with open(filename) as write_file:
        my_obj = json.load(write_file)
    return my_obj
