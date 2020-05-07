import os

# Program to report histogram of hour of day for submissions in mbox.txt, using dict, tuple, etc.
print('Make histogram for the hour of day for email contributors (using dict and tuple).')


fname = input('Enter a file name: ')
if len(fname) == 0 : fname = 'mbox-short.txt'
try:
    fhand = open(fname)
except:
    print('File open error:',fname)
    quit()

my_dict = dict()    # dict to hold {email:count}
for line in fhand:
    words = line.split()
    if len(words) < 6 or words[0] != 'From' : continue
    hr = words[5].split(':')[0]
    my_dict[hr] = my_dict.get(hr,0) + 1

lst = list()    # list to hold (hour, count)
for (k,v) in list(my_dict.items()):
    lst.append( (k, v) )

lst.sort() # sort by hour (key)

print('\n hr',' # ','Histogram')
print('------------------')
for k,v in lst:
    cols = os.get_terminal_size()[0] - 13
    if v < cols:
        b = '■'*v
    else:
        b = '■'*cols
        b = b+'//■■'
    print(' %2s %3d %s' % (k,v,b) )
