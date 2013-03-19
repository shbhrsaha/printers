# THIS SCRIPT RUNS IN THE BACKGROUND
# AND COLLECTS DATA IN MONGODB

import datetime
import urllib, datetime, time
from bs4 import BeautifulSoup

import pymongo
from pymongo import MongoClient

# ESTABLISHED DATABASE CONNECTION
connection = MongoClient()
printerDb = connection.printer
recordsCollec = printerDb.records

# Define MONGODB entry writing

def addEntry(entryDateTime, line):

    # create the object
    new_entry = {
        
        'datetime'           : entryDateTime,
        'location'           : line[0],
        'building'           : line[1],
        'room'               : line[2],
        'status'             : line[3],
        }
    
    recordsCollec.insert(new_entry)

url = "http://clusters-lamp.princeton.edu/cgi-bin/clusterinfo.pl"

while True:
    
    
    print "Pausing for 10 minutes"

    time.sleep(600)
    # Get current DateTime
    now = datetime.datetime.now()
    output = ""
    
    print "Fetching at " + str(now)
    
    # Fetch HTML
    f = urllib.urlopen(url)
    html = f.read()

    # Get BeautifulSoup Object
    soup = BeautifulSoup(html)

    tr_list = soup.find_all('tr')

    length = len(tr_list)
    
    for n in range(1, length):

        tr = tr_list[n]

        line = list()
        
        for td in tr.find_all('td'):

            line.append(td.get_text().strip())

        
        if (line[0] != "1937**" and line[0] != "Forbes**"):
        
            #output += str(now) + ',' + ','.join(line) + '\n'
            addEntry(now, line)

        else:
            
            # need to split Printers A & B into two cases
            
            divided = line[-1].split("Printer")
            
            originalTitle = line[0]
            
            # do Printer A
            line[0] = originalTitle + "A"
            line[-1] = divided[1].strip()[3:]
            #output += str(now) + ',' + ','.join(line) + '\n'
            addEntry(now, line)
            
            # do Printer B
            line[0] = originalTitle + "B"
            line[-1] = divided[2].strip()[3:]
            #output += str(now) + ',' + ','.join(line) + '\n'
            addEntry(now, line)
                
                
    #with open("output.csv", "a") as outputFile:
        #outputFile.write(output)