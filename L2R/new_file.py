import urllib2 as ulib
from bs4 import BeautifulSoup
import re
import wordsegment as ws
from sets import Set

def get_length(text,text_list):
	return len([s for s in text_list if text in s.lower()])


def replace_non_utf8(text):
	return ''.join([i if ord(i) < 128 else '' for i in text])

def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', element):
        return False
    return True

def get_text_from_url(url):
	# this function will return all the visible text without the non utf-8 text and without trailing \n  from the suppllied url
	html = ulib.urlopen(url).read().decode('utf-8', 'ignore')
	soup = BeautifulSoup(html, 'html.parser')
	texts = soup.findAll(text=True)
	visible_texts = filter(visible, texts)
	text_list = [str(replace_non_utf8(text.strip('\n').strip())) + '\n' for text in visible_texts]
	text_list = [text for text in text_list if text != '\n']
	return text_list

def get_occurence_list(url,text_file):
	# this function will give list of number of occurence all the words from the manula text created in the web url 
	# first it will extract the visible text from the url and then find the total occurence  
	text_list_url = get_text_from_url(url)
	with open(text_file,'r') as infile:
		text_list = infile.readlines()

	text_list = [str(replace_non_utf8(text.strip('\n').strip())) for text in text_list]

	return [get_length(text.lower(),text_list_url) for text in text_list]



def getWeight(hashtag,text_file):
	#this function returns a list of weights of the strings in the text_file
	#proxy_handler
	proxy = ulib.ProxyHandler({'https': 'https://10.3.100.207:8080','http' : 'http://10.3.100.207:8080'})
	opener = ulib.build_opener(proxy)
	ulib.install_opener(opener)
	#split the hashtag into words
	spl_hash = ws.segment(hashtag)
	req = ulib.Request('https://www.google.co.in/search?q='+'+'.join(spl_hash), headers={'User-Agent' : "Mozilla/5.0"})
	dumpdata = ulib.urlopen(req).read()
	dumpdata = ulib.unquote(dumpdata)
	
	urls_ = re.findall("(http[s]*://[^:<&%]*?)[\"& ]",dumpdata)
	
	urls = Set()
	
	for _ in urls_:
		if not "google" in _ and not "youtube" in _:
			urls.add(_)
	
	occurance = []
	for _url in urls:
		try:
			temp = get_occurence_list(_url,text_file)
			occurance.append(temp)
			#frequencies of string for url _url
		except:
			pass

	#now occurance is a list of lists containing frequencies for each url
	
	final = [0 for _ in range(len(occurance[0]))]

	_length = len(occurance)
	#_length is total number of urls present
	
	for _x in range(len(occurance[0])):
		_x1 = 0
		for _o in occurance:
			final[_x] += _o[_x]*(_length-_x1)
			#multiplyinng frequency in each url with url position from bottom which gives weight
			_x1 += 1
	return final

if __name__ == '__main__':
	num_list = getWeight('christmasgiftideas','dummy/christmasgiftideas.txt')
	# this function will give list of number of occurence all the words from the manula text created in the web url 
	# first it will extract the visible text from the url and then find the total occurence
	with open('outfile.txt','w') as outfile:
		for text in num_list:
			outfile.write(str(text) + '\n')

