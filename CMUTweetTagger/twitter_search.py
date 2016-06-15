'''
@file : twitter_search.py
@author (A) : Madhu Kumar Dadi.
@project : Social List
@function :
	search(hashtag) :
		@hashtag :  hashtag to search
		return :    returns tweets containing hashtags
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
from socialListSettings import socialListProxy,socialListHttp_Proxy,socialListHttps_Proxy


def search(hashtag):
	CONSUMER_KEY = "eCOrAJmP6PsNo1B86xwjA0aOJ"
	CONSUMER_SECRET = "kjL8ssd6Y9RQsMcEOoZMj9od35ZDZZ08z3cbEzSK6vHjEtRHSC"
	OAUTH_TOKEN = "737867543415820288-cdObK8qk2R0mm5oytmf8wyEUi2uPIbP"
	OAUTH_TOKEN_SECRET = "bQzp78X59hd3oW7XDc7TlRn36xR7T4890eCJ52gjNADrJ"

	oauth1 = OAuth1(CONSUMER_KEY,
	               client_secret=CONSUMER_SECRET,
	               resource_owner_key=OAUTH_TOKEN,
	               resource_owner_secret=OAUTH_TOKEN_SECRET)

	auth = oauth1

	CONSUMER_KEY = "eCOrAJmP6PsNo1B86xwjA0aOJ"
	CONSUMER_SECRET = "kjL8ssd6Y9RQsMcEOoZMj9od35ZDZZ08z3cbEzSK6vHjEtRHSC"
	OAUTH_TOKEN = "737867543415820288-cdObK8qk2R0mm5oytmf8wyEUi2uPIbP"
	OAUTH_TOKEN_SECRET = "bQzp78X59hd3oW7XDc7TlRn36xR7T4890eCJ52gjNADrJ"

	oauth2 = OAuth1(CONSUMER_KEY,
	               client_secret=CONSUMER_SECRET,
	               resource_owner_key=OAUTH_TOKEN,
	               resource_owner_secret=OAUTH_TOKEN_SECRET)

	try:
		while True:
			hashtag = urllib.quote_plus("#"+hashtag.replace("\n", "").lower())
			if socialListProxy:
				proxies = {
					'http' : socialListHttp_Proxy,
					'https' : socialListHttps_Proxy
				}
				r = rq.get(url="https://api.twitter.com/1.1/search/tweets.json?q=" + hashtag+"&lang=en", auth=auth,proxies=proxies)
			else:
				r = rq.get(url="https://api.twitter.com/1.1/search/tweets.json?q=" + hashtag+"&lang=en", auth=auth)
			if r.status_code == 200:
				break
			if auth == oauth1:
				auth == oauth2
			else:
				auth = oauth1
		return r.content
	except:
		pass


def putSearchDataToFile(filename):
	filein = open(filename)
	hashtags = filein.readlines()

	i=0
	for hashtag in hashtags:
		fileout = open(str((i)%100)+"tweets.txt","a")
		try:
			jsondata = json.loads(search(hashtag))
			for i in xrange(len(jsondata['statuses'])):
				fileout.write(jsondata['statuses'][i]['text'])
		except:
			pass
		fileout.close()
		i+=1