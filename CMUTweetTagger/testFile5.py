
def test5(postags):
    postagsent = "".join(postags)
    if (('$' in postagsent)): #Presence of Numbers($)
        print "1"+",",
    else:
        print "0"+",",