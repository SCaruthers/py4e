tot = 0
count = 0
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    try:
        inp = float(inp)
    except:
        print('Invalid input')
        continue
    tot = tot + inp
    count = count + 1
try:
    avg = tot / count
except:
    avg = None
print(tot, count, avg)
    