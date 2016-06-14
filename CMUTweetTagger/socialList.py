'''
@file : socialList.py
@author (A) : Madhu Kumar Dadi.
@project : Social List
@Usage :    python socialList.py finallist.txt finaltype.txt finallist.arff

This script finds the values returned by the features listed as comments for each hashtag in the file
finallist.txt and outputs the values in comma seperated format in the finallist.arff and the file finaltype.txt
contains the class of the hashtag.

@Licence :
	This work is licensed under the
	Creative Commons Attribution-NonCommercial-ShareAlike 4.0
	International License. To view a copy of this license,
	visit http://creativecommons.org/licenses/by-nc-sa/4.0/.
'''

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


file = open(argv[1]) #file containing socialList and nonSocialList hashtags
file_type = open(argv[2]) #file containing the types of hastags
tofile = open(argv[3],"w") #file to take output arff
tofile.close()
idiomsEx = file.readlines()
list_type = file_type.readlines()

sociallists = [] # to take hashtags in a list

for line in idiomsEx:
	sociallists.append(line.replace("\n",""))

parsedSociallists = [] #parse the hashtags using str2num library and add them as a list

for line in sociallists:
	parsedSociallists.append(str2num.words2num(" ".join(ws.segment(line))))

postags = cmu.runtagger_parse(parsedSociallists) #gets a list of postags each for each hashtag

i = 0

for ParsedTag,postag,type in zip(parsedSociallists,postags,list_type):
	checkTweetsret = checkTweets.checkTweets(ParsedTag.replace(" ",""),"test/"+str(i/100)+"tweets.txt")
	#checks for the hashtag in the files provided.

	i+=1

	tofile = open(argv[3],"a")
	tofile.write(str(testFile1.test1(ParsedTag))+","+ #number of charcters in hashtag
	str(testFile2.test2(ParsedTag))+","+ #number of words in hashtag
	str(testFile4.test4(ParsedTag))+","+ #presence of days
	str(testFile5.numbercount(postag))+","+ # presence of numbers
	str(testFile5.prepositioncount(postag))+","+ #presence of prepositions
	str(testFile5.conjuctioncount(postag))+","+ #presence of conjuctions
	str(testFile5.interjectioncount(postag))+","+ #presence of interjections
	str(testFile6.test6(postag))+","+ #presence of nouns
	str(testFile7.test7(postag))+","+ #presence of Adjectives
	str(testFile8.test8(postag))+","+ #presence of verbs
	str(testFile9.test9(postag))+","+ #presence of Adverbs
	str(testFile10.test10(postag))+","+ #presence of pronouns
	str(testFile11.pos_tag_entropy(ParsedTag.replace(" ",""),postag))+","+ #pos_tag entropy
	str(testFile12.test12(ParsedTag.replace(" ","")))+","+ #ratio of non-english to english words
	str(checkTweetsret[0])+","+str(checkTweetsret[1])+","+ #check for number and urls in tweets
	str(Category.checkCategories(ParsedTag.replace(" ","")))+","+ #check for category match
	str(plurals.containspluralNouns(ParsedTag,postag))+","+ #check if hashtag contains plural common noun
	str(type.replace("\n",""))+"\n") #class of hashtag
	tofile.close()
