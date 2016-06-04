import CMUTweetTagger as cmu
import wordsegment as ws

file1 = open()
file2 = open()

data1 = file1.read()
data2 = file2.read()

tweets1 = data1.split("\n\n")

hashtags = []

for tweet1 in tweets1:
	hashtag = tweet1.split("\n")[0]
	hashtags.append(" ".join(ws.segment(hashtag)))

postags = cmu.runtagger_parse(hashtags)

i=0

for postag in postags:
	if '$' in "".join(postag):
		i+=1