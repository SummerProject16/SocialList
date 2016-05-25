
def test7(postags):
    postagsent = "".join(postags)
    if ('A' in postagsent): #Presence of Adjective(A)
        print "1"+",",
    else:
        print "0"+",",