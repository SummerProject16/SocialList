#Presence of Days in Social List
'''
@file : Category.py
@author (A) : Madhu Sai Ravada.
@project : Social List

function :
    returns 1 if the tag contains any day of the week else it will return 0

This work is licensed under the
Creative Commons Attribution-NonCommercial-ShareAlike 4.0
International License. To view a copy of this license,
visit http://creativecommons.org/licenses/by-nc-sa/4.0/.
'''
def test4(tagtotest):
    arr = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
    if any(x in tagtotest.lower() for x in arr):
        return "1"
    else:
	return "0"