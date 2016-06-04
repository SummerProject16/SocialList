from collections import Counter

def test7(postags):
    postagsent = "".join(postags)
    count = Counter(postagsent)
    if count['A'] == 0:
	    return "0"
    return count['A']