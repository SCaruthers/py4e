inp = input('Enter a list of numbers: ')
my_max = None
my_min = None
tot = 0
count = 0
for i in inp.split():
    try:
        tot = tot + float(i)
    except:
        continue
    count += 1
    if my_max is None or my_max < float(i):
        my_max = float(i)
    if my_min is None or my_min > float(i):
        my_min = float(i)
if count > 0:
    print('Count: %i Min: %f Max: %f' % (count, my_min, my_max))
else:
    print('Did you enter any numbers? I think not.')