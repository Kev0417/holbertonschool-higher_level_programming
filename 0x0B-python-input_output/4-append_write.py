#!/usr/bin/python3
"""
	This module contains a function that
writes a string to a text file (UTF8)
	and returns the number of characters written
	"""


	def append_write(filename="", text=""):
	"""
	function that
writes a string to a text file (UTF8)
	and returns the number of characters written
	"""
	with open(filename, encoding="utf-8", mode="a") as a_file:
return (a_file.write(text))
