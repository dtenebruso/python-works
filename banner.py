#!/usr/bin/python

def banner(uName):
	ban_length = len(uName)

	new_length = ban_length +6
	lines = ("*"*new_length)

	print(lines)
	print("\n.::"+uName+"::.\n")
	print(lines)




name = input("What is your name? ")

banner(name)
