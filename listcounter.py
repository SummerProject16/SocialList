from sys import argv

filename = argv[1]

file = open(filename)

data = file.readlines()

count = 0

for line in data:
    parts = line.split()
    if len(parts) == 2:
        if parts[1] == '1':
            count+=1
    else:
        print line

print count