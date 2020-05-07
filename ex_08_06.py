numlist = list()

while True:
    temp = input('Enter a number: ')
    if temp == 'done' : break
    try:
        numlist.append(float(temp))
    except:
        continue
if len(numlist) > 0:
    print('Maximum:', max(numlist))
    print('Minimum:', min(numlist))
    print('Count:  ', len(numlist))
else : print('You entered no numbers!')
