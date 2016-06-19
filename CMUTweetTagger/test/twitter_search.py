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

	CONSUMER_KEY = "nCbw9X2vgTKy1Ngmp9Sun4WGc"
	CONSUMER_SECRET = "vwiRS1RhG1YPa94eqgoDHaL6XuVp2a9p1a2arwuXDBVw8MOUOz"
	OAUTH_TOKEN = "522650777-f7rc84IPDDopwOs98ODq7fnWbdlZ4LI5jcIr0hz1"
	OAUTH_TOKEN_SECRET = "ex3VEndDdbwhy2LyEG6S9n7flzNVBwBe2aKd3KAETNsg3"

	oauth2 = OAuth1(CONSUMER_KEY,
	               client_secret=CONSUMER_SECRET,
	               resource_owner_key=OAUTH_TOKEN,
	               resource_owner_secret=OAUTH_TOKEN_SECRET)

	auth.append(oauth2)
	
	CONSUMER_KEY = "ikWn6Y3GufSzdTQsx6EEnNg18"
	CONSUMER_SECRET = "a7oGslxpsD6QlMukY9QOyqRZYhKShM0uNDffb50R5MEkWAcncP"
	OAUTH_TOKEN = "522650777-55McpBP5ecmCaCQtorPfc8T9BpOgxwNpeO6lfZvW"
	OAUTH_TOKEN_SECRET = "1pDNcmdo8qUyAYtaNBNiExap53VGuofXWsmbI31iBAhG1"

	oauth3 = OAuth1(CONSUMER_KEY,
	               client_secret=CONSUMER_SECRET,
	               resource_owner_key=OAUTH_TOKEN,
	               resource_owner_secret=OAUTH_TOKEN_SECRET)

	auth.append(oauth3)

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
