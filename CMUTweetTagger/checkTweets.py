import tweetsorganised
import TweetCheck
import hashtag

def checkTweets(tweet):
	data = hashtag.getTweetsandUrls(tweet,"tweetsorganized1.txt")
	tweets = data[0]
	urls = data[1]
	if len(tweets) == 0:
		return [2,2]
	numcheck = TweetCheck.checkTweetNums(tweets,30)
	urlcheck = TweetCheck.checkTweetUrls(tweet,urls,5)
	ret = []
	ret.append(numcheck)
	ret.append(urlcheck)
	return ret