'''
@file : plurals.py
@author (A) : Anirudh Gopu
@project : Social List

@function :
	test12(tagtocheck) :
        return :    ratio of non-english to english

This work is licensed under the
Creative Commons Attribution-NonCommercial-ShareAlike 4.0
International License. To view a copy of this license,
visit http://creativecommons.org/licenses/by-nc-sa/4.0/.
'''

import wordsegment as ws
import enchant as en


def test12(tagtocheck):
	d=en.Dict("en-US")
	correct = 0
	incorrect = 0
	words=ws.segment(tagtocheck)
	for x in words:
		if d.check(x)==False:
			incorrect+=1
		else:
			correct+=1
	if correct!= 0:
		return "%.4f"%(float(incorrect)/correct)
	else:
		return 0