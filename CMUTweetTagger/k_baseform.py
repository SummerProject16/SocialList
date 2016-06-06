#Bringing the line into a base format if the same line repeats by varied k value

from wordsegment import segment
from collections import Counter
file = open('../label_idiom.txt')
idiomsEx = file.readlines()
#num_arr = ['one','two','three','four','five','six','seven','eight','nine']
arr_contain_numbers = []
arr_repeat = []
for line in idiomsEx:
    line = line.split()
    seg_line = segment(line[0])
    space_line = " ".join(seg_line)
    #checks if any integer is present in the line
    if(any(char.isdigit() for char in space_line)):
        #eliminating the integers
        line_nonum = ''.join([i for i in space_line if not i.isdigit()])
        arr_contain_numbers.append(line_nonum)
#storing the lines which repeat
for i in xrange(len(arr_contain_numbers)):
    k = arr_contain_numbers.count(arr_contain_numbers[i])
    if(k>1):arr_repeat.append(arr_contain_numbers[i])
#counting the line repeated
l = Counter(arr_repeat)
for x in l:
    print x,l[x]
