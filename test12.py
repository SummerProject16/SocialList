from sys import argv
import wordsegment as ws
import enchant as en
script, filename =argv

txt=open(filename)

eng1=0
neng1=0
neng0=0
eng0=0

d=en.Dict("en-US")

with open(filename,'r')as file:
	for line in file:
		f1=txt.readline()
		f1=f1.split()
		print f1[0],
		if f1[1]=='1':
			print "SocialList"
			words=ws.segment(f1[0])
			eng1=0
			neng1=0
			for x in words:
				check=0
				if d.check(x)==False:
					check=1
				if check==0:
					eng1+=1
				else:
					neng1+=1
			if eng1!=0:
				print float(neng1)/eng1
			elif neng1!=0:
				print 0
		if f1[1]=='0':
			print "Non SocialList"
			words=ws.segment(f1[0])
			eng0=0
			neng0=0
			for x in words:
				check=0
				if d.check(x)==False:
					check=1
				if check==0:
					eng0+=1
				else:
					neng0+=1
			if eng0!=0:
				print float(neng0)/eng0
			elif neng0!=0:
				print 0
