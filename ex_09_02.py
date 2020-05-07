fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('Could not open file:',fname)
    exit()
dow = dict()
for line in fhand:
    words = line.split()
    if len(words) > 2 and words[0] == 'From':
        dow[words[2]] = dow.get(words[2],0) + 1
for k in ['Mon','Tue','Wed','Thu','Fri','Sat','Sun'] :
    if k in dow: print(k,dow[k])
