# ask for the URL of an XML only web page (like: https://www.w3schools.com/xml/cd_catalog.xml) and parse items

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import numpy as np
import matplotlib.pyplot as plt
#from datetime import date
import datetime as dt

PLOT_CASES = False
PLOT_DEATHS = False
PLOT_TOTALS = True

MAX_ITEMS = 20
#import os
#if os.get_terminal_size().columns < 145:
#    os.system('mode con cols=145 lines=40')

# Ignore SSL cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

All_Countries = {}              # Dictionary of all countries in the data file {'code':'countryname'}
Countries = []                  # holds the few Countries to plot, based on "index" iterator.
my_lst = [[],[],[],[],[]]       # List of Lists for data to plot: (year, month, day, #_new_cases, #_new_deaths)
death_count = [[],[],[],[],[]]  # List of Lists to build up cumulative deaths for plotting dimension depends on len(countries)
case_count = [[],[],[],[],[]]   # List of Lists to build up cumulative cases for plotting dimension depends on len(countries)
date_axis = [[],[],[],[],[]]    # List of Lists for date axis when plotting
cases = [[],[],[],[],[]]
xml = []                        # Holds the entire XML data, either from web or file
url = 'https://opendata.ecdc.europa.eu/covid19/casedistribution/xml'
fname = []

def init_lists():
    # empty lists and set up matrix size
    # but don't touch "All_Countries" because we won't download xml again
    global Countries #= []
    global my_lst #= [[],[],[],[],[]]
    global death_count #= [[],[],[],[],[]]  
    global case_count #= [[],[],[],[],[]]
    global date_axis #= [[],[],[],[],[]]
    global cases #= [[],[],[],[],[]]
    Countries = []
    my_lst = []
    death_count = []  
    case_count = []
    date_axis = []
    cases = []
    for i in range(MAX_ITEMS):
        my_lst.append([])
        death_count.append([])  
        case_count.append([])
        date_axis.append([])
        cases.append([])

def getXML(url):
    global fname
    my_choice = input('Enter the number of your choice:\n 1. Local File\n 2. Online XML Source\n1\r')

    if len(my_choice)>0 and (not my_choice.isdigit()):
        print('Please enter only a \"1\" or \"2\", or hit <Enter> to default to \"1\"')
        return []
    if len(my_choice)<1 or int(my_choice) == 1:
        fname = 'covid_data.xml'
        fhand = open(fname, encoding='utf-8')
        xml = fhand.read()
    elif int(my_choice) != 2:
        print('You must select either \"1\" or \"2\", or hit <Enter> to default to \"1\"')
        return []
    else:
        print('Please wait, connecting to',url)
        while True:
            try:
                xml = urllib.request.urlopen(url, context = ctx).read().decode()   #open and read whole page
                break
            except KeyboardInterrupt:
                print('User interrupt.  Quitting...')
                quit()
            except:
                print('Trouble connecting to',url)
                print('Trying again.  Press <ctrl>-c to quit.')
    return xml


##### START MAIN PROGRAM HERE #####

print('\n\n\n      Welcome to COVID-19 Data Plotter by Shelton\n')
print('This program will read data either from a local file (which is old), \nor from the internet (which is updated daily, but slow to download).\n')

while xml == []:
    xml = getXML(url)

tree = ET.fromstring(xml)           # build the tree of tags and data from XML
records = tree.findall('record')    # pull out all the individual records

# iterate through records to find the countries in the data
for record in records:
    tmp_txt = record.find('countryterritoryCode').text
    if (tmp_txt != '') and (tmp_txt != None) and tmp_txt not in All_Countries:
        try:
            All_Countries[tmp_txt] = record.find('countriesAndTerritories').text
        except:
            pass
        #print(tmp_txt, All_Countries)

