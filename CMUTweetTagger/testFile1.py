def strlength(tagtocheck):
	filename = open("../label_idiom.txt")
	maxsl=0
	minsl=50
	maxnsl=0
	minnsl=50
	b=0
	c=0
	avgsl=0
	avgnsl=0
	txt=open(filename)

	with open(filename,'r')as file:
		for line in file:
			a = len(line)-3
			f1=txt.readline()
			f1=f1.split()
			print "%s -- %d" %(f1[0], a)#line " -- " a

def test1(tagtocheck):
	print str(len(tagtocheck))+",",