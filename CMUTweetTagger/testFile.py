import wordsegment as ws
import CMUTweetTagger as ctt
file=open("../label_idiom.txt","r");
datasets=file.read().split('\n')
segData=[]
i=0
for data in datasets:
    print i
    data1=data.split(" ")
    if i<10000 and data1[1] == '1':
        segData.append(" ".join(ws.segment(data1[0])))
    i+=1
print "done"
Tags=ctt.runtagger_parse(segData)
i=0
for x in Tags:
    if 1 :
        print x, i
        print segData[i]
    i+=1