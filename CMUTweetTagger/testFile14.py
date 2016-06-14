'''
@file : testFile14.py
@author (A) : Madhu Kumar Dadi.
@project : Social List
@function :
	test14(parsedTag,postag) :  Searches parsedTag on google for popularity and precision at 10 and 20 urls
		@parsedTag :    hashtag that is searched on google
		@postag :   pos tags of the parsedTag
		return :    a list containing google search popularity and precision at 10 and 20 urls of the parsedTag
This work is licensed under the
Creative Commons Attribution-NonCommercial-ShareAlike 4.0
International License. To view a copy of this license,
visit http://creativecommons.org/licenses/by-nc-sa/4.0/.
'''

import searchWeb
import stemming
import stemming.porter2
import urllib2 as ulib
from wordsegment import segment
import re
from socialListSettings import socialListProxy,socialListHttp_Proxy,socialListHttps_Proxy


# def checkall(postags,parsedSociallists):
# 	j = 0
# 	urlsfile = open("urls.txt","w")
# 	for line in parsedSociallists:
# 		print line,
# 		nounpart = []
# 		k = 0
# 		splitline = line.split()
# 		for x in postags[j]:
# 			if (x is 'M' or x is '^' or x is 'Z'):
# 				nounpart.append(splitline[k])
# 			k += 1
# 		while True:
# 			try:
# 				googledata = searchWeb.searchgoogle(line)
# 				break
# 			except:
# 				continue
# 		urlsfile.write(line+"\n"+str(googledata)+"\n")
# 		count = 0
# 		if " ".join(nounpart) == "":
# 			j+=1
# 			print "2"
# 			continue
# 		i = 1
# 		for site in googledata:
# 			try:
# 				if searchWeb.searchforstring(site,nounpart):
# 					count += 1
# 			except:
# 				print "",
# 			i += 1
# 			if i > 10:
# 				break
# 		if count > 5:
# 			print "1"
# 		else:
# 			print "0"
# 		j += 1

def test14(parsedTag,postag):
	nounpart = []
	k = 0
	ret = []
	splitline = parsedTag.split()
	for x in postag:
		if (x is 'M' or x is '^' or x is 'Z'):
			nounpart.append(splitline[k])
		k+= 1

	if " ".join(nounpart) == "":
		ret.append(2)
	while True:
		try:
			googledata = searchWeb.searchgoogle(parsedTag)
			#gets all the urls for the hashtag on google search
			break
		except:
			continue
	count = 0
	i = 1
	for site in googledata:
		try:
			if searchWeb.searchforstring(site,nounpart):
				#checks if the hashtag noun parts are popular by counting the number of websites they are present
				count += 1
		except:
			pass
		i += 1
		if i > 10:
			break
	if count > 5:
		ret.append(1)
	else:
		ret.append(0)
	seg = parsedTag.split()
	m = []
	for n in seg:
		m.append(stemming.porter2.stem(n))
	seg = " ".join(m)

	if socialListProxy:

		proxy = ulib.ProxyHandler({'http': socialListHttp_Proxy, 'https': socialListHttps_Proxy})
		opener = ulib.build_opener(proxy)
		ulib.install_opener(opener)

	counter = 0
	total = 0
	for site in googledata:
		req = ulib.Request(site, headers={'User-Agent': "Mozilla/5.0"})
		site = segment(site)
		l = []
		for j in site:
			l.append(stemming.porter2.stem(j))
		site = " ".join(l)
		try:
			content = ulib.urlopen(req)
			x = re.findall("<\S*?title\S*?>(.*?)<\S*?/\S*?title\S*?>", content.read())
			#searches for a match of hastag in the title and url of every page
			t = []
			for s in x:
				t.append(stemming.porter2.stem(s))
			t = " ".join(t)
			if ((seg in site) or (seg in t)):
				counter = counter + 1
			total = total + 1
		except:
			pass

		if (total == 10):
			ret.append("%.4f"%(float(counter)/total))
		if (total == 20):
			ret.append("%.4f"%(float(counter)/total))
			break

	if total < 10:
		ret.append("%.4f"%(float(counter)/10.0))
		ret.append("%.4f"%(counter/20.0))
	elif total < 20:
		ret.append("%.4f"%(float(counter)/20.0))
	return ret