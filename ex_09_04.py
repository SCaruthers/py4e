print('Find who has the most emails in a file.')
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

max_count = 0
max_name = None
for name in authors:
    if max_count == 0 or  max_count < authors[name] :
        max_count = authors[name]
        max_name = name
print(max_name, max_count)
        
