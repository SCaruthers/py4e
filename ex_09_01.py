fname = 'words.txt'
fhand = open(fname)

ddd = dict()
for line in fhand:
    for word in line.split():
        if word not in ddd:
            ddd[word] = True
            
print(ddd)