'''
@file : testFile10.py
@author (A) : Madhu Kumar Dadi.
@project : Social List
@function :
	test10(postags) :    checks for the presence of Pronouns in the hashtag
		@postags :  list containing pos tags for a hashtag
		return :    count of Pronouns
@Licence :
	This work is licensed under the
	Creative Commons Attribution-NonCommercial-ShareAlike 4.0
	International License. To view a copy of this license,
	visit http://creativecommons.org/licenses/by-nc-sa/4.0/.
'''

def test10(postags):
    postagsent = "".join(postags)
    if ('O' in postagsent): #Presence of Pronoun(O)
        return 1
    else:
        return 0