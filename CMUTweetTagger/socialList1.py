from sys import argv

import testFile1
import testFile2
import testFile4
import testFile5
import testFile6
import testFile7
import testFile8
import testFile9
import testFile10
import testFile11
import testFile12
import checkTweets
import CMUTweetTagger as cmu
import wordsegment as ws
import tweets.str2num.str2num as str2num
import Category
import plurals


'''
Run this file as python socialList1.py <sociallists file> <socialListsType file> <output arff file>
'''


file = open(argv[1])
file_type = open(argv[2])
tofile = open(argv[3],"w")
tofile.close()
idiomsEx = file.readlines()
list_type = file_type.readlines()
sociallists = []
for line in idiomsEx:
	sociallists.append(line.replace("\n",""))
parsedSociallists = []
for line in sociallists:
	parsedSociallists.append(str2num.words2num(" ".join(ws.segment(line))))
postags = cmu.runtagger_parse(parsedSociallists)

# for x in parsedSociallists:
#      if imdbCheck.checkStringinMovies(x) == True:
#         print x

for ParsedTag,postag,type in zip(parsedSociallists,postags,list_type):
	tofile = open(argv[3],"a")
	tofile.write(str(testFile1.test1(ParsedTag))+","+
	str(testFile2.test2(ParsedTag))+","+
	str(testFile4.test4(ParsedTag))+","+
	str(testFile5.numbercount(postag))+","+
	str(testFile5.prepositioncount(postag))+","+
	str(testFile5.conjuctioncount(postag))+","+
	str(testFile5.interjectioncount(postag))+","+
	str(testFile6.test6(postag))+","+
	str(testFile7.test7(postag))+","+
	str(testFile8.test8(postag))+","+
	str(testFile9.test9(postag))+","+
	str(testFile10.test10(postag))+","+
	str(testFile11.pos_tag_entropy(ParsedTag.replace(" ","")))+","+
	str(testFile12.test12(ParsedTag.replace(" ","")))+","+
	str(checkTweets.checkTweets(ParsedTag.replace(" ","")))+","+
	str(Category.checkCategories(ParsedTag.replace(" ","")))+","+
	str(plurals.containspluralNouns(ParsedTag,postag))+","+
	str(type.replace("\n",""))+"\n")
	tofile.close()
