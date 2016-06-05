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

print checkTweetUrls("5waystoruindate",['http://www.glamour.com/story/5-words-that-will-ruin-a-date'],1)