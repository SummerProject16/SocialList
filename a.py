file1 = open("final_idiom_3_5_16.txt")
file2 = open("final_idiom_3_5_161.txt")
file3 = open("label10k_3_5_16.txt")
file4 = open("label_idiom.txt")
file5 = open("final_eliminated.txt")

file = open("socialLists.txt","w")

data1 = file1.readlines()
data2 = file2.readlines()
data3 = file3.readlines()
data4 = file4.readlines()
data5 = file5.readlines()

data = []

for x in data1:
    s = x.split()
    if s[1] == '1':
        data.append(s[0])

for x in data2:
    s = x.split()
    if s[1] == '1':
        data.append(s[0])

for x in data3:
    s = x.split()
    if s[1] == '1':
        data.append(s[0])

for x in data4:
    s = x.split()
    if s[1] == '1':
        data.append(s[0])

for x in data5:
    s = x.split()
    if s[1] == '1':
        data.append(s[0])
        
final = []

for x in data:
    if x not in final:
        final.append(x)
        
for x in final:
    file.write(x+"\n")