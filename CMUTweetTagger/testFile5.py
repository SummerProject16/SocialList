from collections import Counter

def test5(postags):
    postagsent = "".join(postags)
    count = Counter(postagsent)
    if count['$'] == 0:
	    return "0"
    return count['$']