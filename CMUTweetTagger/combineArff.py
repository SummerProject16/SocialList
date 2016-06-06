'''
@file : combineArff.py
@author (A) : Madhu Kumar Dadi.
@project : Social List

This script combines the arff files obtained from socialList.py and GoogleSearch.py

@Usage :    python combineArff.py socialList.arff GoogleSearch.arff
@Licence :
	This work is licensed under the
	Creative Commons Attribution-NonCommercial-ShareAlike 4.0
	International License. To view a copy of this license,
	visit http://creativecommons.org/licenses/by-nc-sa/4.0/.
'''

from sys import argv

file1 = open(argv[1])
file2 = open(argv[2])
fileout = open(argv[3],"w")

data1 = file1.readlines()
data2 = file2.readlines()

for x,y in zip(data1,data2):
	filedata = x.split(",")
	for index in xrange(len(filedata)-1):
		fileout.write(filedata[index]+",")

	fileout.write(y.replace("\n","")+",")
	fileout.write(filedata[len(filedata)-1].replace("\n","")+"\n")
