'''
@file : testFile6.py
@author (A) : Madhu Kumar Dadi.
@project : Social List
@function :
	test6(postags) :    checks for presence of nouns in the hashtag
		@postags :  a list containing pos tags for a hashtag
		return :    count of nouns
@Licence :
	This work is licensed under the
	Creative Commons Attribution-NonCommercial-ShareAlike 4.0
	International License. To view a copy of this license,
	visit http://creativecommons.org/licenses/by-nc-sa/4.0/.
'''

from collections import Counter

def test6(postags):
	postagsent = "".join(postags)
	count = Counter(postagsent)
	if count['N']+count['^'] == 0:
		return "0"
	return count['N']+count['^']