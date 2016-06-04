from collections import Counter

def numbercount(postags):
    postagsent = "".join(postags)
    count = Counter(postagsent)
    if count['$'] == 0:
	    return "0"
    return "1"

def prepositioncount(postags):
    postagsent = "".join(postags)
    count = Counter(postagsent)
    if count['P'] == 0:
	    return "0"
    return count['&']

def conjuctioncount(postags):
    postagsent = "".join(postags)
    count = Counter(postagsent)
    if count['&'] == 0:
	    return "0"
    return count['&']

def interjectioncount(postags):
    postagsent = "".join(postags)
    count = Counter(postagsent)
    if count['!'] == 0:
	    return "0"
    return count['!']
