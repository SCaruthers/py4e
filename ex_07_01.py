fname = 'mbox-short.txt'

try:
    fopen = open(fname)
except:
    print('File not found.')
    quit()

for line in fopen:
    print(line.rstrip().upper())
