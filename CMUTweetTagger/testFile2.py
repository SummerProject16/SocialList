'''
@file : Category.py
@author (A) : Madhu Sai Ravada.
@project : Social List

@function :gives the number of words in a tag


This work is licensed under the
Creative Commons Attribution-NonCommercial-ShareAlike 4.0
International License. To view a copy of this license,
visit http://creativecommons.org/licenses/by-nc-sa/4.0/.
'''
'''
import wordsegment as ws
def numberofWords():
	file = open('../label_idiom.txt')

	idiomsEx = file.readlines()

	sociallists = []
	m = 0
	n = 0
	for lines in idiomsEx:
		idiomset = lines.split()
		if idiomset[1] == '0':
			sociallists.append(idiomset[0])

	min = 10
	max = 0
	for line in sociallists:
		k = ws.segment(line)
		l = len(k)
		if l > max:
			max = l
		if l < min:
			min = l
		print (line) + " " + str(l)
		m = m + l
		n = n + 1
	print "------------------"
	print "the average number of words in each line is " + str(float(m) / n), "min =", str(min), "max =", str(max)

'''
#To check number of words in tagtocheck
def test2(tagtocheck):
	x = tagtocheck.split()
	return str(len(x))
