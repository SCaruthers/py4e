fname = input('Enter a file: ')
if fname.lower() == 'na na boo boo':
    print('NA NA BOO BOO TO YOU - You have been punk\'d!')
    quit()

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

