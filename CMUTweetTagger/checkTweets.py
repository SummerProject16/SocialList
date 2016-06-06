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