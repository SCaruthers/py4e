def count(str,chr):
    i = 0
    for letter in str:
        if letter == chr:
            i = i+1
    return i


#print(count('banana','a'))
str = input('Enter a string to search: ')
chr = input('Enter a character to find in \"%s\": ' %(str))
if len(chr) > 1:
    print('Please enter only a single character.')
    quit()

print('The character \"%s\" occurs in \"%s\" %d time(s).' %(chr, str, count(str,chr)))

