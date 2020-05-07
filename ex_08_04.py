fname = 'romeo.txt'

fhand = open(fname)

wordlist = list()
for line in fhand:
    temp = line.split()
    for word in temp:
        if word not in wordlist:
            wordlist.append(word)
wordlist.sort()
print(wordlist)
print(sorted(wordlist, key = lambda s: s.lower()))