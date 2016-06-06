from searchWeb import searchforstring
import wordsegment
file = open("tweetsorganized1.txt")
data = file.read()
data = data.split("\n\n")
for lines in data:
    line = lines.split()
    #print line[0]
    k=0
    seg_words = wordsegment.segment(line[0])
    for i in line:
        if("http" in i):
            #print seg_words
            for j in xrange(len(seg_words)):
                try:
                    if(searchforstring(i.replace("\\","")," ".join(seg_words))):
                        k=k+1
                except:
                    pass
    #print line[0]+"-----"+str(k)
    if(k>0):line[0]+"  is present in the urls"
