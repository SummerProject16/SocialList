import wordsegment as ws
import searchWeb
import CMUTweetTagger as cmu

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

postags = cmu.runtagger_parse(parsedSociallists)
j = 0
for line in parsedSociallists:
    nounpart = []
    k = 0
    splitline = line.split()
    for x in postags[j]:
        if (x is 'M' or x is '^' or x is 'Z'):
            nounpart.append(splitline[k])
        k += 1
    googledata = searchWeb.searchgoogle(line)
    count = 0
    print "Noun "+" ".join(nounpart)
    if " ".join(nounpart) == "":
        j+=1
        print "Not required for "+line
        continue
    i = 1
    for site in googledata:
        try:
            if searchWeb.searchforstring(site,nounpart):
                count += 1
        except:
            print "Network Failed for " + site
        i += 1
        if i > 10:
            break
    if count > 5:
        print line + " True"
    else:
        print line + " False"
    j += 1
