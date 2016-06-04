from collections import Counter

def test8(postags):
    postagsent = "".join(postags)
    count = Counter(postagsent)
    if count['V'] == 0:
	    return "0"
    return count['V']