import CMUTweetTagger as cmu
import wordsegment as ws
file = open('../label_idiom.txt')
idiomsEx = file.readlines()
sociallists = []
scount=0
for lines in idiomsEx:
    idiomset = lines.split()
    if idiomset[1] == '1':
        scount+=1
    sociallists.append(idiomset[0])
parsedSociallists = []
for line in sociallists:
    parsedSociallists.append(" ".join(ws.segment(line)))
postags = cmu.runtagger_parse(parsedSociallists)
i=0
stags=0
itags=0
for line in postags:
    postagsent = " ".join(line)
    if ('V' in postagsent) and idiomset[1] == '1':
        print parsedSociallists[i]
        stags+=1
    elif ('V' in postagsent) and idiomset[1] == '0':
        itags+=1
    i+=1

print "Probablity of Social Lists containing Verbs is ",str(stags)+'/'+str(scount),str(float(stags)/scount)
print "Probablity of Non-Social Lists containing Verbs is ",str(itags)+'/'+str(i-scount),str(float(itags)/(i-scount))