
def test6(postags):
    postagsent = "".join(postags)
    if (('N' in postagsent) or ('^' in postagsent)): #Presence of Common Noun(N) or Proper Noun(^)
        print "1"+",",
    else:
        print "0"+",",
