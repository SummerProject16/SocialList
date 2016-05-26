from collections import Counter

def test6(postags):
    postagsent = "".join(postags)
    count = Counter(postagsent)
    if count['N']+count['^'] == 0:
	    return "0"
    return count['N']+count['^']