from sys import argv

import testFile1
import testFile2
import testFile3
import testFile4
import testFile5
import testFile6
import testFile7
import testFile8
import testFile9
import testFile10
import testFile11
import testFile12
import testFile14
import imdbCheck
import CMUTweetTagger as cmu
import wordsegment as ws

file = open(argv[1])
idiomsEx = file.readlines()
sociallists = []
for line in idiomsEx:
    sociallists.append(line.replace("\n",""))
parsedSociallists = []
for line in sociallists:
    parsedSociallists.append(" ".join(ws.segment(line)))
postags = cmu.runtagger_parse(parsedSociallists)

# for x in parsedSociallists:
#      if imdbCheck.checkStringinMovies(x) == True:
#         print x

for sociallist,ParsedTag,postag in zip(sociallists,parsedSociallists,postags):
	testFile1.test1(ParsedTag)
	testFile2.test2(ParsedTag)
	testFile4.test4(ParsedTag)
	testFile5.test5(postag)
	testFile6.test6(postag)
	testFile7.test7(postag)
	testFile8.test8(postag)
	testFile9.test9(postag)
	testFile10.test10(postag)
	testFile11.pos_tag_entropy(sociallist)
	testFile12.test12(sociallist)
	testFile14.test14(ParsedTag,postag)

	print ""
