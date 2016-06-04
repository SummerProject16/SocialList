from sys import argv

import testFile14
import CMUTweetTagger as cmu
import wordsegment as ws

file = open(argv[1])
tofile = open(argv[2], "w")
tofile.close()
idiomsEx = file.readlines()
sociallists = []
for line in idiomsEx:
	sociallists.append(line.replace("\n", ""))
parsedSociallists = []
for line in sociallists:
	parsedSociallists.append(" ".join(ws.segment(line)))
postags = cmu.runtagger_parse(parsedSociallists)

# for x in parsedSociallists:
#      if imdbCheck.checkStringinMovies(x) == True:
#         print x

for ParsedTag, postag in zip(parsedSociallists, postags):
	tofile = open(argv[2], "a")
	a = testFile14.test14(ParsedTag, postag)
	print str(a[0]) + "," + str(a[1]) + "," + str(a[2])
	tofile.write(str(a[0]) + "," + str(a[1]) + "," + str(a[2]) + "\n")
	tofile.close()
