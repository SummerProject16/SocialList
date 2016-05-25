#Presence of Days in Social List

def test4(tagtotest):
    arr = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
    if any(x in tagtotest.lower() for x in arr):
        print "1"+",",
    else:
	    print "0"+",",