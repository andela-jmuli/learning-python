"""
Task:
You are given a string. Split the string on a " " (space) delimiter
and join using a - hyphen.

Input Format :
The first line contains a string consisting of space separated words.

Output Format 
Print the formatted string as explained above.

"""

def splitter(string):
	
	spaced_out = string.split(" ")

	hyphenated = "-".join(string)

	print spaced_out
	print hyphenated




splitter('Batman is the legend')