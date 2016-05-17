import wordsegment as ws
import searchWeb

file = open('../label_idiom.txt')

idiomsEx = file.readlines()

sociallists = []
m = 0
n = 0
for lines in idiomsEx:
    idiomset = lines.split()
    if idiomset[1] == '0':
        sociallists.append(idiomset[0])

print "Number of words in each scentence"
print "---------------------------------"
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