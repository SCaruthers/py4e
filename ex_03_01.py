try:
    hrs = float(input('Enter Hours: '))
except:
    print('Error, please enter a numeric input.')
    quit()
try:
    rate = float(input('Enter Rate: '))
except:
    print('Error, please enter a numeric input.')
    quit()
if hrs<=40:
    pay = hrs * rate
else:
    pay = (40*rate) + ((hrs-40)*(rate*1.5))
print('Pay: ',pay)