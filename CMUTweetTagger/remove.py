file = open("finallist.arff")
file1 = open("test.arff",'w')
data = file.readlines()
k =0
for line in data:
    k=k+1
    if(k>24):
        line = line.split(",")
        del line[4]
        file1.write(",".join(line))
