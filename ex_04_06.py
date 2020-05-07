def computepay(hours, rate):
    if hours<=40:
        return hours * rate
    else:
        return (40*rate) + ((hours-40)*(rate*1.5))


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

print('Pay: ',computepay(hrs, rate))