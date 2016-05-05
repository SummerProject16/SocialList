import wordsegment as ws
import CMUTweetTagger as ctt
file=open("../label_idiom.txt","r");
datasets=file.read().split('\n')
segData=[]
i=0
for data in datasets:
    print i
    segData.append(" ".join(ws.segment(data)))
    i+=1
    if i == 5:
        break
print "done"
Tags=ctt.runtagger_parse(segData)
i=0
for x in Tags:
    if 1 :
        print x
        print segData[i]
    i+=1