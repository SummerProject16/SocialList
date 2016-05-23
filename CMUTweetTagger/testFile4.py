import wordsegment as ws
import searchWeb
import re
#Presence of days in the line 
file = open('../label_idiom.txt')

idiomsEx = file.readlines()

sociallists = []
k=0
#taking only the string
for lines in idiomsEx:
    idiomset = lines.split()
    if idiomset[1] == '0':
        sociallists.append(idiomset[0])

arr = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
for line in sociallists:
    if any(x in line.lower() for x in arr):
        print line
        k=k+1
#number of Sentences which contain numbers
print k

