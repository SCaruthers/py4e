fname = 'mbox-short.txt'
fhand = open(fname)
count = 0
for line in fhand:
    if not line.startswith('From ') : continue
    temp = line.split()
    if len(temp) > 1:
        print(temp[1])
        count = count + 1
print('There were', count, 'lines in the file \"%s\" with From as the first word.' % (fname))