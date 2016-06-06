'''
@file : tweetsorganised.py
@author (A) : Madhu Kumar Dadi.
@project : Social List

This file is not being used anywhere

@Licence :
	This work is licensed under the
	Creative Commons Attribution-NonCommercial-ShareAlike 4.0
	International License. To view a copy of this license,
	visit http://creativecommons.org/licenses/by-nc-sa/4.0/.
'''

import re

def containsurl(string):
	return re.search("http.+?\..+?",string)

def containsnum(string):
	return re.search("\s\d+\s",string)

def tweettypesearch(filename,tweet):
	file1 = open(filename)
	data = file1.read()
	data = data.lower()
	tweetsdata = data.split("\n\n")
	for hashtag in tweetsdata:
		tweets = hashtag.split("\n")
		if tweets[0] == tweet.lower():
			if len(tweets)>1:
				count = 0
				for i in xrange(1,len(tweets)):
					actTweet=tweets[i].split("\t")[3]
					if containsurl(actTweet) or containsnum(actTweet):
						#Checking if the tweet contains either a number or a Url
						count+=1
				if count > 20:
					return 1
				else:
					return 0
			else:
				return 0
	return 2