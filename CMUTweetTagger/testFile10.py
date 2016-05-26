
def test10(postags):
    postagsent = "".join(postags)
    if ('O' in postagsent): #Presence of Pronoun(O)
        return 1
    else:
        return 0