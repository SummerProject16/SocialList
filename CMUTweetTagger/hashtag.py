'''
@file : hashtag.py
@author (A) : Madhu Kumar Dadi.
@project : Social List
@function :
	getTweetsandUrls(hashtag,tweetsFilename) : checks for Tweets and Urls containing the hashtag
		@hashtag :  the hashtag that is to be checked
		@tweetsFilename :   File containing tweets to check for hashtag
		return :    list containing a list of Tweets and a list of Urls
@Licence :
	This work is licensed under the
	Creative Commons Attribution-NonCommercial-ShareAlike 4.0
	International License. To view a copy of this license,
	visit http://creativecommons.org/licenses/by-nc-sa/4.0/.
'''

#from collections import Counter
import re

#
# def seperateTweets():
# 	file = open('../tweet1lk.txt', 'r')
# 	data = file.readlines()
# 	hastags = []
# 	regex = r'#([a-z0-9!@$%&\-_?,.]+)'
# 	pattern = re.compile(regex)
# 	for line in data:
# 		sites = re.findall(pattern, line.lower())
# 		hastags += sites
#
# 	counter = Counter(hastags)
# 	file1 = open("tweetsorganized.txt","w")
# 	file1.close()
# 	data = "".join(data).lower()
# 	i =0
# 	for y in counter:
# 		print i
# 		i+=1
# 		if len(y)>=8:
# 			file1 = open("tweetsorganized.txt","a")
# 			file1.write(y+"\n")
# 			pattern1 = "(^.*?[#]"+y+"\s.*?$)"
# 			tweets = set(re.findall(pattern1,data,re.MULTILINE))
# 			for x in tweets:
# 				if len(x) > 30:
# 					file1.write(x.replace("\n","")+"\n")
# 			file1.write("\n")
# 			file1.close()


def getTweetsandUrls(hashtag,tweetsFilename):
	fileopen = open(tweetsFilename)
	allTweets = fileopen.read()
	pattern1 = "(^.*?[#]"+hashtag.lower()+"\s.*?$)"
	#matches all lines containing the hashtag
	tweets = set(re.findall(pattern1,allTweets.lower(),re.MULTILINE))
	processedTweets = []
	processedUrls = []
	for x in tweets:
		pattern2 = "(http\S+)"
		urls = set(re.findall(pattern2,x))
		if len(urls) > 0:
			processedUrls += urls
		processed = ''
		for y in x:
			if ord(y) < 128:
				processed += y
		#Getting only the tweet part
		processedTweets.append(processed)
	fileopen.close()
	processedTweetsandUrls = []
	processedTweetsandUrls.append(processedTweets)
	processedTweetsandUrls.append(processedUrls)
	return processedTweetsandUrls

#print getTweetsandUrls("askdirectioner","tweetsorganized2.txt")