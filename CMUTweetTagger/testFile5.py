'''
@file : testFile5.py
@author (A) : Madhu Kumar Dadi.
@project : Social List
@function :
	numbercount(postags) :  checks for the presence of numbers(eg. five, 5) in the hashtag
		@postags :  a list containing pos tags for a hashtag
		return :    1 if it contains number(s) else 0
@function :
	prepositioncount(postags) : checks the number of prepositions present in the hashtag
		@postags :  a list containing pos tags for a hashtag
		return :    count of prepositions
@function :
	conjunctioncount(postags) : checks the number of conjuctions present in the hashtag
		@postags :  a list containing pos tags for a hashtag
		return :    count of conjunctions
@funtion :
	interjectioncount(postags) :    checks the number of interjections present in the hashtag
		@postags :  a list containing pos tags for a hashtag
		return :    count of interjections
@Licence :
	This work is licensed under the
	Creative Commons Attribution-NonCommercial-ShareAlike 4.0
	International License. To view a copy of this license,
	visit http://creativecommons.org/licenses/by-nc-sa/4.0/.
'''

from collections import Counter

def numbercount(postags):
	postagsent = "".join(postags)
	count = Counter(postagsent)
	if count['$'] == 0:
		return "0"
	return "1"

def prepositioncount(postags):
	postagsent = "".join(postags)
	count = Counter(postagsent)
	if count['P'] == 0:
		return "0"
	return count['&']

def conjuctioncount(postags):
	postagsent = "".join(postags)
	count = Counter(postagsent)
	if count['&'] == 0:
		return "0"
	return count['&']

def interjectioncount(postags):
	postagsent = "".join(postags)
	count = Counter(postagsent)
	if count['!'] == 0:
		return "0"
	return count['!']
