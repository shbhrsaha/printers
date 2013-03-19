# BASED ON COMMAND LINE ARGUMENTS,
# PRINTS OUT, ONE PER LINE, THE VALUES
# IN EACH CATEGORY

import os, sys, csv

file_path = sys.argv[1]

# prep the file
file  = open(file_path, "rb")
reader = csv.reader(file)

header = True
values = {}

noRows = 0
for row in reader:
    
    if header:
        header = False
        continue
    
    name = row[1]
    status = row[4]

    if name not in values.keys():
        values[name] = 0

    if status == "Up and Running":
        values[name] += 1

    noRows += 1

noPrinters = len(values.keys())
noSamples = float(noRows) / float(noPrinters)

print "printer, likelihood"
for k in values.keys():

    prob = "{0:.2f}".format(float(values[k])/float(noSamples))
    
    print k+","+prob
