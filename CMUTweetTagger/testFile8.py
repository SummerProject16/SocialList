
def test8(postags):
    postagsent = "".join(postags)
    if ('V' in postagsent): #Presence of verb
        print "1"+",",
    else:
        print "0"+",",