fname = input('Enter a file: ')

try:
    fopen = open(fname)
except:
    print('File', fname, 'not found')
    quit()

count = 0
tot = 0
for line in fopen:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    count = count + 1
    pos = line.find(':')+1
    tot = tot + float(line[pos:])
print('Average spam confidence: ', tot/count)

