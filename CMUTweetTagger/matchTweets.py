'''
@file : hashtag.py
@author (A) : Madhu Kumar Dadi.
@project : Social List
@usage : checks presence of numbers in tweets in Big Data from tweets files, this is not used anywhere
@Licence :
	This work is licensed under the
	Creative Commons Attribution-NonCommercial-ShareAlike 4.0
	International License. To view a copy of this license,
	visit http://creativecommons.org/licenses/by-nc-sa/4.0/.
'''

import CMUTweetTagger as cmu
import wordsegment as ws

file1 = open()
file2 = open()

data1 = file1.read()
data2 = file2.read()

tweets1 = data1.split("\n\n")

hashtags = []

for tweet1 in tweets1:
	hashtag = tweet1.split("\n")[0]
	hashtags.append(" ".join(ws.segment(hashtag)))

postags = cmu.runtagger_parse(hashtags)

i=0

for postag in postags:
	if '$' in "".join(postag):
		i+=1