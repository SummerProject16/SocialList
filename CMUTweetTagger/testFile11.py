#Entropy of line
import math
from sets import Set
from nltk import pos_tag, word_tokenize
from wordsegment import segment
from collections import Counter

def pos_tag_entropy(st):
    seg_st = segment(st)
    #print seg_st
    pos_list=  pos_tag(seg_st)
    len_list=len(pos_list)
    #print len_list
    arr = []
    freq_list =[]
    for i in xrange(len_list):
        arr.append(pos_list[i][1])
    #print arr
    k = Counter(arr)
    for x in k:
        #print x, k[x]
        freq = float(k[x])/len_list
        #print x,freq
        freq_list.append(freq)
    #print freq_list
    ent = 0.0
    for j in freq_list:
        ent = ent + j * math.log(j, 2)
    ent = -ent
    print ent
#end of function--
l=0
file = open('../label_idiom.txt')
idiomsEx = file.readlines()
for line in idiomsEx:
    line = line.split()
    print line[0],
    pos_tag_entropy(line[0])
