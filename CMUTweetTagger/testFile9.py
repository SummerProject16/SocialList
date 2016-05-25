
def test9(postags):
    postagsent = "".join(postags)
    if ('R' in postagsent): #Presence of Adverb(R)
        print "1"+",",
    else:
        print "0"+",",