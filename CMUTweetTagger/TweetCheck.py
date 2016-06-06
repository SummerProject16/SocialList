'''
@file : TweetCheck.py
@author (A) : Madhu Kumar Dadi.
@project : Social List
@function :
	checkTweetNums(tweets,minTweets) :    checks the presence of number as adjectives in the tweet
		@tweets :   list of tweets that are to be checked for presence of number
		@minTweets :    minimum number of tweets that are to be present to return 1
		return :    0 if count is less than minTweets else 1
@function :
	checkTweetUrls(hashtag,urls,minUrls) :  checks the presence of hashtag in the Url Page
		@hashtag :  hashtag to be searched
		@urls : list of urls that are to be checked
		@minUrls :   minimum number of urls that has to contain hashtag
		return :    0 if count is less than minUrls else 1
@Licence :
	This work is licensed under the
	Creative Commons Attribution-NonCommercial-ShareAlike 4.0
	International License. To view a copy of this license,
	visit http://creativecommons.org/licenses/by-nc-sa/4.0/.
'''

import CMUTweetTagger as cmu
import wordsegment
import urllib2 as ulib

def checkTweetNums(tweets,minTweets):
	#number as adjective check
	count = 0
	processedtweets = []
	for line in tweets:
		processedtweets.append(" ".join(wordsegment.segment(line)))
	postags = cmu.runtagger_parse(processedtweets)
	for postag in postags:
		postag = "".join(postag)
		if "$N" in postag or "$^" in postag or "$M" in postag or "$Z" in postag:
			#Checking for Consecutive numbers and Nouns
			count += 1
	if count >= minTweets:
		return 1
	else:
		return 0

def checkTweetUrls(hashtag,urls,minUrls):
	#check urls for hashtag matching
	count = 0
	for url in urls:
		proxy = ulib.ProxyHandler({'http': "http://10.3.100.207:8080",'https': "https://10.3.100.207:8080"})
		opener = ulib.build_opener(proxy)
		ulib.install_opener(opener)
		req = ulib.Request(url, headers={'User-Agent' : "Mozilla/5.0"})
		#Getting data from the url
		dumpdata=ulib.urlopen(req)
		dump = dumpdata.read()
		if True: #Will include Jaccard here for match %
			count+=1
	#TODO
	if count >= minUrls:
		return 1
	else:
		return 0

#print checkTweetUrls("5waystoruindate",['http://www.glamour.com/story/5-words-that-will-ruin-a-date'],1)