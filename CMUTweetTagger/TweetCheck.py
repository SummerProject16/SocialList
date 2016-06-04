import CMUTweetTagger as cmu
import wordsegment
import searchWeb

def checkTweetNums(tweets,minTweets):
	#number as adjective check
	count = 0
	processedtweets = []
	for line in tweets:
		processedtweets.append(" ".join(wordsegment.segment(line)))
	postags = cmu.runtagger_parse(processedtweets)
	print processedtweets
	for postag in postags:
		postag = "".join(postag)
		if "$N" in postag or "$^" in postag or "$M" in postag or "$Z" in postag:
			count += 1
	if count >= minTweets:
		return 1
	else:
		return 0

def checkTweetUrls(hashtag,urls,minUrls):
	#check urls for hashtag matching
	count = 0
	for url in urls:
		if searchWeb.searchforstring(url,wordsegment.segment(hashtag)):
			count+=1
	#TODO
	if count >= minUrls:
		return 1
	else:
		return 0

print checkTweetUrls("5waystoruindate",['http://www.glamour.com/story/5-words-that-will-ruin-a-date'],1)