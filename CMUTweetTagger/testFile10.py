
def test10(postags):
    postagsent = "".join(postags)
    if ('O' in postagsent): #Presence of Pronoun(O)
        print "1"+",",
    else:
        print "0"+",",