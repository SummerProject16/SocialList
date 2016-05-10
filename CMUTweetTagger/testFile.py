import wordsegment as ws
import searchWeb

file = open('../label_idiom.txt')

idiomsEx = file.readlines()

sociallists = []

for lines in idiomsEx:
    idiomset = lines.split()
    if idiomset[1] == '1':
        sociallists.append(idiomset[0])

parsedSociallists = []

for line in sociallists:
    parsedSociallists.append(" ".join(ws.segment(line)))

for line in parsedSociallists:
    googledata = searchWeb.searchgoogle(line)
    count = 0
    i = 1
    for site in googledata:
        try:
            if searchWeb.searchforstring(site,line):
                count+=1
        except:
            print "Network Failed for "+site
        i += 1
        if i>10:
            break
    if count > 5:
        print line + " True"
    else:
        print line+" False"