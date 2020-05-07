str = 'X-DSPAM-Confidence:0.8475'

pos = str.find(':')
num = float(str[pos+1:])

print(num)