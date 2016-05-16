from wordsegment import segment
from nltk import pos_tag, word_tokenize
file = open('../label_idiom.txt')
idiomsEx = file.readlines()
for line in idiomsEx:
    line = line.split()
    if(line[1]=="1"):
        a = segment(line[0])
        a = pos_tag(a)
        print a 