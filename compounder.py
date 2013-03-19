# BASED ON COMMAND LINE ARGUMENTS,
# PRINTS OUT, ONE PER LINE, THE VALUES
# IN EACH CATEGORY

import os, sys, csv

file_path = sys.argv[1]
category = sys.argv[2]

# prep the file
file  = open(file_path, "rb")
reader = csv.reader(file)

if category == "-datetime":
    column = 0
if category == "-location":
    column = 1
if category == "-building":
    column = 2
if category == "-room":
    column = 3
if category == "-status":
    column = 4

header = True

values = {}

for row in reader:
    
    if header:
        header = False
        continue

    value = row[column]

    if value in values.keys():
        values[value] += 1
    else:
        values[value] = 1

for value in values.keys():

    print value+","+str(values[value])