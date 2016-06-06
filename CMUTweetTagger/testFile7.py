'''
@file : testFile7.py
@author (A) : Madhu Kumar Dadi.
@project : Social List
@function :
	test7(postags) :    checks for the presence of Adjectives in the hashtag
		@postags :  list containing pos tags for a hashtag
		return :    count of Adjectives
@Licence :
	This work is licensed under the
	Creative Commons Attribution-NonCommercial-ShareAlike 4.0
	International License. To view a copy of this license,
	visit http://creativecommons.org/licenses/by-nc-sa/4.0/.
'''

from collections import Counter

def test7(postags):
	postagsent = "".join(postags)
	count = Counter(postagsent)
	if count['A'] == 0:
		return "0"
	return count['A']