# daywise.py goes down data.csv and keeps a running record of the number of printers of each type at each data point.

import os, sys, csv, datetime

# a dateTimePoint object stores the number of each category, in columns

class dateTimePoint:

    
    dateTimeValue = None
    noResponse = 0
    paperJammed = 0
    outOfPaper = 0
    interventionRequired = 0
    upAndRunning = 0
    noInk = 0
    lowInk = 0
    trayUnavailable = 0
    lowPaper = 0
    printing = 0
    other = 0



file_path = sys.argv[1]

# prep the file
file  = open(file_path, "rb")
reader = csv.reader(file)

header = True

categorized = {}


# READ IN AND CATEGORIZE
for row in reader:
    
    if header:
        header = False
        continue

    # new datetimes, create the object for it!
    if row[0] not in categorized.keys():

        categorized[row[0]] = dateTimePoint()
        categorized[row[0]].dateTimeValue = datetime.datetime.strptime(row[0], "%Y-%m-%dT%H:%M:%SZ")

    # switch statement to count up status cases
    status = row[4]
    dtPoint = categorized[row[0]]

    if status == "" or status == "No answer from device":
        dtPoint.noResponse += 1
    elif status == "Paper Jammed":
        dtPoint.paperJammed += 1
    elif status == "Out of Paper":
        dtPoint.outOfPaper += 1
    elif status == "Intervention Required":
        dtPoint.interventionRequired += 1
    elif status == "Up and Running":
        dtPoint.upAndRunning += 1
    elif status == "No Toner/Ink":
        dtPoint.noInk += 1
    elif status == "Toner/Ink Low":
        dtPoint.lowInk += 1
    elif status == "Input Tray Empty" or status == "Input Tray Missing":
        dtPoint.trayUnavailable += 1
    elif status == "Low Paper":
        dtPoint.lowPaper += 1
    elif status == "Printing":
        dtPoint.printing += 1
    else:
        dtPoint.other += 1


# PRINT OUT CATEGORIZED RESULTS
#print "datetime,no response, paper jammed, no paper, intervention needed, running, no ink, low ink, no tray, low paper, printing, other"
for key in sorted(categorized.iterkeys()):

    dtPoint = categorized[key]
    print datetime.datetime.strftime(dtPoint.dateTimeValue, "%Y-%m-%d %H:%M:%S")+","+str(dtPoint.noResponse)+","+str(dtPoint.paperJammed)+","+str(dtPoint.outOfPaper)+","+str(dtPoint.interventionRequired)+","+str(dtPoint.upAndRunning)+","+str(dtPoint.noInk)+","+str(dtPoint.lowInk)+","+str(dtPoint.trayUnavailable)+","+str(dtPoint.lowPaper)+","+str(dtPoint.printing)+","+str(dtPoint.other)