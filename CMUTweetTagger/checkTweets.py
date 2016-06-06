'''
@file : checkTweets.py
@author (A) : Madhu Kumar Dadi.
@project : Social List
@function :
	checkTweets(tweet,tweetsFile) :  checks tweets containing tweet in the tweetsFile
		@tweet :    hashtag to be checked
		@tweetsFile :   File containing hashtags
		return :    number validity and url validity from TweetCheck package and [2,2] if there are no tweets
@Licence :
	This work is licensed under the
	Creative Commons Attribution-NonCommercial-ShareAlike 4.0
	International License. To view a copy of this license,
	visit http://creativecommons.org/licenses/by-nc-sa/4.0/.
'''


import TweetCheck
import hashtag

def checkTweets(tweet,tweetsFile):
	#checks tweets containing tweet in the tweetsFile and returns number validity and url validity
	data = hashtag.getTweetsandUrls(tweet,tweetsFile)
	tweets = data[0]
	urls = data[1]
	if len(tweets) == 0:
		return [2,2] #if there are no tweets there is no checking
	numcheck = TweetCheck.checkTweetNums(tweets,30)
	urlcheck = TweetCheck.checkTweetUrls(tweet,urls,5)
	ret = []
	ret.append(numcheck)
	ret.append(urlcheck)
	return ret