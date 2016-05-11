import re
import urllib2 as ulib


def searchgoogle(text):
    text = text.replace(" ","+")
    proxy = ulib.ProxyHandler({'https': "https://10.3.100.207:8080"})
    opener = ulib.build_opener(proxy)
    ulib.install_opener(opener)
    req = ulib.Request('https://google.com/search?q='+text, headers={'User-Agent' : "Mozilla/5.0"})
    dumpdata=ulib.urlopen(req)
    data = re.findall('href=\"/url\?q=(.*?)\"',dumpdata.read())
    retdata = []
    for url in data:
        url=ulib.unquote(url).decode('utf-8')
        url = url.split("&")
        retdata.append(url[0])
    return retdata

def searchforstring(url,stringlist):
    proxy = ulib.ProxyHandler({'http': "http://10.3.100.207:8080",'https': "https://10.3.100.207:8080"})
    opener = ulib.build_opener(proxy)
    ulib.install_opener(opener)
    req = ulib.Request(url, headers={'User-Agent' : "Mozilla/5.0"})
    dumpdata=ulib.urlopen(req)
    dump = dumpdata.read()
    for string in stringlist:
        if string in dump:
            continue
        else:
            return False
    return True