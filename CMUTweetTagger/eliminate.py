#for appending data in a file
import wordsegment
prefix = ''
suffix = ' f'
suffix1 = ' 0'
with open('../final_idiom_29k.txt', 'r') as src:
    with open('../', 'w') as dest:
       for line in src:
           seg_line = wordsegment.segment(line)
           if("you" in seg_line):
               dest.write('%s%s%s\n' % (prefix, line.rstrip('\n'), suffix))
           else:
               dest.write('%s%s%s\n' % (prefix, line.rstrip('\n'), suffix1))