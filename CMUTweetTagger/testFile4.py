#Presence of Days in Social List

def test4(tagtotest):
    arr = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
    if any(x in tagtotest.lower() for x in arr):
        return "1"
    else:
	    return "0"