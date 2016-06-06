'''
@file : jsontweets.py
@author (A) : Madhu Kumar Dadi.
@project : Social List
@function :
	jsoncheck(file1) :  converts a json format tweets file to normal tweet
		@file1 :    file containing json data
		return :   none
@Licence :
	This work is licensed under the
	Creative Commons Attribution-NonCommercial-ShareAlike 4.0
	International License. To view a copy of this license,
	visit http://creativecommons.org/licenses/by-nc-sa/4.0/.
'''

import json
import codecs


'''
For parsing the data from twitter json format output
'''


def jsoncheck(file1):
	file2 = codecs.open(file1 + ".txt",encoding="utf8")
	fileout = codecs.open("socialListstweets.txt", "a",encoding="utf8")
	fileout.write(file1 + "\n")
	data = json.load(file2)
	for i in xrange(len(data['statuses'])):
		tweets = data['statuses'][i][u'text'].replace("\n","")
		fileout.write(tweets+"\n")
	fileout.write("\n")
	fileout.close()


jsoncheck("bestbirthdaypresentever")
jsoncheck("childrenarethefuture")
jsoncheck("oldmantweets")
jsoncheck("perksofbeingagirl")
jsoncheck("reasonstobecheerful")
jsoncheck("reasonstocelebrate")
