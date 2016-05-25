import math
from nltk import pos_tag
from wordsegment import segment
from collections import Counter

def pos_tag_entropy(tagtocheck):
    seg_st = segment(tagtocheck)
    pos_list=  pos_tag(seg_st)
    len_list=len(pos_list)
    arr = []
    freq_list =[]
    for i in xrange(len_list):
        arr.append(pos_list[i][1])
    k = Counter(arr) #counts no of pos tags and their multiplicity
    for x in k:
        freq = float(k[x])/len_list
        freq_list.append(freq)
    ent = 0.0
    for j in freq_list:
        ent = ent + j * math.log(j, 2)
    ent = -ent
    print str(float(ent))+",",
#end of function--