fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File error: ',fname)
    exit()

authors = dict()
for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From' : continue
    authors[words[1]] = authors.get(words[1],0) + 1

for name in authors:
    print(name, authors[name])