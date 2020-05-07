c = input('Enter the temperature in Celsius: ')
try:
    f = float(c) * 9 /5 +32
    print(c,'°C','is',f,'°F')
except:
    print('Please type a number value.')