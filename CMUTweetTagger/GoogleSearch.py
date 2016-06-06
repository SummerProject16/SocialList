'''
@file : GoogleSearch.py
@author (A) : Madhu Kumar Dadi.
@project : Social List
@Usage :    python GoogleSearch.py finallist.txt finallist.arff

This scripts searches all the hashtags in file finallist.txt and outputs the
popularity and precision for first 10 and 20 urls and outputs them in comma seperated
format to the finallist.arff file

@Licence :
	This work is licensed under the
	Creative Commons Attribution-NonCommercial-ShareAlike 4.0
	International License. To view a copy of this license,
	visit http://creativecommons.org/licenses/by-nc-sa/4.0/.
'''

from sys import argv

import testFile14
import CMUTweetTagger as cmu
import wordsegment as ws

file = open(argv[1]) #file containing socialList and nonsocialList hashtags
tofile = open(argv[2], "w") #file that takes the arff output
tofile.close()
idiomsEx = file.readlines()
sociallists = []

for line in idiomsEx:
	sociallists.append(line.replace("\n", ""))

parsedSociallists = []

for line in sociallists:
	parsedSociallists.append(" ".join(ws.segment(line)))

postags = cmu.runtagger_parse(parsedSociallists)

'''
file output would be in the format of popularity,precision at 10,precision at 20 in each line for every hashtag

This takes a lot of time to run.
'''

for ParsedTag, postag in zip(parsedSociallists, postags):
	tofile = open(argv[2], "a")
	a = testFile14.test14(ParsedTag, postag)
	#checks the hashtag in google and returns list of its popularity precision at 10 urls and 20 urls
	print str(a[0]) + "," + str(a[1]) + "," + str(a[2])
	tofile.write(str(a[0]) + "," + str(a[1]) + "," + str(a[2]) + "\n")
	tofile.close()
