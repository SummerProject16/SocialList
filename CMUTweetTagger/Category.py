'''
@file : Category.py
@author (A) : Madhu Kumar Dadi.
@project : Social List
@function :
	checkCategories(hashtag) :  compares the hashtag to all the categories
		@hashtag :  string representing a twitter hashtag
		return : 1 if atleast one matches else 0
@function :
	test() :    Tests all the categories with an example each
		return :    None
@Licence :
	This work is licensed under the
	Creative Commons Attribution-NonCommercial-ShareAlike 4.0
	International License. To view a copy of this license,
	visit http://creativecommons.org/licenses/by-nc-sa/4.0/.
'''

import re
import wordsegment as ws

def checkCategories(hashtag):
	matches =[]
	hashtag = " ".join(ws.segment(hashtag))
	matches.append(re.match(".+?in\s\d+\swords",hashtag))
	matches.append(re.match(".+?in\s\d+\ssentences",hashtag))
	matches.append(re.match(".*?\d+\sreasons.+",hashtag))
	matches.append(re.match(".*?\d+\swords\sto.+",hashtag))
	matches.append(re.match("^reasons\s.+",hashtag))
	matches.append(re.match(".*?ways\sto.+",hashtag))
	matches.append(re.match(".*?how\sto.+",hashtag))
	matches.append(re.match(".*?\d+\sways\sto.+",hashtag))
	matches.append(re.match(".*?\d+\sthings\sto.+",hashtag))
	matches.append(re.match("^things.+",hashtag))
	matches.append(re.match("^describe.*?in.*?",hashtag))
	matches.append(re.match("^name\ssome.+?",hashtag))
	#Add new catogories if found any
	for match in matches:
		if match:
			return 1
	return 0

def test():
	print "proposalin5words",checkCategories("proposalin5words")
	print "8reasonstohateiphone",checkCategories("8reasonstohateiphone")
	print "5wordstoremember",checkCategories("5wordstoremember")
	print "reasonstohateandroid",checkCategories("reasonstohateandroid")
	print "fewwaystobeasuccessfulman",checkCategories("fewwaystobeasuccessfulman")
	print "describehowtobuildahouse",checkCategories("describehowtobuildahouse")
	print "Idareyoutotell5waystohackfbpassword",checkCategories("Idareyoutotell5waystohackpassword")
	print "5thingstoworryonchristmas",checkCategories("5thingstoworryonchristmas")
	print "thingstoremember",checkCategories("thingstoremember")
	print "describeX-Meninthreesentences",checkCategories("describeX-Meninthreesentences")
	print "NameSomeBestHeroesYouKnow",checkCategories("NameSomeBestHeroesYouKnow")

#test()#remove # in the beginning to test