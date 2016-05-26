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
tofile = open(argv[2],"w")
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

	tofile.write(str(testFile1.test1(ParsedTag))+","+
	str(testFile2.test2(ParsedTag))+","+
	str(testFile4.test4(ParsedTag))+","+
	str(testFile5.test5(postag))+","+
	str(testFile6.test6(postag))+","+
	str(testFile7.test7(postag))+","+
	str(testFile8.test8(postag))+","+
	str(testFile9.test9(postag))+","+
	str(testFile10.test10(postag))+","+
	str(testFile11.pos_tag_entropy(sociallist))+","+
	str(testFile12.test12(sociallist))+","+
	str(testFile14.test14(ParsedTag,postag))+"\n")
