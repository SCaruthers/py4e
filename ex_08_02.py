# Excercise 2 from Python for Everybody, Chapter 8: Lists
# Read the mbox text file, and print the day on which each email was sent

fhand = open('mbox-short-x.txt')
count = 0
for line in fhand:
    words = line.split()
    #print('Debug: ',words)
    if len(words) < 3 : continue
    if words[0] != 'From' : continue
    #if len(words) > 2 : # actually, just change above from ==0 to <3
    print(words[2])