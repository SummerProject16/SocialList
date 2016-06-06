'''
@file : testFile9.py
@author (A) : Madhu Kumar Dadi.
@project : Social List
@function :
	test9(postags) :    checks for the presence of Adverb in the hashtag
		@postags :  list containing pos tags for a hashtag
		return :    count of Adverb
@Licence :
	This work is licensed under the
	Creative Commons Attribution-NonCommercial-ShareAlike 4.0
	International License. To view a copy of this license,
	visit http://creativecommons.org/licenses/by-nc-sa/4.0/.
'''

def test9(postags):
    postagsent = "".join(postags)
    if ('R' in postagsent): #Presence of Adverb(R)
        return 1
    else:
        return 0