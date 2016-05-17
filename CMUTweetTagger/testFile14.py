import searchWeb

def test14(postags,parsedSociallists):
    j = 0
    urlsfile = open("urls.txt","w")
    for line in parsedSociallists:
        print line,
        nounpart = []
        k = 0
        splitline = line.split()
        for x in postags[j]:
            if (x is 'M' or x is '^' or x is 'Z'):
                nounpart.append(splitline[k])
            k += 1
        while True:
            try:
                googledata = searchWeb.searchgoogle(line)
                break
            except:
                #print "Connection reset Please verify"
                continue
        urlsfile.write(line+"\n"+str(googledata)+"\n")
        count = 0
        #print "Noun "+" ".join(nounpart)
        if " ".join(nounpart) == "":
            j+=1
            print "2"
            continue
        i = 1
        for site in googledata:
            try:
                if searchWeb.searchforstring(site,nounpart):
                    count += 1
            except:
                print "",
            i += 1
            if i > 10:
                break
        if count > 5:
            print "1"
        else:
            print "0"
        j += 1
