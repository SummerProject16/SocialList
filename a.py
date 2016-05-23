import re
import urllib2 as ulib

fileto = open("TopimdbMovies.txt", "w")

proxy = ulib.ProxyHandler({'https': "https://10.3.100.207:8080", 'http': "http://10.3.100.207:8080"})
opener = ulib.build_opener(proxy)
ulib.install_opener(opener)
req = ulib.Request('http://www.imdb.com/search/title?title_type=tv_series', headers={'User-Agent': "Mozilla/5.0"})
dumpdata = ulib.urlopen(req)

a = dumpdata.read()

data = re.findall('<td.*?title.*?>.*?<a.*?>(.*?)</a>.*?</td>', a,re.DOTALL)

for x in data:
    fileto.write(x + "\n")
    print x
