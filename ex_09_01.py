# Program to sort mbox.txt, find the user with max commits, but use Dictionary and tuples to sort.
print('Find top 10 email contributors (using dict and tuple).')

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
    if len(words) < 2 or words[0] != 'From' : continue
    my_dict[words[1]] = my_dict.get(words[1],0) + 1

lst = list()    # list to hold (count, email)
for (k,v) in list(my_dict.items()):
    lst.append( (v, k) )

lst.sort(reverse=True)

for v,k in lst[:1]:
    print(k,v)
