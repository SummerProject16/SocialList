
def test9(postags):
    postagsent = "".join(postags)
    if ('R' in postagsent): #Presence of Adverb(R)
        return 1
    else:
        return 0