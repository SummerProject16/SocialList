import testFile1
import testFile2
import testFile3
import testFile4
import testFile5
import testFile6
import testFile7
import testFile8
import testFile9
import testFile10
import testFile11
import testFile12
import testFile14
import CMUTweetTagger as cmu
import wordsegment as ws

filename = '../label_idiom.txt'

file = open(filename)
idiomsEx = file.readlines()
sociallists = []
scount = 0
idiomset = []
for lines in idiomsEx:
    tempset = lines.split()
    idiomset.append(tempset)
    if tempset[1] == '1':
        scount += 1
    sociallists.append(tempset[0])
parsedSociallists = []
for line in sociallists:
    parsedSociallists.append(" ".join(ws.segment(line)))
postags = cmu.runtagger_parse(parsedSociallists)

testFile5.test5(idiomset,postags,scount)
testFile6.test6(idiomset,postags,scount)
testFile7.test7(idiomset,postags,scount)
testFile8.test8(idiomset,postags,scount)
testFile9.test9(idiomset,postags,scount)
testFile10.test10(idiomset,postags,scount)
testFile14.test14(postags,parsedSociallists)