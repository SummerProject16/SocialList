import wordsegment as ws
import enchant as en

def test12(tagtocheck):
	d=en.Dict("en-US")
	correct = 0
	incorrect = 0
	words=ws.segment(tagtocheck)
	for x in words:
		if d.check(x)==False:
			incorrect+=1
		else:
			correct+=1
	if correct!= 0:
		print str(float(incorrect)/correct) +",",
	else:
		print "0,",