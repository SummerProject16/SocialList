import re
import urllib2 as ulib
import wordsegment as ws


def getWeight(hashtag="",string=""):
	proxy = ulib.ProxyHandler({'https': 'https://10.3.100.207:8080','http' : 'http://10.3.100.207:8080'})
	opener = ulib.build_opener(proxy)
	ulib.install_opener(opener)
	spl_hash = ws.segment(hashtag)
	req = ulib.Request('https://www.google.com/search?q='+'+'.join(spl_hash), headers={'User-Agent' : "Mozilla/5.0"})
	dumpdata = ulib.urlopen(req).read()
	urls = re.findall("(http.*?)[\" ]",dumpdata)
	weight = 0
	url = len(urls)
	occurance = []
	for _url in urls:
		req = ulib.Request(_url,headers={'User-Agent' : "Mozilla/5.0"})
		try:
			pagedata = ulib.urlopen(req).read()
			pagedata = pagedata.lower()
			occurance = re.findall(string.lower(),pagedata)
			weight+=len(occurance)*url
		except:
			pass
		url-=1
	return weight


def getFrequency(filename=""):
	pass

if __name__ == "__main__":
	print getWeight("5waystokill","5 ways to kill")