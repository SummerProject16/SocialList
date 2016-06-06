'''
@file : plurals.py
@author (A) : Anirudh Gopu
@project : Social List

this file is not used anywhere

This work is licensed under the
Creative Commons Attribution-NonCommercial-ShareAlike 4.0
International License. To view a copy of this license,
visit http://creativecommons.org/licenses/by-nc-sa/4.0/.
'''
#To check whole file once

def lengthforall():
	filename =open("file.txt")
	b=0
	c=0
	avgsl=0
	avgnsl=0
	max0=0
	max1=0
	min1=100
	min0=100
	txt=open(filename)

	with open(filename,'r')as file:
		for line in file:
			a = len(line)-3
			f1=txt.readline()
			f1=f1.split()
			if f1[1]=='1':
				avgsl=+a
				b=+1
				if a > max1:
					max1=a
				if a<min1:
					min1=a
			if f1[1]=='0':
				avgnsl=+a
				c=+1
				if a > max0:
					max0=a
				if a<min0:
					min0=a
	d=avgsl/b
	e=avgnsl/c
	print "maximum length of social list is %d" % max1
	print "minimum length of social list is %d" % min1
	print "maximum length of non social list is %d" % max0
	print "minimumlength of non social list is %d" % min0
	print "avg length of social list is %d" % d
	print "avg length of non social list is %d" % e