'''
@file : twitter_search.py
@author (A) : Madhu Kumar Dadi.
@project : Social List
@function :
	search(hashtag) :
		@hashtag :  hashtag to search
		return :    tweets containing hashtags
@function :
	putSearchDataToFile(filename) : Prints the tweets obtained for the hashtags in the file provided to [i]tweets.txt
		@filename : File containing hashtags seperated by new line character
		return :    none
@Licence :
	This work is licensed under the
	Creative Commons Attribution-NonCommercial-ShareAlike 4.0
	International License. To view a copy of this license,
	visit http://creativecommons.org/licenses/by-nc-sa/4.0/.
'''

import urllib
import requests as rq
from requests_oauthlib import OAuth1
import json
import time
import sys

sys.path.append('../')

from socialListSettings import socialListProxy,socialListHttp_Proxy,socialListHttps_Proxy


twitterAuthCheck = 0

def search(hashtag):
	CONSUMER_KEY = "eCOrAJmP6PsNo1B86xwjA0aOJ"
	CONSUMER_SECRET = "kjL8ssd6Y9RQsMcEOoZMj9od35ZDZZ08z3cbEzSK6vHjEtRHSC"
	OAUTH_TOKEN = "737867543415820288-cdObK8qk2R0mm5oytmf8wyEUi2uPIbP"
	OAUTH_TOKEN_SECRET = "bQzp78X59hd3oW7XDc7TlRn36xR7T4890eCJ52gjNADrJ"

	auth = []

	oauth1 = OAuth1(CONSUMER_KEY,
	               client_secret=CONSUMER_SECRET,
	               resource_owner_key=OAUTH_TOKEN,
	               resource_owner_secret=OAUTH_TOKEN_SECRET)

	auth.append(oauth1)

'''	CONSUMER_KEY = "fill consumer key"
	CONSUMER_SECRET = "fill consumer secret"
	OAUTH_TOKEN = "fill access token key"
	OAUTH_TOKEN_SECRET = "fill token secret"

	oauth2 = OAuth1(CONSUMER_KEY,
	               client_secret=CONSUMER_SECRET,
	               resource_owner_key=OAUTH_TOKEN,
	               resource_owner_secret=OAUTH_TOKEN_SECRET)

	auth.append(oauth2)
	
	CONSUMER_KEY = "fill consumer key"
	CONSUMER_SECRET = "fill consumer secret"
	OAUTH_TOKEN = "fill access token"
	OAUTH_TOKEN_SECRET = "Fill token secret"

	oauth3 = OAuth1(CONSUMER_KEY,
	               client_secret=CONSUMER_SECRET,
	               resource_owner_key=OAUTH_TOKEN,
	               resource_owner_secret=OAUTH_TOKEN_SECRET)

	auth.append(oauth3)'''

	global twitterAuthCheck

	try:
		while True:
			hashtag = urllib.quote_plus("#"+hashtag.replace("\n", "").lower())
			if socialListProxy:
				proxies = {
					'http' : socialListHttp_Proxy,
					'https' : socialListHttps_Proxy
				}
				r = rq.get(url="https://api.twitter.com/1.1/search/tweets.json?q=" + hashtag+"&lang=en", auth=auth[twitterAuthCheck],proxies=proxies)
			else:
				r = rq.get(url="https://api.twitter.com/1.1/search/tweets.json?q=" + hashtag+"&lang=en", auth=auth[twitterAuthCheck])

			if r.status_code == 200:
				break

		
			twitterAuthCheck = (twitterAuthCheck+1)%len(auth)
			print "auth changed."

		return r.content
	except:
		pass


def putSearchDataToFile(filename):
	filein = open(filename)
	hashtags = filein.readlines()

	i=0
	for hashtag in hashtags:
		try:
			jsondata = json.loads(search(hashtag))
			for j in xrange(len(jsondata['statuses'])):
				try:
					tempfile = open(str((i)/100)+"tweet.txt")
				except:
					tempfile = open(str((i)/100)+"tweet.txt","w")
					tempfile.close()
					tempfile = open(str((i)/100)+"tweet.txt")
				tempdata = tempfile.readlines()
				tempfile.close()
				fileout = open(str((i)/100)+"tweet.txt","a")
				if jsondata['statuses'][j]['text'].replace("\n"," ")+"\n" not in tempdata:
					fileout.write(jsondata['statuses'][j]['text'].replace("\n"," ")+"\n")
				fileout.close()
		except:
			pass
		print i
		i+=1


putSearchDataToFile("../finallist.txt")
