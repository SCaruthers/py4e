print('Find what domain has the most emails in a file.')
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File error: ',fname)
    exit()

domain = dict()
for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From' : continue
    temp = words[1].split('@')
    domain[temp[1]] = domain.get(temp[1],0) + 1

for name in domain:
    print(name, domain[name])

max_count = 0
max_name = None
for name in domain:
    if max_count == 0 or  max_count < domain[name] :
        max_count = domain[name]
        max_name = name
print('Maximum: ',max_name, max_count)
        
