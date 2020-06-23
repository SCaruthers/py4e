# ask for the URL of an XML only web page (like: https://www.w3schools.com/xml/cd_catalog.xml) and parse items

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt #import date

# Ignore SSL cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Countries = {0:'USA',1:'ITA'}
#Countries = {0:'USA',1:'ESP'}
#Countries = {0:'ESP',1:'ITA'}
#Countries = {0:'USA',1:'GBR'}
#Countries = {0:'GBR',1:'ITA'}
All_Countries = ['USA','AUS','CHN','ESP','GBR','IRN','IRQ','ITA','JPN','KOR','ZAF']
Countries = []

url = 'https://opendata.ecdc.europa.eu/covid19/casedistribution/xml'

print('\n\n\n      Welcome to COVID-19 Data Plotter by Shelton\n')
print('This program will read data either from a local file (which is old), \nor from the internet (which is updated daily, but slow to download).\n')
my_choice = input('Enter the number of your choice:\n1. Local File\n2. Online XML Source\n ?')

fname = 'covid_data.xml'                        # define this, regardless of choice -- to save for later
if len(my_choice)<1 or int(my_choice) == 1:
    fhand = open(fname)
    xml = fhand.read()
else:
    print('Please wait, connecting to',url)
    xml = urllib.request.urlopen(url, context = ctx).read().decode()   #open and read whole page

tree = ET.fromstring(xml)

print('\nYou can select up to 5 countries to plot.')
for index in range(5):
    print('Select Country to plot:')
    for i in range(len(All_Countries)):
        print(str(i)+'. ',All_Countries[i])
    print(str(len(All_Countries))+'. Finished selecting.')
    while True:
        try:
            tmp = int(input('Enter the number for country #'+str(index+1)+' : '))
        except:
            #print('Please enter a number between 0 and',len(All_Countries)-1)
            tmp = -1
        if tmp >= 0 and tmp <= (len(All_Countries)): break
        else: print('Please enter a number between 0 and',len(All_Countries))
    if tmp < len(All_Countries): Countries.append(All_Countries.pop(tmp))
    else: 
        break

if len(Countries) < 1: 
    print('You need to select at least one country to plot anything!')
    quit()
    
#print(xml)
print('')
print('List of Data'.center(50))
print('='*50)



records = tree.findall('record')
my_lst = [[],[],[],[],[]]

for record in records:
    # create lists with items (year, month, day, #_new_cases, #_new_deaths)
    #if record.find('countryterritoryCode').text == Countries[0]:    #'USA'
         #my_lst[0].append((record.find('year').text, record.find('month').text.zfill(2), record.find('day').text.zfill(2), record.find('cases').text,record.find('deaths').text))
    #if record.find('countryterritoryCode').text == Countries[1]:    #'ITA'
         #my_lst[1].append((record.find('year').text, record.find('month').text.zfill(2), record.find('day').text.zfill(2), record.find('cases').text,record.find('deaths').text))
    for index in range(len(Countries)):
        if record.find('countryterritoryCode').text == Countries[index]:   
             my_lst[index].append((record.find('year').text, record.find('month').text.zfill(2), record.find('day').text.zfill(2), record.find('cases').text,record.find('deaths').text))

for index in range(len(Countries)):
    my_lst[index].sort()

print('\n   date  \t Cases\t Deaths\t Case Count\t Death Count')

death_count = [[],[],[],[],[]]
case_count = [[],[],[],[],[]]
date_axis = [[],[],[],[],[]]
for index in range(len(Countries)):
    print('Data for '+Countries[index])
    for item in my_lst[index]:
        if len(death_count[index]) == 0: death_count[index].append(int(item[4]))
        else: death_count[index].append(death_count[index][-1]+int(item[4]))
        if len(case_count[index]) == 0: case_count[index].append(int(item[3]))
        else: case_count[index].append(case_count[index][-1]+int(item[3]))
        date_axis[index].append(dt.date(int(item[0]),int(item[1]),int(item[2])))
        
        print(date_axis[index][-1],'\t',item[3],'\t',item[4],'\t',case_count[index][-1],'\t',death_count[index][-1])


fig, ax = plt.subplots()
ax.set_title('COVID-19 Data')
ax.set_ylabel('Number')
for index in range(len(Countries)):
    ax.plot(date_axis[index],case_count[index],label=Countries[index]+' - Cumulative Cases')
    ax.plot(date_axis[index],death_count[index],label=Countries[index]+' - Cumulative Deaths')
ax.legend()
fig.show()
input('Hit <Enter> when done.')

if not exists(fname):
    try:
        fhand_out = open(fname,'w')
        fhand_out.write(xml)
        fhand_out.close()
    except:
        print('Error writing file.')
else:
    today = dt.datetime.now().date()
    fileday = dt.datetime.fromtimestamp(os.path.getctime(fname))
    print(today,fileday)
    if fileday < today:
        print(fname,'is old.')
