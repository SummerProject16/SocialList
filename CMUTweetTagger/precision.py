'''
@file : precision.py
@author (A) : Madhusai Ravada.
@project : Social List

program to find the precision of search results in google

This work is licensed under the
Creative Commons Attribution-NonCommercial-ShareAlike 4.0
International License. To view a copy of this license,
visit http://creativecommons.org/licenses/by-nc-sa/4.0/.
'''

import re
import urllib2 as ulib
import os
from nltk import PorterStemmer
import stemming.porter2
from wordsegment import segment
from searchWeb import searchgoogle
from socialListSettings import socialListProxy,socialListHttp_Proxy,socialListHttps_Proxy


def precisioncalc(query):
	print query,
	k = searchgoogle(query)
	seg = segment(query)
	m = []
	for n in seg:
		m.append(stemming.porter2.stem(n))
	seg = " ".join(m)
	if socialListProxy:
		proxy = ulib.ProxyHandler({'https': socialListHttps_Proxy, 'http': socialListHttp_Proxy})
		opener = ulib.build_opener(proxy)
		ulib.install_opener(opener)
	counter = 0
	total = 0
	for i in xrange(len(k)):
		req = ulib.Request(k[i], headers={'User-Agent': "Mozilla/5.0"})
		k[i] = segment(k[i])
		l = []
		for j in k[i]:
			l.append(stemming.porter2.stem(j))
		k[i] = " ".join(k[i])
		# print k[i]
		try:
			content = ulib.urlopen(req)
			x = re.findall("<\S*?title\S*?>(.*?)<\S*?/\S*?title\S*?>", content.read())
			t = []
			for s in x:
				t.append(stemming.porter2.stem(s))
			t = " ".join(t)
			# print t
			if ((seg in k[i]) or (seg in t)):
				counter = counter + 1
			total = total + 1
		except:
			pass

		if (total == 10):
			print str(counter)+"/"+str(total),
		if (total == 20):
			print str(counter)+"/"+str(total),


	if total < 10:
		print str(counter)+"/"+str(10), str(counter)+"/"+str(20)
	elif total < 20:
		print str(counter)+"/"+str(20)
	else:
		print ""
#precisioncalc("madhusai") #uncomment this to check the presion of some word