DO_IT = True
while DO_IT:
    #Countries = []
    init_lists()
    print(my_lst)
    print('\nYou can select up to 5 countries to plot.')
    for index in range(MAX_ITEMS):
        print('Select Country to plot:')
        i = 0
        for key in sorted(All_Countries):
            if key not in Countries:
                print(key+' -',All_Countries[key].ljust(42), end='')
                i += 1
                if i == 3:
                    print()
                    i = 0
        if i != 0: print('') 
        print('ZZZ - Finished selecting.')
        while True:
            tmp = input('Enter the 3 letter code for country #'+str(index+1)+' : ').upper()
            if tmp == 'QUIT' or tmp == '': break
            if len(tmp) != 3: 
                print('Please enter a three digit identifier.')
                tmp = ''
            elif tmp in Countries:
                print(tmp,'already selected. Please select another, or ZZZ to quit selecting.')
            elif tmp == 'ZZZ' or tmp in All_Countries: break #it is a valid entry to break out of while and update Countries
            else: print('\"',tmp,'\" is unknonw. Please enter a 3 letter code listed.')
        if tmp in All_Countries: Countries.append(tmp)
        else: 
            break

    if len(Countries) < 1: 
        print('You need to select at least one country to plot anything!')
        try:
            tmp = input('Hit <Enter> to continue, or \"q\" to quit.').upper()
            if len(tmp)>0 and tmp[0]=='Q':
                DO_IT = False
            continue
        except KeyboardInterrupt:
            print('OK.  Bye, then.')
            #quit()
            DO_IT = False
            continue
            
    #print(xml)
    print('')
    #print('List of Data'.center(50))
    #print('='*50)

    print('Plotting data for the following:')
    for key in Countries:
        print(key,All_Countries[key])
    print('')


    for record in records:
        # create lists with items (year, month, day, #_new_cases, #_new_deaths)
        for index in range(len(Countries)):
            if record.find('countryterritoryCode').text == Countries[index]:   
                my_lst[index].append((record.find('year').text, record.find('month').text.zfill(2), record.find('day').text.zfill(2), record.find('cases').text,record.find('deaths').text))
                    
    for index in range(len(Countries)):
        my_lst[index].sort()    #data may not be in order by day, so sort it on date

    #print('\n   Date  \t Cases\t Deaths\t Case Count\t Death Count')


    for index in range(len(Countries)):
        #print('Data for '+Countries[index])
        for item in my_lst[index]:
            if len(death_count[index]) == 0: death_count[index].append(int(item[4]))
            else: death_count[index].append(death_count[index][-1]+int(item[4]))
            if len(case_count[index]) == 0: case_count[index].append(int(item[3]))
            else: case_count[index].append(case_count[index][-1]+int(item[3]))
            date_axis[index].append(dt.date(int(item[0]),int(item[1]),int(item[2])))
            cases[index].append(int(item[3]))
            #print(date_axis[index][-1],'\t',item[3],'\t',item[4],'\t',case_count[index][-1],'\t',death_count[index][-1])

    fig, ax = plt.subplots()
    ax.set_title('COVID-19 Data')
    ax.set_ylabel('Number')
    for index in range(len(Countries)):
        if PLOT_TOTALS: ax.plot(date_axis[index],case_count[index],label=Countries[index]+' - Cumulative Cases')
        if PLOT_TOTALS: cur_color = plt.gca().lines[-1].get_color()
        else: cur_color = '#1f77b4'
        if PLOT_CASES: ax.bar(date_axis[index],cases[index], label=Countries[index]+' - Daily Cases', edgecolor=cur_color, facecolor='none')
        if PLOT_DEATHS: ax.plot(date_axis[index],death_count[index],linestyle=':', color=cur_color, label=Countries[index]+' - Cumulative Deaths')
    ax.legend()
    fig.set_size_inches(10,6)
    fig.show()
    #input('Hit <Enter> when done.')
    tmp = input('Do another plot? [Y/n]').upper()
    if len(tmp) != 0 and tmp[0] == 'N':
        DO_IT = False
        #plt.close()
    else:
        DO_IT = True   #quit the main while loop
        
if len(fname)==0:
    tmp = input('Would you like to save the COVID-19 data to a local file [y/N]?').upper()
    if len(tmp)==0 or tmp[0]!='Y':
        print('Not saving.  Good bye.')
    else:
        fname = 'covid_data.xml'
        try:
            fhand2 = open(fname, 'w', encoding='utf-8')
            fhand2.write(xml)
            fhand2.close()
            print('Data has been saved as',fname)
        except:
            print('Error writing file',fname)
else:
    print('Good bye!')