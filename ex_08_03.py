# Excercise 2 from Python for Everybody, Chapter 8: Lists
# Read the mbox text file, and print the day on which each email was sent

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    #print('Debug: ',words)
    if len(words) < 3 or words[0] != 'From' : continue
    print(words[2])