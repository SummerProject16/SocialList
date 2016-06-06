'''
@file : Category.py
@author (A) : Madhu sai Ravada.
@project : Social List

returns the entropy of postags list of the hastag

This work is licensed under the
Creative Commons Attribution-NonCommercial-ShareAlike 4.0
International License. To view a copy of this license,
visit http://creativecommons.org/licenses/by-nc-sa/4.0/.
'''


import math
from wordsegment import segment
from collections import Counter

def pos_tag_entropy(tagtocheck,pos_list):
    seg_st = segment(tagtocheck)
    len_list=len(pos_list)
    arr = []
    freq_list =[]
    for i in xrange(len_list):
        arr.append(pos_list[i])
    k = Counter(arr) #counts no of pos tags and their multiplicity
    for x in k:
        freq = float(k[x])/len_list
        freq_list.append(freq)
    ent = 0.0
    for j in freq_list:
        ent = ent + j * math.log(j, 2)
    ent = -ent
    return "%.4f"%(float(ent))
#end of function--
