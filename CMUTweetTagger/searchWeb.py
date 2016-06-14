'''
@file : searchWeb.py
@author (A) : Madhu Kumar Dadi.
@project : Social List
@function :
	searchgoogle(text) : Searches google for the text
		@text : the text that is to be searched
		return :    a List containing urls from google search
@function :
	searchforstring(url,stringlist) :   searches for items in stringlist in the web page at url
		@url :  Url where the strings are to be searched
		@stringlist :   List of strings to be searched in the url
		return :    returns True if all the items in stringlist are present in the web page at url else 0
@Licence :
	This work is licensed under the
	Creative Commons Attribution-NonCommercial-ShareAlike 4.0
	International License. To view a copy of this license,
	visit http://creativecommons.org/licenses/by-nc-sa/4.0/.
'''

import re
import urllib2 as ulib
from socialListSettings import socialListProxy,socialListHttp_Proxy,socialListHttps_Proxy


#search for a string using google
def searchgoogle(text):
	#repalcing the spaces with "+"
	text = text.replace(" ","+")
	if socialListProxy:
		proxy = ulib.ProxyHandler({'https': socialListHttps_Proxy,'http' : socialListHttp_Proxy})
		opener = ulib.build_opener(proxy)
		ulib.install_opener(opener)
	req = ulib.Request('https://google.com/search?q='+text, headers={'User-Agent' : "Mozilla/5.0"})
	#opening the url
	dumpdata=ulib.urlopen(req)
	#finding urls
	data = re.findall('href=\"/url\?q=(.*?)\"',dumpdata.read())
	retdata = []
	#storing urls
	for url in data:
		url=ulib.unquote(url).decode('utf-8')
		url = url.split("&")
		retdata.append(url[0])
	return retdata
#seaching for a string in a url
def searchforstring(url,stringlist):

	if socialListProxy:
		proxy = ulib.ProxyHandler({'http': socialListHttp_Proxy,'https': socialListHttps_Proxy})
		opener = ulib.build_opener(proxy)
		ulib.install_opener(opener)
	req = ulib.Request(url, headers={'User-Agent' : "Mozilla/5.0"})
	dumpdata=ulib.urlopen(req)
	dump = dumpdata.read()
	for string in stringlist:
		if string.lower() in dump.lower():
			continue
		else:
			return False
	return True
