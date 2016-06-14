#program to check if how many results differ by k
import re
import urllib2 as ulib
import os
from nltk import PorterStemmer
import stemming.porter2
from wordsegment import segment
from searchWeb import searchgoogle
from collections import Counter
from socialListSettings import socialListProxy,socialListHttp_Proxy,socialListHttps_Proxy

#searching in google
def k_list_repeat(query):
	k = searchgoogle(query)
	m = []

	if socialListProxy:
		proxy = ulib.ProxyHandler({'https': socialListHttps_Proxy, 'http': socialListHttp_Proxy})
		opener = ulib.build_opener(proxy)
		ulib.install_opener(opener)

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
			#reading the title of url
			x = re.findall("<\S*?title\S*?>(.*?)<\S*?/\S*?title\S*?>", content.read())
			t = []
			for s in x:
				t.append(stemming.porter2.stem(s))
			t = " ".join(t)
			m.append(t)

		except:
			pass
	return m

arr_contain_numbers = []
l = k_list_repeat("placesinindia")

#print l
for j in xrange(len(l)):
	if(any(char.isdigit() for char in l[j])):
		line_nonum = ''.join([i for i in l[j] if not i.isdigit()])
		arr_contain_numbers.append(line_nonum)

arr_repeat = []
for i in xrange(len(arr_contain_numbers)):
	k = arr_contain_numbers.count(arr_contain_numbers[i])
	if(k>1):arr_repeat.append(arr_contain_numbers[i])

li = Counter(arr_repeat)
for x in li:
	print x,li[x]
#prints the line and number of times it repeats
