#pos for non social list
from wordsegment import segment
from nltk import pos_tag, word_tokenize
file = open('../label_idiom.txt')
idiomsEx = file.readlines()
file1 = open('../postags1.csv','w')
for line in idiomsEx:
    line = line.split()
    if(line[1]=="1"):
        a = segment(line[0])
        file1.write(line[0]+",")
        a = pos_tag(a)
        x = []
        for i in range(len(a)):
            x.append(a[i][1])
        file1.write(",".join(x)+"\n")